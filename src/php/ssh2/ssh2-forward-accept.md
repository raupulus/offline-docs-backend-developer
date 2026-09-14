---
title: ssh2_forward_accept
description: Acepta una conexión creada por un observador
source_url: https://www.php.net/manual/es/function.ssh2-forward-accept.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-forward-accept.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86520
---

ssh2_forward_accept

Acepta una conexión creada por un observador

## Descripción

```php
ssh2_forward_accept(resource $listener): resource
```php

Acepta una conexión creada por un observador.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`desc`  
Un observador SSH2, obtenido por una llamada a `ssh2_forward_listen`.

## Valores devueltos

Devuelve un recurso de flujo, o `false` si ocurre un error.
