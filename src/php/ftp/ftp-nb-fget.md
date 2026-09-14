---
title: ftp_nb_fget
description: Lee un fichero en un servidor FTP y lo escribe en un fichero (no bloqueante)
source_url: https://www.php.net/manual/es/function.ftp-nb-fget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-nb-fget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: 21840cc59
order: 24530
---

ftp_nb_fget

Lee un fichero en un servidor FTP y lo escribe en un fichero (no bloqueante)

## Descripción

```php
ftp_nb_fget(FTP\Connection $ftp, resource $stream, string $remote_filename, [int $mode], [int $offset]): int
```php

`ftp_nb_fget` lee el fichero `remote_filename` presente en el servidor FTP `ftp`.

La diferencia entre esta función y `ftp_fget` es que esta función puede leer el fichero de manera asíncrona, de modo que su programa pueda realizar otras tareas mientras el fichero se descarga.

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
La posición en el fichero remoto desde la cual debe comenzar la descarga.

## Valores devueltos

Devuelve `FTP_FAILED` o `FTP_FINISHED` o `FTP_MOREDATA`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.3.0 | El argumento `mode` ahora es opcional. Anteriormente era obligatorio. |

## Ejemplos

Ejemplo con `ftp_nb_fget`

```
<?php

// Apertura de algunos ficheros para escritura
$file = 'index.php';
$fp = fopen($file, 'w');

$ftp = ftp_connect($ftp_server);

$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Inicia la descarga
$ret = ftp_nb_fget($ftp, $fp, $file, FTP_BINARY);
while ($ret == FTP_MOREDATA) {

   // Realice lo que desee...
   echo ".";

   // Continúa la descarga...
   $ret = ftp_nb_continue($ftp);
}
if ($ret != FTP_FINISHED) {
   echo "Ocurrió un error durante la descarga del fichero...";
   exit(1);
}

// Cierra el puntero de fichero
fclose($fp);
?>

    
```php

## Véase también

`ftp_nb_get`, `ftp_nb_continue`, `ftp_fget`, `ftp_get`
