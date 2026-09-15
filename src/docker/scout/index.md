---
title: Docker Scout
description: Get an overview on Docker Scout to proactively enhance your software
  supply chain security
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/scout/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: scout
order: 6990
---

Container images consist of layers and software packages, which are susceptible to vulnerabilities.
These vulnerabilities can compromise the security of containers and applications.

Docker Scout is a solution for proactively enhancing your software supply chain security.
By analyzing your images, Docker Scout compiles an inventory of components, also known as a Software Bill of Materials (SBOM).
The SBOM is matched against a continuously updated vulnerability database to pinpoint security weaknesses.

Docker Scout is a standalone service and platform that you can interact with
using Docker Hub, the Docker CLI, and the Docker Scout Dashboard.

{{< grid >}}
