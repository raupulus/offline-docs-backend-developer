---
title: Operadores a nivel de bits
source_url: https://www.php.net/manual/es/language.operators.bitwise.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/bitwise.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2680
---

## Operadores a nivel de bits

Los operadores a nivel de bits permiten manipular los bits en un entero.

| Ejemplo | Nombre | Resultado |
|----|----|----|
| `$a & $b` | And (Y) | Los bits posicionados a 1 en `$a` Y en `$b` son posicionados a 1. |
| `$a | $b` | Or (O) | Los bits posicionados a 1 en `$a` O `$b` son posicionados a 1. |
| `$a ^ $b` | Xor (o exclusivo) | Los bits posicionados a 1 en `$a` O en `$b` pero no en los dos son posicionados a 1. |
| `~ $a` | Not (No) | Los bits que están posicionados a 1 en `$a` son posicionados a 0, y viceversa. |
| `$a << $b` | Desplazamiento a la izquierda | Desplaza los bits de `$a`, `$b` veces a la izquierda (cada desplazamiento equivale a una multiplicación por 2). |
| `$a >> $b` | Desplazamiento a la derecha | Desplaza los bits de `$a`, `$b` veces a la derecha (cada desplazamiento equivale a una división por 2). |

Los operadores a nivel de bits

El desplazamiento de bits en PHP es aritmético. Los bits que son desplazados fuera del entero se pierden. Los desplazamientos a la izquierda hacen aparecer ceros a la derecha, mientras que el bit de signo es desplazado a la izquierda, lo que significa que el signo del entero no es preservado. Los desplazamientos a la derecha desplazan también el bit de signo a la derecha, lo que significa que el signo es preservado.

Utilícense paréntesis para asegurarse de que la [precedencia](#language.operators.precedence) deseada sea aplicada correctamente. Por ejemplo, `$a & $b == true` aplica primero la igualdad, y luego el AND lógico, mientras que `($a & $b) == true` aplica primero el AND lógico, y luego la igualdad.

Si los dos operandos para los operadores `&`, `|` y `^` son strings, entonces la operación será realizada sobre los valores ASCII de los caracteres y el resultado será un string. En todos los otros casos, los dos operandos serán [convertidos en entero](#language.types.integer.casting) y el resultado será un entero.

Si el operando para el operador `~` es un string, la operación será realizada sobre los caracteres ASCII que componen el string y el resultado será un string. De lo contrario, el operando y el resultado serán tratados como enteros.

Los operandos y el resultado de los operadores `<<` y `>>` son tratados como enteros.

El informe de errores de PHP utiliza campos de bits, que son una ilustración de la extinción de bits. Para mostrar los errores, excepto las notificaciones, las instrucciones del php.ini son : `E_ALL & ~E_NOTICE`

\
     Esto se comprende comparando con E_ALL :\
     `00000000000000000111011111111111`\
     Luego, apagando el valor de E_NOTICE...\
     `00000000000000000000000000001000`\
     ... y invirtiéndolo a través de `~`:\
     `11111111111111111111111111110111`\
     Finalmente, se utiliza el AND lógico (&) para leer los bits activados\
     en las dos valores :\
     `00000000000000000111011111110111`\

Otro medio de llegar a este resultado es utilizar el OU exclusivo (`^`), que busca los bits que están activados solo en una de las dos valores, exclusivamente : `E_ALL ^ E_NOTICE`

error_reporting también puede ser utilizado para ilustrar la activación de bits. Para mostrar únicamente los errores y los errores recuperables, se utiliza : `E_ERROR | E_RECOVERABLE_ERROR`

\
     Este enfoque combina E_ERROR\
     `00000000000000000000000000000001`\
     y E_RECOVERABLE_ERROR\
     `00000000000000000001000000000000`\
     Con el operador OR (`|`) para asegurarse de\
     que los bits están activados en una de las dos valores :\
     `00000000000000000001000000000001`\

Operaciones sobre bits y enteros

```php
<?php
/*
 * Ignórese esta parte,
 * es solo formato para clarificar los resultados
 */

$format = '(%1$2d = %1$04b) = (%2$2d = %2$04b)'
        . ' %3$s (%4$2d = %4$04b)' . "\n";

echo <<<EOH
 ---------     ---------  -- ---------
 resultado       valor        prueba
 ---------     ---------  -- ---------
EOH;

/*
 * Aquí están los ejemplos
 */

$values = array(0, 1, 2, 4, 8);
$test = 1 + 4;

echo "\n AND a nivel de bits \n";
foreach ($values as $value) {
    $result = $value & $test;
    printf($format, $result, $value, '&', $test);
}

echo "\n OR inclusivo a nivel de bits \n";
foreach ($values as $value) {
    $result = $value | $test;
    printf($format, $result, $value, '|', $test);
}

echo "\n OR exclusivo a nivel de bits (XOR) \n";
foreach ($values as $value) {
    $result = $value ^ $test;
    printf($format, $result, $value, '^', $test);
}
?>

   
```

El ejemplo anterior mostrará:

    ---------     ---------  -- ---------
     resultado       valor        prueba
     ---------     ---------  -- ---------
     AND a nivel de bits
    ( 0 = 0000) = ( 0 = 0000) & ( 5 = 0101)
    ( 1 = 0001) = ( 1 = 0001) & ( 5 = 0101)
    ( 0 = 0000) = ( 2 = 0010) & ( 5 = 0101)
    ( 4 = 0100) = ( 4 = 0100) & ( 5 = 0101)
    ( 0 = 0000) = ( 8 = 1000) & ( 5 = 0101)

     OR inclusivo a nivel de bits
    ( 5 = 0101) = ( 0 = 0000) | ( 5 = 0101)
    ( 5 = 0101) = ( 1 = 0001) | ( 5 = 0101)
    ( 7 = 0111) = ( 2 = 0010) | ( 5 = 0101)
    ( 5 = 0101) = ( 4 = 0100) | ( 5 = 0101)
    (13 = 1101) = ( 8 = 1000) | ( 5 = 0101)

     OR exclusivo a nivel de bits (XOR)
    ( 5 = 0101) = ( 0 = 0000) ^ ( 5 = 0101)
    ( 4 = 0100) = ( 1 = 0001) ^ ( 5 = 0101)
    ( 7 = 0111) = ( 2 = 0010) ^ ( 5 = 0101)
    ( 1 = 0001) = ( 4 = 0100) ^ ( 5 = 0101)
    (13 = 1101) = ( 8 = 1000) ^ ( 5 = 0101)

Operación sobre bits y strings

```php
<?php
echo 12 ^ 9, PHP_EOL; // Muestra '5'

echo "12" ^ "9", PHP_EOL; // Muestra el carácter de borrado (ascii 8)
                 // ('1' (ascii 49)) ^ ('9' (ascii 57)) = #8

echo "hallo" ^ "hello", PHP_EOL; // Muestra los valores ASCII #0 #4 #0 #0 #0
                        // 'a' ^ 'e' = #4

echo 2 ^ "3", PHP_EOL; // Muestra 1
              // 2 ^ ((int) "3") == 1

echo "2" ^ 3, PHP_EOL; // Muestra 1
              // ((int) "2") ^ 3 == 1
?>

   
```

Desplazamiento de bits sobre enteros

```php
<?php
/*
 * Aquí están algunos ejemplos
 */

echo "\n--- Desplazamientos a la derecha sobre enteros positivos ---\n";

$val = 4;
$places = 1;
$res = $val >> $places;
p($res, $val, '>>', $places, 'copia del bit de signo ahora a la izquierda');

$val = 4;
$places = 2;
$res = $val >> $places;
p($res, $val, '>>', $places);

$val = 4;
$places = 3;
$res = $val >> $places;
p($res, $val, '>>', $places, 'bits salieron por la derecha');

$val = 4;
$places = 4;
$res = $val >> $places;
p($res, $val, '>>', $places, 'mismo resultado que arriba: no hay desplazamiento más allá de 0');

echo "\n--- Desplazamientos a la derecha sobre enteros negativos ---\n";

$val = -4;
$places = 1;
$res = $val >> $places;
p($res, $val, '>>', $places, 'copia del bit de signo ahora a la izquierda');

$val = -4;
$places = 2;
$res = $val >> $places;
p($res, $val, '>>', $places, 'bits salieron por la derecha');

$val = -4;
$places = 3;
$res = $val >> $places;
p($res, $val, '>>', $places, 'mismo resultado que arriba: no hay desplazamiento más allá de -1');

echo "\n--- Desplazamientos a la izquierda sobre enteros positivos ---\n";

$val = 4;
$places = 1;
$res = $val << $places;
p($res, $val, '<<', $places, 'complemento de ceros a la derecha');

$val = 4;
$places = (PHP_INT_SIZE * 8) - 4;
$res = $val << $places;
p($res, $val, '<<', $places);

$val = 4;
$places = (PHP_INT_SIZE * 8) - 3;
$res = $val << $places;
p($res, $val, '<<', $places, 'el bit de signo salió');

$val = 4;
$places = (PHP_INT_SIZE * 8) - 2;
$res = $val << $places;
p($res, $val, '<<', $places, 'bits salieron a la izquierda');

echo "\n--- Desplazamientos a la izquierda sobre enteros negativos ---\n";

$val = -4;
$places = 1;
$res = $val << $places;
p($res, $val, '<<', $places, 'complemento de ceros a la derecha');

$val = -4;
$places = (PHP_INT_SIZE * 8) - 3;
$res = $val << $places;
p($res, $val, '<<', $places);

$val = -4;
$places = (PHP_INT_SIZE * 8) - 2;
$res = $val << $places;
p($res, $val, '<<', $places, 'bits salieron a la izquierda, incluyendo el bit de signo');

/*
 * Ignórese esta sección
 * Contiene código para el formato de este ejemplo
 */

function p($res, $val, $op, $places, $note = '') {
    $format = '%0' . (PHP_INT_SIZE * 8) . "b\n";

    printf("Expresión : %d = %d %s %d\n", $res, $val, $op, $places);

    echo " Decimal :\n";
    printf("  val=%d\n", $val);
    printf("  res=%d\n", $res);

    echo " Binario :\n";
    printf('  val=' . $format, $val);
    printf('  res=' . $format, $res);

    if ($note) {
        echo " Nota : $note\n";
    }

    echo "\n\n";
}
?>

   
```

Resultado del ejemplo anterior en una máquina de 32 bits:

    --- Desplazamientos a la derecha sobre enteros positivos ---
    Expresión : 2 = 4 >> 1
     Decimal :
      val=4
      res=2
     Binario :
      val=00000000000000000000000000000100
      res=00000000000000000000000000000010
     Nota : copia del bit de signo ahora a la izquierda

    Expresión : 1 = 4 >> 2
     Decimal :
      val=4
      res=1
     Binario :
      val=00000000000000000000000000000100
      res=00000000000000000000000000000001

    Expresión : 0 = 4 >> 3
     Decimal :
      val=4
      res=0
     Binario :
      val=00000000000000000000000000000100
      res=00000000000000000000000000000000
     Nota : bits salieron por la derecha

    Expresión : 0 = 4 >> 4
     Decimal :
      val=4
      res=0
     Binario :
      val=00000000000000000000000000000100
      res=00000000000000000000000000000000
     Nota : mismo resultado que arriba: no hay desplazamiento más allá de 0

    --- Desplazamientos a la derecha sobre enteros negativos ---
    Expresión : -2 = -4 >> 1
     Decimal :
      val=-4
      res=-2
     Binario :
      val=11111111111111111111111111111100
      res=11111111111111111111111111111110
     Nota : copia del bit de signo a la izquierda

    Expresión : -1 = -4 >> 2
     Decimal :
      val=-4
      res=-1
     Binario :
      val=11111111111111111111111111111100
      res=11111111111111111111111111111111
     Nota : bits salieron por la derecha

    Expresión : -1 = -4 >> 3
     Decimal :
      val=-4
      res=-1
     Binario :
      val=11111111111111111111111111111100
      res=11111111111111111111111111111111
     Nota : mismo resultado que arriba: no hay desplazamiento más allá de -1

    --- Desplazamientos a la izquierda sobre enteros positivos ---
    Expresión : 8 = 4 << 1
     Decimal :
      val=4
      res=8
     Binario :
      val=00000000000000000000000000000100
      res=00000000000000000000000000001000
     Nota : complemento de ceros a la derecha

    Expresión : 1073741824 = 4 << 28
     Decimal :
      val=4
      res=1073741824
     Binario :
      val=00000000000000000000000000000100
      res=01000000000000000000000000000000

    Expresión : -2147483648 = 4 << 29
     Decimal :
      val=4
      res=-2147483648
     Binario :
      val=00000000000000000000000000000100
      res=10000000000000000000000000000000
     Nota : el bit de signo salió

    Expresión : 0 = 4 << 30
     Decimal :
      val=4
      res=0
     Binario :
      val=00000000000000000000000000000100
      res=00000000000000000000000000000000
     Nota : bits salieron a la izquierda

    --- Desplazamientos a la izquierda sobre enteros negativos ---
    Expresión : -8 = -4 << 1
     Decimal :
      val=-4
      res=-8
     Binario :
      val=11111111111111111111111111111100
      res=11111111111111111111111111111000
     Nota : complemento de ceros a la derecha

    Expresión : -2147483648 = -4 << 29
     Decimal :
      val=-4
      res=-2147483648
     Binario :
      val=11111111111111111111111111111100
      res=10000000000000000000000000000000

    Expresión : 0 = -4 << 30
     Decimal :
      val=-4
      res=0
     Binario :
      val=11111111111111111111111111111100
      res=00000000000000000000000000000000
     Nota : bits salieron a la izquierda, incluyendo el bit de signo

       

Resultado del ejemplo anterior en una máquina de 64 bits:

    --- Desplazamientos a la derecha sobre enteros positivos ---
    Expresión : 2 = 4 >> 1
     Decimal :
      val=4
      res=2
     Binario :
      val=0000000000000000000000000000000000000000000000000000000000000100
      res=0000000000000000000000000000000000000000000000000000000000000010
     Nota : copia del bit de signo ahora a la izquierda

    Expresión : 1 = 4 >> 2
     Decimal :
      val=4
      res=1
     Binario :
      val=0000000000000000000000000000000000000000000000000000000000000100
      res=0000000000000000000000000000000000000000000000000000000000000001

    Expresión : 0 = 4 >> 3
     Decimal :
      val=4
      res=0
     Binario :
      val=0000000000000000000000000000000000000000000000000000000000000100
      res=0000000000000000000000000000000000000000000000000000000000000000
     Nota : bits salieron por la derecha

    Expresión : 0 = 4 >> 4
     Decimal :
      val=4
      res=0
     Binario :
      val=0000000000000000000000000000000000000000000000000000000000000100
      res=0000000000000000000000000000000000000000000000000000000000000000
     Nota : mismo resultado que arriba: no hay desplazamiento más allá de 0

    --- Desplazamientos a la derecha sobre enteros negativos ---
    Expresión : -2 = -4 >> 1
     Decimal :
      val=-4
      res=-2
     Binario :
      val=1111111111111111111111111111111111111111111111111111111111111100
      res=1111111111111111111111111111111111111111111111111111111111111110
     Nota : copia del bit de signo ahora a la izquierda

    Expresión : -1 = -4 >> 2
     Decimal :
      val=-4
      res=-1
     Binario :
      val=1111111111111111111111111111111111111111111111111111111111111100
      res=1111111111111111111111111111111111111111111111111111111111111111
     Nota : bits salieron por la derecha

    Expresión : -1 = -4 >> 3
     Decimal :
      val=-4
      res=-1
     Binario :
      val=1111111111111111111111111111111111111111111111111111111111111100
      res=1111111111111111111111111111111111111111111111111111111111111111
     Nota : mismo resultado que arriba: no hay desplazamiento más allá de -1

    --- Desplazamiento a la izquierda sobre enteros negativos ---
    Expresión : 8 = 4 << 1
     Decimal :
      val=4
      res=8
     Binario :
      val=0000000000000000000000000000000000000000000000000000000000000100
      res=0000000000000000000000000000000000000000000000000000000000001000
     Nota : complemento de ceros a la derecha

    Expresión : 4611686018427387904 = 4 << 60
     Decimal :
      val=4
      res=4611686018427387904
     Binario :
      val=0000000000000000000000000000000000000000000000000000000000000100
      res=0100000000000000000000000000000000000000000000000000000000000000

    Expresión : -9223372036854775808 = 4 << 61
     Decimal :
      val=4
      res=-9223372036854775808
     Binario :
      val=0000000000000000000000000000000000000000000000000000000000000100
      res=1000000000000000000000000000000000000000000000000000000000000000
     Nota : el bit de signo salió

    Expresión : 0 = 4 << 62
     Decimal :
      val=4
      res=0
     Binario :
      val=0000000000000000000000000000000000000000000000000000000000000100
      res=0000000000000000000000000000000000000000000000000000000000000000
     Nota : bits salieron a la izquierda

    --- Desplazamiento a la izquierda sobre enteros negativos ---
    Expresión : -8 = -4 << 1
     Decimal :
      val=-4
      res=-8
     Binario :
      val=1111111111111111111111111111111111111111111111111111111111111100
      res=1111111111111111111111111111111111111111111111111111111111111000
     Nota : complemento de ceros a la derecha

    Expresión : -9223372036854775808 = -4 << 61
     Decimal :
      val=-4
      res=-9223372036854775808
     Binario :
      val=1111111111111111111111111111111111111111111111111111111111111100
      res=1000000000000000000000000000000000000000000000000000000000000000

    Expresión : 0 = -4 << 62
     Decimal :
      val=-4
      res=0
     Binario :
      val=1111111111111111111111111111111111111111111111111111111111111100
      res=0000000000000000000000000000000000000000000000000000000000000000
     Nota : bits salieron a la izquierda, incluyendo el bit de signo

> [!WARNING]
> Úsense las funciones de la extensión [gmp](#book.gmp) para las manipulaciones sobre bits, cuando los enteros exceden `PHP_INT_MAX`.

## Véase también

`pack`, `unpack`, `gmp_and`, `gmp_or`, `gmp_xor`, `gmp_testbit`, `gmp_clrbit`
