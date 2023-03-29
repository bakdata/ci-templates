# Generate Changelog

This action will allow for the automatic generation of a changelog. The changelog template needs to be configured using a `changelog-config.json`. This action will then create a changelog for the new release and update the changelog file in your repository.

## Dependencies

This action is built from the following composite actions:

- [release-changelog-builder-action](https://github.com/mikepenz/release-changelog-builder-action)

## Prerequisites

Create a file called `changelog-config.json` that contains the changelog configurations. The mentioned action's documentation goes into great detail about how to create and utilize config files. A simple configuration may look like this:

```yaml
{
  "categories":
    [
      { "title": "## 🚀 Features", "labels": ["feature", "feat"] },
      { "title": "## 🐛 Fixes", "labels": ["fix", "bug"] },
      { "title": "## 🧪 Dependencies", "labels": ["dependency"] },
    ],
  "ignore_labels": ["ignore"],
  "sort": { "order": "ASC", "on_property": "mergedAt" },
  "template": "# [${{TO_TAG}}](https://github.com/<myorganization>/<myrepository>/releases/tag/${{TO_TAG}}) - ${{TO_TAG_DATE}}\n\n${{CHANGELOG}}\n<details>\n<summary>Uncategorized</summary>\n\n${{UNCATEGORIZED}}\n</details>\n",
  "pr_template": "- ${{TITLE}}\n   - PR: ${{URL}}\n   - Assignees: ${{ASSIGNEES[*]}}\n   - Reviewers: ${{REVIEWERS[*]}}\n   - Approvers: ${{APPROVERS[*]}}",
  "empty_template": "- no changes!",
}
```

Make sure to update the link `https://github.com/<myorganization>/<myrepository>/releases/tag/${{TO_TAG}}` accordingly.

Additional configuration options can be explored [here](https://github.com/mikepenz/release-changelog-builder-action#configuration-specification).

## Input Parameters

| Name                    | Required |           Default Value           | Description                                                                                                                                                  |
| ----------------------- | :------: | :-------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| changelog-file          |    ✅    |                 -                 | Path to the Changelog.md file                                                                                                                                |
| github-token            |    ✅    |                 -                 | The GitHub token for committing the changes                                                                                                                  |
| new-tag                 |    ✅    |                 -                 | New version                                                                                                                                                  |
| old-tag                 |    ✅    |                 -                 | Previous version                                                                                                                                             |
| config                  |    ❌    | "./.github/changelog-config.json" | Path to the changelog config JSON file                                                                                                                       |
| output                  |    ❌    |           "changes.md"            | Relative path to a file to store the resulting changelog in.                                                                                                 |
| fetchReviewers          |    ❌    |              "false"              | Will enable fetching the users/reviewers who approved the PR.                                                                                                |
| fetchReleaseInformation |    ❌    |              "false"              | Will enable fetching additional release information from tags.                                                                                               |
| commitMode              |    ❌    |              "false"              | Special configuration for projects which work without PRs. Uses commit messages as changelog. This mode looses access to information only available for PRs. |

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
