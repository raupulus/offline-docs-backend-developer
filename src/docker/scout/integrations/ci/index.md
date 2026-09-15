---
title: Using Docker Scout in continuous integration
description: How to set up Docker Scout in continuous integration pipelines
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/scout/integrations/ci/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: scout
order: 7170
---

You can analyze Docker images in continuous integration pipelines as you build
them using a GitHub action or the Docker Scout CLI plugin.

Available integrations:

- [GitHub Actions](gha.md)
- [GitLab](gitlab.md)
- [Microsoft Azure DevOps Pipelines](azure.md)
- [Circle CI](circle-ci.md)
- [Jenkins](jenkins.md)

You can also add runtime integration as part of your CI/CD pipeline, which lets
you assign an image to an environment, such as `production` or `staging`, when
you deploy it. For more information, see [Environment monitoring](../environment/index.md).
