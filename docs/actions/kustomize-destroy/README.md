<h1>Description kustomize-destroy composite action</h1>

This action will destroy a <code>kustomization.yaml</code> file on a Kubernetes cluster.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Destroy Kustomize app
    uses: bakdata/ci-templates/actions/kustomize-destroy@main
    with:
      kustomization-path: "my-kustomization-path" #directory containing my kustomization file
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT        |  TYPE  | REQUIRED | DEFAULT |                   DESCRIPTION                   |
|--------------------|--------|----------|---------|-------------------------------------------------|
| kustomization-path | string |   true   |         | Path to the root directory of the kustomization |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
