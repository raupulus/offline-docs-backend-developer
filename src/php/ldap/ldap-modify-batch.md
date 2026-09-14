---
title: ldap_modify_batch
description: Agrupa modificaciones y las ejecuta en una entrada LDAP
source_url: https://www.php.net/manual/es/function.ldap-modify-batch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-modify-batch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: b7cbd468c
order: 43390
---

ldap_modify_batch

Agrupa modificaciones y las ejecuta en una entrada LDAP

## Descripción

```php
ldap_modify_batch(LDAP\Connection $ldap, string $dn, array $modifications_info, [array $controls]): bool
```php

Modifica una entrada existente en un directorio LDAP. Permite especificar de manera detallada las modificaciones a realizar.

## Parámetros

`ldap`  
Un recurso LDAP, devuelto por la función `ldap_connect`.

`dn`  
El nombre único de la entrada LDAP.

`modifications_info`  
Un array que especifica las modificaciones a realizar. Cada entrada de este array es un array asociativo que contiene dos o tres claves: `attrib` corresponde al nombre del atributo a modificar, `modtype` corresponde al tipo de modificación a realizar, y (según el tipo de modificación) `values` corresponde a un array de valores de atributo correspondiente a la modificación.

Los valores posibles para `modtype` son:

`LDAP_MODIFY_BATCH_ADD`  
Cada valor especificado mediante `values` se añade (como valor adicional) al atributo nombrado por `attrib`.

`LDAP_MODIFY_BATCH_REMOVE`  
Cada valor especificado mediante `values` se elimina del atributo nombrado por `attrib`. Todos los valores del atributo que no estén presentes en el array `values` permanecerán sin cambios.

`LDAP_MODIFY_BATCH_REMOVE_ALL`  
Todos los valores se eliminan del atributo nombrado por `attrib`. No es necesario proporcionar una entrada `values`.

`LDAP_MODIFY_BATCH_REPLACE`  
Todos los valores actuales del atributo nombrado por `attrib` se reemplazan con los valores especificados mediante el array `values`.

Tenga en cuenta que todos los valores de `attrib` deben ser strings, todos los valores de `values` deben ser un array de strings, y todos los valores de `modtype` deben ser una de las constantes LDAP_MODIFY_BATCH\_\*.

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

## Ejemplos

Añadir un número de teléfono a un contacto

```
<?php
$dn = "cn=John Smith,ou=Wizards,dc=example,dc=com";
$modifs = [
    [
        "attrib"  => "telephoneNumber",
        "modtype" => LDAP_MODIFY_BATCH_ADD,
        "values"  => ["+1 555 555 1717"],
    ],
];
ldap_modify_batch($connection, $dn, $modifs);
?>

    
```php

Renombrar un usuario

```
<?php
$dn = "cn=John Smith,ou=Wizards,dc=example,dc=com";
$modifs = [
    [
        "attrib"  => "sn",
        "modtype" => LDAP_MODIFY_BATCH_REPLACE,
        "values"  => ["Smith-Jones"],
    ],
    [
        "attrib"  => "givenName",
        "modtype" => LDAP_MODIFY_BATCH_REPLACE,
        "values"  => ["Jack"],
    ],
];
ldap_modify_batch($connection, $dn, $modifs);
ldap_rename($connection, $dn, "cn=Jack Smith-Jones", NULL, TRUE);
?>

    
```php

Añadir dos direcciones de correo electrónico a un usuario

```
<?php
$dn = "cn=Jack Smith-Jones,ou=Wizards,dc=example,dc=com";
$modifs = [
    [
        "attrib"  => "mail",
        "modtype" => LDAP_MODIFY_BATCH_ADD,
        "values"  => [
            "jack.smith@example.com",
            "jack.smith-jones@example.com",
        ],
    ],
];
ldap_modify_batch($connection, $dn, $modifs);
?>

    
```php

Modificar la contraseña de un usuario

```
<?php
$dn = "cn=Jack Smith-Jones,ou=Wizards,dc=example,dc=com";
$modifs = [
    [
        "attrib"  => "userPassword",
        "modtype" => LDAP_MODIFY_BATCH_REMOVE,
        "values"  => ["Tr0ub4dor&3"],
    ],
    [
        "attrib"  => "userPassword",
        "modtype" => LDAP_MODIFY_BATCH_ADD,
        "values"  => ["correct horse battery staple"],
    ],
];
ldap_modify_batch($connection, $dn, $modifs);
?>

    
```php

Modificar la contraseña de un usuario (Active Directory)

```
<?php
function adifyPw($pw)
{
    return iconv("UTF-8", "UTF-16LE", '"' . $pw . '"');
}

$dn = "cn=Jack Smith-Jones,ou=Wizards,dc=ad,dc=example,dc=com";
$modifs = [
    [
        "attrib"  => "unicodePwd",
        "modtype" => LDAP_MODIFY_BATCH_REMOVE,
        "values"  => [adifyPw("Tr0ub4dor&3")],
    ],
    [
        "attrib"  => "unicodePwd",
        "modtype" => LDAP_MODIFY_BATCH_ADD,
        "values"  => [adifyPw("correct horse battery staple")],
    ],
];
ldap_modify_batch($connection, $dn, $modifs);

    
```php
