---
title: SplHeap::compare
description: Compara elementos con el fin de colocarlos correctamente en el montón
  en la parte de arriba
source_url: https://www.php.net/manual/es/splheap.compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splheap/compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84860
---

SplHeap::compare

Compara elementos con el fin de colocarlos correctamente en el montón en la parte de arriba

## Descripción

```php
protected SplHeap::compare(mixed $value1, mixed $value2): int
```php

Comparar `value1` con `value2`.

> [!WARNING]
> Lanza una excepción en SplHeap::compare que puede dañar el montón y colocarlo en un estado bloqueado. Se puede desbloquear llamando a SplHeap::recoverFromCorruption. Sin embargo, algunos elementos podrían no ser colocados correctamente y por lo tanto pueden romper la propiedad del montón.

## Parámetros

`value1`  
El valor de el primer nodo a ser comparado.

`value2`  
El valor de el segundo nodo a ser comparado.

## Valores devueltos

El resultado de la comparación, integer positivo si `value1` es mayor que `value2`, 0 si son iguales, en caso contrario integer negativo.

> [!NOTE]
> No es recomendado tener múltiples elementos con el mismo valor en el montón. Estos terminarán con una posición arbitraria relativa.
