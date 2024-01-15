<h1>Description python-setup-poetry composite action</h1>

This composite action sets up Poetry for the given input version. It supports caching the Python virtualenv between workflow runs.

<h2>Usage</h2>

```yaml
steps:
  # Other Steps in your workflow

<ul>
name: Set up Poetry ${{ inputs.poetry-version }}
  uses: bakdata/ci-templates/actions/python-setup-poetry@main
  with:
    python-version: ${{ inputs.python-version }}
    poetry-version: ${{ inputs.poetry-version }}
    working-directory: ${{ inputs.working-directory }}

  # Rest of your workflow

```
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |  DEFAULT  |                      DESCRIPTION                       |
|-------------------|--------|----------|-----------|--------------------------------------------------------|
|  poetry-version   | string |  false   | <code>"1.2.2"</code> |          The Poetry version to be installed.           |
|  python-version   | string |  false   | <code>"3.10"</code>  | The Python version for the Poetry virtual environment. |
| working-directory | string |  false   |   <code>"."</code>   |       The root directory of the Poetry project.        |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
