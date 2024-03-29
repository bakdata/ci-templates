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

| SECRET              | REQUIRED | DESCRIPTION                                |
| ------------------- | -------- | ------------------------------------------ |
| gke-cluster         | true     | GKE cluster for authentication             |
| gke-project         | true     | GKE project id for authentication          |
| gke-region          | true     | GKE region for authentication              |
| gke-service-account | true     | GKE service account key for authentication |

<!-- AUTO-DOC-SECRETS:END -->
