# import glob
import os

# action_files = glob.glob("actions/**/action.yaml")
# action_files.extend(glob.glob("actions/**/action.yml"))
# for action in action_files:
#     action_name = os.path.basename(os.path.dirname(action))
#     output_dir_action = f"docs/references/actions/{action_name}"


import subprocess

auto_doc_cmd = os.environ.get("DOC_CMD")


# def is_command_available():
#     try:
#         # subprocess.run([f"{auto_doc_cmd} -h"], stdout=subprocess.PIPE,
#         subprocess.run(["ls"], stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE, check=True)
#         return True
#     except subprocess.CalledProcessError:
#         return False
#     except FileNotFoundError:
#         return False


# a = is_command_available()
# print(f"response is: {a}")


def auto_doc_installed():
    auto_doc_cmd = os.environ.get("DOC_CMD")
    try:
        subprocess.run(
            auto_doc_cmd , stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"



