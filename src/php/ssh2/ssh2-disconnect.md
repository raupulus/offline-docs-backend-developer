---
title: ssh2_disconnect
description: Cierra una conexión a un servidor SSH remoto
source_url: https://www.php.net/manual/es/function.ssh2-disconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-disconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86480
---

ssh2_disconnect

Cierra una conexión a un servidor SSH remoto

## Descripción

```php
ssh2_disconnect(resource $session): bool
```php

Cierra una conexión a un servidor SSH remoto.

## Parámetros

`session`  
Un identificador de enlace de conexión SSH, obtenido desde una llamada a `ssh2_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ssh2_connect
