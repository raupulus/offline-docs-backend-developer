---
title: gmp_div_q
description: Divide los números
source_url: https://www.php.net/manual/es/function.gmp-div-q.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-div-q.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 039ab719e
order: 28420
---

gmp_div_q

Divide los números

## Descripción

```php
gmp_div_q(GMP $num1, GMP $num2, [int $rounding_mode]): GMP
```php

Divide `num1` con `num2` y devuelve el entero resultante.

## Parámetros

`num1`  
El número que sera dividido.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`num2`  
El número que `num1` esta siendo dividido.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

`rounding_mode`  
El redondeo resultante es definido por el `rounding_mode`, el cual puede tener uno de los siguientes valores:

- `GMP_ROUND_ZERO`: El resultante es truncado hacia 0.

- `GMP_ROUND_PLUSINF`:El resultado es redondeado hacia `+infinity`.

- `GMP_ROUND_MINUSINF`: El resultado es redondeado hacia `-infinity`.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un objeto `GMP`.

## Ejemplos

Ejemplo de `gmp_div_q`

```
<?php
$div1 = gmp_div_q("100", "5");
echo gmp_strval($div1) . "\n";

$div2 = gmp_div_q("1", "3");
echo gmp_strval($div2) . "\n";

$div3 = gmp_div_q("1", "3", GMP_ROUND_PLUSINF);
echo gmp_strval($div3) . "\n";

$div4 = gmp_div_q("-1", "4", GMP_ROUND_PLUSINF);
echo gmp_strval($div4) . "\n";

$div5 = gmp_div_q("-1", "4", GMP_ROUND_MINUSINF);
echo gmp_strval($div5) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    20
    0
    1
    0
    -1

## Notas

> [!NOTE]
> Esta función también puede ser llamada como `gmp_div`.

## Véase también

`gmp_div_r`, `gmp_div_qr`
