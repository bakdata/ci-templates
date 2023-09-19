# java-maven-release-github

This action releases Java Maven Artifacts.

## Input Parameters

| Name              | Required | Default Value |  Type  | Description                                                                                        |
| ----------------- | :------: | :-----------: | :----: | -------------------------------------------------------------------------------------------------- |
| github-username   |    ✅    |       -       | string | GitHub username for requesting changes from API                                                    |
| github-token      |    ✅    |       -       | string | GitHub token for requesting changes from API                                                       |
| java-distribution |    ❌    |   microsoft   | string | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed |
| java-version      |    ❌    |      11       | string | Java version to be installed                                                                       |
| maven-version     |    ❌    |    wrapper    | string | Maven version to be installed                                                                      |
| working-directory |    ❌    |      "."      | string | Working directory of your Maven artifacts                                                          |

## Usage

```yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-maven-release-github@main
    with:
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      maven-version: "3.8.2"
      working-directory: "." # (Optional)
```
