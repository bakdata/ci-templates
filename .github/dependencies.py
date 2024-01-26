import glob
import os
import yaml


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def print_colored(text, color):
    print(f"{color}{text}{Colors.RESET}")


def extract_dependencies(data):
    uses_values = []

    if isinstance(data, dict):
        for key, run in data.items():
            # if key == "jobs" and isinstance(value, list):
            if key == "runs":
                if isinstance(run, dict):
                    steps = run.get("steps", [])
                    if isinstance(steps, list):
                        for step in steps:
                            if isinstance(step, dict):
                                uses_value = step.get("uses")
                                if uses_value is not None:
                                    uses_values.append(uses_value)
            elif key == "jobs":
                if isinstance(run, dict):
                    jobs = run.items()
                    for _, job in jobs:
                        steps = job.get("steps", [])
                        if isinstance(steps, list):
                            for step in steps:
                                if isinstance(step, dict):
                                    uses_value = step.get("uses")
                                    if uses_value is not None:
                                        uses_values.append(uses_value)

    return uses_values


def generate_link(dependency):
    link = ""
    base = "https://github.com/"
    if "bakdata" in dependency:
        separator = "ci-templates/"
        prefix, sufix = dependency.split(separator)
        base += prefix + separator
        sufix, tag = sufix.split("@")
        tag = f"blob/{tag}/"
        link = base + tag + sufix
    else:
        link = base + dependency.replace("@", "/tree/")
    return link


def main():

    # go through actions
    action_readme_path = "action-README.md"
    action_files = glob.glob("actions/**/action.yaml")
    action_files.extend(glob.glob("actions/**/action.yml"))
    for action_file in action_files:
        action_name = os.path.basename(os.path.dirname(action_file))

        with open(action_file, 'r') as file:
            yaml_data = yaml.safe_load(file)
        uses_values = extract_dependencies(yaml_data)

        with open(action_readme_path, 'a') as file:
            file.write(f"\n# Dependencies for {action_name}\n")
            for dep in uses_values:
                link = generate_link(dep)
                file.write(f"- [{dep}]({link})\n")

    # go through workflows
    workflow_readme_path = "workflow-README.md"
    workflow_dir = ".github/workflows"
    for workflow in os.listdir(workflow_dir):
        workflow_name = workflow.split(".")[0]
        if not workflow.startswith("_") and workflow != "README.md":
            workflow_path = os.path.join(workflow_dir, workflow)
            with open(workflow_path, 'r') as workflow_file:
                workflow_data = yaml.safe_load(workflow_file)
            workflow_uses_values = extract_dependencies(workflow_data)

            with open(workflow_readme_path, 'a') as workflow_file:
                workflow_file.write(f"\n# Dependencies for {workflow_name}\n")
                for dep in workflow_uses_values:
                    link = generate_link(dep)
                    workflow_file.write(f"- [{dep}]({link})\n")


if __name__ == "__main__":
    main()
