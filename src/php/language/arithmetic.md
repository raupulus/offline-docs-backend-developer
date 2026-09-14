---
title: Los operadores aritméticos
source_url: https://www.php.net/manual/es/language.operators.arithmetic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/arithmetic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2650
---

## Los operadores aritméticos

¿Recuerda las operaciones elementales aprendidas en la escuela? Los operadores aritméticos funcionan de la misma manera.

| Ejemplo | Nombre | Resultado |
|----|----|----|
| `+$a` | Identidad | Conversión de `$a` a `int` o `float`, según lo más apropiado. |
| `-$a` | Negación | Opuesto de `$a`. |
| `$a + $b` | Adición | Suma de `$a` y `$b`. |
| `$a - $b` | Sustracción | Diferencia de `$a` y `$b`. |
| `$a * $b` | Multiplicación | Producto de `$a` y `$b`. |
| `$a / $b` | División | Cociente de `$a` y `$b`. |
| `$a % $b` | Módulo | Resto de `$a` dividido por `$b`. |
| `$a ** $b` | Exponenciación | Resultado de elevar `$a` a la potencia `$b`. |

Operaciones elementales

El operador de división `/` devuelve un valor `float` a menos que ambos operandos sean de tipo `int` (o [strings numéricos](#language.types.numeric-strings) que se convierten en `int`) y que el numerador sea un múltiplo del divisor, en cuyo caso se devolverá un valor entero. Para la división entera, ver `intdiv`.

Los operandos del módulo se convierten en `int` antes de la ejecución. Para el módulo en números decimales, ver `fmod`.

El resultado de la operación módulo `%` tiene el mismo signo que el primer operando, por lo que el resultado de `$a % $b` tendrá el signo de `$a`. Por ejemplo:

El Operador Módulo

```php
<?php

var_dump(5 % 3);
var_dump(5 % -3);
var_dump(-5 % 3);
var_dump(-5 % -3);

?>

   
```

El ejemplo anterior mostrará:

    int(2)
    int(2)
    int(-2)
    int(-2)

## Véase también

[Las funciones matemáticas](#ref.math)
