# java-gradle-build-jib-image

This action builds a Jib image using Gradle and uploads an `image.tar` file as a pipeline artifact.

## Input Parameters

| Name                | Required | Default Value  |  Type  | Description                                                                                |
| ------------------- | :------: | :------------: | :----: | ------------------------------------------------------------------------------------------ |
| image-artifact-name |    ❌    | image-artifact | string | Artifact name to upload Jib Docker image, see <https://github.com/actions/upload-artifact> |
| java-distribution   |    ❌    |   microsoft    | string | Java distribution to be installed                                                          |
| java-version        |    ❌    |       11       | string | Java version to be installed                                                               |
| gradle-version      |    ❌    |    wrapper     | string | Gradle version to be installed                                                             |
| working-directory   |    ❌    |      "./"      | string | Working directory of your Gradle artifacts                                                 |

## Usage

```yaml

---
steps:
  - name: Build Jib image
    uses: bakdata/ci-templates/actions/java-gradle-build-jib-image@main
    with:
      image-artifact-name: "image-artifact" # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "./" # (Optional)
```
