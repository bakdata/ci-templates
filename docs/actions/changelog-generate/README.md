<h1>Description generate-changelog composite action</h1>

This action will enable the automated creation of a changelog.
The changelog template needs to be configured using a <code>changelog-config.json</code>.
If there is a global changelog managed by the repository this will be updated.
The action generates a new release changelog and an updated version of
the changelog file in the repository (if there is any).
The default setting updates the repo changelog.
If your current repository does not have any global changelog file,
then pass an empty string to the variable <code>changelog-file</code>.
The action returns both the new tag's changelog and the global changelog.

When generating the changelog, the action evaluates two factors to decide which PRs to consider:
<code>old-tag</code>
(lower bound defining the 'start' from where the changelog will consider merged pull requests)
and <code>new-tag</code>
(upper bound defining until which tag the changelog will consider merged pull requests).

The upper bound might be either existing or new.
If the new tag does not yet exist, the action will
nevertheless create the changelog so that it may be included in the release.

<h2>Dependencies</h2>

This action is built from the following composite actions:

<ul>
<a href="https://github.com/mikepenz/release-changelog-builder-action">release-changelog-builder-action</a>
</ul>

<h2>Prerequisites</h2>

Create a file called <code>changelog-config.json</code> that contains the changelog configurations.
The mentioned action's documentation goes into great detail about how to create and utilize config
files. A simple configuration may look like this:

<code>json
{
  "categories": [{ "title": "### Merged pull requests:" }],
  "ignore<em>labels": ["ignore"],
  "sort": { "order": "ASC", "on</em>property": "mergedAt" },
  "template": "# <a href="https://github.com/#{{OWNER}}/#{{REPO}}/releases/tag/#{{TO_TAG}}">#{{TO<em>TAG}}</a> - Release Date: #{{TO</em>TAG<em>DATE}}\n\n#{{CHANGELOG}}",
  "pr</em>template": "- #{{TITLE}} <a href="#{{URL}}">##{{NUMBER}}</a> (<a href="https://github.com/#{{AUTHOR}}">@#{{AUTHOR}}</a>)\n",
  "empty_template": "- no changes!"
}
</code>

Make sure to update the link
<code>https://github.com/&lt;myorganization&gt;/&lt;myrepository&gt;/releases/tag/${{TO<em>TAG}}</code>
accordingly and make sure to include <code>- Release Date: ${{TO</em>TAG_DATE}}</code>
because the action looks for this pattern to make the date format easily readable.

Additional configuration options can be explored
<a href="https://github.com/mikepenz/release-changelog-builder-action#configuration-specification">here</a>.

<h2>Usage</h2>

By default, just a single commit for the ref/SHA that started the process is retrieved.
In the <a href="https://github.com/actions/checkout">checkout action</a>, enter <code>fetch-depth: 0</code> to retrieve
all history for all branches and tags.
Without it, the changelog action will be unable to track down previous tags.

<code>yaml
steps:
  - uses: bakdata/ci-templates/actions/checkout@1.32.0
    with:
      persist-credentials: false
      fetch-depth: 0
  - name: Create changelog
    id: build<em>changelog
    uses: bakdata/ci-templates/actions/changelog-generate@main
    with:
      github-token: ${{ secrets.GH</em>TOKEN }}
      new-tag: "1.0.0"
      changelog-file: "CHANGELOG.md"
      fetch-reviewers: "true"
      fetch-release-information: "true"
  - name: Use output
    run: |
      echo  "${{ steps.build<em>changelog.outputs.single-changelog }}" &gt; tag</em>changelog.md
      echo  "${{ steps.build<em>changelog.outputs.merged-changelog }}" &gt; global</em>changelog.md
    shell: bash
</code>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|           INPUT           |  TYPE  | REQUIRED |     DEFAULT      |                          DESCRIPTION                           |
|---------------------------|--------|----------|------------------|----------------------------------------------------------------|
|      changelog-file       | string |  false   | <code>"CHANGELOG.md"</code> |      Path to the changelog file in the GitHub repository       |
|        commit-mode        | string |  false   |    <code>"false"</code>     |   Special configuration for projects which work without PRs.   |
|          config           | string |  false   |                  |             Path to the changelog config JSON file             |
| fetch-release-information | string |  false   |    <code>"false"</code>     | Will enable fetching additional release information from tags. |
|      fetch-reviewers      | string |  false   |    <code>"false"</code>     |  Will enable fetching the users/reviewers who approved the PR  |
|       github-token        | string |   true   |                  |          The GitHub token for committing the changes.          |
|          new-tag          | string |   true   |                  |                       Version after bump                       |
|          old-tag          | string |  false   |                  |            Previous version. Let empty for releases            |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|      OUTPUT      |  TYPE  |                      DESCRIPTION                      |
|------------------|--------|-------------------------------------------------------|
| merged-changelog | string | Changelog containing listing of all single changelogs |
| single-changelog | string |    Changelog containing changes of the latest tag     |

<!-- AUTO-DOC-OUTPUT:END -->
