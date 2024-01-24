# Description helm-deploy composite action

This action will deploy a Helm chart on a Kubernetes cluster.

## Prerequisites

Create a `values.yaml` file according to the documentation of the specific Helm chart you want to install and put it somewhere inside your repository.

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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT  | DESCRIPTION                                                                                     |
| ------------------- | ------ | -------- | -------- | ----------------------------------------------------------------------------------------------- |
| chart               | string | true     |          | Helm chart to deploy                                                                            |
| chart-version       | string | false    |          | Chart Version                                                                                   |
| namespace           | string | true     |          | K8s namespace to deploy in                                                                      |
| post-renderer       | string | false    |          | File path as string for a Helm post renderer                                                    |
| release-name        | string | true     |          | Helm release name                                                                               |
| repository-name     | string | false    |          | Helm repository name                                                                            |
| repository-password | string | false    |          | Password for the login to the repository                                                        |
| repository-url      | string | false    |          | Url of the repository                                                                           |
| repository-username | string | false    |          | User for the login to the repository                                                            |
| timeout             | string | false    | `"1200"` | Timeout for the Helm command in seconds                                                         |
| values-yaml         | string | true     |          | File path as string for a single Helm value file or as json array for multiple Helm value files |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
