---
title: ssh2_sftp_chmod
description: Modifica el modo de un fichero
source_url: https://www.php.net/manual/es/function.ssh2-sftp-chmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp-chmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86630
---

ssh2_sftp_chmod

Modifica el modo de un fichero

## Descripción

```php
ssh2_sftp_chmod(resource $sftp, string $filename, int $mode): bool
```php

Intenta modificar el modo del fichero especificado, utilizando el `mode` proporcionado.

## Parámetros

`sftp`  
Un recurso SSH2 SFTP, abierto con la función `ssh2_sftp`.

`filename`  
Ruta hacia el fichero.

`mode`  
Permisos sobre el fichero. Ver la función `chmod` para más detalles concernientes a este parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Cambio del modo del fichero en el servidor remoto

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'nombreUsuario', 'contraseña');
$sftp = ssh2_sftp($connection);

ssh2_sftp_chmod($sftp, '/carpeta/fichero', 0755);
?>

   
```php

## Véase también

chmod

ssh2_sftp

ssh2_connect
