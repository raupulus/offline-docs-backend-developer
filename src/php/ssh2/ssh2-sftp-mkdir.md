---
title: ssh2_sftp_mkdir
description: Crea un directorio
source_url: https://www.php.net/manual/es/function.ssh2-sftp-mkdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-mkdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86650
---

ssh2_sftp_mkdir

Crea un directorio

## Descripción

```php
ssh2_sftp_mkdir(resource $sftp, string $dirname, [int $mode], [bool $recursive]): bool
```php

Crea un directorio en el sistema de ficheros remoto.

Esta función es similar a la función `mkdir` con el gestor [ssh2.sftp://](#wrappers.ssh2).

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto con la función `ssh2_sftp`.

`dirname`  
Ruta del nuevo directorio.

`mode`  
Permisos del nuevo directorio. El modo actual es afectado por la umask actual.

`recursive`  
Si `recursive` vale `true`, todos los directorios requeridos para `dirname` serán también automáticamente creados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Creación de un directorio en un servidor remoto

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');
$sftp = ssh2_sftp($connection);

ssh2_sftp_mkdir($sftp, '/home/username/newdir');
/* O:  mkdir("ssh2.sftp://$sftp/home/username/newdir"); */
?>

   
```php

## Véase también

mkdir

ssh2_sftp_rmdir
