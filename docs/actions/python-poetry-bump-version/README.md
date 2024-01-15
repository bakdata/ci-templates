<h1>Description python-poetry-bump-version composite action</h1>

This composite action bumps the Python package version depending on the release type. The <a href="https://python-poetry.org/docs/cli/#version"><code>poetry version</code></a> command is used to bump the version and change it in the <code>pyproject.toml</code> file. It will output the old and new bumped versions.

<h2>Dependencies</h2>

This action uses another composite action listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/python-setup-poetry">python-setup-poetry</a>
</ul>

<h2>Usage</h2>

```yaml
steps:
  # Other steps in your workflow
  - name: Bump version
    id: bump-version
    uses: bakdata/ci-templates/actions/python-poetry-bump-version@main
    with:
      release-type: ${{ inputs.release-type }}
      python-version: ${{ inputs.python-version }}
      poetry-version: ${{ inputs.poetry-version }}

<ul>
name: Use bump version output
run: echo Bumped version from ${{ steps.bump-version.outputs.old-version }} to ${{ steps.bump-version.outputs.release-version }}
```
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |  DEFAULT  |                                                      DESCRIPTION                                                       |
|-------------------|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------|
|  poetry-version   | string |  false   | <code>"1.2.2"</code> |                                          The Poetry version to be installed.                                           |
|  python-version   | string |  false   | <code>"3.10"</code>  |                                 The Python version for the Poetry virtual environment.                                 |
|   release-type    | string |   true   |           | Scope of the release: patch, minor, major, or snapshot. See https://python-poetry.org/docs/cli/#version for reference. |
| working-directory | string |  false   |   <code>"."</code>   |                                       The root directory of the Poetry project.                                        |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|     OUTPUT      |  TYPE  |             DESCRIPTION             |
|-----------------|--------|-------------------------------------|
|   old-version   | string |  The old version of your package.   |
| release-version | string | The bumped version of your package. |

<!-- AUTO-DOC-OUTPUT:END -->
