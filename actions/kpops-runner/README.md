# kpops-runner

This action runs Kpops with the given config.

## Input Parameters

| Name              | Required | Default Value |                                                     Type                                                      | Description                                                                     |
| ----------------- | :------: | :-----------: | :-----------------------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------- |
| mode              |    ✅    |       -       | 													string  										           | command mode used by Kpops (deploy, destroy, reset, clean)) for possible values |
| pipeline          |    ✅    |       -       |                                                    string                                                     | Pipeline file to be run by Kpops publication                                    |
| working-directory |    ❌    |       .       |                                                    string                                                     | root directory used by Kpops to run pipelines                                   |
| execute           |    ❌    |  	false     |												 		boolean	  													| Execute Kpops command (this applies the infrastructure changes that were executed inside the dry-run command) |
| defaults          |    ❌    |    defaults   | 													string 														|  defaults folder path 														|
| config          |    ❌    |    config.yaml   | 													string 														|  default config.yaml file path 														|



## Usage

```yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/kpops-runner@main
    with:
      mode: deploy
      working-directory: home/my-kpops-root-dir
      pipeline: pipelines/my-pipeline-file.yaml
      execute: true
```
