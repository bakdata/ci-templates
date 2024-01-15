<h1>Description helm-package composite action</h1>

This composite action packages a Helm chart. Afterwards, it creates an index file for the chart repository. If <code>index.yaml</code> exists, it is merged in the new index.

<h2>Usage</h2>

```yaml
steps:
  # ...

<ul>
name: Helm package
  uses: bakdata/ci-templates/actions/helm-package@main
  with:
    helm-version: "v3.10.1" # (Optional)
    charts-dir: "helm-chart" # (Optional) if not set the repository root will be used

<h1>Rest of the workflow steps</h1>

```
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|    INPUT     |  TYPE  | REQUIRED |   DEFAULT   |               DESCRIPTION                |
|--------------|--------|----------|-------------|------------------------------------------|
|  charts-dir  | string |  false   |    <code>"."</code>    | The directory containing the Helm chart. |
| helm-version | string |  false   | <code>"v3.10.1"</code> |            The Helm version.             |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
