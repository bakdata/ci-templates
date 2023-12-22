# Description python-poetry-publish composite action

This composite action uses Poetry to build and publish your Python packages to a package index.

## Usage

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@1.32.0

    # Other steps in your workflow

  - name: Publish to package index
    uses: bakdata/ci-templates/actions/python-poetry-publish@main
    with:
      index-name: index
      index-url: example.org/simple/
      index-username: user123
      index-password: supersecret
      working-directory: ${{ inputs.working-directory }}
```
