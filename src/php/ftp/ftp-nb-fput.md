---
title: ftp_nb_fput
description: Escribe un fichero en un servidor FTP, y lo lee desde un fichero (no
  bloqueante)
source_url: https://www.php.net/manual/es/function.ftp-nb-fput.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-nb-fput.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24540
---

ftp_nb_fput

Escribe un fichero en un servidor FTP, y lo lee desde un fichero (no bloqueante)

## Descripción

```php
ftp_nb_fput(FTP\Connection $ftp, string $remote_filename, resource $stream, [int $mode], [int $offset]): int
```php

`ftp_nb_fput` escribe el fichero `remote_filename` presente en la máquina local, en el servidor FTP `ftp`.

La diferencia entre esta función y `ftp_fput` es que esta función puede leer el fichero de manera asíncrona, para que su programa realice otras tareas mientras el fichero se descarga.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`remote_filename`  
La ruta hacia el fichero remoto.

`stream`  
Un puntero de fichero hacia un fichero local. La lectura se detiene al final del fichero.

`mode`  
El modo de transferencia. Debe ser `FTP_ASCII` o `FTP_BINARY`.

`offset`  
La posición en el fichero remoto desde la cual comenzará la descarga.

## Valores devueltos

Devuelve `FTP_FAILED`, `FTP_FINISHED` o `FTP_MOREDATA`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.3.0 | El argumento `mode` ahora es opcional. Anteriormente era obligatorio. |

## Ejemplos

Ejemplo con `ftp_nb_fput`

```
<?php

$file = 'index.php';

$fp = fopen($file, 'r');

$ftp = ftp_connect($ftp_server);

$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Inicia la subida
$ret = ftp_nb_fput($ftp, $file, $fp, FTP_BINARY);
while ($ret == FTP_MOREDATA) {

   // Realice lo que desee...
   echo ".";

   // Continúa la subida...
   $ret = ftp_nb_continue($ftp);
}
if ($ret != FTP_FINISHED) {
   echo "Ocurrió un problema durante la subida del fichero...";
   exit(1);
}

fclose($fp);
?>

    
```php

## Véase también

`ftp_nb_put`, `ftp_nb_continue`, `ftp_put`, `ftp_fput`
