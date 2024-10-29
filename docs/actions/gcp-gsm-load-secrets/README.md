# gcp-gsm-load-secrets

This action is set to replace GitHub actions integrated secret management.

## Usage

To load a secret from GSM figure out the following:

- check if the repository has access to the secret
  - repository is owned by bakdata
  - repository is private
  - even if the labels are correctly set, you will need to run Terraform to set the proper roles
  - *TBD*
- use this template:

```yaml
- name: Load secrets
  id: load-secrets
  uses: bakdata/ci-templates/actions/gcp-gsm-load-secrets
  with:
    gke-project-name: <can be found from gcp console>
    gke-project-id: <can be found from gcp console>
    secrets-to-inject: |-
      <secret_name>/<optional version, if not set the latest version is loaded>
      <other_secret>/<optional version, if not set the latest version is loaded>
```

- it is possible to load multiple secrets in the same call
- loaded secrets  will be injected as environment variables and the name will be cannonicalized to SCREAMING_SNAKE_CASE. Example: `i-like_trains__why_this?` -> `I_LIKE_TRAINS_WHY_THIS`

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                      | TYPE   | REQUIRED | DEFAULT  | DESCRIPTION                                   |
| -------------------------- | ------ | -------- | -------- | --------------------------------------------- |
| export-to-environment      | string | false    | `"true"` | Export secrets to environment                 |
| gke-project-name           | string | true     |          | GKE project name for authentication           |
| gke-service-account        | string | true     |          | GKE service account for authentication        |
| secrets-to-inject          | string | true     |          | Secrets to inject into the environment        |
| workload-identity-provider | string | true     |          | Workload identity provider for authentication |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT  | TYPE   | DESCRIPTION                        |
| ------- | ------ | ---------------------------------- |
| secrets | string | Secrets loaded from Secret Manager |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
