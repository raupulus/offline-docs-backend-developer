---
title: Iterator::valid
description: Comprueba si la posición actual es válido
source_url: https://www.php.net/manual/es/iterator.valid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/iterator/valid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 460f49a93
order: 3770
---

Iterator::valid

Comprueba si la posición actual es válido

## Descripción

```php
public Iterator::valid(): bool
```php

Este método se llama después de Iterator::rewind y Iterator::next para comprobar si la posición actual es válido.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor de retorno se debe fundir a `bool` y luego evaluar. Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
