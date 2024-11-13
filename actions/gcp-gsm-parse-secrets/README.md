# gcp-gsm-parse-secrets

Converts a lists of strings of secrets references into screaming snake case. Look at the tests.py for furhter details.

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT        | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                   |
| ------------ | ------ | -------- | ------- | --------------------------------------------- |
| project-name | string | true     |         | GKE project name where the secrets are stored |
| secrets-list | string | true     |         | Secrets to inject into the environment        |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT       | TYPE   | DESCRIPTION                     |
| ------------ | ------ | ------------------------------- |
| secrets-list | string | secret list with correct format |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT        | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                   |
| ------------ | ------ | -------- | ------- | --------------------------------------------- |
| project-name | string | true     |         | GKE project name where the secrets are stored |
| secrets-list | string | true     |         | Secrets to inject into the environment        |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT       | TYPE   | DESCRIPTION                     |
| ------------ | ------ | ------------------------------- |
| secrets-list | string | secret list with correct format |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
