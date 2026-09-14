---
title: str_replace
description: Reemplaza todas las ocurrencias en una string
source_url: https://www.php.net/manual/es/function.str-replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89180
---

str_replace

Reemplaza todas las ocurrencias en una string

## Descripción

```php
str_replace(array $search, array $replace, string $subject, [int $count]): string
```php

`str_replace` devuelve una string o un array, donde todas las ocurrencias de `search` en `subject` han sido reemplazadas por `replace`.

Para reemplazar un texto en función de un patrón en lugar de una string fija, utilice `preg_replace`.

## Parámetros

Si los argumentos `search` y `replace` son arrays, entonces la función `str_replace` tomará un valor de cada array y los utilizará para la búsqueda y el reemplazo en `subject`. Si el argumento `replace` tiene menos valores que el argumento `search`, entonces una string vacía será utilizada como valor para el resto de los valores de reemplazo. Si el argumento `search` es un array y el argumento `replace` es una string, entonces esta string de reemplazo será utilizada para cada valor de `search`. Lo inverso no tiene sentido.

Si `search` o `replace` son arrays, los elementos son procesados del primero al último.

`search`  
El valor a buscar, también conocido como *patrón*. Un array puede ser utilizado para designar múltiples patrones.

`replace`  
El valor de reemplazo a sustituir por los valores encontrados. Un array puede ser utilizado para designar múltiples valores de reemplazo.

`subject`  
La string o el array sobre el cual se realizará la búsqueda y el reemplazo, también conocido como *pajar*.

Si `subject` es un array, entonces el reemplazo se realizará en cada elemento del mismo, y el valor devuelto será también un array.

`count`  
Si se proporciona, esta variable contendrá el número de reemplazos realizados.

## Valores devueltos

Esta función devuelve una string, o un array, conteniendo los valores reemplazados.

## Ejemplos

Ejemplo 1 con `str_replace`

```
<?php
// Genera: <body text='black'>
$bodytag = str_replace("%body%", "black", "<body text='%body%'>");
echo $bodytag, PHP_EOL;

// Genera: Hll Wrld f PHP
$vowels = array("a", "e", "i", "o", "u", "A", "E", "I", "O", "U");
$onlyconsonants = str_replace($vowels, "", "Hello World of PHP");
echo $onlyconsonants, PHP_EOL;

// Genera: You should eat pizza, beer, and ice cream every day
$phrase  = "You should eat fruits, vegetables, and fiber every day.";
$healthy = array("fruits", "vegetables", "fiber");
$yummy   = array("pizza", "beer", "ice cream");

$newphrase = str_replace($healthy, $yummy, $phrase);
echo $newphrase, PHP_EOL;

// Genera: good goy miss moy
$str = str_replace("ll", "", "good golly miss molly!", $count);
echo $count, PHP_EOL;

?>

    
```php

Ejemplo 2 con `str_replace`

```
<?php
// Orden de los reemplazos
$str     = "Line 1\nLine 2\rLine 3\r\nLine 4\n";
$order   = array("\r\n", "\n", "\r");
$replace = '<br />';

// Procesamiento del primer \r\n, no serán convertidos dos veces.
$newstr = str_replace($order, $replace, $str);
echo $newstr, PHP_EOL;

// Muestra F porque A es reemplazado por B, luego B es reemplazado por C, y así sucesivamente...
// Finalmente, E es reemplazado por F
$search  = array('A', 'B', 'C', 'D', 'E');
$replace = array('B', 'C', 'D', 'E', 'F');
$subject = 'A';
echo str_replace($search, $replace, $subject), PHP_EOL;

// Muestra: apearpearle pear
// Por las mismas razones que arriba
$letters = array('a', 'p');
$fruit   = array('apple', 'pear');
$text    = 'a p';
$output  = str_replace($letters, $fruit, $text);
echo $output, PHP_EOL;
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

> [!CAUTION]
> Debido a que la función `str_replace` realiza los reemplazos de izquierda a derecha, puede reemplazar un valor previamente insertado durante múltiples reemplazos.

> [!NOTE]
> Esta función es sensible a mayúsculas y minúsculas. Utilice la función `str_ireplace` para un reemplazo insensible a mayúsculas y minúsculas.

## Véase también

`str_ireplace`, `substr_replace`, `preg_replace`, `strtr`
