---
title: ssh2_scp_send
description: Envía un fichero mediante SCP
source_url: https://www.php.net/manual/es/function.ssh2-scp-send.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-scp-send.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86610
---

ssh2_scp_send

Envía un fichero mediante SCP

## Descripción

```php
ssh2_scp_send(resource $session, string $local_file, string $remote_file, [int $create_mode]): bool
```php

Copia un fichero desde el sistema de ficheros local a un servidor remoto usando el protocolo SCP.

## Parámetros

`session`  
Un identificador de enlace de conexión a SSH, obtenido desde una llamada a `ssh2_connect`.

`local_file`  
Ruta del fichero local.

`remote_file`  
Ruta del fichero remoto.

`create_mode`  
El fichero debe ser creado con el modo especificado por `create_mode`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Cargar un fichero via SCP

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');

ssh2_scp_send($connection, '/local/filename', '/remote/filename', 0644);
?>

   
```php

## Véase también

ssh2_scp_recv

copy
