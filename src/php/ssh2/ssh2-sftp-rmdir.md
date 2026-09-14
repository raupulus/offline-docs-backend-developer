---
title: ssh2_sftp_rmdir
description: Elimina un directorio
source_url: https://www.php.net/manual/es/function.ssh2-sftp-rmdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-rmdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86690
---

ssh2_sftp_rmdir

Elimina un directorio

## Descripción

```php
ssh2_sftp_rmdir(resource $sftp, string $dirname): bool
```php

Elimina un directorio del sistema de ficheros remoto.

Esta función es similar al uso de la función `rmdir` con el gestor [ssh2.sftp://](#wrappers.ssh2).

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto por la función `ssh2_sftp`.

`dirname`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Eliminación de un directorio en un servidor remoto

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');
$sftp = ssh2_sftp($connection);

ssh2_sftp_rmdir($sftp, '/home/username/deltodel');
/* O :  rmdir("ssh2.sftp://$sftp/home/username/dirtodel"); */
?>

   
```php

## Véase también

rmdir

ssh2_sftp_mkdir
