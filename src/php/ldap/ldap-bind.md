---
title: ldap_bind
description: Autenticación en el servidor LDAP
source_url: https://www.php.net/manual/es/function.ldap-bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 5bc68add3
order: 43000
---

ldap_bind

Autenticación en el servidor LDAP

## Descripción

```php
#[\SensitiveParameter] ldap_bind(LDAP\Connection $ldap, [string $dn], [string $password]): bool
```php

Autenticación en el servidor LDAP con el RDN y la contraseña especificados.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  

`password`  

Si `password` no está especificado o está vacío, se intenta una autenticación anónima. `dn` también puede dejarse vacío para una conexión anónima. Esto está definido en https://tools.ietf.org/html/rfc2251#section-4.2.2

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |

## Ejemplos

Autenticación con LDAP

```
<?php

// Elementos de autenticación LDAP
$ldaprdn  = 'uname';     // DN o RDN LDAP
$ldappass = 'password';  // Contraseña asociada

// Conexión al servidor LDAP
$ldapconn = ldap_connect("ldap://ldap.example.com")
    or die("No es posible conectarse al servidor LDAP.");

if ($ldapconn) {

    // Conexión al servidor LDAP
    $ldapbind = ldap_bind($ldapconn, $ldaprdn, $ldappass);

    // Verificación de la autenticación
    if ($ldapbind) {
        echo "Conexión LDAP exitosa...";
    } else {
        echo "Conexión LDAP fallida...";
    }

}

?>

    
```php

Conexión anónima a un servidor LDAP

```
<?php

// Conexión anónima a un servidor LDAP

// Conexión al servidor LDAP
$ldapconn = ldap_connect("ldap://ldap.example.com")
    or die("No es posible conectarse al servidor LDAP.");

if ($ldapconn) {

    // Autenticación anónima
    $ldapbind = ldap_bind($ldapconn);

    if ($ldapbind) {
        echo "Conexión LDAP anónima exitosa...";
    } else {
        echo "Conexión LDAP anónima fallida...";
    }

}

?>

    
```php

## Véase también

`ldap_bind_ext`, `ldap_unbind`
