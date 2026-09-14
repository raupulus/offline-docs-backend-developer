---
title: Swoole\MySQL::on
description: Registra una retrollamada basada en el nombre del evento.
source_url: https://www.php.net/manual/es/swoole-mysql.on.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/mysql/on.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 322606e4f
order: 92220
---

Swoole\MySQL::on

Registra una retrollamada basada en el nombre del evento.

## Descripción

```php
public Swoole\MySQL::on(string $event_name, callable $callback): void
```php

Registra una retrollamada basada en el nombre del evento, actualmente solo el evento 'close' es soportado.

## Parámetros

`event_name`  

`callback`  

## Valores devueltos
