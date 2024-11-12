# Description generate-changelog composite action

This action will enable the automated creation of a changelog.
The changelog template needs to be configured using a `changelog-config.json`.
If there is a global changelog managed by the repository this will be updated.
The action generates a new release changelog and an updated version of
the changelog file in the repository (if there is any).
The default setting updates the repo changelog.
If your current repository does not have any global changelog file,
then pass an empty string to the variable `changelog-file`.
The action returns both the new tag's changelog and the global changelog.

When generating the changelog, the action evaluates two factors to decide which PRs to consider:
`old-tag`
(lower bound defining the 'start' from where the changelog will consider merged pull requests)
and `new-tag`
(upper bound defining until which tag the changelog will consider merged pull requests).

The upper bound might be either existing or new.
If the new tag does not yet exist, the action will
nevertheless create the changelog so that it may be included in the release.

## Dependencies

This action is built from the following composite actions:

- [release-changelog-builder-action](https://github.com/mikepenz/release-changelog-builder-action)

## Prerequisites

Create a file called `changelog-config.json` that contains the changelog configurations.
The mentioned action's documentation goes into great detail about how to create and utilize config
files. A simple configuration may look like this:

```json
{
  "categories": [{ "title": "### Merged pull requests:" }],
  "ignore_labels": ["ignore"],
  "sort": { "order": "ASC", "on_property": "mergedAt" },
  "template": "# [#{{TO_TAG}}](https://github.com/#{{OWNER}}/#{{REPO}}/releases/tag/#{{TO_TAG}}) - Release Date: #{{TO_TAG_DATE}}\n\n#{{CHANGELOG}}",
  "pr_template": "- #{{TITLE}} [##{{NUMBER}}](#{{URL}}) ([@#{{AUTHOR}}](https://github.com/#{{AUTHOR}}))\n",
  "empty_template": "- no changes!"
}
```

Make sure to update the link
`https://github.com/<myorganization>/<myrepository>/releases/tag/${{TO_TAG}}`
accordingly and make sure to include `- Release Date: ${{TO_TAG_DATE}}`
because the action looks for this pattern to make the date format easily readable.

Additional configuration options can be explored
[here](https://github.com/mikepenz/release-changelog-builder-action#configuration-specification).

## Usage

By default, just a single commit for the ref/SHA that started the process is retrieved.
In the [checkout action](https://github.com/actions/checkout), enter `fetch-depth: 0` to retrieve
all history for all branches and tags.
Without it, the changelog action will be unable to track down previous tags.

```yaml
steps:
  - uses: bakdata/ci-templates/actions/checkout@main
    with:
      persist-credentials: false
      fetch-depth: 0
  - name: Create changelog
    id: build_changelog
    uses: bakdata/ci-templates/actions/changelog-generate@main
    with:
      github-token: ${{ secrets.GH_TOKEN }}
      new-tag: "1.0.0"
      changelog-file: "CHANGELOG.md"
      fetch-reviewers: "true"
      fetch-release-information: "true"
  - name: Use output
    run: |
      echo  "${{ steps.build_changelog.outputs.single-changelog }}" > tag_changelog.md
      echo  "${{ steps.build_changelog.outputs.merged-changelog }}" > global_changelog.md
    shell: bash
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT          | TYPE   | REQUIRED | DEFAULT          | DESCRIPTION                                         |
| -------------- | ------ | -------- | ---------------- | --------------------------------------------------- |
| changelog-file | string | false    | `"CHANGELOG.md"` | Path to the changelog file in the GitHub repository |
| clean          | string | false    | `"false"`        | Clean the repository before running the action.     |
| github-token   | string | true     |                  | The GitHub token for committing the changes.        |
| tag            | string | true     |                  | Version after bump                                  |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT           | TYPE   | DESCRIPTION                |
| ---------------- | ------ | -------------------------- |
| merged-changelog | string | All changelogs combined.   |
| single-changelog | string | Only the latest changelog. |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
