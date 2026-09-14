---
title: ftp_nb_continue
description: Reanuda la descarga de un fichero (no bloqueante)
source_url: https://www.php.net/manual/es/function.ftp-nb-continue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-nb-continue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24520
---

ftp_nb_continue

Reanuda la descarga de un fichero (no bloqueante)

## Descripción

```php
ftp_nb_continue(FTP\Connection $ftp): int
```php

`ftp_nb_continue` reanuda la descarga de un fichero en la conexión `ftp`, de manera asíncrona.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

## Valores devueltos

Devuelve `FTP_FAILED` o `FTP_FINISHED` o `FTP_MOREDATA`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_nb_continue`

```
<?php

// Inicialización de la descarga
$ret = ftp_nb_get($ftp, "test", "README", FTP_BINARY);
while ($ret == FTP_MOREDATA) {

   // Continúa la descarga...
   $ret = ftp_nb_continue($ftp);
}
if ($ret != FTP_FINISHED) {
   echo "Ha ocurrido un error durante la descarga del fichero...";
   exit(1);
}
?>

    
```php
