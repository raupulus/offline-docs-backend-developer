---
title: ldap_error
description: Devuelve el mensaje LDAP de la última orden LDAP
source_url: https://www.php.net/manual/es/function.ldap-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43140
---

ldap_error

Devuelve el mensaje LDAP de la última orden LDAP

## Descripción

```php
ldap_error(LDAP\Connection $ldap): string
```php

Devuelve el mensaje de error asociado a la conexión `ldap`. Aunque los números de error LDAP están estandarizados, diferentes bibliotecas devuelven diferentes mensajes, o a veces, mensajes en el idioma local. No se debe confiar en el mensaje de error, sino en el número de error.

A menos que se reduzca el nivel de error en `php.ini`, o que se prefijen las órdenes LDAP con `@` para suprimir los mensajes, los errores LDAP también se mostrarán en la salida HTML.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

## Valores devueltos

Devuelve un mensaje de error LDAP.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |

## Véase también

`ldap_err2str`, `ldap_errno`
