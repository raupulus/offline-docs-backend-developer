---
title: ldap_next_entry
description: Lee la siguiente entrada
source_url: https://www.php.net/manual/es/function.ldap-next-entry.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-next-entry.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43420
---

ldap_next_entry

Lee la siguiente entrada

## Descripción

```php
ldap_next_entry(LDAP\Connection $ldap, LDAP\ResultEntry $entry): LDAP\ResultEntry
```php

Lee la siguiente entrada del resultado. Llamadas repetidas a `ldap_next_entry` devolverán todas las entradas hasta que no queden más. La primera llamada debe realizarse con la función `ldap_first_entry`. El argumento `entry` es aquel que fue devuelto por la función `ldap_first_entry`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`entry`  
Una instancia de `LDAP\ResultEntry`.

## Valores devueltos

Devuelve una instancia de `LDAP\ResultEntry` para la siguiente entrada del resultado, donde la primera entrada fue leída por la función `ldap_first_entry`. Si no hay más entradas en el resultado, `false` es devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `entry` ahora espera una instancia de `LDAP\ResultEntry` ; anteriormente, se esperaba un `resource` `ldap result entry` válido. |
| 8.1.0 | Ahora devuelve una instancia de `LDAP\Result`; anteriormente, se devolvía un `resource`. |

## Véase también

`ldap_get_entries`
