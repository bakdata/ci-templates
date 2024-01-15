<h1>Description java-maven-test composite action</h1>

This action runs Junit tests and publishes the test results.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Test
    uses: bakdata/ci-templates/actions/java-maven-test@main
    with:
      maven-version: "3.8.2"
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      working-directory: "." # (Optional)
      command: "test" # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT        |  TYPE  | REQUIRED |    DEFAULT    |                                     DESCRIPTION                                     |
|--------------------|--------|----------|---------------|-------------------------------------------------------------------------------------|
|      command       | string |  false   |   <code>"test"</code>    |                    Command to run tests with. (Default is test)                     |
| download-lfs-files | string |  false   |   <code>"false"</code>   | Whether the Git checkout action should resolve LFS files or not. (Default is false) |
| java-distribution  | string |  false   | <code>"microsoft"</code> |              Java distribution to be installed. (Default is microsoft)              |
|    java-version    | string |  false   |    <code>"11"</code>     |                    Java version to be installed. (Default is 11)                    |
|   maven-version    | string |   true   |               |                           Maven version to be installed.                            |
| working-directory  | string |  false   |     <code>"."</code>     |              Working directory of your Maven artifacts. (Default is .)              |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
