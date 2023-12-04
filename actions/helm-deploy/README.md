# helm-deploy

This action will deploy a Helm chart on a Kubernetes cluster.

## Prerequisites

Create a `values.yaml` file according to the documentation of the specific Helm chart you want to install and put it somewhere inside your repository.

## Input Parameters

| Name                | Required | Default Value |  Type  | Description                                                                                       |
| ------------------- | :------: | :-----------: | :----: | ------------------------------------------------------------------------------------------------- |
| release-name        |    ✅     |       -       | string | The release name of the Helm deployment                                                           |
| namespace           |    ✅     |       -       | string | The namespace of the Helm deployment                                                              |
| chart               |    ✅     |       -       | string | The name of the Helm chart                                                                        |
| values-yaml         |    ✅     |       -       | string | File path as string for a single values.yaml file or as JSON array for multiple values.yaml files |
| chart-version       |    ❌     |       -       | string | The version of the Helm chart                                                                     |
| post-renderer       |    ❌     |       -       | string | File path as string for a Helm post renderer                                                      |
| timeout             |    ❌     |     1200      | string | Timeout for the Helm command in seconds                                                           |
| repository-name     |    ❌     |       -       | string | The local name for adding the Helm repository                                                     |
| repository-url      |    ❌     |       -       | string | The url for adding the Helm repository                                                            |
| repository-username |    ❌     |       -       | string | User for the login to the repository                                                              |
| repository-password |    ❌     |       -       | string | Password for the login to the repository                                                          |

## Usage

```yaml
steps:
  - name: Deploy Helm chart
    uses: bakdata/ci-templates/actions/helm-deploy@main
    with:
      release-name: "my-release"
      namespace: "my-namespace"
      chart: "foo/bar" # Installs the chart 'bar' from the repository called 'foo'
      values-yaml: '["bar/values.yaml", "bar/values-1.yaml"]' # or for a single value file just as a string: "bar/values.yaml"
      chart-version: "1.0.0" # optional
      post-renderer: "path/to/post-renderer" # optional
      timeout: "1000" # optional
      repository-name: "foo" # optional
      repository-url: "https://foo.example.com" # optional
      repository-username: "foo" # optional
      repository-password: "bar123" # optional
```
