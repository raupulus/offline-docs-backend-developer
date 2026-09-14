---
title: gmp_setbit
description: Modifica un bit
source_url: https://www.php.net/manual/es/function.gmp-setbit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-setbit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: f38aa0ef2
order: 28790
---

gmp_setbit

Modifica un bit

## Descripción

```php
gmp_setbit(GMP $num, int $index, [bool $value]): void
```php

Modifica el bit `index` en `num`.

## Parámetros

`num`  
Un objeto `GMP`

`index`  
El índice del byte a definir. El índice 0 representa el byte menos significativo.

`value`  
`true` para definir el byte (definido a 1/on); `false` para reinicializarlo (definido a 0/off).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `gmp_setbit` - índice 0

```
<?php
$a = gmp_init("2"); //
echo gmp_strval($a), ' -> 0b', gmp_strval($a, 2), "\n";
gmp_setbit($a, 0); // 0b10 ahora es 0b11
echo gmp_strval($a), ' -> 0b', gmp_strval($a, 2), "\n";
?>

    
```php

El ejemplo anterior mostrará:

    2 -> 0b10
    3 -> 0b11

Ejemplo con `gmp_setbit` - índice 1

```
<?php
$a = gmp_init("0xfd");
echo gmp_strval($a), ' -> 0b', gmp_strval($a, 2), "\n";
gmp_setbit($a, 1); // el índice comienza en 0
echo gmp_strval($a), ' -> 0b', gmp_strval($a, 2), "\n";
?>

    
```php

El ejemplo anterior mostrará:

    253 -> 0b11111101
    255 -> 0b11111111

Ejemplo con `gmp_setbit` - borra un byte

```
<?php
$a = gmp_init("0xff");
echo gmp_strval($a), ' -> 0b', gmp_strval($a, 2), "\n";
gmp_setbit($a, 0, false); // limpia el bit en el índice 0
echo gmp_strval($a), ' -> 0b', gmp_strval($a, 2), "\n";
?>

    
```php

El ejemplo anterior mostrará:

    255 -> 0b11111111
    254 -> 0b11111110

## Notas

> [!NOTE]
> A diferencia de la mayoría de las otras funciones GMP, `gmp_setbit` debe ser llamada con un objeto GMP ya existente (utilizando `gmp_init` por ejemplo). No será creada automáticamente.

## Véase también

`gmp_clrbit`, `gmp_testbit`
