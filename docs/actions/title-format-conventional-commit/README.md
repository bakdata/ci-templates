# Description of title-format-conventional-commit action

This composite action validates that Pull Request titles follow the [Conventional Commits](https://www.conventionalcommits.org/) format. It ensures consistency in PR titles.

It checks that PR titles match one of the following patterns:

- `type: description`
- `type(scope): description`
- `type(scope)!: description` (breaking change)
- `Draft: type(scope)!: description` (draft PR)

Valid types include: `build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`.

## Prerequisites

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

No special prerequisites are required to use this action. It runs as a standalone validation check on Pull Requests.

<!-- AUTO-DOC-INPUT:END -->

## Usage

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

```yaml
name: Validate PR Title

on:
  pull_request:
    # Optional: Specify trigger types if you want the validation to run when the PR title is edited.
    # If omitted, the workflow triggers on all PR events except 'edited'.
    types: [opened, edited, synchronize, reopened]

jobs:
  validate-pr-title:
    runs-on: ubuntu-latest
    steps:
        - uses: bakdata/ci-templates/actions/title-format-conventional-commit@main
```

<!-- AUTO-DOC-INPUT:END -->

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

No inputs.

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
