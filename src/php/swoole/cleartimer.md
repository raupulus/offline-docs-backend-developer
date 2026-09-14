---
title: Swoole\Server::clearTimer
description: Destruye y detiene un temporizador.
source_url: https://www.php.net/manual/es/swoole-server.cleartimer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/server/cleartimer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 9f63af6fd
order: 92550
---

Swoole\Server::clearTimer

swoole_timer_clear

Destruye y detiene un temporizador.

## Descripción

Estilo orientado a objetos (method):

```php
public Swoole\Server::clearTimer(int $timer_id): void
```php

Estilo procedimental:

```php
swoole_timer_clear(int $timer_id): void
```

Detiene y destruye un temporizador.

## Parámetros

`timer_id`  

## Valores devueltos
