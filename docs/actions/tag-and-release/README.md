# Description tag-and-release composite action

This composite action allows you to create a Git tag and GitHub release.

## Dependencies

This action uses another composite action listed below:

- [action-gh-release](https://github.com/softprops/action-gh-release)

## Usage

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@1.32.0

  - name: Tag and release project
    uses: bakdata/ci-templates/actions/tag-and-release@main
    with:
      tag: "1.0.0"
      release-title: "This should be the title for the GitHub release"
      release-body: "This should be on the text part of the GitHub release"
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT           | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                        |
| --------------- | ------ | -------- | ------- | -------------------------------------------------- |
| github-email    | string | true     |         | The GitHub email for committing the changes.       |
| github-token    | string | true     |         | The GitHub token for committing the changes.       |
| github-username | string | true     |         | The GitHub username for committing the changes.    |
| release-body    | string | false    |         | Description for the GitHub release.                |
| release-title   | string | true     |         | Title for the GitHub release.                      |
| tag             | string | true     |         | The version of the tag to be released, e.g. 1.0.0. |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
