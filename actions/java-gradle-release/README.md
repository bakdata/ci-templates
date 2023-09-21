# java-gradle-release

This action releases Java Gradle artifacts by createing a tag on GitHub.

## Input Parameters

| Name              | Required | Default Value |  Type   | Description                                                                                                   |
| ----------------- | :------: | :-----------: | :-----: | ------------------------------------------------------------------------------------------------------------- |
| release-type      |    ✅    |       -       | string  | Scope of the release                                                                                          |
| github-email      |    ✅    |       -       | string  | GitHub email for requesting changes from API                                                                  |
| github-username   |    ✅    |       -       | string  | GitHub username for requesting changes from API                                                               |
| github-token      |    ✅    |       -       | string  | GitHub token for requesting changes from API                                                                  |
| java-distribution |    ❌    |   microsoft   | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version      |    ❌    |      11       | string  | Java version to be installed                                                                                  |
| gradle-version    |    ❌    |    wrapper    | string  | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| gradle-cache      |    ❌    |     true      | boolean | Whether Gradle caching is enabled or not                                                                      |
| working-directory |    ❌    |      "."      | string  | Working directory of your Gradle artifacts                                                                    |

## Usage

```yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-gradle-release@main
    with:
      release-type: "patch"
      github-email: ${{ secrets.github-email }}
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      gradle-cache: false # (Optional)
      working-directory: "." # (Optional)
```
