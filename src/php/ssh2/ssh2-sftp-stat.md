---
title: ssh2_sftp_stat
description: Obtiene el estado de un fichero en un sistema de ficheros remoto
source_url: https://www.php.net/manual/es/function.ssh2-sftp-stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: cad275c0c
order: 86700
---

ssh2_sftp_stat

Obtiene el estado de un fichero en un sistema de ficheros remoto

## Descripción

```php
ssh2_sftp_stat(resource $sftp, string $path): array
```php

Obtiene el estado de un fichero en un sistema de ficheros remoto, siguiendo los enlaces simbólicos.

Esta función es similar al uso de la función `stat` con el gestor [ssh2.sftp://](#wrappers.ssh2) y devuelve los mismos valores.

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto por la función `ssh2_sftp`.

`path`  

## Valores devueltos

Devuelve un array de estadísticas del fichero dado en caso de éxito o `false` si ocurre un error. Ver la documentación de la función `stat` para los detalles sobre los valores devueltos.

## Ejemplos

Estado de un fichero vía SFTP

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');

$sftp = ssh2_sftp($connection);
$statinfo = ssh2_sftp_stat($sftp, '/path/to/file');

$filesize = $statinfo['size'];
$group = $statinfo['gid'];
$owner = $statinfo['uid'];
$atime = $statinfo['atime'];
$mtime = $statinfo['mtime'];
$mode = $statinfo['mode'];
?>

   
```php

## Véase también

ssh2_sftp_lstat

lstat

stat
