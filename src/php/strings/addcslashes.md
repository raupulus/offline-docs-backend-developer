---
title: addcslashes
description: Añade barras invertidas a un string, al estilo del lenguaje C
source_url: https://www.php.net/manual/es/function.addcslashes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/addcslashes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 88590
---

addcslashes

Añade barras invertidas a un string, al estilo del lenguaje C

## Descripción

```php
addcslashes(string $string, string $characters): string
```php

Devuelve el string `string`, después de haber añadido barras invertidas antes de todos los caracteres que están presentes en la lista `characters`.

## Parámetros

`string`  
El string a escapar.

`characters`  
Una lista de caracteres a escapar. Si `characters` contiene los caracteres `\n`, `\r` etc., serán convertidos al estilo del lenguaje C, mientras que otros caracteres no alfanuméricos con un código ASCII inferior a 26 y superior a 126 son reemplazados por su representación octal.

Al definir una secuencia de caracteres en el parámetro `characters`, asegúrese de que conoce bien todos los caracteres que se encuentran entre los límites de los intervalos.

`addcslashes` con rangos

```
<?php
echo addcslashes('foo[ ]', 'A..z');
// Muestra:  \f\o\o\[ \]
// Todas las mayúsculas y minúsculas serán escapadas
// ... pero también los caracteres [\]^_`
?>

        
```php

Asimismo, si el primer carácter de un intervalo tiene un código ASCII mayor que el segundo, el intervalo no será creado. Solo los límites del intervalo y el carácter punto (.) serán escapados. Utilice la función `ord` para encontrar el valor ASCII de un carácter.

`addcslashes` con caracteres en el orden incorrecto

```
<?php
echo addcslashes("zoo['.']", 'z..A');
// Muestra:  \zoo['\.']
?>

        
```php

Tenga cuidado con el uso de caracteres como 0, a, b, f, n, r, t y v. Serán convertidos en \0, \a, \b, \f, \n, \r, \t y \v, todos siendo secuencias de escape en C. La mayoría de estas secuencias también están definidas en otros lenguajes derivados de C, incluyendo PHP, lo que significa que no se obtendrá el resultado esperado si se utiliza la salida de la función `addcslashes` para generar código para estos lenguajes con los caracteres definidos en el parámetro `characters`.

## Valores devueltos

Devuelve el string escapado.

## Ejemplos

`characters` puede escribirse "\0..\37", lo que identifica todos los caracteres ASCII cuyo código está entre 0 y 37.

Ejemplo con `addcslashes`

```
<?php
$not_escaped = "PHP isThirty\nYears Old!\tYay to the Elephant!\n";
$escaped = addcslashes($not_escaped, "\0..\37!@\177..\377");
echo $escaped;
?>

    
```php

## Véase también

`stripcslashes`, `stripslashes`, `addslashes`, `htmlspecialchars`, `quotemeta`
