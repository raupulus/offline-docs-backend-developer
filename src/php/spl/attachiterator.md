---
title: MultipleIterator::attachIterator
description: Adjunta un iterador
source_url: https://www.php.net/manual/es/multipleiterator.attachiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/multipleiterator/attachiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82620
---

MultipleIterator::attachIterator

Adjunta un iterador

## Descripción

```php
public MultipleIterator::attachIterator(Iterator $iterator, [string $info]): void
```php

Adjunta un iterador.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`iterator`  
El nuevo iterador a adjuntar.

`info`  
Las informaciones del iterador, que deben ser un `int`, un `string` o `null`.

## Valores devueltos

## Errores/Excepciones

Se lanza una excepción `IllegalValueException` si el argumento `iterator` es inválido, o si `info` es una información ya asociada.

## Véase también

MultipleIterator::\_\_construct
