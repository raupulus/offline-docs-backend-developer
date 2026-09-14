---
title: Modificaciones en la gestión de int
source_url: https://www.php.net/manual/es/migration70.incompatible.integers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/incompatible/integers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 86e6094e8
order: 310
---

## Modificaciones en la gestión de `int`

### Literales octales no válidos

Anteriormente, los literales octales que contenían números no válidos se truncaban silenciosamente (`0128` se interpretaba como `012`). Ahora, un literal octal no válido provocará un error de análisis.

### Desplazamiento de bits negativo

Los desplazamientos de bits por números negativos ahora lanzarán una `ArithmeticError`:

```php
<?php
var_dump(1 >> -1);
?>

   
```

Resultado del ejemplo anterior en PHP 5:

    int(0)

        

Resultado del ejemplo anterior en PHP 7:

    Fatal error: Uncaught ArithmeticError: Bit shift by negative number in /tmp/test.php:2
    Stack trace:
    #0 {main}
      thrown in /tmp/test.php on line 2

### Desplazamiento de bits fuera de rango

Los desplazamientos de bits (en ambos sentidos) más allá del ancho de bits de un `int` siempre devolverán 0. Anteriormente, el comportamiento de estos desplazamientos dependía de la arquitectura.

### Cambios en la división por cero

Anteriormente, cuando se utilizaba 0 como divisor en los operadores de división (/) o módulo (%), se emitía un E_WARNING y se devolvía `false`. Ahora, el operador de división devuelve un float como +INF, -INF o NAN, según lo especificado por IEEE 754. La advertencia E_WARNING del operador de módulo se ha eliminado y ahora lanzará una excepción `DivisionByZeroError`.

```php
<?php
var_dump(3/0);
var_dump(0/0);
var_dump(0%0);
?>

   
```

Resultado del ejemplo anterior en PHP 5:

    Warning: Division by zero in %s on line %d
    bool(false)

    Warning: Division by zero in %s on line %d
    bool(false)

    Warning: Division by zero in %s on line %d
    bool(false)

       

Resultado del ejemplo anterior en PHP 7:

    Warning: Division by zero in %s on line %d
    float(INF)

    Warning: Division by zero in %s on line %d
    float(NAN)

    PHP Fatal error:  Uncaught DivisionByZeroError: Modulo by zero in %s line %d
