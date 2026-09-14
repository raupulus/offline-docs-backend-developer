---
title: ldap_bind_ext
description: Vincula un directorio LDAP
source_url: https://www.php.net/manual/es/function.ldap-bind-ext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-bind-ext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 42990
---

ldap_bind_ext

Vincula un directorio LDAP

## Descripción

```php
#[\SensitiveParameter] ldap_bind_ext(LDAP\Connection $ldap, [string $dn], [string $password], [array $controls]): LDAP\Result
```php

Realiza lo mismo que la función `ldap_bind` pero devuelve una instancia `LDAP\Result` para analizar con `ldap_parse_result`.

## Parámetros

Véase `ldap_bind`

## Valores devueltos

Devuelve una instancia de `LDAP\Result`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | Ahora devuelve una instancia de `LDAP\Result`; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |

## Véase también

`ldap_bind`, `ldap_parse_result`
