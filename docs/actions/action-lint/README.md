# Description action-lint composite action

This action will lint all actions and workflows of a repository.

```yaml
steps:
  - name: Lint actions and workflows
    uses: bakdata/ci-templates/actions/action-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
```

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT     | DESCRIPTION                                |
| ------------------- | ------ | -------- | ----------- | ------------------------------------------ |
| action-lint-version | string | false    | `"v1.6.22"` | The action lint repository version to use. |
| ref2                | string | false    |             | The ref name to checkout the repository.   |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
