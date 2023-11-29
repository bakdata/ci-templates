import subprocess
import sys
import os


def format_md_with_dprint(files):
    for file_path in files:
        subprocess.run(['dprint', 'fmt', file_path], check=True)


if __name__ == "__main__":
    # Get the list of files from pre-commit arguments
    files_to_format = sys.argv[1:]

    # Format Markdown files with dprint
    format_md_with_dprint(files_to_format)

    sys.exit(0)
