---
title: ftp_site
description: Ejecuta el comando SITE en un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-site.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-site.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24670
---

ftp_site

Ejecuta el comando SITE en un servidor FTP

## Descripción

```php
ftp_site(FTP\Connection $ftp, string $command): bool
```php

`ftp_site` ejecuta el comando `SITE` en el servidor FTP.

Los comandos `SITE` no están normalizados, y pueden variar de un servidor a otro. Permiten gestionar, entre otras cosas, los permisos de ficheros y los grupos.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`command`  
El comando SITE. Tenga en cuenta que este argumento no se escapa, por lo que pueden producirse comportamientos no deseados si el nombre de los ficheros contiene espacios u otros caracteres.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Envío de un comando SITE a un servidor FTP

```
<?php
// Conexión al servidor FTP
$ftp = ftp_connect('ftp.example.com');
if (!$ftp) die('Imposible conectarse al servidor ftp.example.com');

// Identificación con el usuario "user" y la contraseña "pass"
if (!ftp_login($ftp, 'user', 'pass')) die('Error de identificación en el servidor ftp.example.com');

// Resultado: comando "SITE CHMOD 0600 /home/user/privatefile" en el servidor ftp
if (ftp_site($ftp, 'CHMOD 0600 /home/user/privatefile')) {
   echo "El comando se ha ejecutado correctamente.\n";
} else {
   die('El comando ha fallado.');
}
?>

    
```php

## Véase también

`ftp_raw`
