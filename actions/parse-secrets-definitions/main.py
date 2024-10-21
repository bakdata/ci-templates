import os
import re

import typer
from typing_extensions import Annotated

DEFAULT_DELIMITER = "!!!"

# CAVEAT: will only work for one project at a time
# might be problematic if we want to inject secrets from multiple projects

# CAVEAT: this script can produce lists of secrets that are not valid, e.g. if the secret name is empty or the same secret is referenced multiple times

# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value, delim):
    if os.environ.get("GITHUB_ACTION"):
        f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
        f.write(f'{output_name}<<{delim}\n{output_value}{delim}\n') # ATTENTION: this might lead to problems if the output value contains the delimiter, which will not happen in this program but dont just copy this and expect it to work
        f.close()
    else:
        print("would have set output", output_name, "to", output_value)

# removee special characters and replace with underscores, succevive special characters are replaced with a single underscore
# convert to uppercase
# if the secret would end in an underscore, remove it
# format: SECRET_NAME:PROJECT_NAME/SECRET_NAME/VERSION
def parse_secret(secret, project_name, delim):
    if delim in secret: 
        raise ValueError(f"Invalid secret definition: {DELIMITER} is a reserved keyword")
    components = secret.split("/")

    if len(components) > 2:
        raise ValueError(f"Invalid secret definition: {secret}, not in the format 'secret_name/<version>'")
    secret_name = re.sub('[^0-9a-zA-Z]+', '_', components[0]).upper().rstrip("_")
    out = f"{secret_name}:{project_name}/{components[0]}"
    if len(components) == 2:
        out += f"/{components[1]}"
    return out

def main(
        input_secrets: Annotated[str, typer.Argument(envvar="INPUT_SECRETS_LIST")],
        gcp_project: Annotated[str, typer.Argument(envvar="INPUT_PROJECT_NAME")],
        github_output_delimter: Annotated[str, typer.Argument()] = DEFAULT_DELIMITER
    ):
    input_secrets = input_secrets.splitlines()

    output = ""
    for secret in input_secrets:
        output += parse_secret(secret, gcp_project, github_output_delimter) + "\n"


    set_github_action_output('secrets-list', output, github_output_delimter)


if __name__ == "__main__":
    typer.run(main)