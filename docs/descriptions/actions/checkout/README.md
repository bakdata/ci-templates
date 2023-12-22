# Description checkout composite action

This composite action will checkout your repository and allow you to handle [LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) and [Caching](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows) if needed.

## Prerequisites

Make sure your [LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage) is properly configured.

### Dependencies

This workflow is built from other composite actions listed below:

- [actions/checkout](https://github.com/actions/checkout)
- [actions/cache](https://github.com/actions/cache)

## Usage

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@main
    with:
      lfs: "true"
  - name: print files
    shell: bash
    run: ls -al .
```
