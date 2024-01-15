<h1>Description checkout composite action</h1>

This composite action will checkout your repository and allow you to handle <a href="https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage">LFS</a> and <a href="https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows">Caching</a> if needed.

<h2>Prerequisites</h2>

Make sure your <a href="https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage">LFS</a> is properly configured.

<h3>Dependencies</h3>

This workflow is built from other composite actions listed below:

<ul>
<a href="https://github.com/actions/checkout">actions/checkout</a>
<a href="https://github.com/actions/cache">actions/cache</a>
</ul>

<h2>Usage</h2>

<code>yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@main
    with:
      lfs: "true"
  - name: print files
    shell: bash
    run: ls -al .
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |           DEFAULT            |                                  DESCRIPTION                                  |
|---------------------|--------|----------|------------------------------|-------------------------------------------------------------------------------|
|        cache        | string |  false   |           <code>"true"</code>           |              Describes if the repository is using any LFS files               |
|     fetch-depth     | string |  false   |            <code>"1"</code>             | Number of commits to fetch. 0 indicates all history for all branches and tags |
|         lfs         | string |  false   |          <code>"false"</code>           |              Describes if the repository is using any LFS files               |
| persist-credentials | string |  false   |           <code>"true"</code>           |      Whether to configure the token or SSH key with the local git config      |
|         ref         | string |  false   |                              |                      The branch, tag or SHA to checkout                       |
|     repository      | string |  false   | <code>"${{ github.repository }}"</code> |                        The repository name with owner                         |
|        token        | string |  false   |   <code>"${{ github.token }}"</code>    |           Personal access token (PAT) used to fetch the repository            |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|    OUTPUT     |  TYPE  |                           DESCRIPTION                            |
|---------------|--------|------------------------------------------------------------------|
| lfs-cache-hit | string | A boolean value to indicate an exact match was found for the key |

<!-- AUTO-DOC-OUTPUT:END -->
