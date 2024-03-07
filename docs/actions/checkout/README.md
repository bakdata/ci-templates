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

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT                      | DESCRIPTION                                                                                                      |
| ------------------- | ------ | -------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| cache               | string | false    | `"true"`                     | Describes if the repository is using any LFS files                                                               |
| fetch-depth         | string | false    | `"1"`                        | Number of commits to fetch. 0 indicates all history for all branches and tags                                    |
| lfs                 | string | false    | `"false"`                    | Describes if the repository is using any LFS files                                                               |
| persist-credentials | string | false    | `"true"`                     | Whether to configure the token or SSH key with the local git config                                              |
| ref                 | string | false    |                              | The branch, tag or SHA to checkout                                                                               |
| repository          | string | false    | `"${{ github.repository }}"` | The repository name with owner                                                                                   |
| submodules          | string | false    | `"false"`                    | Whether to checkout submodules: `true` to checkout submodules or `recursive` to recursively checkout submodules. |
| token               | string | false    | `"${{ github.token }}"`      | Personal access token (PAT) used to fetch the repository                                                         |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT        | TYPE   | DESCRIPTION                                                      |
| ------------- | ------ | ---------------------------------------------------------------- |
| lfs-cache-hit | string | A boolean value to indicate an exact match was found for the key |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
