<h1>Description kustomize-deploy composite action</h1>

This action will deploy resources with Kustomize on a Kubernetes cluster.

<h2>Prerequisites</h2>

Create a <code>kustomization.yaml</code> file for your deployment.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Deploy Kustomize app
    uses: bakdata/ci-templates/actions/kustomize-deploy@main
    with:
      kustomization-path: "my-kustomization-path" #directory containing my kustomization file
      timeout: "60" #optional
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT        |  TYPE  | REQUIRED | DEFAULT |                    DESCRIPTION                     |
|--------------------|--------|----------|---------|----------------------------------------------------|
| kustomization-path | string |   true   |         |  Path to the root directory of the kustomization   |
|      timeout       | string |  false   | <code>"60"</code>  | Time out(in seconds) for CustomResourceDefinitions |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
