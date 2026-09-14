---
title: gmp_clrbit
description: Anula un byte
source_url: https://www.php.net/manual/es/function.gmp-clrbit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-clrbit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: f38aa0ef2
order: 28390
---

gmp_clrbit

Anula un byte

## Descripción

```php
gmp_clrbit(GMP $num, int $index): void
```php

Establece a 0 el byte `index` en el número GMP `num`. El índice comienza en cero.

## Parámetros

`num`  
Un objeto `GMP`

`index`  
El índice del byte a anular. El índice 0 representa el último byte significativo.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `gmp_clrbit`

```
<?php
$a = gmp_init("0xff");
gmp_clrbit($a, 0); // el índice comienza en cero
echo gmp_strval($a) . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    254

## Notas

> [!NOTE]
> A diferencia de la mayoría de las otras funciones GMP, `gmp_clrbit` debe ser llamada con un objeto GMP ya existente (usando `gmp_init` por ejemplo). No será creada automáticamente.

## Véase también

`gmp_setbit`, `gmp_testbit`
