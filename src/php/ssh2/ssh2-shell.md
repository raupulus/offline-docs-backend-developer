---
title: ssh2_shell
description: Solicita un shell interactivo
source_url: https://www.php.net/manual/es/function.ssh2-shell.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-shell.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86740
---

ssh2_shell

Solicita un shell interactivo

## Descripción

```php
ssh2_shell(resource $session, [string $termtype], [array $env], [int $width], [int $height], [int $width_height_type]): resource
```php

Abre un shell en el servidor remoto y le asigna un flujo.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde la función `ssh2_connect`.

`termtype`  
`termtype` debe corresponder a una de las entradas del fichero `/etc/termcap` del sistema objetivo.

`env`  
`env` debe ser pasado como un array asociativo de pares nombre/valor a definir en el entorno objetivo.

`width`  
Ancho del terminal virtual.

`height`  
Altura del terminal virtual.

`width_height_type`  
`width_height_type` debe ser o bien `SSH2_TERM_UNIT_CHARS`, o bien `SSH2_TERM_UNIT_PIXELS`.

## Valores devueltos

Devuelve un flujo de `resource` en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejecución de un comando

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
ssh2_auth_password($connection, 'username', 'password');

$stream = ssh2_shell($connection, 'vt102', null, 80, 24, SSH2_TERM_UNIT_CHARS);
?>

   
```php

## Véase también

ssh2_exec

ssh2_tunnel

ssh2_fetch_stream
