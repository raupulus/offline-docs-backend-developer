---
title: SplMinHeap::compare
description: Comparar elementos con el fin de colocarlos correctamente en el montón
  em la parte de arriba
source_url: https://www.php.net/manual/es/splminheap.compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splminheap/compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 85020
---

SplMinHeap::compare

Comparar elementos con el fin de colocarlos correctamente en el montón em la parte de arriba

## Descripción

```php
protected SplMinHeap::compare(mixed $value1, mixed $value2): int
```php

Compara `value1` con `value2`.

## Parámetros

`value1`  
El valor de el primer nodo a ser comparado.

`value2`  
El valor de el segundo nodo a ser comparado.

## Valores devueltos

El resultado de la comparación, un integer positivo si `value1` es menor que `value2`, 0 si son iguales, en caso contrario integer negativo.

> [!NOTE]
> No es recomendable tener múltiples elementos con el mismo valor en el montón. Estos terminarán en una posición arbitraria relativa.
