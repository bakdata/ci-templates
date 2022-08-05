# java-gradle-setup

This action runs Junit test, publishes the test results and tests signing for Sonatype.

## Input Parameters

| Name                    | Required | Default Value |  Type  | Description                                        |
|-------------------------|:--------:|:-------------:|:------:|----------------------------------------------------|
| sonar-token             |    ❌     |       -       | string | Token for Sonarcloud                               |
| signing-secret-key-ring |    ❌     |       -       | string | Key ring file for signing the Sonatype publication |
| signing-key-id          |    ❌     |       -       | string | Key id for signing the Sonatype publication        |
| signing-password        |    ❌     |       -       | string | Password for signing the Sonatype publication      |
| java-distribution       |    ❌     |   microsoft   | string | Java distribution to be installed                  |
| java-version            |    ❌     |      11       | string | Java version to be installed                       |
| gradle-version          |    ❌     |    wrapper    | string | Gradle version to be installed                     |
| working-directory       |    ❌     |     "./"      | string | Working directory of your Gradle artifacts         |

## Usage

```yaml
...
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-gradle-test@main
    with:
      sonar-token: ${{ secrets.sonar-token }}
      signing-secret-key-ring: ${{ secrets.signing-secret-key-ring }}
      signing-key-id: ${{ secrets.signing-key-id }}
      signing-password: ${{ secrets.signing-password }}   
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      gradle-version: "wrapper" # (Optional)
      working-directory: "./" # (Optional)
...
```
