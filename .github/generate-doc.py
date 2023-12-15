import glob
import os
import shutil
import subprocess


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def auto_doc_installed():
    auto_doc_cmd = os.environ.get("DOC_CMD")
    try:
        subprocess.run(
            auto_doc_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


def print_colored(text, color):
    print(f"{color}{text}{Colors.RESET}")


class DocGenerationError(Exception):
    def __init__(self):
        self.message = "Error: The documentation is not up to date. Re running pre-commit may help."
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


def files_equal(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = remove_formatting(file1.read())
        content2 = remove_formatting(file2.read())

        return content1 == content2


def run():
    auto_doc_cmd = os.environ.get("DOC_CMD")

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
        output_dir_action = f"docs/references/actions/{action_name}"
        tmp_docu_output_dir = os.path.join(
            tmp_action, action_name)

        os.makedirs(tmp_docu_output_dir, exist_ok=True)
        tmp_docu_output_action = os.path.join(
            tmp_action, action_name, "Variables.md")

        with open(tmp_docu_output_action, 'w') as file:
            file.writelines([
                f"# Refenrences {action_name} composite action\n",
                "## Inputs\n",
                "## Outputs\n"]
            )

        os.system(
            f"{auto_doc_cmd} -f {action_file} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_action} > /dev/null")
        output_file_action = os.path.join(
            output_dir_action, "Variables.md")
        changes.append({"existing": output_file_action,
                        "tmp_output": tmp_docu_output_action})

    # go through workflows
    tmp_workflow = "tmps/workflows"
    os.makedirs(tmp_workflow, exist_ok=True)

    workflow_dir = ".github/workflows"
    for workflow in os.listdir(workflow_dir):
        workflow_name = workflow.split(".")[0]
        if not workflow.startswith("_") and workflow != "README.md":
            workflow_path = os.path.join(workflow_dir, workflow)
            output_dir_workflow = f"docs/references/workflows/{workflow_name}"

            # create docu in tmp dir
            tmp_workflow_output_dir = os.path.join(
                tmp_workflow, workflow_name)

            os.makedirs(tmp_workflow_output_dir, exist_ok=True)

            tmp_docu_output_workflow = os.path.join(
                tmp_workflow_output_dir, "Variables.md")

            with open(tmp_docu_output_workflow, 'w') as file:
                l1 = f"# Refenrences {workflow_name} reusable Workflow\n"
                l2 = "## Inputs\n"
                l3 = "## Outputs\n"
                l4 = "## Secrets\n"
                file.writelines([l1, l2, l3, l4])

            os.system(
                f"{auto_doc_cmd} -f {workflow_path} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_workflow} -r > /dev/null")
            docs_output_path = os.path.join(
                output_dir_workflow, "Variables.md")

            changes.append({"existing": docs_output_path,
                            "tmp_output": tmp_docu_output_workflow})

    # Correction
    need_updates = []
    for entry in changes:
        existing_f = entry["existing"]
        tmp_f = entry["tmp_output"]
        file_exist = os.path.exists(existing_f)
        if (file_exist and not files_equal(existing_f, tmp_f)) or (not file_exist):
            need_updates.append(entry)

    for entry in need_updates:
        outdated_file = entry["existing"]
        path_to_doc = os.path.dirname(outdated_file)
        print_colored(path_to_doc, Colors.YELLOW)
        os.makedirs(path_to_doc, exist_ok=True)
        new_file = entry["tmp_output"]
        copy_file(new_file, outdated_file)
    if not need_updates:
        print_colored("√ Documentation up to date", Colors.GREEN)
    else:
        raise DocGenerationError()

    safe_remove_directory("tmps")


if __name__ == "__main__":
    if auto_doc_installed():
        run()
