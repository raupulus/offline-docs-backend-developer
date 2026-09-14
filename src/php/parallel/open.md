---
title: parallel\Channel::open
description: Acceso
source_url: https://www.php.net/manual/es/parallel-channel.open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/channel/open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60000
---

parallel\Channel::open

Acceso

## Descripción

```php
public parallel\Channel::open(string $name): Channel
```php

Abre el canal con el nombre dado.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Channel\Error\Existence` si el canal no existe.
