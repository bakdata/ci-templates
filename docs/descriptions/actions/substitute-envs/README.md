# Description substitute-envs composite action

This action will recursively substitute environment variables in a given directory.

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
