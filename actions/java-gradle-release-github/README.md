# java-gradle-release-github

This action releases Java Gradle Artifacts and a generated changelog on Github.

## Input Parameters

| Name              | Required | Default Value  |  Type   | Description                                                                                                   |
| ----------------- | :------: | :------------: | :-----: | ------------------------------------------------------------------------------------------------------------- |
| changelog-file    |    ❌     | "CHANGELOG.md" | string  | Path to the Changelog.md file                                                                                 |
| github-username   |    ✅     |       -        | string  | GitHub username for requesting changes from API                                                               |
| github-token      |    ✅     |       -        | string  | GitHub token for requesting changes from API                                                                  |
| java-distribution |    ❌     |   microsoft    | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version      |    ❌     |       11       | string  | Java version to be installed                                                                                  |
| gradle-version    |    ❌     |    wrapper     | string  | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| gradle-cache      |    ❌     |      true      | boolean | Whether Gradle caching is enabled or not                                                                      |
| working-directory |    ❌     |      "."       | string  | Working directory of your Gradle artifacts                                                                    |

## Usage

```yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-gradle-release-github@main
    with:
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "." # (Optional)
```
