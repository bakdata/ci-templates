# helm-lint

This action will lint all actions and workflows of a repository.

## Prerequisites

You need to create the lint matcher file `actionlint-matcher.json` and configure it to your liking.
The default matcher is the following:

```json
{
  "problemMatcher": [
    {
      "owner": "actionlint",
      "pattern": [
        {
          "regexp": "^(?:\\x1b\\[\\d+m)?(.+?)(?:\\x1b\\[\\d+m)*:(?:\\x1b\\[\\d+m)*(\\d+)(?:\\x1b\\[\\d+m)*:(?:\\x1b\\[\\d+m)*(\\d+)(?:\\x1b\\[\\d+m)*: (?:\\x1b\\[\\d+m)*(.+?)(?:\\x1b\\[\\d+m)* \\[(.+?)\\]$",
          "file": 1,
          "line": 2,
          "column": 3,
          "message": 4,
          "code": 5
        }
      ]
    }
  ]
}
```

## Input Parameters

| Name             | Required |              Default Value              |  Type  | Description                             |
| ---------------- | :------: | :-------------------------------------: | :----: | --------------------------------------- |
| ref              |    ❌    | The branch calling the composite action | string | The ref name to checkout the repository |
| lint-config-path |    ❌    |    ".github/actionlint-matcher.json"    | string | The path to the lint configuration file |

## Usage

```yaml
steps:
  - name: Lint actions and workflows
    uses: bakdata/ci-templates/actions/action-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
      lint-config-path: "my-lint-matcher.json" # (Optional)
```
