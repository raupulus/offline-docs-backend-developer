---
title: ftp_size
description: Devuelve el tamaño de un fichero
source_url: https://www.php.net/manual/es/function.ftp-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24680
---

ftp_size

Devuelve el tamaño de un fichero

## Descripción

```php
ftp_size(FTP\Connection $ftp, string $filename): int
```php

`ftp_size` devuelve el tamaño de un fichero dado en bytes.

> [!NOTE]
> No todos los servidores soportan esta funcionalidad.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`filename`  
El fichero remoto.

## Valores devueltos

Devuelve el tamaño del fichero en caso de éxito, o -1 si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_size`

```
<?php

$file = 'somefile.txt';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Obtención del tamaño del fichero $file
$res = ftp_size($ftp, $file);

if ($res != -1) {
    echo "El tamaño del fichero $file es de $res bytes";
} else {
    echo "No ha sido posible obtener el tamaño del fichero";
}

// Cierre de la conexión
ftp_close($ftp);

?>

    
```php

## Véase también

`ftp_rawlist`
