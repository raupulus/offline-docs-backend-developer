---
title: for
source_url: https://www.php.net/manual/es/control-structures.for.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/for.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: ee1ce6a0e
order: 2150
---

## for

Las bucles `for` son las más complejas en PHP. Funcionan como las bucles for del lenguaje C(C++). La sintaxis de las bucles `for` es la siguiente :

    for (expr1; expr2; expr3)
        comandos

La primera expresión (`expr1`) es evaluada (ejecutada), en cualquier caso al inicio de la bucle.

Al inicio de cada iteración, la expresión `expr2` es evaluada. Si la evaluación es `true`, la bucle continúa y los comandos son ejecutados. Si la evaluación es `false`, la ejecución de la bucle se detiene.

Al final de cada iteración, la expresión `expr3` es evaluada (ejecutada).

Las expresiones pueden eventualmente ser dejadas vacías o pueden contener varias expresiones separadas por comas. En `expr2`, todas las expresiones separadas por una coma son evaluadas pero el resultado se obtiene desde la última parte. Si la expresión `expr2` es dejada vacía, esto significa que es una bucle infinita (PHP considera implícitamente que vale `true`, como en C). Esto no es realmente muy útil, a menos que se desee terminar la bucle con la instrucción condicional [`break`](#control-structures.break) en lugar de la expresión `for`.

Considérese los siguientes ejemplos. Todos muestran los números enteros de 1 a 10 :

```php
<?php
/* ejemplo 1 */

for ($i = 1; $i <= 10; $i++) {
    echo $i;
}

/* ejemplo 2 */

for ($i = 1; ; $i++) {
    if ($i > 10) {
        break;
    }
    echo $i;
}

/* ejemplo 3 */

$i = 1;
for (; ; ) {
    if ($i > 10) {
        break;
    }
    echo $i;
    $i++;
}

/* ejemplo 4 */

for ($i = 1, $j = 0; $i <= 10; $j += $i, print $i, $i++);
?>

   
```

Por supuesto, el primer ejemplo es el más simple de todos (o quizás el cuarto), pero también se puede pensar que usar una expresión vacía en una bucle `for` puede ser útil a veces.

PHP también soporta la siguiente sintaxis alternativa para las bucles `for` :

    for (expr1; expr2; expr3):
        comandos
        ...
    endfor;

Muchas personas tienen la costumbre de iterar a través de arrays, como en el ejemplo a continuación.

```php
<?php
/*
 * Este es un array con datos que queremos modificar
 * a lo largo de la bucle
 */
$people = array(
    array('name' => 'Kalle', 'salt' => 856412),
    array('name' => 'Pierre', 'salt' => 215863)
);

for($i = 0; $i < count($people); ++$i) {
    $people[$i]['salt'] = mt_rand(000000, 999999);
}
?>

   
```

Este código puede ser lento porque debe calcular el tamaño del array en cada iteración. Dado que el tamaño nunca cambia, puede ser fácilmente optimizado utilizando una variable intermedia para almacenar el tamaño en lugar de llamar repetidamente a la función `count` :

```php
<?php
$people = array(
    array('name' => 'Kalle', 'salt' => 856412),
    array('name' => 'Pierre', 'salt' => 215863)
);

for($i = 0, $size = count($people); $i < $size; ++$i) {
    $people[$i]['salt'] = mt_rand(000000, 999999);
}
?>

   
```
