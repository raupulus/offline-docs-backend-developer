---
title: ldap_mod_replace
description: Remplaza un atributo en la entrada actual
source_url: https://www.php.net/manual/es/function.ldap-mod-replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-mod-replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: b7cbd468c
order: 43380
---

ldap_mod_replace

Remplaza un atributo en la entrada actual

## Descripción

```php
ldap_mod_replace(LDAP\Connection $ldap, string $dn, array $entry, [array $controls]): bool
```php

Remplaza uno o varios atributos de la entrada `dn`. También puede añadir o eliminar atributos.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  
El nombre DN de la entrada LDAP.

`entry`  
Array asociativo que enumera los atributos a reemplazar. El envío de un array vacío como valor eliminará el atributo, mientras que el envío de un atributo que no exista aún en esta entrada lo añadirá.

`controls`  
Array de [Controles LDAP](#ldap.controls) a enviar con la petición.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |
| 7.3.0 | Soporte para `controls` ha sido añadido. |

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`ldap_mod_replace_ext`, `ldap_mod_del`, `ldap_mod_add`, `ldap_modify_batch`
