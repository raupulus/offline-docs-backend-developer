---
title: ftp_mkdir
description: Crea un directorio en un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-mkdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-mkdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 181e9c557
order: 24500
---

ftp_mkdir

Crea un directorio en un servidor FTP

## Descripción

```php
ftp_mkdir(FTP\Connection $ftp, string $directory): string
```php

`ftp_mkdir` crea el directorio nombrado `directory` en el servidor FTP.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`directory`  
El nombre del directorio que debe ser creado.

## Valores devueltos

Retorna el nombre del directorio creado en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el directorio ya existe o los permisos correspondientes impiden la creación del directorio.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_mkdir`

```
<?php

$dir = 'www';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Intento de creación del directorio $dir
if (ftp_mkdir($ftp, $dir)) {
 echo "El directorio $dir ha sido creado con éxito\n";
} else {
 echo "Ha ocurrido un problema durante la creación del directorio $dir\n";
}

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php

## Véase también

`ftp_rmdir`
