# Description of helm-release reusable Workflow

This workflow will lint a Helm chart, bump its version according to the `.bumpversion.cfg` file, package the chart, update the Helm index, and deploy it on GitHub pages.

## Prerequisites

Your Helm chart and `.bumpversion.cfg` need to be located inside the `charts-dir` folder of your repository (repository root by default) to use this workflow. A minimal configuration with `charts-dir=charts` could look like this:

```cfg
[bumpversion]
current_version = 0.0.1

[bumpversion:file:charts/Chart.yaml]
search = version: {current_version}
replace = version: {new_version}
```

Additionally, you need to create the lint configuration file `.github/lint-config.yaml` and configure it to your liking.
A minimal configuration could look like this:

```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

Moreover, choose a GitHub user who will commit and push the changes. Make sure to configure admin access to the repository for the selected user because admins can still push on the default branch
even if there is a protection rule in place.

Finally, set up GitHub pages for your repository in Settings → Pages → Build and deployment source → GitHub Actions. A special `gh-pages` branch is not needed, since we will use GitHub actions to deploy a Pages artifact.
Currently, it is not possible to download a previously created Pages artifact as they quickly expire after deploying it. When releasing an update to a Helm chart, we want to keep all previous versions of the Helm chart available. Therefore, as a workaround, we download the `index.yaml` file from Pages, parse all referenced releases and download these .tgz packages from Pages as well. Then we package the new version and update the index. Afterward, a new Pages artifact is created from these files and finally deployed.

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT            | TYPE    | REQUIRED | DEFAULT                                           | DESCRIPTION                                                                                                                |
| ---------------- | ------- | -------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| artifact-dir     | string  | false    | `"artifact"`                                      | Directory inside `charts-dir` for preparation of the GitHub pages artifact.                                                |
| charts-dir       | string  | false    | `"."`                                             | The directory containing the Helm chart and `.bumpversion.cfg` file.                                                       |
| helm-version     | string  | false    | `"v3.10.1"`                                       | The Helm version.                                                                                                          |
| lint-config-path | string  | false    | `".github/lint-config.yaml"`                      | The path to the lint configuration file (See https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml). |
| page-url         | string  | true     |                                                   | URL to the GitHub pages website of the repository.                                                                         |
| ref              | string  | false    | `"${{ github.event.repository.default_branch }}"` | The ref name to checkout the repository.                                                                                   |
| release-type     | string  | true     |                                                   | Scope of the release (major, minor or patch).                                                                              |
| skip-download    | boolean | false    | `false`                                           | Skip downloading index.yaml and previous Chart versions from GitHub pages. (To be used during setup of this workflow)      |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | VALUE                                                | DESCRIPTION                                      |
| --------------- | ---------------------------------------------------- | ------------------------------------------------ |
| old-version     | `"${{ jobs.helm-release.outputs.old-version }}"`     | The old version in your `.bumpversion.cfg` file. |
| release-version | `"${{ jobs.helm-release.outputs.release-version }}"` | The bumped version.                              |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
