---
title: ldap_parse_exop
description: Analiza un objeto de resultado de una operación extendida LDAP
source_url: https://www.php.net/manual/es/function.ldap-parse-exop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-parse-exop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43440
---

ldap_parse_exop

Analiza un objeto de resultado de una operación extendida LDAP

## Descripción

```php
ldap_parse_exop(LDAP\Connection $ldap, LDAP\Result $result, [string $response_data], [string $response_oid]): bool
```php

Analiza los datos de una operación extendida LDAP a partir de un objeto de resultado `result`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`result`  
Una instancia de `LDAP\Result`, devuelta por `ldap_list` o `ldap_search`.

`response_data`  
Será rellenado con los datos de respuesta.

`response_oid`  
Será rellenado con el OID de respuesta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `LDAP\Result` ; anteriormente, se esperaba un `resource` `ldap result` válido. |

## Véase también

`ldap_exop`
