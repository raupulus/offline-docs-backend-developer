---
title: sscanf
description: Analiza una cadena utilizando un formato
source_url: https://www.php.net/manual/es/function.sscanf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/sscanf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 9947012f7
order: 89090
---

sscanf

Analiza una cadena utilizando un formato

## Descripción

```php
sscanf(string $string, string $format, mixed ...$vars): array
```php

`sscanf` es la función inversa de `printf`. `sscanf` lee datos de la cadena `string` e los interpreta según el formato `format`.

Todos los caracteres en blanco en la cadena `format` corresponden a un carácter en blanco en la cadena `string`. Esto significa que incluso una tabulación (`\t`) en la cadena de formato puede corresponder a un simple espacio en la cadena `str`.

## Parámetros

`string`  
La cadena a analizar.

`format`  
El formato interpretado para `string` se describe en la documentación de la `sprintf` con las siguientes diferencias: La función no tiene en cuenta el contexto local., `F`, `g`, `G` y `b` no son soportados., `D` representa un número decimal., `i` representa un número entero con detección de base., `n` representa el número de caracteres tratados hasta este punto., `s` detiene la lectura en cada carácter de espacio., `*` en lugar de `argnum$` elimina la asignación de esta especificación de conversión.

`vars`  
Opcionalmente, se pueden pasar variables en este parámetro, por referencia que contendrán los valores del análisis.

## Valores devueltos

Si solo se proporcionan dos parámetros, los valores encontrados se devolverán como un `array`. De lo contrario, si se proporcionan los parámetros opcionales, la función devolverá el número de valores asignados. El parámetro opcional debe pasarse por referencia.

Si hay más subcadenas esperadas en el parámetro `format` que las disponibles en `string`, entonces `null` será devuelto.

Cuando se usan parámetros opcionales y se alcanza el final de la cadena de entrada `string` antes de que se haya analizado ningún valor, se devuelve `-1`.

## Ejemplos

Ejemplo con `sscanf`

```
<?php
// Lectura de un número de serie
list($serial) = sscanf("SN/2350001", "SN/%d");
// y la fecha de fabricación
$mandate = "January 01 2000";
list($month, $day, $year) = sscanf($mandate, "%s %d %d");
echo "El producto $serial fue fabricado el: $year-" . substr($month, 0, 3) . "-$day\n";
?>

   
```php

Si se pasan parámetros opcionales, `sscanf` devolverá el número de valores asignados.

`sscanf` - uso de parámetros opcionales

```
<?php
// lee la información del autor y genera una entrada DocBook
$auth = "24\tLewis Carroll";
$n = sscanf($auth, "%d\t%s %s", $id, $first, $last);
echo "<author id='$id'>
    <firstname>$first</firstname>
    <surname>$last</surname>
</author>\n";
?>

   
```php

## Véase también

printf

sprintf

fprintf

vprintf

vsprintf

vfprintf

fscanf

number_format

date
