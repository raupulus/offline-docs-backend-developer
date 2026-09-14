---
title: ftp_nb_get
description: Lee un fichero en un servidor FTP y lo escribe en un fichero (no bloqueante)
source_url: https://www.php.net/manual/es/function.ftp-nb-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-nb-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: ce3f60dc2
order: 24550
---

ftp_nb_get

Lee un fichero en un servidor FTP y lo escribe en un fichero (no bloqueante)

## Descripción

```php
ftp_nb_get(FTP\Connection $ftp, string $local_filename, string $remote_filename, [int $mode], [int $offset]): int
```php

`ftp_nb_get` lee el fichero `remote_filename` presente en el servidor FTP `ftp` y lo guarda en un fichero local.

La diferencia entre esta función y `ftp_fget` es que esta función puede leer el fichero de manera asíncrona, para que el programa realice otras tareas mientras el fichero se descarga.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`local_filename`  
La ruta hacia el fichero local (será sobrescrito si el fichero ya existe).

`remote_filename`  
La ruta hacia el fichero remoto.

`mode`  
El modo de transferencia. Debe ser `FTP_ASCII` o `FTP_BINARY`.

`offset`  
La posición en el fichero remoto a partir de la cual debe comenzar la descarga.

## Valores devueltos

Devuelve `FTP_FAILED` o `FTP_FINISHED` o `FTP_MOREDATA`, o `false` en caso de fallo al abrir el fichero local.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.3.0 | El argumento `mode` ahora es opcional. Anteriormente era obligatorio. |

## Ejemplos

Ejemplo con `ftp_nb_get`

```
<?php

// Inicia la descarga
$ret = ftp_nb_get($ftp, "test", "README", FTP_BINARY);
while ($ret == FTP_MOREDATA) {

   // Realice lo que desee...
   echo ".";

   // Continúa la descarga...
   $ret = ftp_nb_continue($ftp);
}
if ($ret != FTP_FINISHED) {
   echo "Hubo un problema durante la descarga...";
   exit(1);
}
?>

    
```php

Reanudación de una descarga con `ftp_nb_get`

```
<?php

// Inicializa
$ret = ftp_nb_get($ftp, "test", "README", FTP_BINARY,
                      filesize("test"));
// O: $ret = ftp_nb_get($ftp, "test", "README",
//                           FTP_BINARY, FTP_AUTORESUME);
while ($ret == FTP_MOREDATA) {

   // Realice lo que desee...
   echo ".";

   // Continúa la descarga...
   $ret = ftp_nb_continue($ftp);
}
if ($ret != FTP_FINISHED) {
   echo "Hubo un problema durante la descarga del fichero...";
   exit(1);
}
?>

    
```php

Reanudación de una descarga desde la posición 100 en un nuevo fichero con `ftp_nb_get`

```
<?php

// Desactiva AutoSeek
ftp_set_option($ftp, FTP_AUTOSEEK, false);

// Inicialización
$ret = ftp_nb_get($ftp, "newfile", "README", FTP_BINARY, 100);
while ($ret == FTP_MOREDATA) {

   /* ... */

   // Continúa la descarga...
   $ret = ftp_nb_continue($ftp);
}
?>

    
```php

En el ejemplo anterior, `newfile` es 100 bytes más pequeño que `README` en el sitio FTP, ya que comenzamos a leer desde el offset 100. Si no hubiéramos desactivado la opción `FTP_AUTOSEEK`, los primeros 100 bytes del fichero `newfile` serían rellenados con `'\0'`.

## Véase también

`ftp_nb_fget`, `ftp_nb_continue`, `ftp_fget`, `ftp_get`
