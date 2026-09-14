---
title: floatval
description: Convierte una cadena en un número de punto flotante
source_url: https://www.php.net/manual/es/function.floatval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/floatval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: fca392077
order: 100480
---

floatval

Convierte una cadena en un número de punto flotante

## Descripción

```php
floatval(mixed $value): float
```php

`floatval` devuelve el valor de tipo `float` (número de punto flotante), extraído del argumento `value`.

## Parámetros

`value`  
Puede ser de cualquier tipo escalar. `floatval` no debe ser utilizado en objetos; en caso de que así sea, se emitirá una alerta de nivel `E_WARNING` y la función devolverá 1.

## Valores devueltos

El valor flotante de la variable dada. Un array vacío devuelve 0, mientras que un array no vacío devuelve 1.

Las cadenas de caracteres devolverán la mayoría de las veces 0, pero esto depende del carácter más a la izquierda de la cadena. Las reglas clásicas de [conversión de un número de punto flotante](#language.types.float.casting) son aplicadas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El nivel de error al convertir un objeto ha sido modificado de `E_NOTICE` a `E_WARNING`. |

## Ejemplos

Ejemplo con `floatval`

```
<?php
$var = '122.34343The';
$float_value_of_var = floatval($var);
echo $float_value_of_var; // 122.34343
?>

    
```php

Ejemplo con `floatval` con caracteres no numéricos a la izquierda

```
<?php
$var = 'The122.34343';
$float_value_of_var = floatval($var);
echo $float_value_of_var; // 0
?>

    
```php

## Véase también

`boolval`, `intval`, `strval`, `settype`, [Manipulación de tipos](#language.types.type-juggling)
