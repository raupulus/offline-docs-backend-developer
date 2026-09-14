---
title: Transliterator::create
description: Crea un Transliterator
source_url: https://www.php.net/manual/es/transliterator.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/transliterator/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 42540
---

Transliterator::create

transliterator_create

Crea un Transliterator

## Descripción

Estilo orientado a objetos

```php
public static Transliterator::create(string $id, [int $direction]): Transliterator
```php

Estilo procedimental

```php
transliterator_create(string $id, [int $direction]): Transliterator
```

Abre un Transliterator por su identificador.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`id`  
El identificador. Una lista de todos los identificadores transliterator registrados puede ser encontrada utilizando el método Transliterator::listIDs.

`direction`  
La dirección, por omisión [Transliterator::FORWARD](#transliterator.constants.forward). Puede ser igualmente definido como [Transliterator::REVERSE](#transliterator.constants.reverse).

## Valores devueltos

Devuelve un objeto `Transliterator` en caso de éxito, o `null` si ocurre un error.

## Véase también

Transliterator::getErrorMessage, Transliterator::\_\_construct
