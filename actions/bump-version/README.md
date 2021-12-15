# bump-version
This action will bump the version of your project according to the `.bumpversion.cfg` file. To use this action you need to have a few things setup in the repository:

1. Add a `.bumpversion.cfg` file in the root directory of your repository with the following content. Make sure to replace `VERSION` with the current version of your project:
```cfg
[bumpversion]
current_version = VERSION
commit = True
tag = True
```

2. Add the following steps to your workflow:
```yaml
...
steps:
  # check out current repository
  - uses: actions/checkout@v2
    with:
      # needed to push the bumped charts
      persist-credentials: false

  # check out ci-templates repository into ./ci-templates
  - uses: actions/checkout@v2
    with:
      repository: "bakdata/ci-templates"
      path: "ci-templates"
  
  # bump the version of your project
  - name: Bump version
      uses: ./ci-templates/bump-version
      with:
        githubToken: "${{ secrets.GH_TOKEN }}"
        githubUsername: "${{ secrets.GH_USERNAME }}"
        githubEmail: "${{ secrets.GH_EMAIL }}"
```

4. Choose a Github user that is going to push the tags and version updates. Create a repository secret for the Github username (`GH_USERNAME`), the Github Email (`GH_EMAIL`) and a personal access token (`GH_TOKEN`) of the user. For the email you can use the no reply github email: `[username]@users.noreply.github.com`. Make sure to configure admin access to the repository for the selected user because admins can still push on the default branch even if there is a protection rule in place.

## Optional parameters
You can optionally set the `releaseType` to `major`, `minor` or `patch`. This can also be done via a workflow input:
```yaml
name: bumpversion

on:
  workflow_dispatch:
    inputs:
      releaseType:
        description: "The type of the release."
        default: "patch"
        required: false

jobs:
  release:
    runs-on: ubuntu-20.04
    steps:
      # check out current repository
      - uses: actions/checkout@v2
        with:
          # needed to push the bumped charts
          persist-credentials: false

      # check out ci-templates repository into ./ci-templates
      - uses: actions/checkout@v2
        with:
          repository: "bakdata/ci-templates"
          path: "ci-templates"
      
      # bump the version of your project
      - name: Bump version
          uses: ./ci-templates/bump-version
          with:
            githubToken: "${{ secrets.GH_TOKEN }}"
            githubUsername: "${{ secrets.GH_USERNAME }}"
            githubEmail: "${{ secrets.GH_EMAIL }}"
            releaseType: "${{ github.event.inputs.releaseType }}"
```
