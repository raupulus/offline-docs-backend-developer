---
title: ssh2_sftp_realpath
description: Resuelve la ruta real de una ruta proporcionada
source_url: https://www.php.net/manual/es/function.ssh2-sftp-realpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-realpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: cad275c0c
order: 86670
---

ssh2_sftp_realpath

Resuelve la ruta real de una ruta proporcionada

## Descripción

```php
ssh2_sftp_realpath(resource $sftp, string $filename): string
```php

Traduce un nombre de fichero `filename` en su ruta realmente efectiva en el sistema de ficheros remoto.

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto por la función `ssh2_sftp`.

`filename`  

## Valores devueltos

Devuelve la ruta real, en forma de `string` o `false` si ocurre un error.

## Ejemplos

Resolver un nombre de ruta

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');
$sftp = ssh2_sftp($connection);

$realpath = ssh2_sftp_realpath($sftp, '/home/username/../../../..//./usr/../etc/passwd');
/* $realpath es ahora: '/etc/passwd' */
?>

   
```php

## Véase también

realpath

ssh2_sftp_symlink

ssh2_sftp_readlink
