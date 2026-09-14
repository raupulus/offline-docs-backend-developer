---
title: parallel\Channel::__construct
description: Construcción de canal
source_url: https://www.php.net/manual/es/parallel-channel.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/channel/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 59980
---

parallel\Channel::\_\_construct

Construcción de canal

## Descripción

```php
public parallel\Channel::__construct()
```php

Crear un canal anónimo no tamponado.

```php
public parallel\Channel::__construct(int $capacity)
```

Crear un canal anónimo tamponado con la capacidad dada.

## Parámetros

`capacity`  
Puede ser `Channel::Infinite` o un integer positivo
