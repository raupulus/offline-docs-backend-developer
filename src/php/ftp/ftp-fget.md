---
title: ftp_fget
description: Descarga un fichero a través de FTP en un fichero local
source_url: https://www.php.net/manual/es/function.ftp-fget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-fget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: 4d1c34c9b
order: 24440
---

ftp_fget

Descarga un fichero a través de FTP en un fichero local

## Descripción

```php
ftp_fget(FTP\Connection $ftp, resource $stream, string $remote_filename, [int $mode], [int $offset]): bool
```php

`ftp_fget` descarga el fichero `remote_filename` desde el servidor FTP y lo escribe en el fichero identificado por `stream`.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`stream`  
Un puntero de fichero abierto en el que se escriben los datos.

`remote_filename`  
La ruta hacia el fichero remoto.

`mode`  
El modo de transferencia. Debe ser `FTP_ASCII` o `FTP_BINARY`.

`offset`  
La posición del fichero remoto desde la cual comienza la descarga.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.3.0 | El argumento `mode` ahora es opcional. Anteriormente era obligatorio. |

## Ejemplos

Ejemplo con `ftp_fget`

```
<?php

// Ruta hacia el fichero remoto
$remote_file = 'somefile.txt';
$local_file = 'localfile.txt';

// Apertura del fichero para escritura
$handle = fopen($local_file, 'w');

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Intento de descargar el fichero $remote_file y guardarlo en $handle
if (ftp_fget($ftp, $handle, $remote_file, FTP_ASCII, 0)) {
 echo "Escritura en el fichero $local_file con éxito\n";
} else {
 echo "Hay un problema durante la descarga del fichero $remote_file en $local_file\n";
}

// Cierre de la conexión y del puntero de fichero
ftp_close($ftp);
fclose($handle);
?>

    
```php

## Véase también

`ftp_get`, `ftp_nb_get`, `ftp_nb_fget`
