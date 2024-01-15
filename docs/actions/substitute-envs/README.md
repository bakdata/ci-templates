<h1>Description substitute-envs composite action</h1>

This action will recursively substitute environment variables in a given directory.

<h2>Usage</h2>

<h2>```yaml</h2>

steps:
  - name: Substitute env variables
    id: substitute
    uses: bakdata/ci-templates/actions/substitute-envs@main
    with:
      path: "path/to/directory"

<ul>
name: Use substitute output
run: echo "${{ steps.substitute.outputs.path }}"
```
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT |  TYPE  | REQUIRED | DEFAULT |                         DESCRIPTION                          |
|-------|--------|----------|---------|--------------------------------------------------------------|
| path  | string |   true   |         | Path to the directory to substitute environment variables in |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT |  TYPE  |                    DESCRIPTION                     |
|--------|--------|----------------------------------------------------|
|  path  | string | Path to the temporary directory after substitution |

<!-- AUTO-DOC-OUTPUT:END -->
