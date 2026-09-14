---
title: parallel\Channel::make
description: Acceso
source_url: https://www.php.net/manual/es/parallel-channel.make.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/channel/make.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 59990
---

parallel\Channel::make

Acceso

## Descripción

```php
public parallel\Channel::make(string $name): Channel
```php

Crear un canal no tamponado con el nombre dado.

```php
public parallel\Channel::make(string $name, int $capacity): Channel
```

Crear un canal tamponado con el nombre y la capacidad dados.

## Parámetros

`name`  
El nombre del canal.

`capacity`  
Puede ser `Channel::Infinite` o un entero positivo.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Channel\Error\Existence` si el canal ya existe.
