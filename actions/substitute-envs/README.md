# substitute-envs

This action will recursively substitute environment variables in a given directory.

## Input Parameters

| Name | Required | Default Value |  Type  | Description                                                  |
| ---- | :------: | :-----------: | :----: | ------------------------------------------------------------ |
| path |    ✅    |       -       | string | Path to the directory to substitute environment variables in |

## Output Parameters

| Name | Description                                        |
| ---- | -------------------------------------------------- |
| path | Path to the temporary directory after substitution |

## Usage

```yaml
---
steps:
  - name: Substitute env variables
    id: substitute
    uses: bakdata/ci-templates/actions/substitute-envs@main
    with:
      path: "path/to/directory"

  - name: Use substitute output
    run: echo "${{ steps.substitute.outputs.path }}"
```
