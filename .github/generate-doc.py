import glob
import markdown2
import os
import re
import shutil
import subprocess


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def format_markdown_file(filename):
    with open(filename, 'r+') as file:
        content = file.read()
        formatted_content = markdown2.markdown(content)
    with open(filename, 'w') as file:
        file.write(formatted_content)
    replace_string_in_markdown(filename, "<p>", "")
    replace_string_in_markdown(filename, "</p>", "")
    # replace_string_in_markdown(filename, "<li>", "")
    # replace_string_in_markdown(filename, "</li>", "")


def contains_subsection(file_path, target_subsection_title):
    section_pattern = re.compile(r'^\s*#{1}\s+(.*)$', re.MULTILINE)
    subsection_pattern = re.compile(r'^\s*#{2}\s+(.*)$', re.MULTILINE)

    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    section_matches = section_pattern.finditer(markdown_text)

    for match in section_matches:
        section_title = match.group(1)
        section_start = match.end()

        if section_title.lower() == target_subsection_title.lower():
            return bool(subsection_pattern.search(markdown_text, section_start))

    return False


def replace_string_in_markdown(file_path, old_string, new_string):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    modified_content = content.replace(old_string, new_string)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)
    return modified_content


def extract_subsection(file_path, target_subsection_title):
    html_subsection_pattern = re.compile(
        r'<h2>(.*?)<\/h2>', re.IGNORECASE | re.DOTALL)
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    html_subsection_matches = html_subsection_pattern.finditer(markdown_text)

    # Iterate over matches to find the target subsection
    for match in html_subsection_matches:
        current_subsection_title = match.group(1).strip()

        if current_subsection_title.lower() == target_subsection_title.lower():

            subsection_start = match.start()
            next_subsection_match = next(html_subsection_matches, None)
            subsection_end = next_subsection_match.start(
            ) if next_subsection_match else len(markdown_text)

            subsection_content = markdown_text[match.end(
            ):subsection_end].strip()

            subsubsection_matches = html_subsection_pattern.finditer(
                subsection_content)
            subsubsections = [{"title": submatch.group(1).strip(
            ), "content": ''} for submatch in subsubsection_matches]

            return {
                "title": current_subsection_title,
                "content": subsection_content,
                "subsubsections": subsubsections
            }

    return None


def update_doc(readme_path, reference_path):
    placeholder = [
        '\n',
        '## References',
        '\n',
        'Empty substring created',
        '\n',
        '### Subsubsection',
        '\n',
        'Placeholder']
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
            file.writelines(placeholder)

    with open(readme_path, 'r', encoding='utf-8') as file1:
        readme_content = file1.read()

    target_subsection_title = 'References'

    # add subsection if it does not exist
    if not readme_content.__contains__(f"## {target_subsection_title}") and not readme_content.__contains__(f"<h2>{target_subsection_title}</h2>"):
        with open(readme_path, 'a', encoding='utf-8') as file_readme:
            file_readme.writelines(placeholder)
    format_markdown_file(readme_path)
    readme_extraction_result = extract_subsection(
        readme_path, target_subsection_title)

    reference_extraction_result = extract_subsection(
        reference_path, target_subsection_title)

    if file_exist:
        readme_result_as_str = readme_extraction_result["content"]
        reference_result_as_str = reference_extraction_result["content"]

        # if not readme_result_as_str == new_content:
        if not contents_equal(readme_result_as_str, reference_result_as_str):
            replace_string_in_markdown(
                readme_path, readme_result_as_str, reference_result_as_str)
            print_colored(readme_path, Colors.YELLOW)
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


def remove_formatting(content):
    # Remove whitespaces and newlines and hyphens
    return content.replace(" ", "").replace("\n", "").replace("-", "")


def contents_equal(file1, file2):
    content1 = remove_formatting(file1)
    content2 = remove_formatting(file2)

    return content1 == content2


def run():
    auto_doc_cmd = os.environ.get("DOC_CMD")
    if auto_doc_cmd is None or auto_doc_cmd == "":
        auto_doc_cmd = "auto-doc"

    template = [
        "# References",
        "## Inputs",
        "## Outputs",
        "## Secrets"]

 # go through actions
    os.makedirs("tmps", exist_ok=True)
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
        format_markdown_file(tmp_docu_output_action)
        output_file_action = os.path.join(
            output_dir_action, "README.md")
        changes.append({"readme": output_file_action,
                        "tmp_output": tmp_docu_output_action})

    # go through workflows
    tmp_workflow = "tmps/workflows"
    os.makedirs(tmp_workflow, exist_ok=True)

    workflow_dir = ".github/workflows"
    for workflow in os.listdir(workflow_dir):
        workflow_name = workflow.split(".")[0]
        if not workflow.startswith("_") and workflow != "README.md":
            workflow_path = os.path.join(workflow_dir, workflow)
            # Test with only one workflow
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

            format_markdown_file(tmp_docu_output_workflow)
            workflow_doc_file = os.path.join(
                output_dir_workflow, "README.md")

            changes.append({"readme": workflow_doc_file,
                            "tmp_output": tmp_docu_output_workflow})

    # Correction
    count = 0
    for entry in changes:
        readme_f = entry["readme"]
        tmp_f = entry["tmp_output"]
        was_updated = update_doc(readme_f, tmp_f)

        if was_updated:
            count += 1
    if count == 0:
        print_colored("√ Documentation up to date", Colors.GREEN)
        safe_remove_directory("tmps")
    else:
        safe_remove_directory("tmps")
        raise DocGenerationError(count)


if __name__ == "__main__":
    if auto_doc_installed():
        run()
