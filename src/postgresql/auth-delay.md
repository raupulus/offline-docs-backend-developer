---
title: auth_delay — pause on authentication failure
source_url: https://www.postgresql.org/docs/17/auth-delay.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: auth-delay.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 130
---

## auth_delay pause on authentication failure

auth_delay

`auth_delay` causes the server to pause briefly before reporting authentication failure, to make brute-force attacks on database passwords more difficult. Note that it does nothing to prevent denial-of-service attacks, and may even exacerbate them, since processes that are waiting before reporting authentication failure will still consume connection slots.

In order to function, this module must be loaded via [???](#guc-shared-preload-libraries) in `postgresql.conf`.

## Configuration Parameters

`auth_delay.milliseconds` (`integer`) <span class="indexterm"></span>  
The number of milliseconds to wait before reporting an authentication failure. The default is 0.

These parameters must be set in `postgresql.conf`. Typical usage might be:

    # postgresql.conf
    shared_preload_libraries = 'auth_delay'

    auth_delay.milliseconds = '500'

## Author

KaiGai Kohei <kaigai@ak.jp.nec.com>
