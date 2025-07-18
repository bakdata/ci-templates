# Description of helm-gke-deploy reusable Workflow

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT              | TYPE   | REQUIRED | DEFAULT     | DESCRIPTION                                                                                     |
| ------------------ | ------ | -------- | ----------- | ----------------------------------------------------------------------------------------------- |
| chart              | string | true     |             | Helm chart to deploy                                                                            |
| chart-version      | string | false    |             | Chart version                                                                                   |
| gcloud-sdk-version | string | false    | `"376.0.0"` | GCloud SDK version                                                                              |
| helm-version       | string | false    | `"v3.8.1"`  | Helm version                                                                                    |
| kubectl-version    | string | false    | `"v1.23.0"` | Kubectl version                                                                                 |
| namespace          | string | true     |             | K8s namespace to deploy in                                                                      |
| post-renderer      | string | false    |             | File path as string for a Helm post renderer                                                    |
| release-name       | string | true     |             | Helm release name                                                                               |
| repository-name    | string | false    |             | Helm repository name                                                                            |
| repository-url     | string | false    |             | Url of the repository                                                                           |
| timeout            | string | false    | `"1200"`    | Timeout for the Helm command in seconds                                                         |
| values-yaml        | string | true     |             | File path as string for a single Helm value file or as json array for multiple Helm value files |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET                            | REQUIRED | DESCRIPTION                                                |
| --------------------------------- | -------- | ---------------------------------------------------------- |
| GOOGLE_PROJECT_ID                 | true     | The id of the project which contains the secrets           |
| GOOGLE_SERVICE_ACCOUNT            | true     | The service account to use to fetch the secrets            |
| GOOGLE_WORKLOAD_IDENTITY_PROVIDER | true     | The workload identity provider to use for fetching secrets |

<!-- AUTO-DOC-SECRETS:END -->
