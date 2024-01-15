<h1>Description setup-credentials composite action</h1>

This action will set up authentication for GCloud and a Google Kubernetes Engine cluster.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Setup environment
    uses: bakdata/ci-templates/actions/setup-credentials@main
    with:
      gke-service-account: ${{ secrets.GKE<em>SERVICE</em>ACCOUNT }}
      gke-project: "my-awesome-project"
      gke-region: "us-west1"
      gke-cluster: "my-awesome-cluster"
      gcloud-sdk-version: "376.0.0" # optional
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|        INPUT        |  TYPE  | REQUIRED |   DEFAULT   |                DESCRIPTION                 |
|---------------------|--------|----------|-------------|--------------------------------------------|
| gcloud-sdk-version  | string |  false   | <code>"376.0.0"</code> |             GCloud SDK version             |
|     gke-cluster     | string |   true   |             |       GKE cluster for authentication       |
|     gke-project     | string |   true   |             |     GKE project id for authentication      |
|     gke-region      | string |   true   |             |       GKE region for authentication        |
| gke-service-account | string |   true   |             | GKE service account key for authentication |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
