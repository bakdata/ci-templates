# kpops-runner

This action runs Kpops with the given config.

## Input Parameters

| Name                    | Required | Default Value |  Type  | Description                                                                                                   |
| ----------------------- | :------: | :-----------: | :----: | ------------------------------------------------------------------------------------------------------------- |
| mode |    ✅    |       -       | string | command mode used by Kpops (deploy, destroy, reset, clean)                                                |
| working-directory          |    ✅    |       .      | string | root directory used by Kpops to run pipelines                                                                   |
| pipeline       |    ✅    |       -       | string | Pipeline file to be run by Kpops publication                                                                 |
| execute      |    ✅    |       false       | boolean | Execute Kpops command (this applies the infrastructure changes that were executed inside the dry-run command)                                                                    |
| defaults   |    ✅    |       defaults      | string | defaults folder path                                                                 |
| config       |    ✅    |   config   | string | default config.yaml file path            |
