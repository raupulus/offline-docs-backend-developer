---
title: CallbackFilterIterator::accept
description: Llama la llamada de retorno con el valor actual, la clave actual y el
  iterador interior como argumentos
source_url: https://www.php.net/manual/es/callbackfilteriterator.accept.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/callbackfilteriterator/accept.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 81770
---

CallbackFilterIterator::accept

Llama la llamada de retorno con el valor actual, la clave actual y el iterador interior como argumentos

## Descripción

```php
public CallbackFilterIterator::accept(): bool
```php

Este método llama a la llamada de retorno con el valor actual, la clave actual y el iterador interno.

La llamada de retorno se espera que devuelva `true` si el elemento actual es aceptado, o en caso contrario `false`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` para aceptar el elemento actual, o en caso contrario `false`.

## Véase también

[Ejemplos de CallbackFilterIterator](#callbackfilteriterator.examples), CallbackFilterIterator::\_\_construct
