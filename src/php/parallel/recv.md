---
title: parallel\Channel::recv
description: Compartir
source_url: https://www.php.net/manual/es/parallel-channel.recv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/channel/recv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60010
---

parallel\Channel::recv

Compartir

## Descripción

```php
public parallel\Channel::recv(): mixed
```php

Recibe un valor de este canal.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Channel\Error\Closed` si el canal está cerrado.
