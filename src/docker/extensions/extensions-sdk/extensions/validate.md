---
title: Validate your extension
description: Step three in the extension creation process
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/extensions/extensions-sdk/extensions/validate.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: extensions
order: 6710
---

Validate your extension before you share or publish it. Validating the extension ensures that the extension:

- Is built with the [image labels](labels.md) it requires to display correctly in the marketplace
- Installs and runs without problems

The Extensions CLI lets you validate your extension before installing and running it locally.

The validation checks if the extension’s `Dockerfile` specifies all the required labels and if the metadata file is valid against the JSON schema file.

To validate, run:

```console
$ docker extension validate <name-of-your-extension>
```

If your extension is valid, the following message displays:

```console
The extension image "name-of-your-extension" is valid
```

Before the image is built, it's also possible to validate only the `metadata.json` file:

```console
$ docker extension validate /path/to/metadata.json
```

The JSON schema used to validate the `metadata.json` file against can be found under the [releases page](https://github.com/docker/extensions-sdk/releases/latest).
