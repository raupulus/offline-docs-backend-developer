---
title: ldap_next_attribute
description: Lee el siguiente atributo
source_url: https://www.php.net/manual/es/function.ldap-next-attribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-next-attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 303580c0b
order: 43410
---

ldap_next_attribute

Lee el siguiente atributo

## Descripción

```php
ldap_next_attribute(LDAP\Connection $ldap, LDAP\ResultEntry $entry): string
```php

Lee el siguiente atributo de una entrada. La primera llamada a `ldap_next_attribute` se realiza con el `entry` devuelto por `ldap_first_attribute`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`entry`  
Una instancia de `LDAP\ResultEntry`.

## Valores devueltos

Devuelve el siguiente atributo de la entrada en caso de éxito, y `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `entry` ahora espera una instancia de `LDAP\ResultEntry` ; anteriormente, se esperaba un `resource` `ldap result entry` válido. |
| 8.0.0 | El tercer argumento no utilizado `ber_identifier` ya no es aceptado. |

## Véase también

`ldap_get_attributes`
