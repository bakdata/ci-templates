# ci-templates

This is a collection of reusable workflows and composite actions for GitHub that Bakdata uses for open-source projects.

## Using reusable workflows

You can use reusable workflows in this repository like this:

```yaml
---
jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/my-workflow.yaml@main
    with:
      foo: bar
```

## Using composite actions

You can use composite actions in this repository like this:

```yaml
---
steps:
  - uses: bakdata/ci-templates/actions/my-action@main
    with:
      foo: bar
```

## Pre-commit

We are using pre-commit in this repository to automatically create the documentation. Make sure you install it [here](https://pre-commit.com/#install).

Also, follow the following steps to ensure that you can create the documentation locally:

### install `auto-doc` which is the software used for documentation generation:

- On MacOS:
  - using brew: `brew install auto-doc`
  - using the GitHub repository:
    ```shell
    wget https://github.com/tj-actions/auto-doc/releases/download/v3.4.0/auto-doc_3.4.0_Darwin_arm64.tar.gz
    tar -xf auto-doc_3.4.0_Darwin_arm64.tar.gz
    ```
- Linux:
  - using the GitHub repository:
    ```shell
    wget https://github.com/tj-actions/auto-doc/releases/download/v3.4.0/auto-doc_3.4.0_Linux_x86_64.tar.gz
    tar -xf auto-doc_3.4.0_Linux_x86_64.tar.gz
    ```

### Use `auto-doc`

In case you used the GitHub repository to install `auto-doc` make sure you set the path to the executable file as an environment variable before running the pre-commit command:

```shell
export DOC_CMD=./auto-doc
```

### Run pre-commit

Is mandatory to run pre-commit before pushing your changes. This can be done in two ways:

#### manually

Run the pre-commit every time before pushing your changes:

```shell
pre-commit run --all-files
```

#### automatically (strongly recommended)

You can let your pre-commit run automatically every time you execute a `git commit` command without having to do it on your own. To do so, run the following command locally just once in the root directory of this repository:

```shell
pre-commit install
```
