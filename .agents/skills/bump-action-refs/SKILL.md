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

For **each** action or workflow name from step 1, search for all `uses:` references in action and workflow YAML files.

**CRITICAL — actions and workflows are different things and must be searched separately:**

- An **action** lives at `actions/<name>/action.yaml` and is referenced as `bakdata/ci-templates/actions/<name>@<version>`.
- A **reusable workflow** lives at `.github/workflows/<name>.yaml` and is referenced as `bakdata/ci-templates/.github/workflows/<name>.yaml@<version>`.

An action and a workflow **can share the same base name** (e.g. `actions/python-poetry-publish-pypi/` and `.github/workflows/python-poetry-publish-pypi.yaml`). They have **independent dependency chains**. When a file is modified, determine **whether it is an action or a workflow** by its file path and search only with the corresponding grep pattern:

- If the modified file is an **action** (`actions/<name>/action.yaml`): `grep -rn 'bakdata/ci-templates/actions/<name>@' .github/workflows/ actions/ --include='*.yaml' --include='*.yml'`
- If the modified file is a **workflow** (`.github/workflows/<name>.yaml`): `grep -rn 'bakdata/ci-templates/\.github/workflows/<name>\.yaml@' .github/workflows/ --include='*.yaml' --include='*.yml'`

**Anchoring:** Action grep patterns must use `/<name>@` (with the leading `/`) to prevent partial prefix matches. For example, searching for `python-poetry-publish` must not accidentally match `python-poetry-publish-pypi`. The `/` before `<name>` and the `@` after it together ensure an exact action-name match.

**Never assume that bumping a workflow also requires bumping a same-named action, or vice versa.** Only bump a reference if the target it points to was actually modified or transitively depends on something that was modified.

Search all names in parallel where possible. Collect all matches into a single list of files and lines to update.

**Scope**: Only `actions/**/action.yaml`, `actions/**/action.yml`, and `.github/workflows/*.yaml` files. Skip `docs/` and `README.md` files — those are documentation and should not be bumped.

### 3. Replace version pins

For each match from step 2, replace the `@<old-version>` suffix with `@<current-branch>` where `<current-branch>` is the currently checked-out Git branch name (available from the repository context attachment or via `git branch --show-current`).

### 4. Recurse into transitive dependents

For every action or workflow file that was modified in step 3, repeat steps 2–3 using that file's action/workflow name as the new search target, **respecting the action-vs-workflow distinction**:

- If `actions/<name>/action.yaml` was modified → `grep -rn 'bakdata/ci-templates/actions/<name>@' .github/workflows/ actions/ --include='*.yaml' --include='*.yml'`
- If `.github/workflows/<name>.yaml` was modified → `grep -rn 'bakdata/ci-templates/\.github/workflows/<name>\.yaml@' .github/workflows/ --include='*.yaml' --include='*.yml'`

**Do not cross types**: modifying a workflow does not require bumping a same-named action, and vice versa. The grep pattern determines the type.

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
- **Strictly distinguish actions from workflows.** An action (`actions/<name>/`) and a workflow (`.github/workflows/<name>.yaml`) can share the same base name but have completely independent dependency chains. Use `grep` with the exact reference pattern to determine dependents deterministically — never infer dependencies from name similarity alone.

## Example

Given a change to the **action** `python-setup-poetry`, the dependency chain looks like:

```
python-setup-poetry (changed action)
├── actions/python-poetry-bump-version/action.yaml          →  @branch  (uses the action)
│   ├── .github/workflows/python-poetry-publish-snapshot.yaml  →  @branch  (uses the action)
│   └── .github/workflows/python-poetry-release.yaml           →  @branch  (uses the action)
└── .github/workflows/python-poetry-publish-pypi.yaml       →  @branch  (uses the action)
    (no further dependents — no workflows call .github/workflows/python-poetry-publish-pypi.yaml)
```

**Note:** There also exists an **action** called `actions/python-poetry-publish-pypi/` which shares the same base name as the workflow `.github/workflows/python-poetry-publish-pypi.yaml`. The action does **not** depend on `python-setup-poetry`, so it must **not** be bumped. The workflow does depend on it, so it is bumped. Always verify via `grep` which exact `uses:` reference pattern appears — do not confuse same-named actions and workflows.
