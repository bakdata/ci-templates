# java-gradle-release

This action releases Java Gradle artifacts by createing a tag on GitHub.

## Dependencies

This action uses the composite actions listed below:

- [checkout](https://github.com/bakdata/ci-templates/actions/checkout)
- [bump-version](https://github.com/bakdata/ci-templates/actions/bump-version)
- [changelog-generate](https://github.com/bakdata/ci-templates/actions/changelog-generate)
- [commit-and-push](https://github.com/bakdata/ci-templates/actions/commit-and-push)

## Input Parameters

| Name              | Required | Default Value |  Type   | Description                                                                                                   |
| ----------------- | :------: | :-----------: | :-----: | ------------------------------------------------------------------------------------------------------------- |
| github-email      |    ✅    |       -       | string  | GitHub email for requesting changes from API                                                                  |
| github-username   |    ✅    |       -       | string  | GitHub username for requesting changes from API                                                               |
| github-token      |    ✅    |       -       | string  | GitHub token for requesting changes from API                                                                  |
| changelog-file    |    ❌    |      11       | string  | Path to the changelog file                                                                                    |
| gradle-cache      |    ❌    |     true      | boolean | Whether Gradle caching is enabled or not                                                                      |
| gradle-version    |    ❌    |    wrapper    | string  | [Gradle version](https://github.com/gradle/gradle-build-action#use-a-specific-gradle-version) to be installed |
| java-distribution |    ❌    |   microsoft   | string  | [Java distribution](https://github.com/actions/setup-java#supported-distributions) to be installed            |
| java-version      |    ❌    |      11       | string  | Java version to be installed                                                                                  |
| working-directory |    ❌    |      "."      | string  | Working directory of your Gradle artifacts                                                                    |

## Output Variables

| Name            | Description                        |
| --------------- | ---------------------------------- |
| release-version | The bumped version of your release |

## Usage

```yaml
steps:
  - name: Release on Github
    uses: bakdata/ci-templates/actions/java-gradle-release@main
    with:
      github-email: ${{ secrets.github-email }}
      github-username: ${{ secrets.github-username }}
      github-token: ${{ secrets.github-token }}
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      gradle-cache: false # (Optional)
      working-directory: "." # (Optional)
```
