# python-poetry-release

This composite action uses Poetry to build and push your Python packages either to TestPyPI or PyPI.

## Dependencies

This action uses another composite action listed below:

- [python-setup-poetry](https://github.com/bakdata/ci-templates/tree/main/actions/python-setup-poetry)

## Input Parameters

| Name         | Required | Default Value | Description                                                                  |
| ------------ | :------: | :-----------: | ---------------------------------------------------------------------------- |
| tag          |    ✅    |       -       | The version of the tag to be publish and released e.g 1.0.0                  |
| release-text |    ✅    |       -       | Text for the github release (this describes the release content / Changelog) |

|

## Usage

```yaml
steps:
  - name: Check out repository
    uses: actions/checkout@v3
    with:
      persist-credentials: false # required for pushing changed pyproject.toml

  - name: Release to (Test)PyPI
    uses: bakdata/ci-templates/actions/tag-and-release@main
    with:
        tag: 1.0.0
        release-text: "This should be on the release section on github. Normally a Changelog"
```
