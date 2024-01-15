<h1>Description bump-version composite action</h1>

This action will bump the version of your project according to the <code>.bumpversion.cfg</code> file.

<h2>Prerequisites</h2>

You need a <code>.bumpversion.cfg</code> file in <code>working-directory</code> (repository root by default). A minimal configuration could look like this:

<code>cfg
[bumpversion]
current_version = 0.0.1
</code>

<blockquote>
  <strong>Note</strong>
  Changes made to the <code>.bumpversion.cfg</code> file by this action are <strong>not</strong> pushed back to GitHub. If you need this functionality, please use the <a href="https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push">commit-and-push</a> action subsequently.
</blockquote>

<h2>Usage</h2>

Add the following steps to your workflow:

<code>yaml
steps:
  # check out current repository
  - uses: bakdata/ci-templates/actions/checkout@1.32.0
  # bump the version of your project
name: Bump version
uses: bakdata/ci-templates/actions/bump-version@main
with:
release-type: "patch"
working-directory: "."
new-version: "2.0.0"
</code>

</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT          | DESCRIPTION                                                      |
| ----------------- | ------ | -------- | ---------------- | ---------------------------------------------------------------- |
| new-version       | string | false    |                  |                                                                  |
| release-type      | string | true     |                  | The type of the release (major, minor or patch).                 |
| working-directory | string | false    | <code>"."</code> | The directory containing the <code>.bumpversion.cfg</code> file. |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | TYPE   | DESCRIPTION                                                 |
| --------------- | ------ | ----------------------------------------------------------- |
| old-version     | string | The old version in your <code>.bumpversion.cfg</code> file. |
| release-version | string | The bumped version of your project.                         |

<!-- AUTO-DOC-OUTPUT:END -->
