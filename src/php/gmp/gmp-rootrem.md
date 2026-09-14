---
title: gmp_rootrem
description: Tomar la parte entera y el resto de una raíz enésima
source_url: https://www.php.net/manual/es/function.gmp-rootrem.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-rootrem.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: 039ab719e
order: 28760
---

gmp_rootrem

Tomar la parte entera y el resto de una raíz enésima

## Descripción

```php
gmp_rootrem(GMP $num, int $nth): array
```php

Toma la raíz enésima dada por `nth` de `num` y devuelve el componente entero y el resto del resultado.

## Parámetros

`num`  
Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`nth`  
La raíz positiva a tomar de `num`.

## Valores devueltos

Un array de dos elementos, donde el primero es el componente entero de la raíz, y el segundo es el resto, ambos representados como números GMP.
