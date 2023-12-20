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
