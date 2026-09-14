---
title: ldap_first_attribute
description: Retorna el primer atributo
source_url: https://www.php.net/manual/es/function.ldap-first-attribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-first-attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 303580c0b
order: 43220
---

ldap_first_attribute

Retorna el primer atributo

## Descripción

```php
ldap_first_attribute(LDAP\Connection $ldap, LDAP\ResultEntry $entry): string
```php

Retorna el primer atributo de la entrada proporcionada. Los demás atributos son leídos mediante la función `ldap_next_attribute`, llamada tantas veces como sea necesario.

De manera similar a la lectura de las entradas, los atributos son leídos uno tras otro, para una entrada.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`entry`  
Una instancia de `LDAP\ResultEntry`.

## Valores devueltos

Retorna el primer atributo de la entrada en caso de éxito, y `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `entry` ahora espera una instancia de `LDAP\ResultEntry` ; anteriormente, se esperaba un `resource` `ldap result entry` válido. |
| 8.0.0 | El tercer parámetro no utilizado `ber_identifier` ya no es aceptado. |

## Véase también

`ldap_next_attribute`, `ldap_get_attributes`
