---
title: SplFixedArray::current
description: Devuelve la entrada del array actual
source_url: https://www.php.net/manual/es/splfixedarray.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84670
---

SplFixedArray::current

Devuelve la entrada del array actual

## Descripción

```php
public SplFixedArray::current(): mixed
```php

Obtiene la entrada del elemento array actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor del elemento actual.

## Errores/Excepciones

Lanza una excepción de tipo `RuntimeException` cuando el puntero interno del array apunta a un índice no válido o está fuera de los límites.
