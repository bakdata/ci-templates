# Refenrences kustomize-gke-destroy reusable Workflow
## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT        |  TYPE  | REQUIRED |   DEFAULT   |                   DESCRIPTION                   |
|--------------------|--------|----------|-------------|-------------------------------------------------|
| gcloud-sdk-version | string |  false   | `"376.0.0"` |               GCloud SDK version                |
|    helm-version    | string |  false   | `"v3.8.1"`  |                  Helm version                   |
|  kubectl-version   | string |  false   | `"v1.23.0"` |                 Kubectl version                 |
| kustomization-path | string |   true   |             | Path to the root directory of the kustomization |

<!-- AUTO-DOC-INPUT:END -->
## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
