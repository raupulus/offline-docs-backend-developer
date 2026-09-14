---
title: ssh2_forward_listen
description: Enlaza un puerto en el servidor remoto y observa las conexiones
source_url: https://www.php.net/manual/es/function.ssh2-forward-listen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-forward-listen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86530
---

ssh2_forward_listen

Enlaza un puerto en el servidor remoto y observa las conexiones

## Descripción

```php
ssh2_forward_listen(resource $session, int $port, [string $host], [int $max_connections]): resource
```php

Enlaza un puerto en el servidor remoto y observa las conexiones.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`session`  
Un recurso de sesión SSH, obtenido mediante una llamada a `ssh2_connect`.

`port`  
Un puerto del servidor remoto.

`host`  

`max_connections`  

## Valores devueltos

Devuelve un observador SSH2, o `false` si ocurre un error.

## Véase también

ssh2_forward_accept
