---
title: ssh2_fetch_stream
description: Recorre un flujo extendido de datos
source_url: https://www.php.net/manual/es/function.ssh2-fetch-stream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-fetch-stream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86500
---

ssh2_fetch_stream

Recorre un flujo extendido de datos

## Descripción

```php
ssh2_fetch_stream(resource $channel, int $streamid): resource
```php

Recorre un subflujo alternativo asociado a un flujo de canal SSH2. El protocolo SSH2 define actualmente un solo subflujo, STDERR, que tiene un identificador de subflujo de `SSH2_STREAM_STDERR` (definido a 1).

## Parámetros

`channel`  

`streamid`  
Un canal de flujo SSH2.

## Valores devueltos

Devuelve el recurso, representando el flujo solicitado.

## Ejemplos

Apertura de un shell y recuperación del flujo stderr que le está asociado

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');

$stdio_stream = ssh2_shell($connection);
$stderr_stream = ssh2_fetch_stream($stdio_stream, SSH2_STREAM_STDERR);
?>

   
```php

## Véase también

ssh2_shell

ssh2_exec

ssh2_connect
