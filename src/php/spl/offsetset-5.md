---
title: SplFixedArray::offsetSet
description: Establece un nuevo valor para el índice específicado
source_url: https://www.php.net/manual/es/splfixedarray.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/offsetset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84760
---

SplFixedArray::offsetSet

Establece un nuevo valor para el índice específicado

## Descripción

```php
public SplFixedArray::offsetSet(int $index, mixed $value): void
```php

Establece el valor en el `index` específicado en `value`.

## Parámetros

`index`  
El índice a ser establecido.

`value`  
El nuevo valor para `index`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción de tipo `RuntimeException` cuando `index` está fuera del tamaño definido del array o cuando `index` no se puede procesar como un entero.
