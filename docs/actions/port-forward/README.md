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

## Dependencies

- [azure/setup-kubectl@v3](https://github.com/azure/setup-kubectl/tree/v3)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT           | TYPE   | REQUIRED | DEFAULT    | DESCRIPTION                                 |
| --------------- | ------ | -------- | ---------- | ------------------------------------------- |
| kubectl-version | string | false    | `"latest"` | kubectl version, e.g. `v1.23.0` or `latest` |
| namespace       | string | true     |            | Kubernetes namespace                        |
| port            | string | true     |            | Port to be forwarded                        |
| service         | string | true     |            | Name of Kubernetes service                  |
| timeout         | string | false    | `"30"`     | Timeout for portfowrd                       |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
