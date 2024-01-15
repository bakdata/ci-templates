<h1>Description of kustomize-gke-destroy reusable Workflow</h1>

This workflow will uninstall deployments using Kustomize.

<h2>Dependencies</h2>

This workflow is built from multiple composite actions listed below:

<ul>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/helm-setup">helm-setup</a>
<a href="https://github.com/bakdata/ci-templates/tree/main/actions/kustomize-gke-destroy">kustomize-gke-destroy</a>
</ul>

<h2>Calling the workflow</h2>

```yaml
name: Call this reusable workflow

on:
  workflow_dispatch:
    inputs:
      kustomization-path:
        description: "Path to the root directory of the kustomization"
        default: "kustomization-path"
        required: false
      timeout:
        description: "Time out(in seconds) for CustomResourceDefinitions"
        default: "60"
        required: false

jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/kustomize-gke-destroy.yaml@main
    with:
      kustomization-path: ${{ inputs.kustomization-path }}
      gcloud-sdk-version: "376.0.0" #optional
      kubectl-version: "v1.23.0" #optional
      helm-version: "v3.8.1" #optional
    secrets:
      gke-service-account: ${{ secrets.GKE<em>DEV</em>SERVICE<em>ACCOUNT }}
      gke-project: ${{ secrets.GKE</em>DEV<em>PROJECT }}
      gke-region: ${{ secrets.GKE</em>DEV<em>REGION }}
      gke-cluster: ${{ secrets.GKE</em>DEV_CLUSTER }}
```

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT        |  TYPE  | REQUIRED |   DEFAULT   |                   DESCRIPTION                   |
|--------------------|--------|----------|-------------|-------------------------------------------------|
| gcloud-sdk-version | string |  false   | <code>"376.0.0"</code> |               GCloud SDK version                |
|    helm-version    | string |  false   | <code>"v3.8.1"</code>  |                  Helm version                   |
|  kubectl-version   | string |  false   | <code>"v1.23.0"</code> |                 Kubectl version                 |
| kustomization-path | string |   true   |             | Path to the root directory of the kustomization |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->

<h3>Secrets</h3>

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

|       SECRET        | REQUIRED |                DESCRIPTION                 |
|---------------------|----------|--------------------------------------------|
|     gke-cluster     |   true   |       GKE cluster for authentication       |
|     gke-project     |   true   |     GKE project id for authentication      |
|     gke-region      |   true   |       GKE region for authentication        |
| gke-service-account |   true   | GKE service account key for authentication |

<!-- AUTO-DOC-SECRETS:END -->
