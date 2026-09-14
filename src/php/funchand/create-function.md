---
title: create_function
description: Crea una función anónima
source_url: https://www.php.net/manual/es/function.create-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/create-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: true
translation_revision: 39752929c
order: 24740
---

create_function

Crea una función anónima

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0 y ha sido *ELIMINADA* a partir de PHP 8.0.0.

## Descripción

```php
create_function(string $args, string $code): string
```php

`create_function` crea una función anónima, a partir de los argumentos pasados, y devuelve un nombre de función único.

> [!CAUTION]
> Esta función, internamente, utiliza la función `eval` y por lo tanto los requisitos de seguridad son idénticos a los de la función `eval`. Además, el rendimiento no es óptimo y el uso de memoria es significativo.
>
> Una [función anónima](#functions.anonymous) nativa debería ser utilizada en su lugar.

## Parámetros

Generalmente, los argumentos `args` son presentados en forma de una cadena entre comillas simples, y la misma recomendación aplica para `code`. La razón de usar comillas simples es proteger los nombres de variables del reemplazo por su valor. Si se usan comillas dobles, no se olvide de escapar los nombres de variables (i.e. `\$avar`).

`args`  
Los argumentos de la función.

`code`  
El código de la función.

## Valores devueltos

Devuelve un nombre de función único, en forma de una `string`, o `false` si ocurre un error.

## Ejemplos

Creación de una función anónima con `create_function`

Esta función puede ser utilizada para (por ejemplo) crear una función a partir de información recolectada durante la ejecución:

```
<?php
$newfunc = create_function('$a,$b', 'return "ln($a) + ln($b) = " . log($a * $b);');
echo "Nueva función anónima: $newfunc\n";
echo $newfunc(2, M_E) . "\n";
// mostrará:
// Nueva función anónima: lambda_1
// ln(2) + ln(2.718281828459) = 1.6931471805599
?>

    
```php

O, para poder aplicar una función genérica a una lista de argumentos.

Procesamiento genérico por función con `create_function`

```
<?php
function process($var1, $var2, $farr)
{
    foreach ($farr as $f) {
        echo $f($var1, $var2) . "\n";
    }
}

// Creación de una serie de funciones matemáticas
$f1 = 'if ($a >=0) {return "b*a^2 = ".$b*sqrt($a);} else {return false;}';
$f2 = "return \"min(b^2+a, a^2,b) = \".min(\$a*\$a+\$b,\$b*\$b+\$a);";
$f3 = 'if ($a > 0 && $b != 0) {return "ln(a)/b = ".log($a)/$b; } else { return false; }';
$farr = array(
    create_function('$x,$y', 'return "un poco de trigonometría: ".(sin($x) + $x*cos($y));'),
    create_function('$x,$y', 'return "una hipotenusa: ".sqrt($x*$x + $y*$y);'),
    create_function('$a,$b', $f1),
    create_function('$a,$b', $f2),
    create_function('$a,$b', $f3)
    );

echo "\nUso de la primera lista de funciones anónimas\n";
echo "parámetros: 2.3445, M_PI\n";
process(2.3445, M_PI, $farr);

// Ahora una lista de funciones sobre cadenas de caracteres
$garr = array(
    create_function('$b,$a', 'if (strncmp($a, $b, 3) == 0) return "** \"$a\" '.
    'and \"$b\"\n** Look the same to me! (looking at the first 3 chars)";'),
    create_function('$a,$b', 'return "CRCs: " . crc32($a) . ", ".crc32($b);'),
    create_function('$a,$b', 'return "similaridad (a,b) = " . similar_text($a, $b, &$p) . "($p%)";')
    );
echo "\nUso de la segunda lista de funciones anónimas\n";
process("Twas brilling and the slithy toves", "Twas the night", $garr);
?>

    
```php

El ejemplo anterior mostrará:

    Uso de la primera lista de funciones anónimas
    parámetros: 2.3445, M_PI
    un poco de trigonometría: -1.6291725057799
    una hipotenusa: 3.9199852871011
    b*a^2 = 4.8103313314525
    min(b^2+a, a^2,b) = 8.6382729035898
    ln(a)/b = 0.27122299212594

    Uso de la segunda lista de funciones anónimas
    ** "Twas the night" and "Twas brilling and the slithy toves"
    ** Estas cadenas se parecen! (mirando los tres primeros caracteres)
    CRCs: -725381282, 342550513
    similaridad (a,b) = 11(45.833333333333%)

Pero el uso más común de las funciones lambda es la función de devolución de llamada, por ejemplo, al utilizar `array_walk` o `usort`

Uso de funciones anónimas como función de devolución de llamada

```
<?php
$av = array("la ", "una ", "cette ", "une certaine ");
array_walk($av, create_function('&$v,$k', '$v = $v . "maison";'));
print_r($av);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
      [0] => la maison
      [1] => une maison
      [2] => cette maison
      [3] => une certaine maison
    )

        

un array de cadenas de caracteres ordenadas de la más corta a la más larga

```
<?php

$sv = array("petite", "longue", "une très longue chaîne", "une phrase toute entière");
print_r($sv);

?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
      [0] => petite
      [1] => longue
      [2] => une très longue chaîne
      [3] => une phrase toute entière
    )

        

ordenadas de la más larga a la más corta

```
<?php

usort($sv, create_function('$a,$b','return strlen($b) - strlen($a);'));
print_r($sv);

?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
      [0] => une phrase toute entière
      [1] => une très longue chaîne
      [2] => longue
      [3] => petite
    )

## Véase también

[Funciones anónimas](#functions.anonymous)
