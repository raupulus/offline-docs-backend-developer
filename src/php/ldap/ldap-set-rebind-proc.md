---
title: ldap_set_rebind_proc
description: Configura una función de retorno para rehacer las ligaduras durante la
  búsqueda de referentes
source_url: https://www.php.net/manual/es/function.ldap-set-rebind-proc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-set-rebind-proc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43530
---

ldap_set_rebind_proc

Configura una función de retorno para rehacer las ligaduras durante la búsqueda de referentes

## Descripción

```php
ldap_set_rebind_proc(LDAP\Connection $ldap, callable $callback): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.0.0 | `callback` ahora es nullable. |
