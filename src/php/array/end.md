---
title: end
description: Posiciona el puntero del array al final del array
source_url: https://www.php.net/manual/es/function.end.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/end.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: 0a192fcd9
order: 5800
---

end

Posiciona el puntero del array al final del array

## Descripción

```php
end(array $array): mixed
```php

`end` desplaza el puntero interno del array `array` hasta el último elemento y devuelve su valor.

## Parámetros

`array`  
El array. Este array es pasado por referencia ya que será modificado por la función. Esto significa que debe pasar una verdadera variable y no una función que devuelva un array, ya que actualmente, solo las variables pueden ser pasadas por referencia.

## Valores devueltos

Devuelve el valor del último elemento o `false` si el array está vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | O bien convertir el `object` en un `array` utilizando `get_mangled_object_vars` primero, o utilizar los métodos proporcionados por una clase que implemente Iterator, tal como `ArrayIterator`. |
| 7.4.0 | A partir de PHP 7.4.0, las instancias de clases [SPL](#book.spl) son tratadas como objetos vacíos sin propiedades en lugar de llamar al método Iterator con el mismo nombre que esta función. |

## Ejemplos

Ejemplo con `end`

```
<?php

$fruits = array('apple', 'banana', 'cranberry');
echo end($fruits); // cranberry

?>

    
```php

## Véase también

`current`, `each`, `prev`, `reset`, `next`, `array_key_last`
