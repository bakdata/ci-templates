# java-maven-release

This action releases Java Maven artifacts by createing a tag on GitHub.

## Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                        |
| ----------------- | :------: | :-----------: | :----: | -------------------------------------------------------------------------------------------------- |
| release-type      |    ✅     |       -       | string | Scope of the release                                                                               |
| github-email      |    ✅     |       -       | string | GitHub email for requesting changes from API                                                       |
| github-username   |    ✅     |       -       | string | GitHub username for requesting changes from API                                                    |
| github-token      |    ✅     |       -       | string | GitHub token for requesting changes from API                                                       |
| maven-version     |    ✅     |       -       | string | Maven version to be installed                                                                      |
| java-distribution |    ❌     |   microsoft   | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed |
| java-version      |    ❌     |      11       | string | Java version to be installed                                                                       |
| working-directory |    ❌     |      "."      | string | Working directory of your Maven artifacts                                                          |

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
