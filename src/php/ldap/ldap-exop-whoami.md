---
title: ldap_exop_whoami
description: Ayuda de la operación extendida WHOAMI
source_url: https://www.php.net/manual/es/function.ldap-exop-whoami.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-exop-whoami.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43190
---

ldap_exop_whoami

Ayuda de la operación extendida WHOAMI

## Descripción

```php
ldap_exop_whoami(LDAP\Connection $ldap): string
```php

Realiza una operación extendida WHOAMI y devuelve los datos.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

## Valores devueltos

Los datos devueltos por el servidor, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |

## Véase también

`ldap_exop`
