import os
import re

# CAVEAT: will only work for one project at a time
# might be problematic if we want to inject secrets from multiple projects

# CAVEAT: this script can produce lists of secrets that are not valid, e.g. if the secret name is empty or the same secret is referenced multiple times

# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value, delim=''):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}<<EOF{output_value}EOF\n') # ATTENTION: this might lead to problems if the output value contains the delimiter, which will not happen in this program but dont just copy this and expect it to work
    f.close()    


# removee special characters and replace with underscores, succevive special characters are replaced with a single underscore
# convert to uppercase
# if the secret would end in an underscore, remove it
# format: SECRET_NAME:PROJECT_NAME/SECRET_NAME/VERSION
def parse_secret(secret, project_name):
    if secret.contains("EOF"): 
        raise ValueError("Invalid secret definition: EOF is a reserved keyword FIXME")
    components = secret.split("/")

    if len(components) > 2:
        raise ValueError(f"Invalid secret definition: {secret}, not in the format 'secret_name/<version>'")
    secret_name = re.sub('[^0-9a-zA-Z]+', '_', components[0]).upper().rstrip("_")
    out = f"{secret_name}:{project_name}/{components[0]}"
    if len(components) == 2:
        out += f"/{components[1]}"
    return out

def main():
    print(os.environ)
    input_secrets = os.environ["INPUT_SECRETS-LIST"].splitlines()
    gcp_project = os.environ["INPUT_PROJECT-NAME"]

    output = ""
    for secret in input_secrets:
        output += parse_secret(secret, gcp_project) + "\n"


    set_github_action_output('secrets-list', output)


if __name__ == "__main__":
    main()
    # print(parse_secret("alksdjoioe4j####@!@#!1123asdlolw!!asd!!print(/1", "project"))