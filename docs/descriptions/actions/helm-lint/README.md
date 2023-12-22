# Description helm-lint composite action

This action will lint Helm charts inside the `charts` folder of your repository.

## Prerequisites

You need to create the lint configuration file `.github/lint-config.yaml` and configure it to your liking.
A minimal configuration could look like this:

```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

## Usage

```yaml
steps:
  - name: Lint helm charts
    uses: bakdata/ci-templates/actions/helm-lint@main
    with:
      ref: "my-awesome-ref" # (Optional)
      lint-config-path: "my-lint-config.yaml" # (Optional)
      helm-version: "v3.10.1" # (Optional)
```
