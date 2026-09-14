---
title: ldap_mod_del
description: Elimina un atributo de la entrada actual
source_url: https://www.php.net/manual/es/function.ldap-mod-del.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-mod-del.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: b7cbd468c
order: 43360
---

ldap_mod_del

Elimina un atributo de la entrada actual

## Descripción

```php
ldap_mod_del(LDAP\Connection $ldap, string $dn, array $entry, [array $controls]): bool
```php

Elimina uno o varios atributos de la entrada `dn`. La eliminación de objetos se realiza mediante `ldap_delete`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  
El nombre DN de la entrada LDAP.

`entry`  

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

`ldap_mod_del_ext`, `ldap_mod_add`, `ldap_mod_replace`, `ldap_modify_batch`
