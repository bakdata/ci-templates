# bump-version
This action will bump the version of your project according to the `.bumpversion.cfg` file.


## Prerequisites
You need a `.bumpversion.cfg` file in the root directory of your repository. A minimal configuration could look like this:
```cfg
[bumpversion]
current_version = 0.0.1
commit = True
tag = True
```

Moreover, choose a GitHub user who will change, commit, and push the version in your `.bumpversion.cfg` file. Make sure to configure
admin access to the repository for the selected user because admins can still push on the default branch even if there
is a protection rule in place.

## Input Parameters
| Name              | Required  |             Default Value             |  Type   | Description                                        |
|-------------------|:---------:|:-------------------------------------:|:-------:|----------------------------------------------------|
| release-type      |    ✅     |                  -                    | string  | The scope of the release (major, minor or patch)   |

### Outputs
This action outputs the following variables:

| Name        | Description                                           |
|-------------|-------------------------------------------------------|
| old-tag     | Defines the old version in your .bumpversion.cfg file |
| release-tag | The bumped version of your project                    |

## Usage
Add the following steps to your workflow:
```yaml
...
steps:
  # check out current repository
  - uses: actions/checkout@v2

  # check out ci-templates repository into ./ci-templates
  - uses: actions/checkout@v2
    with:
      repository: "bakdata/ci-templates"
      path: "ci-templates"
  
  # set up python
  - uses: actions/setup-python@v2
    with:
      python-version: "${{ inputs.python-version }}"
  
  # bump the version of your project
  - name: Bump version
      uses: ./ci-templates/bump-version
      with:
        release-type: "patch"
...
```
