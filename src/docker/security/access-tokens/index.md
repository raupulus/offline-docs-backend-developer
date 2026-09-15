---
title: Access tokens
description: Create and manage personal and organization access tokens for Docker
  Hub authentication.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/security/access-tokens/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: security
order: 7330
---

Access tokens let you authenticate to Docker Hub without using your password.
Use a token for the Docker CLI, automation, and any account that has
two-factor authentication (2FA) or enforced single sign-on (SSO), because
password sign-in to the CLI is not supported in those cases.

## Choose a token type

| Token | Ownership | Use when | Limitations |
| --- | --- | --- | --- |
| Personal access token (PAT) | Tied to an individual Docker account | CLI access, local tools, and automation that should run as you. Required for CLI sign-in when 2FA is on or SSO is enforced | Access ends if the account leaves the organization or the token is revoked |
| Organization access token (OAT) | Owned by the organization. Any organization owner can manage it | CI/CD and other automation that must keep working when membership changes | Incompatible with Docker Desktop and Image Access Management |

For GitHub Actions, [OIDC connections](../authentication/oidc-connections/index.md)
are an alternative to storing a long-lived organization access token.

## Next steps

{{< grid >}}
