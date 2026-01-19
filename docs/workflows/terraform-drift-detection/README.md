# Description of terraform-drift-detection reusable Workflow

This workflow regularly checks for drift between your infrastructure and your Terraform configuration.

## Prerequisites

Prepare a GCP Service Account and a Workload Identity Provider to authenticate with Google Cloud.

## Dependencies

This workflow is built from the following actions:

- [checkout](https://github.com/bakdata/ci-templates/tree/main/actions/checkout)
- [google-github-actions/auth](https://github.com/google-github-actions/auth)
- [hashicorp/setup-terraform](https://github.com/hashicorp/setup-terraform)

## Calling the workflow

```yaml
name: Scheduled Drift Detection

on:
  schedule:
    # Run every day at 08:00 UTC
    - cron: "0 8 * * *"
  workflow_dispatch: # Allow manual triggering

jobs:
  detect-drift:
    uses: bakdata/ci-templates/.github/workflows/terraform-drift-detection.yaml@main
    with:
      working-directory: "infrastructure/prod"
      gcp-project-id: "your-gcp-project-id"
      source-branch: "main"
    secrets:
      google-workload-identity-provider: ${{ secrets.GOOGLE_WORKLOAD_IDENTITY_PROVIDER }}
      google-service-account: ${{ secrets.GOOGLE_SERVICE_ACCOUNT }}
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->
<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->
<!-- AUTO-DOC-SECRETS:END -->
