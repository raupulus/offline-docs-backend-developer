---
title: SCIM overview
description: Learn how System for Cross-domain Identity Management works and how to
  set it up.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/security/provisioning/scim/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: security
order: 7500
---

{{< summary-bar feature_name="SSO" >}}

Automate user management for your Docker organization using System for
Cross-domain Identity Management (SCIM). SCIM automatically provisions and
de-provisions users, synchronizes team memberships, and keeps your Docker
organization in sync with your identity provider.

This page shows you how to automate user provisioning and de-provisioning for
Docker using SCIM.

## Prerequisites

Before you begin, you must have:

- SSO configured for your organization
- Administrator access to Docker Home and your identity provider

## How SCIM works

SCIM automates user provisioning and de-provisioning for Docker through your
identity provider. After you enable SCIM, any user assigned to your
Docker application in your identity provider is automatically provisioned and
added to your Docker organization. When a user is removed from the Docker
application in your identity provider, SCIM deactivates and removes them from
your Docker organization.

In addition to provisioning and removal, SCIM also syncs profile updates like
name changes made in your identity provider. You can use SCIM alongside Docker's
default Just-in-Time (JIT) provisioning or on its own with JIT disabled.

SCIM automates:

- Creating users
- Updating user profiles
- Removing and deactivating users
- Re-activating users
- Group mapping

> [!NOTE]
>
> SCIM only manages users provisioned through your identity provider after
> SCIM is enabled. It cannot remove users who were manually added to your Docker
> organization before SCIM was set up.
>
> To remove those users, delete them manually from your Docker organization.
> For more information, see
> [Manage organization members](../../../accounts/organization/manage/members.md).

## Next steps

- [Migrate JIT to SCIM](migrate-scim.md) if users were provisioned with Just-in-Time (JIT) before you enabled SCIM.
- [Group mapping](group-mapping.md) to sync identity provider groups with members.
- [Troubleshoot provisioning](../troubleshoot-provisioning.md) for SCIM, JIT, and attribute issues.
