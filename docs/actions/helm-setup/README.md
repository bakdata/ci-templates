<h1>Description helm-setup composite action</h1>

This action will set up everything necessary to deploy or destroy Helm charts.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Setup environment
    uses: bakdata/ci-templates/actions/helm-setup@main
    with:
      kubectl-version: "v1.23.0" # optional
      helm-version: "v3.10.1" # optional
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|      INPUT      |  TYPE  | REQUIRED |   DEFAULT   |   DESCRIPTION   |
|-----------------|--------|----------|-------------|-----------------|
|  helm-version   | string |  false   | <code>"v3.10.1"</code> |  Helm version   |
| kubectl-version | string |  false   | <code>"v1.23.0"</code> | Kubectl version |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
