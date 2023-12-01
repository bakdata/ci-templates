# Refenrences port-forward composite action

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT           | TYPE   | REQUIRED | DEFAULT    | DESCRIPTION                                 |
| --------------- | ------ | -------- | ---------- | ------------------------------------------- |
| kubectl-version | string | false    | `"latest"` | kubectl version, e.g. `v1.23.0` or `latest` |
| namespace       | string | true     |            | Kubernetes namespace                        |
| port            | string | true     |            | Port to be forwarded                        |
| service         | string | true     |            | Name of Kubernetes service                  |
| timeout         | string | false    | `"30"`     | Timeout for portfowrd                       |

<!-- AUTO-DOC-INPUT:END -->

## Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->
