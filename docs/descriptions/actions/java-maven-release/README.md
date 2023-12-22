# Description java-maven-release composite action

This action releases Java Maven artifacts by creating a tag on GitHub.

## Usage

```yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-maven-release@main
    with:
      release-type: "patch"
      github-email: ${{ secrets.github-email }}
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      maven-version: "3.8.2"
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      working-directory: "." # (Optional)
```
