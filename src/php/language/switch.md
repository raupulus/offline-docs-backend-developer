---
title: switch
source_url: https://www.php.net/manual/es/control-structures.switch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/switch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: d149b6ddc
order: 2250
---

## switch

La instrucción `switch` equivale a una serie de instrucciones `if`. En numerosas ocasiones, se necesitará comparar la misma variable (o expresión) con un gran número de valores diferentes, y ejecutar diferentes partes de código según el valor al que sea igual. Esto es exactamente para lo que sirve la instrucción `switch`.

> [!NOTE]
> Téngase en cuenta que, a diferencia de otros lenguajes, la estructura [continue](#control-structures.continue) se aplica a las estructuras `switch` y se comporta de la misma manera que `break`. Si se tiene un `switch` dentro de un bucle, y se desea continuar hasta la siguiente iteración del bucle externo, se debe utilizar `continue 2`.

> [!NOTE]
> Téngase en cuenta que switch/case provoca una [comparación amplia](#types.comparisions-loose).

En el siguiente ejemplo, cada bloque de código es equivalente. Uno utiliza una serie de instrucciones `if` y `elseif`, y el otro una instrucción de tipo `switch`. En cada caso, la salida es la misma.

Instrucción `switch`

```php
<?php
// Este switch:

switch ($i) {
    case 0:
        echo "i igual 0";
        break;
    case 1:
        echo "i igual 1";
        break;
    case 2:
        echo "i igual 2";
        break;
}

// Equivale a:

if ($i == 0) {
    echo "i igual 0";
} elseif ($i == 1) {
    echo "i igual 1";
} elseif ($i == 2) {
    echo "i igual 2";
}
?>

   
```

Es importante entender que la instrucción `switch` ejecuta cada una de las cláusulas en orden. La instrucción `switch` se ejecuta línea por línea. Al principio, no se ejecuta ningún código. Solo cuando se encuentra una instrucción `case` cuya expresión se evalúa a un valor que coincide con el valor de la expresión `switch`, PHP ejecuta entonces las instrucciones correspondientes. PHP continúa ejecutando las instrucciones hasta el final del bloque de instrucciones del `switch`, o bien hasta que encuentra la instrucción `break`. Si no se puede utilizar la instrucción `break` al final de la instrucción `case`, PHP continuará ejecutando todas las instrucciones que siguen. Por ejemplo :

```php
<?php
switch ($i) {
    case 0:
        echo "i igual 0";
    case 1:
        echo "i igual 1";
    case 2:
        echo "i igual 2";
}
?>

   
```

En este ejemplo, si `$i` es igual a 0, PHP ejecutará todas las instrucciones que siguen ! Si `$i` es igual a 1, PHP ejecutará las dos últimas instrucciones. Y solo si `$i` es igual a 2, se obtendrá el resultado esperado, es decir, la visualización de "i igual 2". Por lo tanto, es importante no olvidar la instrucción `break` (aunque es posible que se omita en ciertas circunstancias).

En un comando `switch`, una condición se evalúa solo una vez, y el resultado se compara con cada `case`. En una estructura `elseif`, las condiciones se evalúan en cada comparación. Si la condición es más complicada que una simple comparación, o bien forma parte de un bucle, `switch` será más rápido.

La lista de comandos de un `case` puede estar vacía, en cuyo caso PHP utilizará la lista de comandos del caso siguiente.

```php
<?php
switch ($i) {
    case 0:
    case 1:
    case 2:
        echo "i es menor que 3 pero no es negativo";
        break;
    case 3:
        echo "i igual 3";
}
?>

   
```

Un caso especial es `default`. Este caso se utiliza cuando todos los otros casos han fallado. Por ejemplo :

```php
<?php
switch ($i) {
    case 0:
        echo "i igual 0";
        break;
    case 1:
        echo "i igual 1";
        break;
    case 2:
        echo "i igual 2";
        break;
    default:
       echo "i no es igual a 2, ni a 1, ni a 0.";
}
?>

   
```

> [!NOTE]
> Varios casos default generarán un error de nivel `E_COMPILE_ERROR`.

> [!NOTE]
> Técnicamente, el caso `default` puede ser colocado en cualquier posición. Solo se utilizará si ningún otro caso coincide. Sin embargo, por convención, es preferible colocarlo al final.

Si ningún `case` coincide, y no hay un `default`, entonces no se ejecutará ningún código, al igual que si ninguna instrucción `if` fuera verdadera.

Un valor de `case` puede ser dado en forma de expresión. Sin embargo, esta expresión será evaluada sola, y luego comparada de manera aproximada con el valor del `switch`. Esto significa que no puede ser utilizada para evaluaciones complejas del valor del `switch`. Por ejemplo :

```php
<?php
$target = 1;
$start = 3;

switch ($target) {
    case $start - 1:
        print "A";
        break;
    case $start - 2:
        print "B";
        break;
    case $start - 3:
        print "C";
        break;
    case $start - 4:
        print "D";
        break;
}

// Muestra "B"
?>

   
```

Para comparaciones más complejas, el valor `true` puede ser utilizado como valor de switch. O, alternativamente, bloques `if`-`else` en lugar de `switch`.

```php
<?php
$offset = 1;
$start = 3;

switch (true) {
    case $start - $offset === 1:
        print "A";
        break;
    case $start - $offset === 2:
        print "B";
        break;
    case $start - $offset === 3:
        print "C";
        break;
    case $start - $offset === 4:
        print "D";
        break;
}

// Muestra "B"
?>

   
```

La sintaxis alternativa para esta estructura de control es la siguiente : (para más información, ver [sintaxis alternativas](#control-structures.alternative-syntax)).

```php
<?php
switch ($i):
    case 0:
        echo "i igual 0";
        break;
    case 1:
        echo "i igual 1";
        break;
    case 2:
        echo "i igual 2";
        break;
    default:
        echo "i no es igual a 2, ni a 1, ni a 0";
endswitch;
?>

   
```

Es posible utilizar un punto y coma en lugar de dos puntos después de un case, como sigue :

```php
<?php
switch($beer)
{
    case 'leffe';
    case 'grimbergen';
    case 'guinness';
        echo 'Buena elección';
        break;
    default;
        echo 'Por favor, haga una elección...';
        break;
}
?>

   
```

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta característica está altamente desaconsejado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | La sintaxis alternativa que usa un punto y coma después de `case` ha sido desaprobada. |

## Véase también

[match](#control-structures.match)
