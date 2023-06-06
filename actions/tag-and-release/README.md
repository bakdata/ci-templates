# tag-and-release

This composite action allows you to tag a release a repository.

## Dependencies

This action uses another composite action listed below:

- [action-gh-release](https://github.com/softprops/action-gh-release)

## Input Parameters

| Name         | Required | Default Value | Description                                                                  |
| ------------ | :------: | :-----------: | ---------------------------------------------------------------------------- |
| tag          |    ✅    |       -       | The version of the tag to be publish and released e.g 1.0.0                  |
| release-text |    ✅    |       -       | Text for the github release (this describes the release content / Changelog) |

## Usage

```yaml
steps:
  - name: Check out repository
    uses: actions/checkout@v3

  - name: Release to (Test)PyPI
    uses: bakdata/ci-templates/actions/tag-and-release@main
    with:
      tag: 1.0.0
      release-text: "This should be on the release section on github. Normally a Changelog"
```
