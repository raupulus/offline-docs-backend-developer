---
title: ldap_delete
description: Elimina una entrada en un directorio
source_url: https://www.php.net/manual/es/function.ldap-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: b7cbd468c
order: 43100
---

ldap_delete

Elimina una entrada en un directorio

## Descripción

```php
ldap_delete(LDAP\Connection $ldap, string $dn, [array $controls]): bool
```php

Elimina una entrada específica de un directorio LDAP.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  
El nombre DN de la entrada LDAP.

`controls`  
Array de [Controles LDAP](#ldap.controls) a enviar con la petición.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |
| 7.3.0 | Se ha añadido soporte para `controls`. |

## Véase también

`ldap_delete_ext`, `ldap_add`
