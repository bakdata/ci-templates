<h1>Description python-poetry-publish composite action</h1>

This composite action uses Poetry to build and publish your Python packages to a package index.

<h2>Usage</h2>

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@1.32.0

<pre><code># Other steps in your workflow
</code></pre>

<ul>
name: Publish to package index
uses: bakdata/ci-templates/actions/python-poetry-publish@main
with:
  index-name: index
  index-url: example.org/simple/
  index-username: user123
  index-password: supersecret
  working-directory: ${{ inputs.working-directory }}
```
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED | DEFAULT |                                DESCRIPTION                                 |
|-------------------|--------|----------|---------|----------------------------------------------------------------------------|
|    index-name     | string |   true   |         |              The package index name for publishing packages.               |
|  index-password   | string |   true   |         |            The package index password for publishing packages.             |
|     index-url     | string |   true   |         |               The package index url for publishing packages.               |
|  index-username   | string |   true   |         |            The package index username for publishing packages.             |
| working-directory | string |  false   | <code>"./"</code>  | The working directory of your Python packages. (Default is root directory) |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
