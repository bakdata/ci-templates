# Description java-gradle-build-jib composite action

This action builds an image tarball using [Jib Gradle](https://github.com/GoogleContainerTools/jib/tree/master/jib-gradle-plugin) and uploads an `image.tar` file as an artifact.

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
