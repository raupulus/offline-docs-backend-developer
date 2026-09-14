---
title: ssh2_sftp_rename
description: Renombra un fichero remoto
source_url: https://www.php.net/manual/es/function.ssh2-sftp-rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86680
---

ssh2_sftp_rename

Renombra un fichero remoto

## Descripción

```php
ssh2_sftp_rename(resource $sftp, string $from, string $to): bool
```php

Renombra un fichero remoto.

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto por la función `ssh2_sftp`.

`from`  
El fichero actual a renombrar.

`to`  
El nuevo nombre del fichero.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Renombrar un fichero vía sftp

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');
$sftp = ssh2_sftp($connection);

ssh2_sftp_rename($sftp, '/home/username/oldname', '/home/username/newname');
?>

   
```php

## Véase también

rename
