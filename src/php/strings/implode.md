---
title: implode
description: Une elementos de un array en un string
source_url: https://www.php.net/manual/es/function.implode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/implode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 5dfba3d91
order: 88820
---

implode

Une elementos de un array en un string

## Descripción

```php
implode(string $separator, array $array): string
```php

Firma alternativa (no se admite argumentos con nombre):

```php
implode(array $array): string
```

Firma heredada (obsoleta a partir de PHP 7.4.0, eliminada a partir de PHP 8.0.0):

```php
implode(array $array, string $separator): string
```php

Une los elementos de un array con el string `separator`.

## Parámetros

`separator`  
Opcional. Por defecto es un string vacío.

`array`  
El array de strings a ser usados por implode.

## Valores devueltos

Devuelve un string que contiene la representación de todos los elementos del array en el mismo orden, con el string 'glue' entre cada elemento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Pasar el parámetro `separator` después del `array` ya no es compatible. |
| 7.4.0 | Pasar el parámetro `separator` después del `array` (es decir, sin utilizar el orden documentado de los parámetros) es obsoleto. |

## Ejemplos

Ejemplo de `implode`

```
<?php

$array = ['lastname', 'email', 'phone'];
var_dump(implode(",", $array)); // string(20) "lastname,email,phone"

// Devuelve un string vacío si se usa un array vacío:
var_dump(implode('hello', [])); // string(0) ""

// El separador es opcional:
var_dump(implode(['a', 'b', 'c'])); // string(3) "abc"

?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`explode`, `preg_split`, `http_build_query`
