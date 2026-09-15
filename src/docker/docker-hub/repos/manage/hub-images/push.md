---
title: Push images to a repository
description: Learn how to add content to a repository on Docker Hub.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/docker-hub/repos/manage/hub-images/push.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: docker-hub
order: 4440
---

To add content to a repository on Docker Hub, you need to tag your Docker image
and then push it to your repository. This process lets you share your
images with others or use them in different environments.

1. Tag your Docker image.

   The `docker tag` command assigns a tag to your Docker image, which includes
   your Docker Hub namespace and the repository name. The general syntax is:

   ```console
   $ docker tag [SOURCE_IMAGE[:TAG]] [NAMESPACE/REPOSITORY[:TAG]]
   ```

   Example:

   If your local image is called `my-app` and you want to tag it for the
   repository `my-namespace/my-repo` with the tag `v1.0`, run:

   ```console
   $ docker tag my-app my-namespace/my-repo:v1.0
   ```

2. Push the image to Docker Hub.

   Use the `docker push` command to upload your tagged image to the specified
   repository on Docker Hub.

   Example:

   ```console
   $ docker push my-namespace/my-repo:v1.0
   ```

   This command pushes the image tagged `v1.0` to the `my-namespace/my-repo` repository.

3. Verify the image on Docker Hub.

   Sign in to [Docker Hub](https://hub.docker.com) and navigate to your
   repository (`my-namespace/my-repo` in this example). Select the **Tags**
   tab to confirm that your tag (`v1.0` in this example) appears in the list.
