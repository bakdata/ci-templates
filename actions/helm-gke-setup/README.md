# helm-gke-setup

This action will set up everything necessary to deploy or destroy Helm charts on a Google Kubernetes Engine cluster.

## Input Parameters

| Name                | Required | Default Value |  Type  | Description                                                                               |
| ------------------- | :------: | :-----------: | :----: | ----------------------------------------------------------------------------------------- |
| gke-service-account |    ✅    |       -       | string | The service account key for accessing the Google Kubernetes Engine cluster                |
| gke-project         |    ✅    |       -       | string | The name of the Google Cloud project that the Google Kubernetes Engine cluster belongs to |
| gke-region          |    ✅    |       -       | string | The name of the Google Cloud region that the Google Kubernetes Engine cluster belongs to  |
| gke-cluster         |    ✅    |       -       | string | The name of the Google Kubernetes engine cluster                                          |
| python-version      |    ❌    |     3.10      | string | The python version to install                                                             |
| gcloud-sdk-version  |    ❌    |    376.0.0    | string | The Google Cloud SDK version to install                                                   |
| kubectl-version     |    ❌    |    v1.23.0    | string | The kubectl version to install                                                            |
| helm-version        |    ❌    |    v3.10.1    | string | The Helm version to install                                                               |

## Usage

```yaml
...
steps:
  - name: Setup environment
    uses: bakdata/ci-templates/actions/helm-gke-setup@main
    with:
      gke-service-account: ${{ secrets.GKE_SERVICE_ACCOUNT }}
      gke-project: "my-awesome-project"
      gke-region: "us-west1"
      gke-cluster: "my-awesome-cluster"
      python-version: "3.10" # optional
      gcloud-sdk-version: "376.0.0" # optional
      kubectl-version: "v1.23.0" # optional
      helm-version: "v3.10.1" # optional
...
```
