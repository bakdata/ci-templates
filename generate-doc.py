import os
import shutil


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def print_colored(text, color):
    print(f"{color}{text}{Colors.RESET}")


class DocGenerationError(Exception):
    def __init__(self):
        self.message = "Error: The documentation is not up to date. Re running pre-commit may help."
        super().__init__(f"{Colors.RED}{self.message}{Colors.RESET}")


def safe_make_dir(directory_path):
    if not os.path.isdir(directory_path):
        try:
            os.makedirs(directory_path)
        except FileExistsError:
            shutil.rmtree(directory_path)
            safe_make_dir(directory_path)
        except Exception as e:
            print_colored(
                f"Error while removing directory '{directory_path}': {e}", Colors.BLUE)


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
 # go through actions
    safe_make_dir("tmps")
    tmp_action = "tmps/actions"
    safe_make_dir(tmp_action)
    action_dir = "actions"
    changes = []
    for action_name in os.listdir(action_dir):
        action_subdir_path = os.path.join(action_dir, action_name)
        output_dir_action = f"docs/references/actions/{action_name}"

        # Itterate over subidrs of the actions dir
        if not os.path.isfile(action_subdir_path):
            action_file = f"{action_subdir_path}/action.y*"
            action_file1 = f"{action_subdir_path}/action.yml"
            action_file2 = f"{action_subdir_path}/action.yaml"

            # exclude action directory without an action.yaml file
            if os.path.exists(action_file1) or os.path.exists(action_file2):
                # create docu in tmp dir
                tmp_docu_output_dir = os.path.join(
                    tmp_action, action_name)
                safe_make_dir(tmp_docu_output_dir)

                tmp_docu_output_action = os.path.join(
                    tmp_action, action_name, "Variables.md")

                with open(tmp_docu_output_action, 'w') as file:
                    l1 = f"# Refenrences {action_name} composite action\n"
                    l2 = "## Inputs\n"
                    l3 = "## Outputs\n"
                    file.writelines([l1, l2, l3])
                os.system(
                    f"auto-doc -f {action_file} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_action} > /dev/null")
                output_file_action = os.path.join(
                    output_dir_action, "Variables.md")
                changes.append({"existing": output_file_action,
                                "tmp_output": tmp_docu_output_action})

    # go through workflows
    tmp_workflow = "tmps/workflows"
    safe_make_dir(tmp_workflow)

    workflow_dir = ".github/workflows"
    for workflow in os.listdir(workflow_dir):
        workflow_name = workflow.split(".")[0]
        if not workflow.startswith("_") and workflow != "README.md":
            workflow_path = os.path.join(workflow_dir, workflow)
            output_dir_workflow = f"docs/references/workflows/{workflow_name}"

            # create docu in tmp dir
            tmp_workflow_output_dir = os.path.join(
                tmp_workflow, workflow_name)
            safe_make_dir(tmp_workflow_output_dir)

            tmp_docu_output_workflow = os.path.join(
                tmp_workflow_output_dir, "Variables.md")

            with open(tmp_docu_output_workflow, 'w') as file:
                l1 = f"# Refenrences {workflow_name} reusable Workflow\n"
                l2 = "## Inputs\n"
                l3 = "## Outputs\n"
                l4 = "## Secrets\n"
                file.writelines([l1, l2, l3, l4])

            os.system(
                f"auto-doc -f {workflow_path} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_workflow} -r > /dev/null")
            docs_output_path = os.path.join(
                output_dir_workflow, "Variables.md")

            changes.append({"existing": docs_output_path,
                            "tmp_output": tmp_docu_output_workflow})
    print_colored(
        "--------------------------------------------------------", Colors.BLUE)

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
        path_to_doc = outdated_file.split("/Variables.md")[0]
        print_colored(path_to_doc, Colors.YELLOW)
        safe_make_dir(path_to_doc)
        new_file = entry["tmp_output"]
        copy_file(new_file, outdated_file)

    if not need_updates:
        print_colored("√ Documentation up to date", Colors.GREEN)
    else:
        raise DocGenerationError()

    safe_remove_directory("tmps")


if __name__ == "__main__":
    run()
