# helm-lint
This action will lint helm charts inside the `charts` folder of your repository.

## Prerequisites

You need to create the lint configuration file `.github/lint-config.yaml` and configure it to your liking.
A minimal configuration could look like this:
```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

## Input Parameters
| Name              | Required  |             Default Value             |  Type   | Description                                                                                                                              |
|-------------------|:---------:|:-------------------------------------:|:-------:|------------------------------------------------------------------------------------------------------------------------------------------|
| lint-config-path  |    ❌     |      ".github/lint-config.yaml"       | string  | The path to the lint configuration file (For an example see https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml) |

## Usage

```yaml
...
steps:
  # check out current repository
  - uses: actions/checkout@v2
    with:
      # this is only needed if your workflow runs on pull_requests
      fetch-depth: 0

  # check out ci-templates into ./ci-templates
  - uses: actions/checkout@v2
    with:
      repository: "bakdata/ci-templates"
      path: "ci-templates"

  # set up helm
  - uses: azure/setup-helm@v1
    with:
      version: "v3.4.0"
  
  # lint all charts
  - name: Lint helm charts
    uses: ./ci-templates/helm-lint
    with:
      lint-config-path: "my-lint-config.yaml" # (Optional)
...
```
