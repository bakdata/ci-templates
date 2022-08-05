# helm-gke-deploy

This action will deploy a helm chart on a Google Kubernetes Engine cluster.

## Prerequisites

Create a `values.yaml` file according to the documentation of the specific helm chart you want to install and put it somewhere inside your repository.

## Input Parameters

| Name                | Required | Default Value |  Type  | Description                                                                                       |
|---------------------|:--------:|:-------------:|:------:|---------------------------------------------------------------------------------------------------|
| gke-service-account |    ✅     |       -       | string | The service account key for accessing the Google Kubernetes Engine cluster                        |
| gke-project         |    ✅     |       -       | string | The name of the Google Cloud project that the Google Kubernetes Engine cluster belongs to         |
| gke-region          |    ✅     |       -       | string | The name of the Google Cloud region that the Google Kubernetes Engine cluster belongs to          |
| gke-cluster         |    ✅     |       -       | string | The name of the Google Kubernetes engine cluster                                                  |
| release-name        |    ✅     |       -       | string | The release name of the helm deployment                                                           |
| namespace           |    ✅     |       -       | string | The namespace of the helm deployment                                                              |
| chart               |    ✅     |       -       | string | The name of the helm chart                                                                        |
| chart-version       |    ✅     |       -       | string | The version of the helm chart                                                                     |
| values-yaml         |    ✅     |       -       | string | File path as string for a single values.yaml file or as JSON array for multiple values.yaml files |
| repository-name     |    ❌     |       -       | string | The local name for adding the helm repository                                                     |
| repository-url      |    ❌     |       -       | string | The url for adding the helm repository                                                            |
| python-version      |    ❌     |     3.10      | string | The python version to install                                                                     |
| gcloud-sdk-version  |    ❌     |    376.0.0    | string | The Google Cloud SDK version to install                                                           |
| kubectl-version     |    ❌     |    v1.23.0    | string | The kubectl version to install                                                                    |
| helm-version        |    ❌     |    v3.8.1     | string | The helm version to install                                                                       |

## Usage

```yaml
...
steps:
  - name: Deploy helm chart
    uses: bakdata/ci-templates/actions/helm-gke-deploy@main
    with:
      gke-service-account: ${{ secrets.GKE_SERVICE_ACCOUNT }}
      gke-project: "my-awesome-project"
      gke-region: "us-west1"
      gke-cluster: "my-awesome-cluster"
      release-name: "my-release"
      namespace: "my-namespace"
      chart: "foo/bar" # Installs the chart 'bar' from the repository called 'foo'
      chart-version: "1.0.0"
      values-yaml: '["bar/values.yaml", "bar/values-1.yaml"]' # or for a single value file just as a string: "bar/values.yaml"
      repository-name: "foo" # optional
      repository-url: "https://foo.example.com" # optional
      python-version: "3.10" # optional
      gcloud-sdk-version: "376.0.0" # optional
      kubectl-version: "v1.23.0" # optional
      helm-version: "v3.8.1" # optional
...
```
