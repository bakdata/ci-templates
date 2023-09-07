# checkout

This composite action will checkout your repository and allow you to handle [LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) and [Caching](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows) if needed.

## Prerequisites

Make sure your [LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage) is properly configured.

### Dependencies

This workflow is built from other composite actions listed below:

- [actions/checkout](https://github.com/actions/checkout)
- [actions/cache](https://github.com/actions/cache)

### Input Parameters

| Name                | Required |       Default Value        |  Type  | Description                                                                                                  |
| ------------------- | :------: | :------------------------: | :----: | ------------------------------------------------------------------------------------------------------------ |
| cache               |    ❌    |           "true"           | string | Whether to cache the LFS files in this repository. This variable has an impact only if lfs is set to `true`. |
| fetch-depth         |    ❌    |            "1"             | string | Number of commits to fetch. 0 indicates all history for all branches and tags.                               |
| lfs                 |    ❌    |          "false"           | string | Define whether to use LFS files.                                                                             |
| persist-credentials |    ❌    |           "true"           | string | Whether to configure the token or SSH key with the local git config.                                         |
| ref                 |    ❌    |             ""             | string | The branch, tag or SHA to checkout.                                                                          |
| repository          |    ❌    | "${{ github.repository }}" | string | The repository name with owner.                                                                              |
| token               |    ❌    |   "${{ github.token }}"    | string | Personal access token (PAT) used to fetch the repository.                                                    |

### Outputs

| Name          | Description                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| lfs-cache-hit | A [boolean value](https://github.com/actions/cache#outputs) to indicate an exact match was found for the key. |

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