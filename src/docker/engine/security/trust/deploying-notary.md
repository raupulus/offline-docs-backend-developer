---
title: Deploy Notary Server with Compose
description: Deploying Notary
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/engine/security/trust/deploying_notary.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: engine
order: 5670
---

The easiest way to deploy Notary Server is by using Docker Compose. To follow the procedure on this page, you must have already [installed Docker Compose](../../../compose/install/index.md).

1. Clone the Notary repository.
   
   ```console
   $ git clone https://github.com/theupdateframework/notary.git
   ```

2. Build and start Notary Server with the sample certificates.

   ```console
   $ docker compose up -d 
   ```

   For more detailed documentation about how to deploy Notary Server, see the [instructions to run a Notary service](https://github.com/theupdateframework/notary/blob/master/docs/running_a_service.md) as well as [the Notary repository](https://github.com/theupdateframework/notary) for more information.

3. Make sure that your Docker or Notary client trusts Notary Server's certificate before you try to interact with the Notary server.

See the instructions for [Docker](/reference/cli/docker/#notary) or
for [Notary](https://github.com/docker/notary#using-notary) depending on which one you are using.

## If you want to use Notary in production

The Compose sample on this page is for local testing and uses sample
certificates. For a production deployment, follow the upstream
[instructions to run a Notary service](https://github.com/theupdateframework/notary/blob/master/docs/running_a_service.md)
and the rest of [the Notary repository](https://github.com/theupdateframework/notary).
