---
title: DROP SUBSCRIPTION
description: remove a subscription
source_url: https://www.postgresql.org/docs/17/sql-dropsubscription.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_subscription.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2570
---

DROP SUBSCRIPTION

DROP SUBSCRIPTION

7

SQL - Language Statements

DROP SUBSCRIPTION

remove a subscription

DROP SUBSCRIPTION \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP SUBSCRIPTION` removes a subscription from the database cluster.

To execute this command the user must be the owner of the subscription.

`DROP SUBSCRIPTION` cannot be executed inside a transaction block if the subscription is associated with a replication slot. (You can use [`ALTER SUBSCRIPTION`](#sql-altersubscription) to unset the slot.)

## Parameters

`IF EXISTS`  
Do not throw an error if the subscription does not exist. A notice is issued in this case.

\<name\>  
The name of a subscription to be dropped.

`CASCADE`; `RESTRICT`  
These key words do not have any effect, since there are no dependencies on subscriptions.

## Notes

When dropping a subscription that is associated with a replication slot on the remote host (the normal state), `DROP SUBSCRIPTION` will connect to the remote host and try to drop the replication slot (and any remaining table synchronization slots) as part of its operation. This is necessary so that the resources allocated for the subscription on the remote host are released. If this fails, either because the remote host is not reachable or because the remote replication slot cannot be dropped or does not exist or never existed, the `DROP SUBSCRIPTION` command will fail. To proceed in this situation, first disable the subscription by executing [ `ALTER SUBSCRIPTION ... DISABLE`](#sql-altersubscription-params-disable), and then disassociate it from the replication slot by executing [ `ALTER SUBSCRIPTION ... SET (slot_name = NONE)`](#sql-altersubscription-params-set). After that, `DROP SUBSCRIPTION` will not attempt to drop the subscription's own replication slot. It may still connect to the publisher to drop internally-created table synchronization slots if some table synchronization is left unfinished; if the publisher is unreachable, those slots (and the main slot, if it still exists) must be dropped manually. Otherwise it/they will continue to reserve WAL and might eventually cause the disk to fill up. See also [???](#logical-replication-subscription-slot).

If a subscription is associated with a replication slot, then `DROP SUBSCRIPTION` cannot be executed inside a transaction block.

## Examples

Drop a subscription:

    DROP SUBSCRIPTION mysub;

## Compatibility

`DROP SUBSCRIPTION` is a PostgreSQL extension.

## See Also
