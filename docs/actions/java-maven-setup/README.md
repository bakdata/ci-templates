<h1>Description java-maven-setup composite action</h1>

This action sets up Java and Maven.

<h2>Usage</h2>

<code>yaml
steps:
  - name: Set up Maven
    uses: bakdata/ci-templates/actions/java-maven-setup@main
    with:
      maven-version: "3.8.2"
      java-distribution: "microsoft" # (Optional)
      java-version: "11" # (Optional)
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|       INPUT       |  TYPE  | REQUIRED |    DEFAULT    |                        DESCRIPTION                        |
|-------------------|--------|----------|---------------|-----------------------------------------------------------|
| java-distribution | string |  false   | <code>"microsoft"</code> | Java distribution to be installed. (Default is microsoft) |
|   java-version    | string |  false   |    <code>"11"</code>     |       Java version to be installed. (Default is 11)       |
|   maven-version   | string |   true   |               |              Maven version to be installed.               |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
