<h1>Description of helm-gke-deploy reusable Workflow</h1>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT        |  TYPE  | REQUIRED |   DEFAULT   |                                           DESCRIPTION                                           |
|--------------------|--------|----------|-------------|-------------------------------------------------------------------------------------------------|
|       chart        | string |   true   |             |                                      Helm chart to deploy                                       |
|   chart-version    | string |  false   |             |                                          Chart version                                          |
| gcloud-sdk-version | string |  false   | <code>"376.0.0"</code> |                                       GCloud SDK version                                        |
|    helm-version    | string |  false   | <code>"v3.8.1"</code>  |                                          Helm version                                           |
|  kubectl-version   | string |  false   | <code>"v1.23.0"</code> |                                         Kubectl version                                         |
|     namespace      | string |   true   |             |                                   K8s namespace to deploy in                                    |
|   post-renderer    | string |  false   |             |                          File path as string for a Helm post renderer                           |
|    release-name    | string |   true   |             |                                        Helm release name                                        |
|  repository-name   | string |  false   |             |                                      Helm repository name                                       |
|   repository-url   | string |  false   |             |                                      Url of the repository                                      |
|      timeout       | string |  false   |  <code>"1200"</code>   |                             Timeout for the Helm command in seconds                             |
|    values-yaml     | string |   true   |             | File path as string for a single Helm value file or as json array for multiple Helm value files |

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
