---
title: ftp_pwd
description: Devuelve el nombre del directorio actual
source_url: https://www.php.net/manual/es/function.ftp-pwd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-pwd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24600
---

ftp_pwd

Devuelve el nombre del directorio actual

## Descripción

```php
ftp_pwd(FTP\Connection $ftp): string
```php

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

## Valores devueltos

Devuelve el nombre del directorio actual o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_pwd`

```
<?php

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Cambia el directorio a public_html
ftp_chdir($ftp, 'public_html');

// Muestra el directorio actual
echo ftp_pwd($ftp); // /public_html

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php

## Véase también

`ftp_chdir`, `ftp_cdup`
