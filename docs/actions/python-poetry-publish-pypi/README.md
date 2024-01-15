<h1>Description python-poetry-publish-pypi composite action</h1>

This composite action uses Poetry to build and publish your Python packages either on TestPyPI or PyPI.

<h2>Usage</h2>

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@1.32.0

<pre><code># Other steps in your workflow
</code></pre>

<ul>
name: Publish to (Test)PyPI
uses: bakdata/ci-templates/actions/python-poetry-publish-pypi@main
with:
  pypi-token: ${{ secrets.pypi-token }}
  publish-to-test: ${{ inputs.publish-to-test }}
  working-directory: ${{ inputs.working-directory }}
```
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED | DEFAULT  |                                DESCRIPTION                                 |
|-------------------|--------|----------|----------|----------------------------------------------------------------------------|
|  publish-to-test  | string |  false   | <code>"true"</code> |   If set to false, the packages are published to PyPI. (Default is true)   |
|    pypi-token     | string |   true   |          |                  The PyPI token for publishing packages.                   |
| working-directory | string |  false   |  <code>"./"</code>  | The working directory of your Python packages. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
