---
title: ldap_errno
description: Devuelve el número de error LDAP de la última orden ejecutada
source_url: https://www.php.net/manual/es/function.ldap-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: fbc6f9055
order: 43130
---

ldap_errno

Devuelve el número de error LDAP de la última orden ejecutada

## Descripción

```php
ldap_errno(LDAP\Connection $ldap): int
```php

Devuelve el número de error estándar, generado por la última orden LDAP, para la conexión `link_identifier`. Este número puede ser convertido en mensaje textual con `ldap_err2str`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

## Valores devueltos

Devuelve el número de error LDAP generado por la última orden.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |

## Ejemplos

A menos que se reduzca suficientemente el nivel de error en `php.ini`, o que se prefijen las órdenes LDAP con `@` (arroba) para suprimir los mensajes, los errores LDAP también se mostrarán en la salida HTML.

Generar e interceptar un error

```
<?php
// Este ejemplo contiene un error, que se interceptará.
$ld = ldap_connect("localhost");
$bind = ldap_bind($ld);
// error de sintaxis en la expresión del filtro (errno 87),
// debe ser "objectclass=*" para funcionar.
$res =  @ldap_search($ld, "o=Myorg, c=DE", "objectclass");
if (!$res) {
    echo "LDAP-Errno: " . ldap_errno($ld) . "<br />\n";
    echo "LDAP-Error: " . ldap_error($ld) . "<br />\n";
    die("Argh!<br />\n");
}
$info = ldap_get_entries($ld, $res);
echo $info["count"] . " entradas coinciden.<br />\n";
?>

    
```php

## Véase también

`ldap_err2str`, `ldap_error`
