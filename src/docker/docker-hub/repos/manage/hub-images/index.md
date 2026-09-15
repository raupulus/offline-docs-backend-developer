---
title: Image management
description: Learn how to manage images in Docker Hub repositories
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/docker-hub/repos/manage/hub-images/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: docker-hub
order: 4380
---

Docker Hub provides powerful features for managing and organizing your
repository content, ensuring that your images and artifacts are accessible,
version-controlled, and easy to share. This section covers key image management
tasks, including tagging, pushing images, transferring images between
repositories, and supported software artifacts.


- [Tags](tags.md): Tags help you version and organize different iterations of
  your images within a single repository. This topic explains tagging and
  provides guidance on how to create, view, and delete tags in Docker Hub.
- [Image Management](manage.md): View, filter, and delete images and image
  indexes in your repository.
- [Software artifacts](oci-artifacts.md): Docker Hub supports OCI (Open
  Container Initiative) artifacts, allowing you to store, manage, and distribute
  a range of content beyond standard Docker images, including Helm charts,
  vulnerability reports, and more. This section provides an overview of OCI
  artifacts as well as some examples of pushing them to Docker Hub.
- [Push images to Hub](push.md): Docker Hub enables you to push local images
  to it, making them available for your team or the Docker community. Learn how
  to configure your images and use the `docker push` command to upload them to
  Docker Hub.
- [Move images between repositories](move.md): Organizing content across
  different repositories can help streamline collaboration and resource
  management. This topic details how to move images from one Docker Hub
  repository to another, whether for personal consolidation or to share images
  with an organization.
