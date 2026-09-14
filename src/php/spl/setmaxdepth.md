---
title: RecursiveIteratorIterator::setMaxDepth
description: Define la profundidad máxima
source_url: https://www.php.net/manual/es/recursiveiteratoriterator.setmaxdepth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursiveiteratoriterator/setmaxdepth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83380
---

RecursiveIteratorIterator::setMaxDepth

Define la profundidad máxima

## Descripción

```php
public RecursiveIteratorIterator::setMaxDepth([int $maxDepth]): void
```php

Define la profundidad máxima permitida.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`maxDepth`  
La profundidad máxima permitida. `-1` será utilizado para una profundidad infinita.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Emite una `Exception` si `maxDepth` es inferior a `-1`.
