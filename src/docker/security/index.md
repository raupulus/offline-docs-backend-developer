---
title: Security
description: Secure Docker accounts, manage access, and control membership for individuals
  and organizations in Docker Home.
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/security/_index.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: security
order: 7320
---

Security helps individual users and organization owners secure their
accounts, manage access, and control membership. You configure these
settings in [Docker Home](https://app.docker.com/).

## Individual accounts

You sign in with your individual account.

- [Two-factor authentication](authentication/2fa/index.md)
(2FA) adds a time-based one-time password (TOTP) from an authenticator
app to your password.
- A [personal access token](access-tokens/personal-access-tokens.md)
(PAT) authenticates the Docker CLI and tools without your password, and
is required for CLI sign-in when 2FA is on or single sign-on (SSO) is
enforced.

## Organization accounts

Organization and company owners set up how members sign in, add them to
the organization, configure automation, and control what members can do.

- [Single sign-on](authentication/single-sign-on/index.md)
(SSO) federates sign-in through your identity provider, which can cover
one organization or every organization in a company.
- [Provisioning](provisioning/index.md) adds users with
System for Cross-domain Identity Management (SCIM), Just-in-Time (JIT)
provisioning, auto-provisioning, or domain matching.
- An [organization access token](access-tokens/organization-access-tokens.md)
(OAT) stays with the organization when membership changes.
- [OIDC connections](authentication/oidc-connections/index.md)
use OpenID Connect to authenticate GitHub Actions with short-lived
tokens, as an alternative to a long-lived OAT.
- [Roles and permissions](roles-and-permissions/index.md)
control what members can do after they join.

## Next steps

{{< grid >}}
