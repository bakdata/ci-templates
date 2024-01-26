import glob
import os
import re
import shutil
import subprocess


TARGET_SUBSECTION_TITLE = 'References'
README_FILE = "README.md"


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def replace_string_in_markdown(file_path, old_string, new_string):
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = content.replace(old_string, new_string)
    with open(file_path, 'w') as file:
        file.write(modified_content)


def extract_subsection_content(markdown_content, subsection_title):
    # Define the pattern for detecting headers (## Subsection Title)
    pattern = re.compile(
        r'^##\s' + re.escape(subsection_title) + r'\s*$', re.MULTILINE)

    # Find the start and end positions of the subsection
    match = pattern.search(markdown_content)
    if match:
        start_position = match.end()
        next_header = pattern.search(markdown_content[start_position:])
        end_position = next_header.start() if next_header else len(markdown_content)

        # Extract the content of the subsection
        subsection_content = markdown_content[start_position:end_position].strip(
        )
        return subsection_content
    else:
        return None


def remove_formatting(content):
    # Remove whitespaces and newlines and hyphens
    try:
        return content.replace(
            " ", "").replace("\n", "").replace("-", "")
    except Exception as e:
        print(f"An error occurred: {e}")


def contents_equal(file1, file2):
    content1 = remove_formatting(file1)
    content2 = remove_formatting(file2)

    return content1 == content2


def update_doc(readme_path, reference_path):
    subsection_placeholder = ['## References', 'Empty substring created',
                              '### Subsubsection', 'Placeholder']
    updated = False

    # Create the dir in case documentation is not created yet
    directory_path = os.path.dirname(readme_path)
    os.makedirs(directory_path, exist_ok=True)

    # Create Readme if it does not exist yet
    ci_name = os.path.basename(directory_path)
    file_exist = os.path.exists(readme_path)
    if not file_exist:
        with open(readme_path, 'w') as file:
            file.write(f"# Documentation for {ci_name}")
            for line in subsection_placeholder:
                file.write(line + "\n")

    with open(readme_path, 'r') as file1:
        readme_content = file1.read()
    with open(reference_path, 'r') as file2:
        reference_content = file2.read()

    # add subsection if it does not exist
    if f"## {TARGET_SUBSECTION_TITLE}" not in readme_content:
        try:
            with open(readme_path, 'a') as file_readme:
                for line in subsection_placeholder:
                    file_readme.write(line + "\n")
        except Exception as e:
            print(f"An error occurred: {e}")

    readme_extraction_result = extract_subsection_content(
        readme_content, TARGET_SUBSECTION_TITLE)

    reference_extraction_result = extract_subsection_content(
        reference_content, TARGET_SUBSECTION_TITLE)

    if not contents_equal(readme_extraction_result, reference_extraction_result):
        replace_string_in_markdown(
            readme_path, readme_extraction_result, reference_extraction_result)
        updated = True

    return updated


def auto_doc_installed():
    auto_doc_cmd = os.environ.get("DOC_CMD")
    if auto_doc_cmd is None or auto_doc_cmd == "":
        auto_doc_cmd = "auto-doc"
    try:
        subprocess.run(
            auto_doc_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


def print_colored(text, color):
    print(f"{color}{text}{Colors.RESET}")


class DocGenerationError(Exception):
    def __init__(self, count):
        self.message = f"Error: The documentation is not up to date. {count} inconsistency(ies) where found.  Re running pre-commit may help."
        super().__init__(f"{Colors.RED}{self.message}{Colors.RESET}")


def safe_remove_directory(directory_path):
    if os.path.isdir(directory_path):
        try:
            shutil.rmtree(directory_path)
        except Exception as e:
            print(f"Error while removing directory '{directory_path}': {e}")
    else:
        print(f"Directory '{directory_path}' does not exist.")


def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
    except FileNotFoundError:
        print_colored(f"Source file not found.", Colors.RED)
    except PermissionError:
        print_colored(
            "Permission error. Make sure you have the necessary permissions.", Colors.RED)
    except Exception as e:
        print_colored(f"An error occurred: {e}", Colors.RED)


def run():
    auto_doc_cmd = os.environ.get("DOC_CMD")
    if auto_doc_cmd is None or auto_doc_cmd == "":
        auto_doc_cmd = "auto-doc"

    template = [
        "# References",
        "\n",
        "## Inputs",
        "\n",
        "## Outputs",
        "\n",
        "## Secrets",
        "\n"]

 # go through actions
    os.makedirs("tmps/", exist_ok=True)
    tmp_action = "tmps/actions"
    os.makedirs(tmp_action, exist_ok=True)
    changes = []

    action_files = glob.glob("actions/**/action.yaml")
    action_files.extend(glob.glob("actions/**/action.yml"))
    for action_file in action_files:
        action_name = os.path.basename(os.path.dirname(action_file))
        # create docu in tmp dir
        output_dir_action = f"docs/actions/{action_name}"
        tmp_docu_output_dir = os.path.join(
            tmp_action, action_name)

        os.makedirs(tmp_docu_output_dir, exist_ok=True)
        tmp_docu_output_action = os.path.join(
            tmp_action, action_name, "Variables.md")

        with open(tmp_docu_output_action, 'w') as file_action_template:
            for line in template[: -1]:
                file_action_template.write(line + '\n')
        os.system(
            f"{auto_doc_cmd} -f {action_file} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_action} > /dev/null")
        replace_string_in_markdown(tmp_docu_output_action, "# ", "## ")

        output_file_action = os.path.join(
            output_dir_action, README_FILE)
        changes.append({"readme": output_file_action,
                        "tmp_output": tmp_docu_output_action})

    # go through workflows
    tmp_workflow = "tmps/workflows"
    os.makedirs(tmp_workflow, exist_ok=True)

    workflow_dir = ".github/workflows"
    for workflow in os.listdir(workflow_dir):
        workflow_name = workflow.split(".")[0]
        if not workflow.startswith("_") and workflow != README_FILE:
            workflow_path = os.path.join(workflow_dir, workflow)
            output_dir_workflow = f"docs/workflows/{workflow_name}"

            # create docu in tmp dir
            tmp_workflow_output_dir = os.path.join(
                tmp_workflow, workflow_name)

            os.makedirs(tmp_workflow_output_dir, exist_ok=True)

            tmp_docu_output_workflow = os.path.join(
                tmp_workflow_output_dir, "Variables.md")

            with open(tmp_docu_output_workflow, 'w') as file_workflow_template:
                for line in template:
                    file_workflow_template.write(line + '\n')

            os.system(
                f"{auto_doc_cmd} -f {workflow_path} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_workflow} -r > /dev/null")
            replace_string_in_markdown(
                tmp_docu_output_workflow, "# ", "## ")

            workflow_doc_file = os.path.join(
                output_dir_workflow, README_FILE)

            changes.append({"readme": workflow_doc_file,
                            "tmp_output": tmp_docu_output_workflow})

    # Correction
    count = 0
    inconsistencies = []
    for entry in changes:
        readme_f = entry["readme"]
        tmp_f = entry["tmp_output"]
        was_updated = update_doc(readme_f, tmp_f)
        if was_updated:
            inconsistencies.append(readme_f)
            count += 1
    if count == 0:
        print_colored("√ Documentation up to date", Colors.GREEN)
        safe_remove_directory("tmps/")
    else:
        safe_remove_directory("tmps/")
        for i in inconsistencies:
            print_colored(i, Colors.YELLOW)
        raise DocGenerationError(count)


if __name__ == "__main__":
    if auto_doc_installed():
        run()
