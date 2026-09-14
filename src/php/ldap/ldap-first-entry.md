---
title: ldap_first_entry
description: Devuelve la primera entrada
source_url: https://www.php.net/manual/es/function.ldap-first-entry.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-first-entry.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: fbc6f9055
order: 43230
---

ldap_first_entry

Devuelve la primera entrada

## Descripción

```php
ldap_first_entry(LDAP\Connection $ldap, LDAP\Result $result): LDAP\ResultEntry
```php

Devuelve la primera entrada del resultado. Las siguientes serán leídas mediante la función `ldap_next_entry`, llamándola tantas veces como sea necesario.

Las entradas de un resultado LDAP se leen secuencialmente con las funciones `ldap_first_entry` y `ldap_next_entry`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`result`  
Una instancia de `LDAP\Result`, devuelta por `ldap_list` o `ldap_search`.

## Valores devueltos

Devuelve una instancia de `LDAP\ResultEntry`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `LDAP\Result` ; anteriormente, se esperaba un `resource` `ldap result` válido. |
| 8.1.0 | Ahora devuelve una instancia de `LDAP\ResultEntry`; anteriormente, se devolvía un `resource`. |

## Véase también

`ldap_get_entries`
