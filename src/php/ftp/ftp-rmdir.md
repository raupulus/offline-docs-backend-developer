---
title: ftp_rmdir
description: Elimina un directorio FTP
source_url: https://www.php.net/manual/es/function.ftp-rmdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-rmdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24650
---

ftp_rmdir

Elimina un directorio FTP

## Descripción

```php
ftp_rmdir(FTP\Connection $ftp, string $directory): bool
```php

`ftp_rmdir` elimina el directorio `directory`.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`directory`  
El directorio a eliminar. Debe ser una ruta absoluta o una ruta relativa hacia un directorio vacío.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_rmdir`

```
<?php

$dir = 'www/';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Intento de eliminación del directorio $dir
if (ftp_rmdir($ftp, $dir)) {
    echo "El directorio $dir ha sido eliminado con éxito\n";
} else {
    echo "Hubo un problema al eliminar el directorio $dir\n";
}

ftp_close($ftp);

?>

    
```php

## Véase también

`ftp_mkdir`
