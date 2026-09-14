---
title: ldap_8859_to_t61
description: Convierte los caracteres 8859 en caracteres t61
source_url: https://www.php.net/manual/es/function.ldap-8859-to-t61.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-8859-to-t61.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 76f8c0151
order: 42960
---

ldap_8859_to_t61

Convierte los caracteres 8859 en caracteres t61

## Descripción

```php
ldap_8859_to_t61(string $value): string
```php

Convierte los caracteres `ISO-8859` en caracteres `t61`.

Esta función es útil si se debe utilizar un servidor `LDAPv2`.

## Parámetros

`value`  
El texto a convertir.

## Valores devueltos

Devuelve la conversión en `t61` del texto `value`, o `false` si ocurre un error.

## Véase también

`ldap_t61_to_8859`
