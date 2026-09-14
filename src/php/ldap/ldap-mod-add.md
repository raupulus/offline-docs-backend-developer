---
title: ldap_mod_add
description: Añade un atributo a la entrada actual
source_url: https://www.php.net/manual/es/function.ldap-mod-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-mod-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 43340
---

ldap_mod_add

Añade un atributo a la entrada actual

## Descripción

```php
ldap_mod_add(LDAP\Connection $ldap, string $dn, array $entry, [array $controls]): bool
```php

Añade el atributo `entry` a la entrada `dn`. Para añadir un nuevo objeto completo, consulte la función `ldap_add`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  
El nombre DN de la entrada LDAP.

`entry`  
Array asociativo que enumera los valores de los atributos a añadir. Si un atributo no existía previamente, será añadido. Si un atributo existe, solo pueden añadirse valores si admite múltiples valores.

`controls`  
Array de [Controles LDAP](#ldap.controls) a enviar con la petición.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |
| 7.3.0 | Se añadió soporte para `controls`. |

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`ldap_mod_add_ext`, `ldap_mod_del`, `ldap_mod_replace`, `ldap_modify_batch`
