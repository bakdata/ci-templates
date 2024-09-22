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

| INPUT                 | TYPE   | REQUIRED | DEFAULT                                                                | DESCRIPTION                                |
| --------------------- | ------ | -------- | ---------------------------------------------------------------------- | ------------------------------------------ |
| export-to-environment | string | false    | `"true"`                                                               | Export secrets to environment              |
| gke-project-id        | string | true     |                                                                        | GKE project ID for authentication          |
| gke-project-name      | string | true     |                                                                        | GKE project name for authentication        |
| gke-service-account   | string | true     | `"wid-dummy-test-account@gcp-bakdata-cluster.iam.gserviceaccount.com"` | GKE service account key for authentication |
| secrets-to-inject     | string | true     |                                                                        | Secrets to inject into the environment     |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT  | TYPE   | DESCRIPTION                        |
| ------- | ------ | ---------------------------------- |
| secrets | string | Secrets loaded from Secret Manager |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
