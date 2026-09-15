---
title: Overview of the Extensions SDK
description: Overall index for Docker Extensions SDK documentation
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/extensions/extensions-sdk/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: extensions
order: 6430
---

> [!IMPORTANT]
>
> New submissions to the Docker Extensions Marketplace are paused while Docker reviews Marketplace security. You can still update existing extensions, and private Marketplace extensions are unaffected. Contact extensions@docker.com if you have additional questions.

The resources in this section help you create your own Docker extension.

The Docker CLI tool provides a set of commands to help you build and publish your extension, packaged as a 
specially formatted Docker image.

At the root of the image filesystem is a `metadata.json` file which describes the content of the extension. 
It's a fundamental element of a Docker extension.

An extension can contain a UI part and backend parts that run either on the host or in the Desktop virtual machine.
For further information, see [Architecture](architecture/index.md).

You distribute extensions through Docker Hub. However, you can develop them locally without the need to push 
the extension to Docker Hub. See [Extensions distribution](extensions/distribution.md) for further details.

{{% include "extensions-form.md" %}}

{{< grid >}}
