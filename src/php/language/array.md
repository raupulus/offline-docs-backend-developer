---
title: Operadores de arrays
source_url: https://www.php.net/manual/es/language.operators.array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2660
---

## Operadores de arrays

| Ejemplo | Nombre | Resultado |
|----|----|----|
| \$a + \$b | Unión | Unión de `$a` y `$b`. |
| \$a == \$b | Igualdad | `true` si `$a` y `$b` contienen las mismas pares clave/valor. |
| \$a === \$b | Idéntico | `true` si `$a` y `$b` contienen las mismas pares clave/valor en el mismo orden y del mismo tipo. |
| \$a != \$b | Desigualdad | `true` si `$a` no es igual a `$b`. |
| \$a \<\> \$b | Desigualdad | `true` si `$a` no es igual a `$b`. |
| \$a !== \$b | No idéntico | `true` si `$a` no es idéntico a `$b`. |

Operadores de arrays

El operador `+` devuelve el array de la izquierda al cual se añaden los elementos del array de la derecha. Para las claves presentes en los 2 arrays, los elementos del array de la izquierda serán utilizados mientras que los elementos correspondientes en el array de la derecha serán ignorados.

El operador de adición a un array

```php
<?php
$a = array("a" => "manzana", "b" => "plátano");
$b = array("a" =>"pera", "b" => "fresa", "c" => "cereza");

$c = $a + $b; // Unión de $a y $b
echo "Unión de \$a y \$b : \n";
var_dump($c);

$c = $b + $a; // Unión de $b y $a
echo "Unión de \$b y \$a : \n";
var_dump($c);

$a += $b; // Unión de $a += $b es $a y $b
echo "Unión de \$a += \$b: \n";
var_dump($a);
?>

   
```

El ejemplo anterior mostrará:

```php
Unión de $a y $b :
array(3) {
  ["a"]=>
  string(7) "manzana"
  ["b"]=>
  string(7) "plátano"
  ["c"]=>
  string(6) "cereza"
}
Unión de $b y $a :
array(3) {
  ["a"]=>
  string(4) "pera"
  ["b"]=>
  string(5) "fresa"
  ["c"]=>
  string(6) "cereza"
}
Unión de $a += $b:
array(3) {
  ["a"]=>
  string(7) "manzana"
  ["b"]=>
  string(7) "plátano"
  ["c"]=>
  string(6) "cereza"
}

   
```

Los elementos de un array son iguales en términos de comparación si tienen la misma clave y el mismo valor.

Comparar arrays

```php
<?php
$a = array("manzana", "plátano");
$b = array(1 => "plátano", "0" => "manzana");

var_dump($a == $b); // bool(true)
var_dump($a === $b); // bool(false)
?>

   
```

## Véase también

[El tipo array](#language.types.array), [Las Funciones de Arrays](#ref.array)
