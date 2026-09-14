---
title: Números de punto flotante
source_url: https://www.php.net/manual/es/language.types.float.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/float.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: e587d0655
order: 4430
---

## Números de punto flotante

Los números de punto flotante (también conocidos como "floats", "doubles" o "números reales") pueden ser especificados utilizando las siguientes sintaxis:

```php
<?php
$a = 1.234;
$b = 1.2e3;
$c = 7E-10;
$d = 1_234.567; // a partir de PHP 7.4.0
?>

  
```

Formalmente a partir de PHP 7.4.0 (anteriormente, los guiones bajos no estaban permitidos):

    LNUM          [0-9]+(_[0-9]+)*
    DNUM          ({LNUM}?"."{LNUM}) | ({LNUM}"."{LNUM}?)
    EXPONENT_DNUM (({LNUM} | {DNUM}) [eE][+-]? {LNUM})

El tamaño de un `float` depende de la plataforma, sin embargo, un número máximo de aproximadamente 1.8e308 con una precisión de 14 dígitos es un valor común (formato de 64 bits IEEE).

> [!WARNING]
> Los números de punto flotante tienen una precisión limitada. Aunque dependen del sistema, PHP utiliza el formato de precisión decimal IEEE 754, que dará un error relativo máximo del orden de 1.11e-16 (debido a los redondeos). Las operaciones aritméticas no elementales pueden dar errores más grandes y, por supuesto, los errores deben ser tenidos en cuenta cuando se realizan múltiples operaciones.
>
> Asimismo, los números racionales exactamente representables como números de punto flotante en base 10, como `0.1` o `0.7`, no tienen una representación exacta como números de punto flotante en base 2, utilizada internamente, y esto independientemente del tamaño de la mantisa. Por lo tanto, no pueden ser convertidos sin una pequeña pérdida de precisión. Esto puede llevar a resultados confusos: por ejemplo, `floor((0.1+0.7)*10)` normalmente devolverá `7` en lugar del `8` esperado, ya que la representación interna será algo como `7.9999999999999991118...`.
>
> Por lo tanto, nunca se debe confiar en los últimos dígitos de un número de punto flotante, y tampoco se debe comparar la igualdad de 2 números de punto flotante directamente. Si se necesita una mayor precisión, las [funciones matemáticas de precisión arbitraria](#ref.bc) y las funciones [gmp](#ref.gmp) están disponibles.
>
> Para una explicación "simple", ver el [guía relativa a los números de punto flotante](http://floating-point-gui.de/).

## Convertir a un número de punto flotante

### Desde cadenas de caracteres

Si una cadena es [numérica](#language.types.numeric-strings) o numérica de cabeza entonces será transformada en su valor de punto flotante correspondiente, de lo contrario será convertida a cero(`0`).

### Desde otros tipos

Para los valores de otros tipos, la conversión se realiza convirtiendo el valor primero en `int` y luego en `float`. Ver [conversión a entero](#language.types.integer.casting) para más información.

> [!NOTE]
> Como algunos tipos tienen un comportamiento indefinido al convertirse en `int`, esto también es el caso al convertirse en `float`.

## Comparación de números de punto flotante

Como se mencionó anteriormente, la prueba de igualdad de valores de números de punto flotante es problemática, debido a la forma en que se representan internamente. Sin embargo, existen formas de realizar esta comparación.

Para probar la igualdad de valores de números de punto flotante, se utiliza un límite superior del error relativo al redondeo. Este valor es conocido como el epsilon de la máquina, o unit roundoff, y es la diferencia más pequeña aceptable en los cálculos.

`$a` y `$b` son iguales en 5 números después de la coma.

Comparación de números de punto flotante

```php
<?php
$a = 1.23456789;
$b = 1.23456780;
$epsilon = 0.00001;

if( abs($a - $b) < $epsilon) {
    echo "true";
}
?>

   
```

## NaN

Algunas operaciones numéricas pueden dar como resultado un valor representado por la constante `NAN`. Este resultado representa un valor indefinido o no representable en cálculos con números de punto flotante. Cualquier comparación, incluso estricta de este valor con otro valor, incluyendo esta constante misma, excepto si es igual a `true`, dará un valor de `false`.

Debido a que `NAN` representa cualquier número de valores diferentes, `NAN` no debe ser comparado con otros valores, incluyendo esta constante misma, y en su lugar, debe ser verificado utilizando la función `is_nan`.
