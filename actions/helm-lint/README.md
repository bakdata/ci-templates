# helm-lint
To use this action you need to have a few things setup in the repository:

1. Add a `./github/lint-config.yaml` file with the following content and set the target branch to the default branch of your repository:
```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

2. Add the following steps to your workflow:
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
  
  # lint all charts
  - name: Lint helm charts
    uses: ./ci-templates/helm-lint
```
