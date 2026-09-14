---
title: ftp_login
description: Autenticación en un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-login.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-login.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 24480
---

ftp_login

Autenticación en un servidor FTP

## Descripción

```php
#[\SensitiveParameter] ftp_login(FTP\Connection $ftp, string $username, string $password): bool
```php

`ftp_login` autentica la conexión FTP en el servidor, con el nombre de usuario `username` y la contraseña `password`.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`username`  
El nombre de usuario (`USER`).

`password`  
La contraseña (`PASS`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si la autenticación falla, PHP lanzará una advertencia.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_login`

```
<?php

$ftp_server = "ftp.example.com";
$ftp_user = "foo";
$ftp_pass = "bar";

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server) or die("No se ha podido conectar a $ftp_server");

// Intento de autenticación
if (@ftp_login($ftp, $ftp_user, $ftp_pass)) {
    echo "Conectado como $ftp_user@$ftp_server\n";
} else {
    echo "Conexión imposible como $ftp_user\n";
}

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php
