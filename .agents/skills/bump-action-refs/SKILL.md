---
name: bump-action-refs
description: "Recursively bump version references for a changed composite action or reusable workflow. Use when: updating action refs, bumping version pins, propagating branch references through dependent actions and workflows, replacing @version tags in uses: lines."
argument-hint: "Optional: name of the action or workflow that was changed (e.g. python-setup-poetry). If omitted, auto-detects from git diff."
---

# Bump Action References

Recursively update all `uses:` version references for changed actions or reusable workflows so that the entire dependency chain points to the current branch.

## When to Use

- After modifying a composite action or reusable workflow in this repository
- To propagate the current branch name through all transitive dependents before testing

## Procedure

### 1. Identify the changed actions

If the user provides an explicit action or workflow name (e.g. `python-setup-poetry`), use that as the starting point.

If no explicit name is provided, auto-detect by running:

```bash
git diff --name-only main -- 'actions/' '.github/workflows/'
```

From the output, extract the changed action and workflow names:
- For files matching `actions/<action-name>/action.yaml` or `actions/<action-name>/action.yml`, extract `<action-name>`.
- For files matching `.github/workflows/<workflow-name>.yaml`, extract `<workflow-name>`.

Deduplicate the list. Each unique name becomes a starting point for the recursive bump.

### 2. Find direct dependents

For **each** action or workflow name from step 1, search for all `uses:` references in action and workflow YAML files:

- For actions: `grep pattern: bakdata/ci-templates/actions/<action-name>@`
- For workflows: `grep pattern: bakdata/ci-templates/.github/workflows/<workflow-name>@`

Search all names in parallel where possible. Collect all matches into a single list of files and lines to update.

**Scope**: Only `actions/**/action.yaml`, `actions/**/action.yml`, and `.github/workflows/*.yaml` files. Skip `docs/` and `README.md` files — those are documentation and should not be bumped.

### 3. Replace version pins

For each match from step 2, replace the `@<old-version>` suffix with `@<current-branch>` where `<current-branch>` is the currently checked-out Git branch name (available from the repository context attachment or via `git branch --show-current`).

### 4. Recurse into transitive dependents

For every action or workflow file that was modified in step 3, repeat steps 2–3 using that file's action/workflow name as the new search target.

Continue until no new references are found.

### 5. Report the dependency chain

After all replacements, summarize the full dependency tree that was updated, showing:
- Which files were modified
- Which `uses:` lines were changed
- The old and new version refs

## Rules

- **Never modify docs or READMEs** — only action YAML and workflow YAML files.
- **Always use the current branch name** as the replacement version.
- **Track visited actions** to avoid infinite loops in case of circular references.
- **Use `multi_replace_string_in_file`** for efficiency when multiple replacements are needed.
- **Include 3–5 lines of context** around each replacement to ensure unique matches.

## Example

Given a change to `python-setup-poetry`, the dependency chain might look like:

```
python-setup-poetry (changed)
├── actions/python-poetry-bump-version/action.yaml  →  @branch
├── .github/workflows/python-poetry-publish-pypi.yaml  →  @branch
│   └── .github/workflows/python-poetry-publish-snapshot.yaml  →  @branch
├── python-poetry-bump-version (updated above, now trace its dependents)
│   ├── .github/workflows/python-poetry-publish-snapshot.yaml  →  @branch
│   └── .github/workflows/python-poetry-release.yaml  →  @branch
└── python-poetry-publish-pypi (updated above, now trace its dependents)
    ├── .github/workflows/python-poetry-publish-pypi.yaml  →  @branch  (self-ref)
    └── .github/workflows/python-poetry-publish-snapshot.yaml  →  @branch
```
