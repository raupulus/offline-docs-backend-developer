---
title: ldap_add_ext
description: Añade una entrada en un directorio LDAP
source_url: https://www.php.net/manual/es/function.ldap-add-ext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-add-ext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: fbc6f9055
order: 42970
---

ldap_add_ext

Añade una entrada en un directorio LDAP

## Descripción

```php
ldap_add_ext(LDAP\Connection $ldap, string $dn, array $entry, [array $controls]): LDAP\Result
```php

Realiza lo mismo que la función `ldap_add` pero devuelve una instancia `LDAP\Result` para analizar con `ldap_parse_result`.

## Parámetros

Ver la función `ldap_add`

## Valores devueltos

Devuelve una instancia de `LDAP\Result`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | Ahora devuelve una instancia de `LDAP\Result`; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`ldap_add`, `ldap_parse_result`
