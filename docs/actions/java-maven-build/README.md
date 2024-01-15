<h1>Description java-maven-build composite action</h1>

This action builds Java artifacts using Maven.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Build
    uses: bakdata/ci-templates/actions/java-maven-build@main
    with:
      maven-version: "3.8.2"
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
      working-directory: "." # (Optional)
      command: "compile" # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |    DEFAULT    |                        DESCRIPTION                        |
|-------------------|--------|----------|---------------|-----------------------------------------------------------|
|      command      | string |  false   |  <code>"compile"</code>  |      Command to run build with. (Default is compile)      |
| java-distribution | string |  false   | <code>"microsoft"</code> | Java distribution to be installed. (Default is microsoft) |
|   java-version    | string |  false   |    <code>"11"</code>     |       Java version to be installed. (Default is 11)       |
|   maven-version   | string |   true   |               |              Maven version to be installed.               |
| working-directory | string |  false   |     <code>"."</code>     | Working directory of your Maven artifacts. (Default is .) |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
