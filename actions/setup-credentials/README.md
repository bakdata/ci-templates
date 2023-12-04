# setup-credentials

This action will set up authentication for GCloud and a Google Kubernetes Engine cluster.

## Input Parameters

| Name                | Required | Default Value |  Type  | Description                                                                               |
| ------------------- | :------: | :-----------: | :----: | ----------------------------------------------------------------------------------------- |
| gke-service-account |    ✅    |       -       | string | The service account key for accessing the Google Kubernetes Engine cluster                |
| gke-project         |    ✅    |       -       | string | The name of the Google Cloud project that the Google Kubernetes Engine cluster belongs to |
| gke-region          |    ✅    |       -       | string | The name of the Google Cloud region that the Google Kubernetes Engine cluster belongs to  |
| gke-cluster         |    ✅    |       -       | string | The name of the Google Kubernetes engine cluster                                          |
| gcloud-sdk-version  |    ❌    |    376.0.0    | string | The Google Cloud SDK version to install                                                   |

## Usage

```yaml
---
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
