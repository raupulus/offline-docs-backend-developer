---
title: ftp_pasv
description: Activa o desactiva el modo pasivo
source_url: https://www.php.net/manual/es/function.ftp-pasv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-pasv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24580
---

ftp_pasv

Activa o desactiva el modo pasivo

## Descripción

```php
ftp_pasv(FTP\Connection $ftp, bool $enable): bool
```php

`ftp_pasv` activa o desactiva el modo pasivo. En modo pasivo, las conexiones de datos son iniciadas por el cliente, en lugar del servidor. Este modo puede ser necesario cuando el cliente está detrás de un firewall.

Tenga en cuenta que `ftp_pasv` solo puede ser llamada después de una identificación exitosa, de lo contrario, la función fallará.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`enable`  
Si `true`, el modo pasivo es activado, de lo contrario, es desactivado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_pasv`

```
<?php
$file = 'somefile.txt';
$remote_file = 'readme.txt';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Activación del modo pasivo
ftp_pasv($ftp, true);

// Carga de un fichero
if (ftp_put($ftp, $remote_file, $file, FTP_ASCII)) {
 echo "El fichero $file ha sido cargado con éxito\n";
} else {
 echo "Ha habido un problema al cargar el fichero $file\n";
}

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php
