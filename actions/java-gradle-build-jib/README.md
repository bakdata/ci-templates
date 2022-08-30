# java-gradle-build-jib

This action builds an image tarball using [Jib Gradle](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) and uploads an `image.tar` file as an artifact.

## Input Parameters

| Name                | Required | Default Value  |  Type  | Description                                                                                                   |
| ------------------- | :------: | :------------: | :----: | ------------------------------------------------------------------------------------------------------------- |
| image-artifact-name |    ❌    | image-artifact | string | Artifact name to upload tarball image, see <https://github.com/actions/upload-artifact>                    |
| java-distribution   |    ❌    |   microsoft    | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version        |    ❌    |       11       | string | Java version to be installed                                                                                  |
| gradle-version      |    ❌    |    wrapper     | string | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| working-directory   |    ❌    |      "."       | string | Working directory of your Gradle artifacts                                                                    |

## Usage

```yaml
steps:
  - name: Build tarball image
    uses: bakdata/ci-templates/actions/java-gradle-build-jib@main
    with:
      image-artifact-name: "image-artifact" # (Optional)
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```
