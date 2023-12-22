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
