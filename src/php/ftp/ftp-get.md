---
title: ftp_get
description: Descarga un fichero desde un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: 4d1c34c9b
order: 24470
---

ftp_get

Descarga un fichero desde un servidor FTP

## Descripción

```php
ftp_get(FTP\Connection $ftp, string $local_filename, string $remote_filename, [int $mode], [int $offset]): bool
```php

`ftp_get` descarga el fichero `remote_filename` desde el servidor FTP, y lo guarda en el fichero local `local_filename`.

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
La posición en el fichero remoto desde la cual comienza la descarga.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |
| 7.3.0 | El argumento `mode` ahora es opcional. Anteriormente era obligatorio. |

## Ejemplos

Ejemplo con `ftp_get`

```
<?php

// Definición de algunas variables
$local_file = 'local.zip';
$server_file = 'server.zip';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Intento de descargar el fichero $server_file y guardarlo en el fichero $local_file
if (ftp_get($ftp, $local_file, $server_file, FTP_BINARY)) {
    echo "El fichero $local_file ha sido escrito con éxito\n";
} else {
    echo "Hay un problema\n";
}

// Cierre de la conexión
ftp_close($ftp);

?>

    
```php

## Véase también

`ftp_pasv`, `ftp_fget`, `ftp_nb_get`, `ftp_nb_fget`
