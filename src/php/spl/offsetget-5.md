---
title: SplFixedArray::offsetGet
description: Devuelve el valor en el índice específicado
source_url: https://www.php.net/manual/es/splfixedarray.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/offsetget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84750
---

SplFixedArray::offsetGet

Devuelve el valor en el índice específicado

## Descripción

```php
public SplFixedArray::offsetGet(int $index): mixed
```php

Devuelve el valor en el índice `index` específicado.

## Parámetros

`index`  
El índice con el valor.

## Valores devueltos

El valor específicado en `index`.

## Errores/Excepciones

Lanza una excepción de tipo `RuntimeException` cuando `index` está fuera del tamaño definido del array o cuando `index` no se puede procesar como un entero.
