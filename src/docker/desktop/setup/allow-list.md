---
title: Allowlist for Docker Desktop
description: A list of domain URLs required for Docker Desktop to function correctly
  within an organization.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/desktop/setup/allow-list.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: desktop
order: 3140
---

{{< summary-bar feature_name="Allow list" >}}

This page contains the domain URLs that you need to add to a firewall allowlist to ensure Docker Desktop works properly within your organization.

## Domain URLs to allow

| Domains                                                                              | Description                                  |
| ------------------------------------------------------------------------------------ | -------------------------------------------- |
| https://notify.bugsnag.com                                                           | Error reports                                |
| https://sessions.bugsnag.com                                                         | Error reports                                |
| https://auth.docker.io                                                               | Authentication                               |
| https://cdn.auth0.com                                                                | Authentication                               |
| https://login.docker.com                                                             | Authentication                               |
| https://auth.docker.com                                                              | Authentication                               |
| https://desktop.docker.com                                                           | Update                                       |
| https://hub.docker.com                                                               | Docker Hub                                   |
| https://registry-1.docker.io                                                         | Docker Pull/Push                             |
| https://production.cloudfront.docker.com                                             | Docker Pull/Push                             |
| https://docker-pinata-support.s3.amazonaws.com                                       | Troubleshooting                              |
| https://api.dso.docker.com                                                           | Docker Scout service                         |
| https://api.docker.com                                                               | New API                                      |
| https://api.offload.docker.com                                                       | Docker Offload                               |
| https://dhi.io                                                                       | Docker Hardened Images                       |
| https://registry.scout.docker.com                                                    | Docker Scout registry for DHI attestations   |
| https://ai-backend-service.docker.com                                                | [Gordon](../../ai/gordon/index.md)       |
