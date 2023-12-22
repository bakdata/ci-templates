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
