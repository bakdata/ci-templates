# helm-destroy

This action will destroy a Helm chart on a Kubernetes cluster.

## Input Parameters

| Name         | Required | Default Value |  Type  | Description                             |
| ------------ | :------: | :-----------: | :----: | --------------------------------------- |
| release-name |    ✅    |       -       | string | The release name of the Helm deployment |
| namespace    |    ✅    |       -       | string | The namespace of the Helm deployment    |

## Usage

```yaml
steps:
  - name: Destroy Helm chart
    uses: bakdata/ci-templates/actions/helm-destroy@main
    with:
      release-name: "my-release"
      namespace: "my-namespace"
```
