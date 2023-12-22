# Description java-gradle-publish-plugin composite action

This action uses Gradle to publish Java plugins to the Gradle Plugin Portal.

## Usage

```yaml
steps:
  - name: Publish
    uses: bakdata/ci-templates/actions/java-gradle-publish-plugin@main
    with:
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }}
      signing-key-id: ${{ secrets.signing-key-id }}
      signing-password: ${{ secrets.signing-password }}
      gradle-publish-key: ${{ secrets.gradle-publish-key }}
      gradle-publish-secret: ${{ secrets.gradle-publish-secret }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```
