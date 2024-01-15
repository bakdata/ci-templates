<h1>Description helm-destroy composite action</h1>

This action will destroy a Helm chart on a Kubernetes cluster.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Destroy Helm chart
    uses: bakdata/ci-templates/actions/helm-destroy@main
    with:
      release-name: "my-release"
      namespace: "my-namespace"
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|    INPUT     |  TYPE  | REQUIRED | DEFAULT |         DESCRIPTION         |
|--------------|--------|----------|---------|-----------------------------|
|  namespace   | string |   true   |         | K8s namespace to destroy in |
| release-name | string |   true   |         |      Helm release name      |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
