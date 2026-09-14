---
title: ssh2_sftp_readlink
description: Devuelve el destino de un enlace simbólico
source_url: https://www.php.net/manual/es/function.ssh2-sftp-readlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-readlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: cad275c0c
order: 86660
---

ssh2_sftp_readlink

Devuelve el destino de un enlace simbólico

## Descripción

```php
ssh2_sftp_readlink(resource $sftp, string $link): string
```php

Devuelve el destino de un enlace simbólico.

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto por la función `ssh2_sftp`.

`link`  
Ruta hacia el enlace simbólico.

## Valores devueltos

Devuelve el destino del enlace simbólico `link` o `false` si ocurre un error.

## Ejemplos

Lectura de un enlace simbólico

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');
$sftp = ssh2_sftp($connection);

$target = ssh2_sftp_readlink($sftp, '/tmp/mysql.sock');
/* $target es ahora (e.g.): '/var/run/mysql.sock' */
?>

   
```php

## Véase también

readlink

ssh2_sftp_symlink
