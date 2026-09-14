---
title: ftp_rename
description: Renombra un fichero en un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 6ce59dacb
order: 24640
---

ftp_rename

Renombra un fichero en un servidor FTP

## Descripción

```php
ftp_rename(FTP\Connection $ftp, string $from, string $to): bool
```php

`ftp_rename` renombra el fichero o el directorio `from` a `to`, en el servidor `ftp`.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`from`  
El nombre antiguo del directorio / fichero.

`to`  
El nuevo nombre.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. En caso de fallo (como intentar renombrar un fichero inexistente), se emitirá un error `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_rename`

```
<?php
$old_file = 'somefile.txt.bak';
$new_file = 'somefile.txt';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Intento de renombrar $old_file a $new_file
if (ftp_rename($ftp, $old_file, $new_file)) {
   echo "Renombrado con éxito de $old_file a $new_file\n";
} else {
   echo "Hubo un problema al renombrar $old_file a $new_file\n";
}

// Cierre de la conexión
ftp_close($ftp);

?>

    
```php
