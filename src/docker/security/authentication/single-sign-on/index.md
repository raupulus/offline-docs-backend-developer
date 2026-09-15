---
title: Single sign-on overview
description: Learn how single sign-on works, how to set it up, and the required SSO
  attributes.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/security/authentication/single-sign-on/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: security
order: 7420
---

{{< summary-bar feature_name="SSO" >}}

Single sign-on (SSO) lets users access Docker by authenticating through their
identity providers (IdPs). SSO can be configured for an entire company,
including all associated organizations, or for a single organization that has a
Docker Business subscription.

## How SSO works

When SSO is enabled, Docker supports a non-IdP-initiated flow for user sign-in.
Instead of signing in with a Docker username and password, users are redirected
to your IdP’s sign-in page. Users must initiate the SSO authentication process
by signing in to Docker Hub or Docker Desktop.

The following diagram illustrates how SSO operates and is managed between
Docker Hub, Docker Desktop, and your IdP.

![SSO architecture](images/SSO.png)

## Set up SSO

To configure SSO in Docker, follow these steps:

1. [Configure your domain](connect.md) by creating and verifying it.
1. [Create your SSO connection](connect.md) in Docker and your IdP.
1. Link Docker to your identity provider.
1. Test your SSO connection.
1. Provision users in Docker.
1. Optional. [Enforce sign-in](../../../enterprise/security/enforce-sign-in/index.md).
1. [Manage your SSO configuration](manage.md).

Once configuration is complete, users can sign in to Docker services using
their company email address. After signing in, users are added to your company,
assigned to an organization, and added to a team.

> [!IMPORTANT]
>
> When SSO is enforced, CLI password-based sign-in is no longer supported.
> Use a personal access token (PAT) for CLI access. For more information, see the
> [security announcement](../../security-announcements.md#deprecation-of-password-logins-on-cli-when-sso-enforced).

## Next steps

- Start [configuring SSO](connect.md).
- Read the [FAQs](../../../faqs/security.md).
- [Troubleshoot](troubleshoot-sso.md) SSO issues.
