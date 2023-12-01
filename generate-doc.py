import hashlib
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


def calculate_sha(file_path):
    sha = hashlib.sha256()

    with open(file_path, 'rb') as file:
        # Read the file in chunks to avoid memory issues with large files
        chunk_size = 8192
        while chunk := file.read(chunk_size):
            sha.update(chunk)

    return sha.hexdigest()


def copy_file(source_path, destination_path):
    try:
        # Copy the file from source_path to destination_path
        shutil.copy(source_path, destination_path)
        print_colored(
            f"File updated successfully from {source_path} to {destination_path}", Colors.BLUE)
    except FileNotFoundError:
        print_colored(f"Source file not found.", Colors.RED)
    except PermissionError:
        print_colored(
            "Permission error. Make sure you have the necessary permissions.", Colors.RED)
    except Exception as e:
        print_colored(f"An error occurred: {e}", Colors.RED)


def run():

    # actions
    tmp_action = "tmps/actions"
    if not os.path.exists(tmp_action):
        os.makedirs(tmp_action)
    action_dir = "actions"
    changes = []
    for action_name in os.listdir(action_dir):
        action_subdir_path = os.path.join(action_dir, action_name)
        output_dir_action = f"docs/references/actions/{action_name}"
        # checking if it is a subidr
        if not os.path.isfile(action_subdir_path):
            action_file = os.path.join(action_subdir_path, "action.y*")

            # create docu in tmp dir
            tmp_docu_output_dir = os.path.join(
                tmp_action, action_name)
            if not os.path.exists(tmp_docu_output_dir):
                os.makedirs(tmp_docu_output_dir)

            tmp_docu_output_action = os.path.join(
                tmp_action, action_name, "Variables.md")

            with open(tmp_docu_output_action, 'w') as file:
                l1 = f"# Refenrences {action_name} composite action\n"
                l2 = "## Inputs\n"
                l3 = "## Outputs\n"
                file.writelines([l1, l2, l3])
            os.system(
                f"auto-doc -f {action_file} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_action}")

            output_file_action = f"docs/references/actions/{action_name}/Variables.md"
            changes.append({"existing": output_file_action,
                            "tmp_output": tmp_docu_output_action})

    # workflows
    tmp_workflow = "tmps/workflows"
    if not os.path.exists(tmp_workflow):
        os.makedirs(tmp_workflow)

    workflow_dir = ".github/workflows"
    for workflow in os.listdir(workflow_dir):
        workflow_name = workflow.split(".")[0]
        if not workflow.startswith("_") and workflow != "README.md":
            workflow_path = os.path.join(workflow_dir, workflow)
            output_dir_workflow = f"docs/references/workflows/{workflow_name}"

            # create docu in tmp dir
            tmp_workflow_output_dir = os.path.join(
                tmp_workflow, workflow_name)
            if not os.path.exists(tmp_workflow_output_dir):
                os.makedirs(tmp_workflow_output_dir)

            tmp_docu_output_workflow = os.path.join(
                tmp_workflow_output_dir, "Variables.md")

            with open(tmp_docu_output_workflow, 'w') as file:
                l1 = f"# Refenrences {workflow_name} reusable Workflow\n"
                l2 = "## Inputs\n"
                l3 = "## Outputs\n"
                l4 = "## Secrets\n"
                file.writelines([l1, l2, l3, l4])

            os.system(
                f"auto-doc -f {workflow_path} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_workflow} -r")
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
        if os.path.exists(existing_f):
            hash_existing_file = calculate_sha(existing_f)
            hash_tmp_file = calculate_sha(tmp_f)
            if hash_existing_file != hash_tmp_file or not os.path.exists(tmp_docu_output_dir):
                need_updates.append(entry)
        else:
            need_updates.append(entry)

    for entry in need_updates:
        outdated_file = entry["existing"]
        path_to_doc = outdated_file.split("/Variables.md")[0]
        print_colored(path_to_doc, Colors.BLUE)
        if not os.path.exists(path_to_doc):
            os.makedirs(path_to_doc)
        new_file = entry["tmp_output"]
        print_colored(
            f"File {outdated_file} needs to be updated ", Colors.YELLOW)
        copy_file(new_file, outdated_file)

    if not need_updates:
        print_colored("√ Documentation up to date", Colors.GREEN)
    else:
        print_colored(
            "Error: The documentation is not up to date. Re running pre-commit may help.", Colors.RED)
        os._exit(1)

    if os.path.exists("tmps"):
        shutil.rmtree("tmps")


if __name__ == "__main__":

    run()
    # exit succcesfully
    # remove tmp dir
    os._exit(0)