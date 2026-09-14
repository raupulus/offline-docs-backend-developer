---
title: ldap_get_dn
description: Lee el DN de una entrada
source_url: https://www.php.net/manual/es/function.ldap-get-dn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-get-dn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43270
---

ldap_get_dn

Lee el DN de una entrada

## Descripción

```php
ldap_get_dn(LDAP\Connection $ldap, LDAP\ResultEntry $entry): string
```php

Lee el DN de una entrada de un resultado.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`entry`  
Una instancia de `LDAP\ResultEntry`.

## Valores devueltos

Devuelve el DN de la entrada del resultado, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `entry` ahora espera una instancia de `LDAP\ResultEntry` ; anteriormente, se esperaba un `resource` `ldap result entry` válido. |
