---
title: ldap_rename_ext
description: Cambia el nombre de una entrada
source_url: https://www.php.net/manual/es/function.ldap-rename-ext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-rename-ext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: b7cbd468c
order: 43480
---

ldap_rename_ext

Cambia el nombre de una entrada

## Descripción

```php
ldap_rename_ext(LDAP\Connection $ldap, string $dn, string $new_rdn, string $new_parent, bool $delete_old_rdn, [array $controls]): LDAP\Result
```php

Realiza la misma operación que `ldap_rename` pero devuelve una instancia de `LDAP\Result` para analizar con `ldap_parse_result`.

## Parámetros

Consulte `ldap_rename`

## Valores devueltos

Devuelve una instancia de `LDAP\Result`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | Ahora devuelve una instancia de `LDAP\Result`; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |
| 7.3.0 | Se ha añadido el soporte para `controls` |

## Véase también

`ldap_rename`, `ldap_parse_result`
