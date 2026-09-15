---
title: Account FAQs
description: FAQs about Docker IDs, account creation, organizations, companies, seats,
  and members
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/faqs/accounts.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: faqs
order: 6840
---

## Individual accounts

### What is a Docker ID?

A Docker ID is a username for your Docker account that lets you access Docker
products. To create a Docker ID you need one of the following:

- An email address
- A Google account
- A GitHub account

Your Docker ID must be between 4 and 30 characters long, and can only contain
numbers and lowercase letters. You can't use any special characters or spaces.

For more information, see
[Create a Docker account](../accounts/individual/create-account.md).

### Can I change my Docker ID?

No. You can't change your Docker ID once it's created. If you need a different
Docker ID, you must create a new Docker account with a new Docker ID.

Docker IDs can't be reused after deactivation.

### What if my Docker ID is taken?

All Docker IDs are first-come, first-served except for companies that have a
U.S. Trademark on a username.

If you have a trademark for your Docker ID,
[Docker Support](https://hub.docker.com/support/contact/) can retrieve the
Docker ID for you.

## Organizations

### What's an organization name or namespace?

The organization name, sometimes referred to as the organization namespace or
the organization ID, is the unique identifier of a Docker organization. The
organization name can't be the same as an existing Docker ID.

For more information, see
[Organization accounts](../accounts/organization/index.md).

### How can I see how many active users are in my organization?

If your organization uses a Software Asset Management tool, you can use it to
find out how many users have Docker Desktop installed. If your organization
doesn't use this software, you can run an internal survey
to find out who is using Docker Desktop.

For more information, see [Identify your Docker users and their Docker accounts](../accounts/organization/setup/onboard.md#step-one-identify-your-docker-users).

### Do users need to authenticate with Docker before an owner can add them to an organization?

No. Organization owners can invite users with their email addresses, and also
assign them to a team during the invite process.

### Can I force my organization's members to authenticate before using Docker Desktop and are there any benefits?

Yes. You can
[enforce sign-in](../enterprise/security/enforce-sign-in/index.md).

Some benefits of enforcing sign-in are:

- Ensures users receive the benefits of your subscription.
- Ensures security features like [Image Access Management](../enterprise/security/hardened-desktop/image-access-management.md) and [Registry Access Management](../enterprise/security/hardened-desktop/registry-access-management.md) are applied.
- Ensures you gain insights into users' activity.

### Can I convert my personal Docker ID to an organization account?

Yes. You can convert your user account to an organization account. Once you
convert a user account into an organization, it's not possible to
revert it to a personal user account.

For prerequisites and instructions, see
[Convert an account into an organization](../accounts/organization/setup/convert-account.md).

### Do organization invitees take up seats?

Yes. A user invited to an organization will take up one of the provisioned
seats, even if that user hasn’t accepted their invitation yet.

To manage invites, see [Manage organization members](../accounts/organization/manage/members.md).

### Do organization owners take a seat?

Yes. Organization owners occupy a seat.

### What is the difference between user, invitee, seat, and member?

- User: Docker user with a Docker ID.
- Invitee: A user that an administrator has invited to join an organization but
  has not yet accepted their invitation.
- Seats: The number of purchased seats in an organization.
- Member: A user who has received and accepted an invitation to join an
  organization. Member can also refer to a member of a team within an
  organization.

### If I have two organizations and a user belongs to both organizations, do they take up two seats?

Yes. In a scenario where a user belongs to two organizations, they take up one
seat in each organization.

### Companies

#### Can I use a parent company if some of my organizations don’t have a Docker Business subscription?

Yes, but you can only add organizations with a Docker Business subscription
to a company. For more details, see [Add more organizations](../accounts/company/manage.md#add-more-organizations).

#### What happens if one of my organizations downgrades from Docker Business, but I still need access as a company owner?

To access and manage a nested organization, it must have a Docker Business
subscription. If an organization downgrades from Docker Business, its owner must
manage it outside of the company. For more details, see
[Add more organizations](../accounts/company/manage.md#add-more-organizations).

#### Do company owners occupy a subscription seat?

Company owners don't occupy a seat unless one of the following is true:

- They are added as a member of an organization under your company
- SSO is enabled and the company owner signs in through SSO, which
  automatically adds them as an organization member

When you first create a company, your account is both a company owner and an
organization owner, so it occupies a seat as long as you remain an organization
owner. To free up that seat,
[assign another user as the organization owner](../accounts/organization/manage/members.md#update-a-member-role)
and remove yourself from the organization. You keep full administrative access
as a company owner without using a subscription seat.

#### What permissions does the company owner have in the associated/nested organizations?

Company owners can navigate to the **Organizations** page to view all their
nested organizations in a single location. They can also view or edit
organization members and change single sign-on (SSO) and System for
Cross-domain Identity Management (SCIM) settings. Changes to company settings
impact all users in each organization under the company.

For more information, see [Roles and permissions](/manuals/security/roles-and-permissions.md).
