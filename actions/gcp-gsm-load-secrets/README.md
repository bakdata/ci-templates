# gcp-gsm-load-secrets

This action is set to replace GitHub actions integrated secret management.

## How to use

To load a secret from GSM figure out the following:

- check if the repository has access to the secret
  - repository is owned by bakdata
  - repository is private
  - even if the labels are correctly set, you will need to run Terraform to set the proper roles
  - _TBD_
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
- loaded secrets will be injected as environment variables and the name will be cannonicalized to SCREAMING_SNAKE_CASE. Example: `i-like_trains__why_this?` -> `I_LIKE_TRAINS_WHY_THIS`