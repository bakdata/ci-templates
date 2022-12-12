# Kpops-Runner

This action runs Kpops with the given config.

## Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                                   |
| ----------------- | :------: | :-----------: | :----: | ------------------------------------------------------------------------------------------------------------- |
| mode              |    ✅    |       -       | string | command mode used by Kpops (deploy, destroy, reset, clean) for possible values                                |
| pipeline          |    ✅    |       -       | string | Pipeline file to be run by Kpops publication                                                                  |
| working-directory |    ❌    |       .       | string | root directory used by Kpops to run pipelines                                                                 |
| execute           |    ❌    |     false     | string | Execute Kpops command (this applies the infrastructure changes that were executed inside the dry-run command) |
| defaults          |    ❌    |   defaults    | string | defaults folder path                                                                                          |
| config            |    ❌    |  config.yaml  | string | config.yaml file path                                                                                         |
| components        |    ❌    |       -       | string | components package path                                                                                       |
| kpops-version     |    ❌    |   0.2.0.dev20221202163038  | string | kpops version used to deploy pipeline  |

## Usage

```yaml
steps:
  - name: Deploy Kafka pipeline
    uses: bakdata/ci-templates/actions/kpops-runner@main
    with:
      mode: deploy
      working-directory: home/my-kpops-root-dir
      pipeline: pipelines/my-pipeline-file.yaml
      execute: true
```
