---
title: ftp_delete
description: Elimina un fichero en un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24420
---

ftp_delete

Elimina un fichero en un servidor FTP

## Descripción

```php
ftp_delete(FTP\Connection $ftp, string $filename): bool
```php

`ftp_delete` elimina el fichero `filename` en un servidor FTP.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`filename`  
El fichero a eliminar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_delete`

```
<?php
$file = 'public_html/old.txt';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Intento de eliminar el fichero $file
if (ftp_delete($ftp, $file)) {
 echo "$file eliminado con éxito\n";
} else {
 echo "No se pudo eliminar el fichero $file\n";
}

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php
