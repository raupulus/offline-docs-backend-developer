---
title: ssh2_scp_recv
description: Solicita un fichero mediante SCP
source_url: https://www.php.net/manual/es/function.ssh2-scp-recv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-scp-recv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86600
---

ssh2_scp_recv

Solicita un fichero mediante SCP

## Descripción

```php
ssh2_scp_recv(resource $session, string $remote_file, string $local_file): bool
```php

Copia un fichero desde el servidor remoto al sistema de ficheros local usando el protocolo SCP.

## Parámetros

`session`  
Un identificador de enlace de conexión a SSH, obtenido desde una llamada a `ssh2_connect`.

`remote_file`  
Ruta del fichero remoto.

`local_file`  
Ruta del fichero local.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Descargar un fichero mediante SCP

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');

ssh2_scp_recv($connection, '/remote/filename', '/local/filename');
?>

   
```php

## Véase también

ssh2_scp_send

copy
