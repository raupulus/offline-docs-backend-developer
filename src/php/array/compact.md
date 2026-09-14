---
title: compact
description: Crea un array a partir de variables y su valor
source_url: https://www.php.net/manual/es/function.compact.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/compact.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: true
translation_revision: d58ee8eaa
order: 5760
---

compact

Crea un array a partir de variables y su valor

## Descripción

```php
compact(array $var_name, array ...$var_names): array
```php

Crea un array a partir de variables y su valor.

Para cada uno de los argumentos `varname`, `...`, `compact` busca una variable con el mismo nombre en la [tabla actual de símbolos](#features.gc.refcounting-basics), y la añade al array, de manera que se tenga la relación nombre =\> 'valor de variable'. En resumen, es lo contrario de la función `extract`.

> [!NOTE]
> Antes de PHP 7.3, todas las cadenas no definidas eran ignoradas en silencio.

## Parámetros

`var_name`; `var_names`  
`compact` acepta diferentes parámetros `varname`. Los parámetros pueden ser variables que contienen cadenas, o un array de cadenas, que puede contener otros arrays de nombres de variables, que `compact` tratará de manera recursiva.

## Valores devueltos

Devuelve el array de salida que contiene todas las variables añadidas.

## Errores/Excepciones

`compact` emite un error de nivel `E_WARNING` si una cadena dada hace referencia a una variable no definida.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si una cadena dada hace referencia a una variable no definida, se emite un error de nivel `E_WARNING`. |
| 7.3.0 | `compact` emite ahora un error de nivel `E_NOTICE` si una cadena dada hace referencia a una variable no definida. Anteriormente, estas cadenas eran ignoradas en silencio. |

## Ejemplos

Ejemplo con `compact`

```
<?php

$city  = "San Francisco";
$state = "CA";
$event = "SIGGRAPH";

$location_vars = array("city", "state");

$result = compact("event", $location_vars);
print_r($result);

?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [event] => SIGGRAPH
    [city] => San Francisco
    [state] => CA
)

    
```php

## Notas

> [!NOTE]
> Debido a que las [variables variables](#language.variables.variable) no deben ser utilizadas con los [arrays superglobales](#language.variables.superglobals) en funciones, los arrays Superglobales no deben ser pasados a la función `compact`.

## Véase también

`extract`
