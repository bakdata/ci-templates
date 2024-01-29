from dependencies import contents_equal, extract_dependencies, extract_subsection_content, generate_links, read_file, replace_string_in_markdown, update_dependencies
import glob
import os
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


def print_colored(text, color):
    print(f"{color}{text}{Colors.RESET}")


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

    readme_content = read_file(readme_path)
    reference_content = read_file(reference_path)

    # add subsection if it does not exist
    if f"## {TARGET_SUBSECTION_TITLE}" not in readme_content:
        try:
            with open(readme_path, 'a') as file_readme:
                for line in subsection_placeholder:
                    file_readme.write(line + "\n")
        except Exception as e:
            print(f"An error occurred: {e}")
    new_readme_content = read_file(readme_path)
    readme_extraction_result = extract_subsection_content(
        new_readme_content, TARGET_SUBSECTION_TITLE)
    readme_references_subsection = readme_extraction_result.split("\n## ")[0]

    reference_extraction_result = extract_subsection_content(
        reference_content, TARGET_SUBSECTION_TITLE)

    if not contents_equal(readme_references_subsection, reference_extraction_result):
        replace_string_in_markdown(
            readme_path, readme_references_subsection, reference_extraction_result)
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


class DocGenerationError(Exception):
    def __init__(self, count, inconsistencies):
        inconsistencies_str = f"{Colors.RED}Error: The documentation is not up to date. {count} inconsistency(ies) where found. Re running pre-commit may help. Inconstencies:\n{Colors.RESET}"
        for i in inconsistencies:
            inconsistencies_str += f"{Colors.RED}- {i}\n{Colors.RESET}"
        super().__init__(inconsistencies_str)


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

        # generate a list of dependencies containing links to GH-repos
        action_dependencies = extract_dependencies(action_file)
        action_dependencies_links = generate_links(action_dependencies)

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
                        "tmp_output": tmp_docu_output_action,
                       "dependencies": action_dependencies_links})

    # go through workflows
    tmp_workflow = "tmps/workflows"
    os.makedirs(tmp_workflow, exist_ok=True)

    workflow_dir = ".github/workflows"
    for workflow in os.listdir(workflow_dir):
        workflow_name = workflow.split(".")[0]
        if not workflow.startswith("_") and workflow != README_FILE:

            # generate a list of dependencies containing links to GH-repos
            workflow_dependencies = extract_dependencies(action_file)
            workflow_dependencies_links = generate_links(workflow_dependencies)

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
                            "tmp_output": tmp_docu_output_workflow,
                            "dependencies": workflow_dependencies_links})

    # Correction
    count = 0
    inconsistencies = []
    for entry in changes:
        readme_f = entry["readme"]
        tmp_f = entry["tmp_output"]
        dependencies_found = entry["dependencies"]

        dep_updated = update_dependencies(
            readme_path=readme_f, dependencies=dependencies_found)

        was_updated = update_doc(readme_f, tmp_f)

        if was_updated or dep_updated:
            inconsistencies.append(readme_f)
            count += 1
    if count == 0:
        print_colored("√ Documentation up to date", Colors.GREEN)
        safe_remove_directory("tmps/")
    else:
        safe_remove_directory("tmps/")
        raise DocGenerationError(count, inconsistencies)


if __name__ == "__main__":
    if auto_doc_installed():
        run()
