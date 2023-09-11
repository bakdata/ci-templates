# port-forward

This action creates a port forward for a Kubernetes service and keeps it open in the background.

## Input Parameters

| Name            | Required | Default Value |  Type  | Description                                 |
| --------------- | :------: | :-----------: | :----: | ------------------------------------------- |
| service         |    ✅    |       -       | string | Name of Kubernetes service                  |
| port            |    ✅    |       -       | string | Port to be forwarded                        |
| namespace       |    ✅    |       -       | string | Kubernetes namespace                        |
| kubectl-version |    ❌    |    latest     | string | kubectl version, e.g. `v1.23.0` or `latest` |
| timeout         |    ❌    |      30       | string | Timeout in seconds                          |

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
