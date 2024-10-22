# Description port-forward composite action

This action creates a port forward for a Kubernetes service and keeps it open in the background.

## Usage

```yaml
steps:
  - name: Setup port forward Kafka Connect
    uses: bakdata/ci-templates/actions/port-forward@main
    with:
      service: k8kafka-cp-kafka-connect
      port: 8083
      namespace: infrastructure
```

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
