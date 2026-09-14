---
title: ftp_put
description: Carga un fichero en un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-put.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-put.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: 4d1c34c9b
order: 24590
---

ftp_put

Carga un fichero en un servidor FTP

## Descripción

```php
ftp_put(FTP\Connection $ftp, string $remote_filename, string $local_filename, [int $mode], [int $offset]): bool
```php

`ftp_put` registra el fichero `local_filename` en el servidor FTP.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`remote_filename`  
La ruta hacia el fichero remoto.

`local_filename`  
La ruta hacia el fichero local.

`mode`  
El modo de transferencia. Debe ser `FTP_ASCII` o `FTP_BINARY`.

`offset`  
La posición en el fichero remoto desde la cual comenzará la carga.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.3.0 | El argumento `mode` ahora es opcional. Anteriormente era obligatorio. |

## Ejemplos

Ejemplo con `ftp_put`

```
<?php
$file = 'somefile.txt';
$remote_file = 'readme.txt';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Carga un fichero
if (ftp_put($ftp, $remote_file, $file, FTP_ASCII)) {
 echo "El fichero $file ha sido cargado con éxito\n";
} else {
 echo "Ha ocurrido un problema al cargar el fichero $file\n";
}

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php

## Véase también

`ftp_pasv`, `ftp_fput`, `ftp_nb_fput`, `ftp_nb_put`
