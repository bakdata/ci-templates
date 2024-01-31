import os
import re
import yaml


DEPENDENCIES_SUBSECTION_TITLE = "Dependencies"
DEPENDENCIES_PLACEHOLDER = ['## Dependencies',
                            'No external actions in use here.']


def create_non_existing_docu(file_path: str, placeholder: list):
    # Create the dir in case documentation is not created yet
    directory_path = os.path.dirname(file_path)
    os.makedirs(directory_path, exist_ok=True)

    # Create Readme if it does not exist yet
    ci_name = os.path.basename(directory_path)
    file_exist = os.path.exists(file_path)
    if not file_exist:
        with open(file_path, 'w') as file:
            file.write(f"# Documentation for {ci_name}\n")
            for line in placeholder:
                file.write(line + "\n")


def read_file(file_path: str):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def remove_formatting(content):
    # Remove whitespaces and newlines and hyphens
    try:
        return content.replace(
            " ", "").replace("\n", "").replace("-", "")
    except Exception as e:
        print(f"An error occurred: {e}")


def replace_string_in_markdown(file_path, old_string, new_string):
    content = read_file(file_path)
    modified_content = content.replace(old_string, new_string)
    with open(file_path, 'w') as file:
        file.write(modified_content)


def contents_equal(file1, file2):
    content1 = remove_formatting(file1)
    content2 = remove_formatting(file2)

    return content1 == content2


def extract_subsection_content(markdown_content, subsection_title):
    # Defines the pattern for detecting headers (## Subsection Title)
    pattern = re.compile(
        r'^##\s' + re.escape(subsection_title) + r'\s*$', re.MULTILINE)

    # Finds the start and end positions of the subsection
    match = pattern.search(markdown_content)
    if match:
        start_position = match.end()
        next_header = pattern.search(markdown_content[start_position:])
        if next_header:
            end_position = next_header.start() + start_position
        else:
            end_position = len(markdown_content)

        # Extracs the content of the subsection
        subsection_content = markdown_content[start_position:end_position].strip(
        )
        return subsection_content
    else:
        return None


def extract_dependencies(ci_file):
    uses_values = []

    with open(ci_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    if isinstance(yaml_data, dict):
        for key, run in yaml_data.items():
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


def generate_links(used_ci):
    dependencies = []
    for dep in used_ci:
        link = ""
        dependency_link = ""
        base = "https://github.com/"
        if "bakdata" in dep:
            separator = "ci-templates/"
            prefix, sufix = dep.split(separator)
            base += prefix + separator
            sufix, tag = sufix.split("@")
            tag = f"blob/{tag}/"
            link = base + tag + sufix
        else:
            link = base + dep.replace("@", "/tree/")

        dependency_link = f"- [{dep}]({link})\n"
        dependencies.append(dependency_link)

    return dependencies


def update_dependencies(readme_path: str, dependencies: list):
    updated = False

    create_non_existing_docu(file_path=readme_path,
                             placeholder=DEPENDENCIES_PLACEHOLDER)
    if dependencies:
        readme_content = read_file(readme_path)

        if f"## {DEPENDENCIES_SUBSECTION_TITLE}" not in readme_content:
            try:
                with open(readme_path, 'a') as file_readme:
                    for line in DEPENDENCIES_PLACEHOLDER:
                        file_readme.write(line + "\n")
                    file_readme.write("\n")
            except Exception as e:
                print(f"An error occurred: {e}")
        new_readme_content = read_file(readme_path)
        readme_extraction_result = extract_subsection_content(
            new_readme_content, DEPENDENCIES_SUBSECTION_TITLE)
        param_join_result = ''.join(dependencies)
        dependencies_subsection = readme_extraction_result.split("\n## ")[0]
        if not contents_equal(dependencies_subsection, param_join_result):
            replace_string_in_markdown(
                readme_path, dependencies_subsection, param_join_result)
            updated = True
    return updated
