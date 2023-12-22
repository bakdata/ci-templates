# Description helm-setup composite action

This action will set up everything necessary to deploy or destroy Helm charts.

## Usage

```yaml
steps:
  - name: Setup environment
    uses: bakdata/ci-templates/actions/helm-setup@main
    with:
      kubectl-version: "v1.23.0" # optional
      helm-version: "v3.10.1" # optional
```
