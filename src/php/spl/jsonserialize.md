---
title: SplFixedArray::jsonSerialize
description: Devuelve una representación que puede ser convertida a JSON
source_url: https://www.php.net/manual/es/splfixedarray.jsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray/jsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d715365c0
order: 84710
---

SplFixedArray::jsonSerialize

Devuelve una representación que puede ser convertida a JSON

## Descripción

```php
public SplFixedArray::jsonSerialize(): array
```php

Serializa el array en un valor que puede ser serializado de forma nativa por `json_encode`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de datos que puede ser serializado por `json_encode`, que es un valor de cualquier tipo excepto una `resource`.
