---
title: ftp_mdtm
description: Devuelve la fecha de última modificación de un fichero en un servidor
  FTP
source_url: https://www.php.net/manual/es/function.ftp-mdtm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-mdtm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24490
---

ftp_mdtm

Devuelve la fecha de última modificación de un fichero en un servidor FTP

## Descripción

```php
ftp_mdtm(FTP\Connection $ftp, string $filename): int
```php

`ftp_mdtm` lee la fecha de última modificación de un fichero remoto.

> [!NOTE]
> No todos los servidores soportan esta funcionalidad.

> [!NOTE]
> `ftp_mdtm` no funciona con directorios.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`filename`  
El fichero desde el cual se debe extraer la fecha de última modificación.

## Valores devueltos

Devuelve la fecha de última modificación como un timestamp *locale* Unix en caso de éxito, o -1 si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_mdtm`

```
<?php

$file = 'somefile.txt';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

//  Obtención de la fecha de última modificación
$buff = ftp_mdtm($ftp, $file);

if ($buff != -1) {
    // somefile.txt fue modificado por última vez el: March 26 2003 14:16:41.
    echo "$file fue modificado por última vez: " . date("F d Y H:i:s.", $buff);
} else {
    echo "No se pudo obtener mdtime";
}

// Cierre de la conexión
ftp_close($ftp);

?>

    
```php
