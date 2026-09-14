---
title: isset
description: Determina si una variable está declarada y es diferente de null
source_url: https://www.php.net/manual/es/function.isset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/isset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: dd100db2c
order: 100720
---

isset

Determina si una variable está declarada y es diferente de

null

## Descripción

```php
isset(mixed $var, mixed ...$vars): bool
```php

Determina si una variable es considerada definida, lo que significa que está declarada y es diferente de `null`.

Si una variable ha sido destruida con la función `unset`, ya no se considera como definida.

`isset` devolverá `false` al verificar una variable con valor `null`. Asimismo, cabe señalar que el carácter nulo (`"\0"`) no es equivalente a la constante PHP `null`.

Si se proporcionan varios argumentos, entonces `isset` devolverá `true` solo si todos los argumentos están definidos. La evaluación se realiza de izquierda a derecha y se detiene en cuanto se encuentra una variable no definida.

## Parámetros

`var`  
La variable a analizar.

`vars`  
Variables adicionales.

## Valores devueltos

Devuelve `true` si `var` existe y tiene un valor distinto de `null`. `false` en caso contrario.

## Ejemplos

Ejemplo con `isset`

```
<?php

$var = '';

// Esto es verdadero, por lo que el texto se muestra
if (isset($var)) {
    echo 'Esta variable existe, por lo que puede ser mostrada.', PHP_EOL;
}

// En los siguientes ejemplos, utilizamos var_dump() para mostrar
// el retorno de la función isset().

$a = 'test';
$b = 'anothertest';

var_dump(isset($a));      // TRUE
var_dump(isset($a, $b)); // TRUE

unset($a);

var_dump(isset($a));     // FALSE
var_dump(isset($a, $b)); // FALSE

$foo = NULL;
var_dump(isset($foo));   // FALSE

?>

    
```php

También funciona con arrays:

Ejemplo de `isset` con elementos de array

```
<?php

$a = array('test' => 1, 'bonjour' => NULL, 'pie' => array('a' => 'apple'));

var_dump(isset($a['test']));            // TRUE
var_dump(isset($a['foo']));             // FALSE
var_dump(isset($a['bonjour']));         // FALSE

// La clave 'bonjour' vale NULL y es considerada como no existente
// Si se desea verificar la existencia de esta clave, utilice esta función
var_dump(array_key_exists('bonjour', $a)); // TRUE

// Verificación de valores en profundidad
var_dump(isset($a['pie']['a']));        // TRUE
var_dump(isset($a['pie']['b']));        // FALSE
var_dump(isset($a['cake']['a']['b']));  // FALSE
?>

    
```php

`isset` sobre posiciones en un string

```
<?php
$expected_array_got_string = 'somestring';
var_dump(isset($expected_array_got_string['some_key']));
var_dump(isset($expected_array_got_string[0]));
var_dump(isset($expected_array_got_string['0']));
var_dump(isset($expected_array_got_string[0.5]));
var_dump(isset($expected_array_got_string['0.5']));
var_dump(isset($expected_array_got_string['0 Mostel']));
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
    bool(true)
    bool(true)
    bool(false)
    bool(false)

## Notas

> [!WARNING]
> `isset` funciona únicamente con variables, ya que el uso de cualquier otra cosa resultará en un error de análisis. Para verificar si una [constante](#language.constants) está definida, utilice la función `defined`.

> [!NOTE]
> Como esto es una estructura del lenguaje, y no una función, no es posible llamarla con las [funciones variables](#functions.variable-functions) o [argumentos nombrados](#functions.named-arguments).

> [!NOTE]
> Al utilizar esta función sobre propiedades de objeto inaccesibles, se llamará al método mágico [\_\_isset()](#object.isset) si existe.

## Véase también

`empty`, [\_\_isset()](#object.isset), `unset`, `defined`, [la tabla de comparación de tipos](#types.comparisons), `array_key_exists`, `is_null`, el operador de control de informe de errores [@](#language.operators.errorcontrol)
