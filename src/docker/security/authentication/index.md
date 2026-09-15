---
title: Authentication
description: Configure single sign-on, OIDC connections, and two-factor authentication.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/security/authentication/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: security
order: 7380
---

Authentication in Docker Home is how users and workloads prove who they are
before they access Docker products.

Two-factor authentication (2FA) protects an individual account. Single
sign-on (SSO) federates sign-in for an organization or company. OpenID
Connect (OIDC) connections authenticate CI workloads such as GitHub Actions.

## Choose an authentication method

| Method | Who it covers | Who configures it | How authentication works |
| --- | --- | --- | --- |
| Two-factor authentication (2FA) | An individual Docker account | The account holder | Password plus a time-based one-time password (TOTP) from an authenticator app |
| Single sign-on (SSO) | An organization or company | An organization or company owner | Users sign in through the organization's identity provider (IdP) |
| OIDC connections | GitHub Actions and similar workloads | An organization owner or editor | Docker exchanges short-lived tokens issued per workflow run |

SSO requires a Docker Business subscription. OIDC connections require a
Docker Team or Business subscription.

To require Docker Desktop users to sign in as organization members, see
[Enforce sign-in](../../enterprise/security/enforce-sign-in/index.md).
Enforce sign-in is configured in Enterprise, not in this section.

## Next steps

{{< grid >}}
