# helm-setup

This action will set up everything necessary to deploy or destroy Helm charts.

## Input Parameters

| Name                | Required | Default Value |  Type  | Description                                                                               |
| ------------------- | :------: | :-----------: | :----: | ----------------------------------------------------------------------------------------- |
| python-version      |    ❌    |     3.10      | string | The python version to install                                                             |
| kubectl-version     |    ❌    |    v1.23.0    | string | The kubectl version to install                                                            |
| helm-version        |    ❌    |    v3.10.1    | string | The Helm version to install                                                               |

## Usage

```yaml
...
steps:
  - name: Setup environment
    uses: bakdata/ci-templates/actions/helm-setup@main
    with:
      python-version: "3.10" # optional
      kubectl-version: "v1.23.0" # optional
      helm-version: "v3.10.1" # optional
...
```
