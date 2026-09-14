---
title: ftp_fput
description: Carga un fichero en un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-fput.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-fput.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: 4d1c34c9b
order: 24450
---

ftp_fput

Carga un fichero en un servidor FTP

## Descripción

```php
ftp_fput(FTP\Connection $ftp, string $remote_filename, resource $stream, [int $mode], [int $offset]): bool
```php

`ftp_fput` carga los datos del fichero identificado por `stream` hasta el final del fichero.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`remote_filename`  
La ruta hacia el fichero remoto.

`stream`  
Un puntero de fichero abierto sobre el fichero local. La lectura se detiene al final del fichero.

`mode`  
El modo de transferencia. Debe ser `FTP_ASCII` o `FTP_BINARY`.

`offset`  
La posición en el fichero remoto a partir de la cual comenzará la carga.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.3.0 | El argumento `mode` es ahora opcional. Anteriormente era obligatorio. |

## Ejemplos

Ejemplo con `ftp_fput`

```
<?php

// Apertura de algunos ficheros para lectura
$file = 'somefile.txt';
$fp = fopen($file, 'r');

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Intento de cargar el fichero $file
if (ftp_fput($ftp, $file, $fp, FTP_ASCII)) {
    echo "Carga exitosa del fichero $file\n";
} else {
    echo "Hubo un problema durante la carga del fichero $file\n";
}

// Cierre de la conexión y del puntero de fichero
ftp_close($ftp);
fclose($fp);

?>

    
```php

## Véase también

`ftp_put`, `ftp_nb_fput`, `ftp_nb_put`
