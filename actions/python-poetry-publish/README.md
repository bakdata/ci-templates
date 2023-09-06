# python-poetry-publish

This composite action uses Poetry to build and publish your Python packages to a package index.

## Input Parameters

| Name              | Required | Default Value | Description                                        |
| ----------------- | :------: | :-----------: | -------------------------------------------------- |
| index-name        |    ✅    |       -       | The package index name for publishing packages     |
| index-url         |    ✅    |       -       | The package index url for publishing packages      |
| index-username    |    ✅    |       -       | The package index username for publishing packages |
| index-password    |    ✅    |       -       | The package index password for publishing packages |
| working-directory |    ❌    |     "./"      | The working directory of your Python package.      |

## Usage

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@v1.26.0

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
