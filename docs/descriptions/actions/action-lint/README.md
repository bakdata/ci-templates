# Description action-lint composite action

This action will lint all actions and workflows of a repository.

```yaml
steps:
  - name: Lint actions and workflows
    uses: bakdata/ci-templates/actions/action-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
```
