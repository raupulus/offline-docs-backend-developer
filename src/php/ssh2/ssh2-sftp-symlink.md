---
title: ssh2_sftp_symlink
description: Crea un enlace simbólico
source_url: https://www.php.net/manual/es/function.ssh2-sftp-symlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-symlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86710
---

ssh2_sftp_symlink

Crea un enlace simbólico

## Descripción

```php
ssh2_sftp_symlink(resource $sftp, string $target, string $link): bool
```php

Crea un enlace simbólico en el sistema de ficheros remoto.

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto por la función `ssh2_sftp`.

`target`  
Objetivo del enlace simbólico.

`link`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Creación de un enlace simbólico

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');
$sftp = ssh2_sftp($connection);

ssh2_sftp_symlink($sftp, '/var/run/mysql.sock', '/tmp/mysql.sock');
?>

   
```php

## Véase también

ssh2_sftp_readlink

symlink
