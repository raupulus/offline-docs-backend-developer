---
title: ssh2_sftp
description: Inicializa un subsistema SFTP
source_url: https://www.php.net/manual/es/function.ssh2-sftp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-sftp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: true
translation_revision: 12f0e7220
order: 86730
---

ssh2_sftp

Inicializa un subsistema SFTP

## Descripción

```php
ssh2_sftp(resource $session): resource
```php

Solicita un subsistema SFTP desde un servidor ya conectado mediante SSH2.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde la función `ssh2_connect`.

## Valores devueltos

Este método devuelve un recurso `SSH2 SFTP` para su uso con todos los métodos `ssh2_sftp_*()` así como el gestor abierto [ssh2.sftp://](#wrappers.ssh2), o `false` si ocurre un error.

## Ejemplos

Apertura de un fichero mediante SFTP

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');

$sftp = ssh2_sftp($connection);

$stream = fopen('ssh2.sftp://' . intval($sftp) . '/path/to/file', 'r');
?>

   
```php

## Véase también

ssh2_scp_recv

ssh2_scp_send
