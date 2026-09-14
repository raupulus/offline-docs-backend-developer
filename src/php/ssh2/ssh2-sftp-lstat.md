---
title: ssh2_sftp_lstat
description: Estado de un enlace simbólico
source_url: https://www.php.net/manual/es/function.ssh2-sftp-lstat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-lstat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: cad275c0c
order: 86640
---

ssh2_sftp_lstat

Estado de un enlace simbólico

## Descripción

```php
ssh2_sftp_lstat(resource $sftp, string $path): array
```php

Estado de un enlace simbólico en el sistema de ficheros remoto *sin* seguir el enlace.

Esta función es similar a la utilización de la función `lstat` con el gestor [ssh2.sftp://](#wrappers.ssh2) y devuelve los mismos valores.

## Parámetros

`sftp`  
Un recurso SSH2 SFTP abierto por `ssh2_sftp`.

`path`  
Ruta hacia el enlace simbólico remoto.

## Valores devueltos

Devuelve un array de estadísticas del enlace simbólico dado en caso de éxito o `false` si ocurre un error. Ver la documentación de la función `stat` para los detalles concernientes a los valores devueltos.

## Ejemplos

Estado de un enlace simbólico vía SFTP

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');

$sftp = ssh2_sftp($connection);
$statinfo = ssh2_sftp_lstat($sftp, '/path/to/symlink');

$filesize = $statinfo['size'];
$group = $statinfo['gid'];
$owner = $statinfo['uid'];
$atime = $statinfo['atime'];
$mtime = $statinfo['mtime'];
$mode = $statinfo['mode'];
?>

   
```php

## Véase también

ssh2_sftp_stat

lstat

stat
