---
title: ftp_connect
description: Establece una conexión FTP
source_url: https://www.php.net/manual/es/function.ftp-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: 4d1c34c9b
order: 24410
---

ftp_connect

Establece una conexión FTP

## Descripción

```php
ftp_connect(string $hostname, [int $port], [int $timeout]): FTP\Connection
```php

`ftp_connect` establece una conexión FTP con el host `hostname`.

## Parámetros

`hostname`  
La dirección del servidor FTP. Este argumento nunca debe terminar con una barra y no debe estar prefijado con `ftp://`.

`port`  
Este argumento especifica un número de puerto alternativo para la conexión. Si se omite o se define como cero, se utilizará el puerto FTP por defecto, 21.

`timeout`  
Este argumento especifica el tiempo de espera de conexión en segundos para todas las operaciones de red posteriores. Si se omite, el valor por defecto será de 90 segundos. El tiempo de espera de conexión puede modificarse y consultarse en cualquier momento con las funciones `ftp_set_option` y `ftp_get_option`.

## Valores devueltos

Devuelve una instancia de `FTP\Connection` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `FTP\Connection`; anteriormente se devolvía un `resource`. |

## Ejemplos

Ejemplo con `ftp_connect`

```
<?php

$ftp_server = "ftp.example.com";

// Establecimiento de una conexión
$ftp = ftp_connect($ftp_server) or die("No se puede conectar al servidor $ftp_server");

?>

    
```php

## Véase también

`ftp_close`, `ftp_ssl_connect`
