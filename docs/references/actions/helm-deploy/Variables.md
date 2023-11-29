# Refenrences helm-deploy composite action
## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED | DEFAULT  |                                           DESCRIPTION                                           |
|---------------------|--------|----------|----------|-------------------------------------------------------------------------------------------------|
|        chart        | string |   true   |          |                                      Helm chart to deploy                                       |
|    chart-version    | string |  false   |          |                                          Chart Version                                          |
|      namespace      | string |   true   |          |                                   K8s namespace to deploy in                                    |
|    post-renderer    | string |  false   |          |                          File path as string for a Helm post renderer                           |
|    release-name     | string |   true   |          |                                        Helm release name                                        |
|   repository-name   | string |  false   |          |                                      Helm repository name                                       |
| repository-password | string |  false   |          |                            Password for the login to the repository                             |
|   repository-url    | string |  false   |          |                                      Url of the repository                                      |
| repository-username | string |  false   |          |                              User for the login to the repository                               |
|       timeout       | string |  false   | `"1200"` |                             Timeout for the Helm command in seconds                             |
|     values-yaml     | string |   true   |          | File path as string for a single Helm value file or as json array for multiple Helm value files |

<!-- AUTO-DOC-INPUT:END -->
## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
