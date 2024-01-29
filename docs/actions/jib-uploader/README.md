# Description jib-uploader composite action

This composite action utilizes Jib to efficiently build a container image and automatically upload it to the referenced container repository.

## Usage

```yaml
- name: Build SentenceProducer image for tag  release
  uses: bakdata/ci-templates/actions/jib-uploader@main
  with:
    image: my-docker-registry/my-docker-image
    class: org.example.MyClass
    tags: latest,${GITHUB_REF/refs\/tags\//}
    working-directory: "./"
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT | DESCRIPTION                                   |
| ----------------- | ------ | -------- | ------- | --------------------------------------------- |
| class             | string | true     |         | The entrypoint class to be used for the image |
| image             | string | true     |         | The image name with its repository name       |
| tags              | string | true     |         | The tags to use to release the image          |
| working-directory | string | true     |         | working directory to run the commands         |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
