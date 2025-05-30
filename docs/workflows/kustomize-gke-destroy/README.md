# Description of kustomize-gke-destroy reusable Workflow

This workflow will uninstall deployments using Kustomize.

## Dependencies

This workflow is built from multiple composite actions listed below:

- [helm-setup](https://github.com/bakdata/ci-templates/tree/main/actions/helm-setup)
- [kustomize-gke-destroy](https://github.com/bakdata/ci-templates/tree/main/actions/kustomize-gke-destroy)

## Calling the workflow

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
      gke-service-account: ${{ secrets.GKE_DEV_SERVICE_ACCOUNT }}
      gke-project: ${{ secrets.GKE_DEV_PROJECT }}
      gke-region: ${{ secrets.GKE_DEV_REGION }}
      gke-cluster: ${{ secrets.GKE_DEV_CLUSTER }}
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT              | TYPE   | REQUIRED | DEFAULT     | DESCRIPTION                                     |
| ------------------ | ------ | -------- | ----------- | ----------------------------------------------- |
| gcloud-sdk-version | string | false    | `"376.0.0"` | GCloud SDK version                              |
| helm-version       | string | false    | `"v3.8.1"`  | Helm version                                    |
| kubectl-version    | string | false    | `"v1.23.0"` | Kubectl version                                 |
| kustomization-path | string | true     |             | Path to the root directory of the kustomization |

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
