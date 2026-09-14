---
title: ldap_get_entries
description: Lee todas las entradas del resultado
source_url: https://www.php.net/manual/es/function.ldap-get-entries.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-get-entries.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43280
---

ldap_get_entries

Lee todas las entradas del resultado

## Descripción

```php
ldap_get_entries(LDAP\Connection $ldap, LDAP\Result $result): array
```php

Lee todas las entradas del resultado proporcionado, así como los atributos y los valores múltiples.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`result`  
Una instancia de `LDAP\Result`, devuelta por `ldap_list` o `ldap_search`.

## Valores devueltos

Devuelve todas las entradas del resultado en forma de un array multidimensional, o `false` si ocurre un error.

La estructura del array es la siguiente. El índice de atributo se convierte a minúsculas (los atributos son sensibles a mayúsculas/minúsculas para los servidores de directorio, pero no lo son cuando se utilizan como índices de arrays).

    return_value["count"] = número de entradas en el resultado
    return_value[0] : se refiere a los detalles de la primera entrada

    return_value[i]["dn"] =  DN de la i-ésima entrada del resultado

    return_value[i]["count"] = número de atributos de la i-ésima entrada
    return_value[i][j] = Nombre del j-ésimo atributo de la i-ésima entrada del resultado

    return_value[i]["attribute"]["count"] = número de valores de los atributos de la i-ésima entrada
    return_value[i]["attribute"][j] = j-ésimo valor de la i-ésima entrada

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `LDAP\Result` ; anteriormente, se esperaba un `resource` `ldap result` válido. |

## Véase también

`ldap_first_entry`, `ldap_next_entry`
