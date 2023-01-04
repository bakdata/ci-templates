# action-lint

This action will lint all actions and workflows of a repository.

## Input Parameters

| Name | Required |              Default Value              |  Type  | Description                             |
| ---- | :------: | :-------------------------------------: | :----: | --------------------------------------- |
| ref  |    ❌    | The branch calling the composite action | string | The ref name to checkout the repository |

## Usage

```yaml
steps:
  - name: Lint actions and workflows
    uses: bakdata/ci-templates/actions/action-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
```
