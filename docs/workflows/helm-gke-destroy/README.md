# Description of helm-gke-destroy reusable Workflow

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT              | TYPE   | REQUIRED | DEFAULT     | DESCRIPTION                 |
| ------------------ | ------ | -------- | ----------- | --------------------------- |
| gcloud-sdk-version | string | false    | `"376.0.0"` | GCloud SDK version          |
| helm-version       | string | false    | `"v3.8.1"`  | Helm version                |
| kubectl-version    | string | false    | `"v1.23.0"` | Kubectl version             |
| namespace          | string | true     |             | K8s namespace to destroy in |
| release-name       | string | true     |             | Helm release name           |

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
