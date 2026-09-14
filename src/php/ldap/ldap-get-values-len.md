---
title: ldap_get_values_len
description: Lee todos los valores binarios de una entrada
source_url: https://www.php.net/manual/es/function.ldap-get-values-len.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-get-values-len.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_revision: fbc6f9055
order: 43300
---

ldap_get_values_len

Lee todos los valores binarios de una entrada

## Descripción

```php
ldap_get_values_len(LDAP\Connection $ldap, LDAP\ResultEntry $entry, string $attribute): array
```php

Lee todos los valores binarios de una entrada de un resultado.

Esta función se utiliza exactamente como la función `ldap_get_values`, con la excepción de que maneja datos binarios, y no strings.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`entry`  
Una instancia de `LDAP\ResultEntry`.

`attribute`  

## Valores devueltos

Devuelve un array de valores para el atributo en caso de éxito, y `false` en caso de error. Los valores son accesibles individualmente, con los índices numéricos del array. La indexación comienza en `0`. El número de valores devueltos está disponible en el índice 'count' del array devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `entry` ahora espera una instancia de `LDAP\ResultEntry` ; anteriormente, se esperaba un `resource` `ldap result entry` válido. |

## Véase también

`ldap_get_values`
