---
title: ldap_count_references
description: Cuenta el número de referencias en un resultado de búsqueda
source_url: https://www.php.net/manual/es/function.ldap-count-references.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-count-references.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43080
---

ldap_count_references

Cuenta el número de referencias en un resultado de búsqueda

## Descripción

```php
ldap_count_references(LDAP\Connection $ldap, LDAP\Result $result): int
```php

Cuenta el número de referencias en un resultado de búsqueda.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`result`  
Una instancia de `LDAP\Result`, devuelta por `ldap_list` o `ldap_search`.

## Valores devueltos

Devuelve el número de referencias en un resultado de búsqueda.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `LDAP\Result` ; anteriormente, se esperaba un `resource` `ldap result` válido. |

## Véase también

ldap_connect
