# Refenrences checkout composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT                      | DESCRIPTION                                                                   |
| ------------------- | ------ | -------- | ---------------------------- | ----------------------------------------------------------------------------- |
| cache               | string | false    | `"true"`                     | Describes if the repository is using any LFS files                            |
| fetch-depth         | string | false    | `"1"`                        | Number of commits to fetch. 0 indicates all history for all branches and tags |
| lfs                 | string | false    | `"false"`                    | Describes if the repository is using any LFS files                            |
| persist-credentials | string | false    | `"true"`                     | Whether to configure the token or SSH key with the local git config           |
| ref                 | string | false    |                              | The branch, tag or SHA to checkout                                            |
| repository          | string | false    | `"${{ github.repository }}"` | The repository name with owner                                                |
| token               | string | false    | `"${{ github.token }}"`      | Personal access token (PAT) used to fetch the repository                      |

<!-- AUTO-DOC-INPUT:END -->

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT               | TYPE   | REQUIRED | DEFAULT                      | DESCRIPTION                                                                   |
| ------------------- | ------ | -------- | ---------------------------- | ----------------------------------------------------------------------------- |
| cache               | string | false    | `"true"`                     | Describes if the repository is using any LFS files                            |
| fetch-depth         | string | false    | `"1"`                        | Number of commits to fetch. 0 indicates all history for all branches and tags |
| lfs                 | string | false    | `"false"`                    | Describes if the repository is using any LFS files                            |
| persist-credentials | string | false    | `"true"`                     | Whether to configure the token or SSH key with the local git config           |
| ref                 | string | false    |                              | The branch, tag or SHA to checkout                                            |
| repository          | string | false    | `"${{ github.repository }}"` | The repository name with owner                                                |
| token               | string | false    | `"${{ github.token }}"`      | Personal access token (PAT) used to fetch the repository                      |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT        | TYPE   | DESCRIPTION                                                      |
| ------------- | ------ | ---------------------------------------------------------------- |
| lfs-cache-hit | string | A boolean value to indicate an exact match was found for the key |

<!-- AUTO-DOC-OUTPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT        | TYPE   | DESCRIPTION                                                      |
| ------------- | ------ | ---------------------------------------------------------------- |
| lfs-cache-hit | string | A boolean value to indicate an exact match was found for the key |

<!-- AUTO-DOC-OUTPUT:END -->
