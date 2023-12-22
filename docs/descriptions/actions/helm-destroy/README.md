# Description helm-destroy composite action

This action will destroy a Helm chart on a Kubernetes cluster.

## Usage

```yaml
steps:
  - name: Destroy Helm chart
    uses: bakdata/ci-templates/actions/helm-destroy@main
    with:
      release-name: "my-release"
      namespace: "my-namespace"
```
