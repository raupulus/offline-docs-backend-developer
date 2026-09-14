---
title: ftp_chmod
description: Modifica los permisos de un fichero mediante FTP
source_url: https://www.php.net/manual/es/function.ftp-chmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-chmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24390
---

ftp_chmod

Modifica los permisos de un fichero mediante FTP

## Descripción

```php
ftp_chmod(FTP\Connection $ftp, int $permissions, string $filename): int
```php

`ftp_chmod` modifica los permisos de acceso al fichero `filename` en el servidor FTP `ftp`, asignándole los permisos de `permissions`, especificado en forma de entero en base octal.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`permissions`  
Los nuevos permisos, dados como valor *octal*.

`filename`  
El fichero remoto.

## Valores devueltos

Devuelve los nuevos permisos del fichero en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_chmod`

```
<?php
$file = 'public_html/index.php';

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Autenticación con nombre de usuario y contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Intento de modificación de los permisos del fichero $file a 644
if (ftp_chmod($ftp, 0644, $file) !== false) {
 echo "Los permisos del fichero $file han sido modificados correctamente a 644\n";
} else {
 echo "No ha sido posible modificar los permisos del fichero $file\n";
}

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php

## Véase también

`chmod`
