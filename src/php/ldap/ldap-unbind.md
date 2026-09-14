---
title: ldap_unbind
description: Desconecta de un servidor LDAP
source_url: https://www.php.net/manual/es/function.ldap-unbind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-unbind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43570
---

ldap_unbind

Desconecta de un servidor LDAP

## Descripción

```php
ldap_unbind(LDAP\Connection $ldap): bool
```php

Desconecta de un servidor LDAP.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |

## Véase también

`ldap_bind`
