# Generate Changelog

This action will allow for the automatic generation of a changelog. The changelog template needs to be configured using a `changelog-config.json`. Depending on whether there is other documentation besides the GitHub changelog or not, one or two `Changelog` files will be updated.

## Prerequisites

Create a `changelog-config.json` file containing the configurations of the changelogs.

## Input Parameters

| Name                 | Required |           Default Value           | Description                                                                                                        |
| -------------------- | :------: | :-------------------------------: | ------------------------------------------------------------------------------------------------------------------ |
| gh-changelog         |    ✅    |                 -                 | Path to the Changelog.md file                                                                                      |
| github-email         |    ✅    |                 -                 | The GitHub email for committing the changes                                                                        |
| github-token         |    ✅    |                 -                 | The GitHub token for committing the changes                                                                        |
| github-username      |    ✅    |                 -                 | The GitHub username for committing the changes                                                                     |
| new-tag              |    ✅    |                 -                 | New version                                                                                                        |
| old-tag              |    ✅    |                 -                 | Previous version                                                                                                   |
| bugLabels            |    ❌    |            "type/bug"             | Issues with the specified labels will be added to Fixed bugs section                                               |
| compareLink          |    ❌    |              "true"               | Include compare link (Full Changelog) between older version and newer version                                      |
| config               |    ❌    | "./.github/changelog-config.json" | Path to the changelog config JSON file                                                                             |
| doc-changelog        |    ❌    |                ""                 | Path to the documentation changelog (if any exists). If the variable is empty then no further file will be updated |
| enhancementLabels    |    ❌    |        "type/enhancement"         | Issues with the specified labels will be added to Implemented enhancements section                                 |
| httpCache            |    ❌    |              "true"               | Use HTTP Cache to cache GitHub API requests (useful for large repos)                                               |
| issues               |    ❌    |              "true"               | Include closed issues in changelog                                                                                 |
| issuesLabel          |    ❌    |       "**Miscellaneous:**"        | Set up custom label for closed-issues section                                                                      |
| issuesWoLabels       |    ❌    |              "true"               | Include closed issues without labels in changelog                                                                  |
| output               |    ❌    |           "changes.md"            | Name of the output file for the generate changelog step                                                            |
| outpprWoLabelsut     |    ❌    |              "false"              | Include pull requests without labels in changelog                                                                  |
| pullRequests         |    ❌    |              "false"              | Include pull-requests in changelog                                                                                 |
| stripGeneratorNotice |    ❌    |              "false"              | Strip generator notice                                                                                             |
| unreleased           |    ❌    |              "true"               | Add to log unreleased closed issues                                                                                |
| verbose              |    ❌    |              "true"               | Run verbosely                                                                                                      |

## Calling the workflow

```yaml
steps:
  # check out current repository
  - uses: actions/checkout@v3
  # generate changelog
  - name: Create changelog
    uses: bakdata/ci-templates/actions/generate-changelog@main
    with:
      old-tag: "1.0.0"
      new-tag: "1.0.1"
      gh-changelog: "CHANGELOG.md"
      doc-changelog: "./docs/Changelog.md"
      config: "./.github/changelog-config.json"
      github-email: "${{ secrets.GH_EMAIL }}"
      github-username: "${{ secrets.GH_USERNAME }}"
      github-token: "${{ secrets.GH_TOKEN }}"
```
