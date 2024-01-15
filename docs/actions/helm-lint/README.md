<h1>Description helm-lint composite action</h1>

This action will lint Helm charts inside the <code>charts</code> folder of your repository.

<h2>Prerequisites</h2>

You need to create the lint configuration file <code>.github/lint-config.yaml</code> and configure it to your liking.
A minimal configuration could look like this:

```yaml

<h1>check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations</h1>

target-branch: "main"
```

<h2>Usage</h2>

<code>yaml
steps:
  - name: Lint helm charts
    uses: bakdata/ci-templates/actions/helm-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
      lint-config-path: "my-lint-config.yaml" # (Optional)
      helm-version: "v3.10.1" # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|      INPUT       |  TYPE  | REQUIRED |           DEFAULT            |                                                                DESCRIPTION                                                                |
|------------------|--------|----------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
|   helm-version   | string |  false   |         <code>"v3.10.1"</code>          |                                                             The Helm version.                                                             |
| lint-config-path | string |  false   | <code>".github/lint-config.yaml"</code> | The path to the lint configuration file (For an example see https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
|       ref        | string |  false   |  <code>"${{ github.ref_name }}"</code>  |                                                 The ref name to checkout the repository.                                                  |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
