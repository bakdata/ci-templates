<h1>Description tag-and-release composite action</h1>

This composite action allows you to create a Git tag and GitHub release.

<h2>Dependencies</h2>

This action uses another composite action listed below:

<ul>
<a href="https://github.com/softprops/action-gh-release">action-gh-release</a>
</ul>

<h2>Usage</h2>

```yaml
steps:
  - name: Check out repository
    uses: bakdata/ci-templates/actions/checkout@1.32.0

<ul>
name: Tag and release project
uses: bakdata/ci-templates/actions/tag-and-release@main
with:
  tag: "1.0.0"
  release-title: "This should be the title for the GitHub release"
  release-body: "This should be on the text part of the GitHub release"
```
</ul>

<h2>References</h2>

<h3>Inputs</h3>

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|      INPUT      |  TYPE  | REQUIRED | DEFAULT |                    DESCRIPTION                     |
|-----------------|--------|----------|---------|----------------------------------------------------|
|  github-email   | string |   true   |         |    The GitHub email for committing the changes.    |
|  github-token   | string |   true   |         |    The GitHub token for committing the changes.    |
| github-username | string |   true   |         |  The GitHub username for committing the changes.   |
|  release-body   | string |  false   |         |        Description for the GitHub release.         |
|  release-title  | string |   true   |         |           Title for the GitHub release.            |
|       tag       | string |   true   |         | The version of the tag to be released, e.g. 1.0.0. |

<!-- AUTO-DOC-INPUT:END -->

<h3>Outputs</h3>

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->
No outputs.
<!-- AUTO-DOC-OUTPUT:END -->
