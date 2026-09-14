---
title: ssh2_sftp_unlink
description: Borra un fichero
source_url: https://www.php.net/manual/es/function.ssh2-sftp-unlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-unlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86720
---

ssh2_sftp_unlink

Borra un fichero

## Descripción

```php
ssh2_sftp_unlink(resource $sftp, string $filename): bool
```php

Borra un fichero en el sistema de ficheros remoto.

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto por la función `ssh2_sftp`.

`filename`  
El nombre del fichero a borrar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Borrado de un fichero

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');
$sftp = ssh2_sftp($connection);

ssh2_sftp_unlink($sftp, '/home/username/stale_file');
?>

   
```php

## Véase también

unlink
