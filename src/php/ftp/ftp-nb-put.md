---
title: ftp_nb_put
description: Envía un fichero a un servidor FTP (no bloqueante)
source_url: https://www.php.net/manual/es/function.ftp-nb-put.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-nb-put.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: 4d1c34c9b
order: 24560
---

ftp_nb_put

Envía un fichero a un servidor FTP (no bloqueante)

## Descripción

```php
ftp_nb_put(FTP\Connection $ftp, string $remote_filename, string $local_filename, [int $mode], [int $offset]): int
```php

`ftp_nb_put` escribe el fichero `remote_filename` presente en la máquina local, en el servidor FTP `ftp`.

La diferencia entre esta función y `ftp_put` es que esta función puede leer el fichero de manera asíncrona, de modo que el programa pueda realizar otras tareas mientras el fichero se está descargando.

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
La posición en el fichero remoto desde la cual comenzará la descarga.

## Valores devueltos

Devuelve `FTP_FAILED`, `FTP_FINISHED` o `FTP_MOREDATA`, o `false` en caso de fallo al abrir el fichero local.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.3.0 | El argumento `mode` ahora es opcional. Anteriormente era obligatorio. |

## Ejemplos

Ejemplo con `ftp_nb_put`

```
<?php

// Inicialización de la carga
$ret = ftp_nb_put($ftp, "test.remote", "test.local", FTP_BINARY);
while ($ret == FTP_MOREDATA) {

   // Realice lo que desee...
   echo ".";

   // Continúa la carga...
   $ret = ftp_nb_continue($ftp);
}
if ($ret != FTP_FINISHED) {
   echo "Ocurrió un problema durante la carga del fichero...";
   exit(1);
}
?>

    
```php

Reanudación de una carga con `ftp_nb_put`

```
<?php

// Inicialización
$ret = ftp_nb_put($ftp, "test.remote", "test.local",
                      FTP_BINARY, ftp_size("test.remote"));
// O: $ret = ftp_nb_put($ftp, "test.remote", "test.local",
//                           FTP_BINARY, FTP_AUTORESUME);

while ($ret == FTP_MOREDATA) {

   // Realice lo que desee...
   echo ".";

   // Continúa la carga...
   $ret = ftp_nb_continue($ftp);
}
if ($ret != FTP_FINISHED) {
   echo "Ocurrió un problema durante la carga...";
   exit(1);
}
?>

    
```php

## Véase también

`ftp_nb_fput`, `ftp_nb_continue`, `ftp_put`, `ftp_fput`
