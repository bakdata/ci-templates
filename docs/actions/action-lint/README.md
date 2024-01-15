<h1>Description action-lint composite action</h1>

This action will lint all actions and workflows of a repository.

<code>yaml
steps:
  - name: Lint actions and workflows
    uses: bakdata/ci-templates/actions/action-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |   DEFAULT   |                DESCRIPTION                 |
|---------------------|--------|----------|-------------|--------------------------------------------|
| action-lint-version | string |  false   | <code>"v1.6.22"</code> | The action lint repository version to use. |
|         ref         | string |  false   |             |  The ref name to checkout the repository.  |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
