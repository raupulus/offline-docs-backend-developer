---
title: ldap_rename
description: Modifica el nombre de una entrada
source_url: https://www.php.net/manual/es/function.ldap-rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: b7cbd468c
order: 43490
---

ldap_rename

Modifica el nombre de una entrada

## Descripción

```php
ldap_rename(LDAP\Connection $ldap, string $dn, string $new_rdn, string $new_parent, bool $delete_old_rdn, [array $controls]): bool
```php

Modifica la entrada `dn`, tanto en su nombre como en su ubicación.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  
El nombre DN de la entrada LDAP.

`new_rdn`  
El nuevo RDN.

`new_parent`  
La nueva entrada padre/superior.

`delete_old_rdn`  
Si este argumento vale `true`, el valor RDN antiguo es eliminado. De lo contrario, se conserva como un valor no distinguido.

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
> `ldap_rename` actualmente solo funciona con LDAPv3. Puede ser necesario utilizar `ldap_set_option` antes de conectarse para poder usar LDAPv3. Esta función solo está disponible cuando se utiliza OpenLDAP 2.x.x O Netscape Directory SDK x.x.

## Véase también

`ldap_rename_ext`, `ldap_modify`
