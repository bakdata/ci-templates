# action-lint

This action will lint all actions and workflows of a repository.

## Input Parameters

| Name                | Required | Default Value |  Type  | Description                                |
| ------------------- | :------: | :-----------: | :----: | ------------------------------------------ |
| ref                 |    ❌    |      ""       | string | The ref name to checkout the repository.   |
| action-lint-version |    ❌    |    v1.6.22    | string | The action lint repository version to use. |

## Usage

```yaml
steps:
  - name: Lint actions and workflows
    uses: bakdata/ci-templates/actions/action-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
```
