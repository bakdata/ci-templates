# Description setup-credentials composite action

This action will set up authentication for GCloud and a Google Kubernetes Engine cluster.

## Usage

```yaml
steps:
  - name: Setup environment
    uses: bakdata/ci-templates/actions/setup-credentials@main
    with:
      gke-service-account: ${{ secrets.GKE_SERVICE_ACCOUNT }}
      gke-project: "my-awesome-project"
      gke-region: "us-west1"
      gke-cluster: "my-awesome-cluster"
      gcloud-sdk-version: "376.0.0" # optional
```

## Dependencies

- [google-github-actions/auth@v2](https://github.com/google-github-actions/auth/tree/v2)
- [google-github-actions/setup-gcloud@v0.6.0](https://github.com/google-github-actions/setup-gcloud/tree/v0.6.0)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT     | DESCRIPTION                                |
| ------------------- | ------ | -------- | ----------- | ------------------------------------------ |
| gcloud-sdk-version  | string | false    | `"376.0.0"` | GCloud SDK version                         |
| gke-cluster         | string | true     |             | GKE cluster for authentication             |
| gke-project         | string | true     |             | GKE project id for authentication          |
| gke-region          | string | true     |             | GKE region for authentication              |
| gke-service-account | string | true     |             | GKE service account key for authentication |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
