---
title: Operadores funcionales
source_url: https://www.php.net/manual/es/language.operators.functional.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/functional.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 2f1812217
order: 2720
---

## Operadores funcionales

PHP 8.5 y versiones posteriores admiten un operador que funciona directamente con callables. El operador `|>`, o “pipe”, acepta un callable de un solo parámetro en el lado derecho y le pasa el valor del lado izquierdo, evaluando el resultado del callable. El callable en el lado derecho puede ser cualquier callable válido en PHP: una `Closure`, un [callable de primera clase](#functions.first_class_callable_syntax), un objeto que implemente [\_\_invoke()](#object.invoke), etc.

Esto significa que las siguientes dos líneas son lógicamente equivalentes.

Usando `|>`

```php
<?php
$result = "Hola Mundo" |> strlen(...);
echo $result, PHP_EOL;

$result = strlen("Hola Mundo");
echo $result, PHP_EOL;
?>

   
```

El ejemplo anterior mostrará:

    10
    10

Para una única llamada, no resulta especialmente útil. Se vuelve útil cuando se encadenan múltiples llamadas. Es decir, los siguientes dos fragmentos de código son lógicamente equivalentes:

Encadenando llamadas \|\>

```php
<?php
$result = "PHP Rocks"
    |> htmlentities(...)
    |> str_split(...)
    |> (fn($x) => array_map(strtoupper(...), $x))
    |> (fn($x) => array_filter($x, fn($v) => $v != 'O'))
;
print_r($result);

$temp = "PHP Rocks";
$temp = htmlentities($temp);
$temp = str_split($temp);
$temp = array_map(strtoupper(...), $temp);
$temp = array_filter($temp, fn($v) => $v != 'O');
$result = $temp;
print_r($result);
?>

   
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => P
        [1] => H
        [2] => P
        [3] =>
        [4] => R
        [6] => C
        [7] => K
        [8] => S
    )
    Array
    (
        [0] => P
        [1] => H
        [2] => P
        [3] =>
        [4] => R
        [6] => C
        [7] => K
        [8] => S
    )

El lado izquierdo del operador pipe puede ser cualquier valor o expresión. El lado derecho puede ser cualquier callable válido en PHP que acepte un solo parámetro, o cualquier expresión que se evalúe como tal. Las funciones que requieren más de un parámetro no están permitidas y fallarán como si se llamaran normalmente con argumentos insuficientes. Las funciones que reciben variables por referencia tampoco están permitidas. Si el lado derecho no se evalúa como un callable válido, se lanzará un error.

> [!NOTE]
> Tenga en cuenta que, para evitar ambigüedades de sintaxis, las [funciones de flecha](#functions.arrow) DEBEN estar entre paréntesis cuando se utilicen con el operador pipe, como en los ejemplos anteriores. No hacerlo provocará un error fatal.

## Véase también

`Closure`
