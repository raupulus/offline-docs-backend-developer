---
title: ldap_delete_ext
description: Elimina una entrada de un directorio
source_url: https://www.php.net/manual/es/function.ldap-delete-ext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-delete-ext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: fbc6f9055
order: 43090
---

ldap_delete_ext

Elimina una entrada de un directorio

## Descripción

```php
ldap_delete_ext(LDAP\Connection $ldap, string $dn, [array $controls]): LDAP\Result
```php

Realiza lo mismo que la función `ldap_delete` pero devuelve una instancia `LDAP\Result` para analizar con `ldap_parse_result`.

## Parámetros

Ver la función `ldap_delete`

## Valores devueltos

Devuelve una instancia de `LDAP\Result`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | Ahora devuelve una instancia de `LDAP\Result`; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |

## Véase también

`ldap_delete`, `ldap_parse_result`
