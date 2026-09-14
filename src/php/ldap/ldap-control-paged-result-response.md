---
title: ldap_control_paged_result_response
description: Recupera el cookie de paginación LDAP
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-control-paged-result-response.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: e706a6b55
order: 43050
---

ldap_control_paged_result_response

Recupera el cookie de paginación LDAP

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y fue *ELIMINADA* a partir de PHP 8.0.0. En su lugar, se debe utilizar el parámetro `controls` de `ldap_search`. Véase también [LDAP Controls](#ldap.controls) para más detalles.

## Descripción

```php
ldap_control_paged_result_response(resource $link, resource $result, [string $cookie], [int $estimated]): bool
```php

Recupera las informaciones de paginación enviadas por el servidor.

## Parámetros

`link`  
Un `resource` LDAP, retornado por `ldap_connect`.

`result`  

`cookie`  
Una estructura opaca enviada por el servidor.

`estimated`  
El número estimado de entradas a recuperar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                         |
|---------|-------------------------------------|
| 8.0.0   | Esta función ha sido suprimida.     |
| 7.4.0   | Esta función se ha vuelto obsoleta. |

## Véase también

`ldap_control_paged_result`, [RFC2696 : Extensión de control LDAP para una manipulación simplificada de los resultados paginados](https://datatracker.ietf.org/doc/html/rfc2696)
