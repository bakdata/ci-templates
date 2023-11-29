import hashlib
import os
import shutil


def calculate_sha(file_path):
    sha = hashlib.sha256()

    with open(file_path, 'rb') as file:
        # Read the file in chunks to avoid memory issues with large files
        chunk_size = 8192
        while chunk := file.read(chunk_size):
            sha.update(chunk)

    return sha.hexdigest()


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
        tmp_docu_output_action = os.path.join(
            tmp_action, action_name, "Variables.md")

        if not os.path.exists(tmp_docu_output_dir):
            os.makedirs(tmp_docu_output_dir)

        with open(tmp_docu_output_action, 'w') as file:
            l1 = f"# Refenrences {action_name} composite action \n"
            l2 = "## Inputs \n"
            l3 = "## Outputs \n"
            file.writelines([l1, l2, l3])
        os.system(
            f"auto-doc -f {action_file} --colMaxWidth 10000 --colMaxWords 2000 -o {tmp_docu_output_action}")

        output_file_action = f"docs/references/actions/{action_name}/Variables.md"
        changes.append({"existing": output_file_action,
                       "tmp_output": tmp_docu_output_action})
    # os.system(f'echo {action_file}')
for entry in changes:
    existing_f = entry["existing"]
    tmp_f = entry["tmp_output"]
    # with open(entry["existing"], "rb") as f:
    #     digest_existing = hashlib.file_digest(f, "sha256")
    # with open(entry["tmp_output"], "rb") as f2:
    #     digest_tmp = hashlib.file_digest(f2, "sha256")

    # hash_existing_file = digest_existing.hexdigest()
    # hash_tmp_file = digest_tmp.hexdigest()
    hash_existing_file = calculate_sha(existing_f)
    hash_tmp_file = calculate_sha(tmp_f)

    print(f"{hash_existing_file}\n{hash_tmp_file}\n---")

# workflows
# tmp_workflow = "tmps/workflows"
# if not os.path.exists(tmp_workflow):
#     os.makedirs(tmp_workflow)


# remove tmp dir
# shutil.rmtree("tmps")
