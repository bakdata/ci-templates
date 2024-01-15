<h1>Description port-forward composite action</h1>

This action creates a port forward for a Kubernetes service and keeps it open in the background.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Setup port forward Kafka Connect
    uses: bakdata/ci-templates/actions/port-forward@main
    with:
      service: k8kafka-cp-kafka-connect
      port: 8083
      namespace: infrastructure
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|      INPUT      |  TYPE  | REQUIRED |  DEFAULT   |                 DESCRIPTION                 |
|-----------------|--------|----------|------------|---------------------------------------------|
| kubectl-version | string |  false   | <code>"latest"</code> | kubectl version, e.g. <code>v1.23.0</code> or <code>latest</code> |
|    namespace    | string |   true   |            |            Kubernetes namespace             |
|      port       | string |   true   |            |            Port to be forwarded             |
|     service     | string |   true   |            |         Name of Kubernetes service          |
|     timeout     | string |  false   |   <code>"30"</code>   |            Timeout for portfowrd            |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
