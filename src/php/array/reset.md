---
title: reset
description: Reinicia el puntero interno del array al principio
source_url: https://www.php.net/manual/es/function.reset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/reset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 0a192fcd9
order: 5940
---

reset

Reinicia el puntero interno del array al principio

## Descripción

```php
reset(array $array): mixed
```php

`reset` reemplaza el puntero del array `array` al primer elemento y devuelve el valor del primer elemento.

## Parámetros

`array`  
El array de entrada.

## Valores devueltos

Devuelve el valor del primer elemento del array, o `false` si el array está vacío.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | O bien convertir el `object` en un `array` utilizando `get_mangled_object_vars` primero, o utilizar los métodos proporcionados por una clase que implemente Iterator, tal como `ArrayIterator`. |
| 7.4.0 | A partir de PHP 7.4.0, las instancias de clases [SPL](#book.spl) son tratadas como objetos vacíos sin propiedades en lugar de llamar al método Iterator con el mismo nombre que esta función. |

## Ejemplos

Ejemplo con `reset`

```
<?php

$array = array('step one', 'step two', 'step three', 'step four');

// Por omisión, el puntero está en el primer elemento
echo current($array) . "<br />\n"; // "step one"

// se saltan dos elementos
next($array);
next($array);
echo current($array) . "<br />\n"; // "step three"

// se reinicia el puntero al principio
reset($array);
echo current($array) . "<br />\n"; // "step one"

?>

    
```php

## Notas

> [!NOTE]
> El valor devuelto para un array vacío no es distinguible del valor devuelto para un array que contiene un valor `bool` `false` como primer elemento. Para verificar correctamente el valor del primer elemento de un array, que puede contener un elemento `false`, se debe primero verificar el `count` del array, o verificar si la `key` no es `null`, después de haber llamado `reset`.

## Véase también

`current`, `each`, `end`, `next`, `prev`, `array_key_first`
