---
title: bindec
description: Convierte de binario a decimal
source_url: https://www.php.net/manual/es/function.bindec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/bindec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 44560
---

bindec

Convierte de binario a decimal

## Descripción

```php
bindec(string $binary_string): int
```php

Devuelve la conversión de un número binario representado por la cadena `binary_string` a decimal.

`bindec` convierte un número binario en un `int`, o, si es necesario por razones de tamaño, en un `float`.

`bindec` interpreta todos los valores `binary_string` como enteros no firmados. Esto se debe a que la función `bindec` ve el primer bit como otro orden de magnitud en lugar de como el bit de signo.

## Parámetros

`binary_string`  
La cadena binaria a convertir. Cualquier carácter inválido en `binary_string` es ignorado silenciosamente. A partir de PHP 7.4.0, proporcionar caracteres inválidos está deprecado.

> [!WARNING]
> Este parámetro debe ser un `string`. El uso de otro tipo de datos produce resultados inesperados.

## Valores devueltos

El valor decimal de `binary_string`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Proporcionar caracteres inválidos generará ahora una advertencia deprecada. El resultado se calculará siempre como si los caracteres inválidos no existieran. |

## Ejemplos

Ejemplo con `bindec`

```
<?php
echo bindec('110011') . "\n";
echo bindec('000110011') . "\n";

echo bindec('111');
?>

    
```php

El ejemplo anterior mostrará:

    51
    51
    7

`bindec` interpreta la entrada como un entero no firmado

```
<?php
/*
 * Lo más importante en este ejemplo está en la salida
 * más que en el código PHP en sí.
 */

$magnitude_lower = pow(2, (PHP_INT_SIZE * 8) - 2);
p($magnitude_lower - 1);
p($magnitude_lower, '¿Ha visto el cambio? Esté atento la próxima vez...');

p(PHP_INT_MAX, 'PHP_INT_MAX');
p(~PHP_INT_MAX, 'interpretado como superior a PHP_INT_MAX');

if (PHP_INT_SIZE == 4) {
    $note = 'interpretado como el mayor entero no firmado';
} else {
    $note = 'interpretado como el mayor entero no firmado
              (18446744073709551615) pero distorsionado por la precisión de los flotantes';
}
p(-1, $note);

function p($input, $note = '') {
    echo "entrada :        $input\n";

    $format = '%0' . (PHP_INT_SIZE * 8) . 'b';
    $bin = sprintf($format, $input);
    echo "binario :       $bin\n";

    ini_set('precision', 20);  // Para mayor legibilidad en PC de 64 bits.
    $dec = bindec($bin);
    echo 'bindec() :     ' . $dec . "\n";

    if ($note) {
        echo "Nota :         $note\n";
    }

    echo "\n";
}
?>

    
```php

Resultado del ejemplo anterior en una máquina de 32 bits:

    entrada :        1073741823
    binario :       00111111111111111111111111111111
    bindec() :     1073741823

    entrada :        1073741824
    binario :       01000000000000000000000000000000
    bindec():     1073741824
    Nota :         ¿Ha visto el cambio? Esté atento la próxima vez...

    entrada :        2147483647
    binario :       01111111111111111111111111111111
    bindec():     2147483647
    Nota :         PHP_INT_MAX

    entrada :        -2147483648
    binario :       10000000000000000000000000000000
    bindec():     2147483648
    Nota :         interpretado como superior a PHP_INT_MAX

    entrada :        -1
    binario :       11111111111111111111111111111111
    bindec():     4294967295
    Nota :         interpretado como el mayor entero no firmado

        

Resultado del ejemplo anterior en una máquina de 64 bits:

    entrada :        4611686018427387903
    binario :       0011111111111111111111111111111111111111111111111111111111111111
    bindec() :     4611686018427387903

    entrada :        4611686018427387904
    binario :       0100000000000000000000000000000000000000000000000000000000000000
    bindec() :     4611686018427387904
    Nota :         ¿Ha visto el cambio? Esté atento la próxima vez...

    entrada :        9223372036854775807
    binario :       0111111111111111111111111111111111111111111111111111111111111111
    bindec() :     9223372036854775807
    Nota :         PHP_INT_MAX

    entrada :        -9223372036854775808
    binario :       1000000000000000000000000000000000000000000000000000000000000000
    bindec() :     9223372036854775808
    Nota :         interpretado como superior a PHP_INT_MAX

    entrada :        -1
    binario :       1111111111111111111111111111111111111111111111111111111111111111
    bindec() :     18446744073709551616
    Nota :         interpretado como el mayor entero no firmado
                  (18446744073709551615) pero distorsionado por la precisión de los flotantes

## Notas

> [!NOTE]
> La función puede convertir números que son demasiado grandes para caber en un tipo `int`, en cuyo caso estos valores se devuelven como `float`.

## Véase también

`decbin`, `octdec`, `hexdec`, `base_convert`
