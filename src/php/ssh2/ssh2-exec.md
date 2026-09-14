---
title: ssh2_exec
description: Ejecuta un comando en un servidor remoto
source_url: https://www.php.net/manual/es/function.ssh2-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86490
---

ssh2_exec

Ejecuta un comando en un servidor remoto

## Descripción

```php
ssh2_exec(resource $session, string $command, [string $pty], [array $env], [int $width], [int $height], [int $width_height_type]): resource
```php

Ejecuta un comando en un servidor remoto.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde la función `ssh2_connect`.

`command`  

`pty`  

`env`  
`env` puede ser pasado bajo la forma de un array asociativo de pares nombre/valor, a definir en el entorno objetivo.

`width`  
Ancho del terminal virtual.

`height`  
Altura del terminal virtual.

`width_height_type`  
`width_height_type` puede valer `SSH2_TERM_UNIT_CHARS` o `SSH2_TERM_UNIT_PIXELS`.

## Valores devueltos

Devuelve un flujo en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejecución de un comando

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');

$stream = ssh2_exec($connection, '/usr/local/bin/php -i');
?>

   
```php

## Véase también

ssh2_connect

ssh2_shell

ssh2_tunnel
