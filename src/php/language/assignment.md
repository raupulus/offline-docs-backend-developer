---
title: Los operadores de asignación
source_url: https://www.php.net/manual/es/language.operators.assignment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/assignment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2670
---

## Los operadores de asignación

El operador de asignación más simple es el signo "=". El primer reflejo es pensar que este signo significa "igual a". No es el caso. Significa que el operando de la izquierda se ve asignado el valor de la expresión que está a la derecha del signo igual.

El valor de una expresión de asignación es el valor asignado. Por ejemplo, el valor de la expresión '`$a = 3`' es el valor 3. Esto permite utilizar trucos tales como:

Asignaciones anidadas

```php
<?php
$a = ($b = 4) + 5;
// $a ahora es igual a 9, y $b vale 4.
var_dump($a);
?>

   
```

Además del simple operador de asignación, existen "operadores combinados" para todos los operadores [aritméticos](#language.operators), la unión de arrays y para los operadores sobre los strings. Esto permite utilizar el valor de una variable en una expresión y asignar el resultado de esta expresión a esta variable. Por ejemplo:

Asignaciones Combinadas

```php
<?php
$a = 3;
$a += 5; // asigna el valor 8 a la variable $a corresponde a la instrucción '$a = $a + 5';
$b = "Hola ";
$b .= " a todos!";  // asigna el valor "Hola a todos!" a
                          //  la variable $b
                          //  idéntico a $b = $b." a todos!";

var_dump($a, $b);
?>

   
```

Se puede observar que la asignación copia el contenido de la variable original en la nueva variable (asignación por valor), lo que hace que los cambios de valor de una variable no modificarán el valor de la otra. Esto puede ser importante al copiar un gran array durante un bucle.

Una excepción al comportamiento de asignación por valor en PHP es el tipo `object`, estos son asignados por referencia. La copia de objeto debe ser explícitamente solicitada gracias al mot-clé [clone](#language.oop5.cloning).

## Asignación por referencia

La asignación por referencia también es soportada, mediante la sintaxis "`$var = &$othervar;`". La asignación por referencia significa que las dos variables apuntan al mismo contenedor de datos, nada es copiado en ningún lugar.

Asignación por referencia

```php
<?php
$a = 3;
$b = &$a; // $b es una referencia a $a

print "$a\n"; // muestra 3
print "$b\n"; // muestra 3

$a = 4; // cambia $a

print "$a\n"; // muestra 4
print "$b\n"; // muestra 4 también, porque $b es una referencia a $a, que ha sido
              // cambiada
?>

    
```

El operador [new](#language.oop5.basic.new) devuelve una referencia automáticamente, por lo tanto, asignar el resultado de [new](#language.oop5.basic.new) por referencia es un error

Nuevo operador por referencia

```php
<?php
class C {}

$o = &new C;
?>

    
```

El ejemplo anterior mostrará:

    Parse error: syntax error, unexpected token ";", expecting "("

Más información sobre las referencias y sus usos posibles pueden ser encontrados en la sección del manual [Las referencias explicadas](#language.references).

## Los operadores de asignación aritméticos

| Ejemplo       | Equivalente        | Operación      |
|---------------|--------------------|----------------|
| \$a += \$b    | \$a = \$a + \$b    | Adición        |
| \$a -= \$b    | \$a = \$a - \$b    | Sustracción    |
| \$a \*= \$b   | \$a = \$a \* \$b   | Multiplicación |
| \$a /= \$b    | \$a = \$a / \$b    | División       |
| \$a %= \$b    | \$a = \$a % \$b    | Módulo         |
| \$a \*\*= \$b | \$a = \$a \*\* \$b | Exponenciación |

## Operadores de asignación bits a bits

| Ejemplo       | Equivalente        | Operación                     |
|---------------|--------------------|-------------------------------|
| \$a &= \$b    | \$a = \$a & \$b    | Operador And                  |
| \$a \|= \$b   | \$a = \$a \| \$b   | Operador Or                   |
| \$a ^= \$b    | \$a = \$a ^ \$b    | Operador Xor                  |
| \$a \<\<= \$b | \$a = \$a \<\< \$b | Desplazamiento a la izquierda |
| \$a \>\>= \$b | \$a = \$a \>\> \$b | Desplazamiento a la derecha   |

## Otros operadores de asignación

| Ejemplo     | Equivalente      | Operación                    |
|-------------|------------------|------------------------------|
| \$a .= \$b  | \$a = \$a . \$b  | Concatenación de un string   |
| \$a ??= \$b | \$a = \$a ?? \$b | Operador de coalescencia nul |

## Véase también

[los operadores aritméticos](#language.operators.arithmetic), [los operadores bits a bits](#language.operators.bitwise), [los operadores de coalescencia nul](#language.operators.comparison.coalesce)
