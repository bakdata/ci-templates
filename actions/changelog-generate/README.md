# Generate Changelog

This action will enable the automated creation of a changelog. The changelog template needs to be configured using a `changelog-config.json`.
If there is a global changelog managed by the repository this will be updated.
The action generates a new release changelog and an updated version of the changelog file in the repository(if there is any). The default setting updates the repo changelog. If your current repository does not have any global changelog file, then pass an empty string to the variable `changelog-file`.
The action returns both the new tag's changelog and the global changelog.

When generating the changelog, the action evaluates two factors to decide which PRs to consider: `old-tag` (lower bound defining the 'start' from where the changelog will consider merged pull requests) and `new-tag` (upper bound defining until which tag the changelog will consider merged pull requests).

If this is the initial release, leaving `old-tag` empty allows the action to utilize the first commit as the lower bound.

The upper bound might be either existing or new. If the new tag does not yet exist, the operation will nevertheless create the changelog so that it may be included in the release.

## Dependencies

This action is built from the following composite actions:

- [release-changelog-builder-action](https://github.com/mikepenz/release-changelog-builder-action)
- [tag-exists-action](https://github.com/mukunku/tag-exists-action)

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

## Outputs

| Name             | Description                                           |
| ---------------- | ----------------------------------------------------- |
| single-changelog | Changelog containing changes of the latest tag        |
| merged-changelog | Changelog containing listing of all single changelogs |

## Calling the workflow

```yaml
steps:
  # check out current repository
  - uses: actions/checkout@v3
  # generate changelog
  - name: Create changelog
    id: build_changelog
    uses: bakdata/ci-templates/actions/changelog-generate@main
    with:
      token: ${{ secrets.GH_TOKEN }}
      configuration: "./.github/changelog-config.json"
      fromTag: "1.0.0"
      toTag: "1.0.1"
      fetchReviewers: "true"
      fetchReleaseInformation: "true"
  # access generated changelog
  - name: Use output
    run: |
      echo  "${{ steps.build_changelog.outputs.single-changelog }}" >> tag_changelog.md
      echo  "${{ steps.build_changelog.outputs.merged-changelog }}" >> global_changelog.md
    shell: bash
```