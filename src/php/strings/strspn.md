---
title: strspn
description: Encuentra la longitud del segmento inicial de un string que contiene
  todos los caracteres de una máscara dada
source_url: https://www.php.net/manual/es/function.strspn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strspn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 422bb0322
order: 89450
---

strspn

Encuentra la longitud del segmento inicial de un string que contiene todos los caracteres de una máscara dada

## Descripción

```php
strspn(string $string, string $characters, [int $offset], [int $length]): int
```php

Encuentra la longitud del segmento inicial de `string` que contiene *únicamente* los caracteres desde la máscara `characters`.

Si los parámetros `offset` y `length` son omitidos, entonces todo el string `string` será analizado. Si son proporcionados, entonces los efectos serán idénticos a llamar `strspn(substr($string, $offset, $length), $characters)` (ver [???](#function.substr) para más información).

El código siguiente:

```
<?php
$var = strspn("42 es la respuesta, pero ¿cuál es la pregunta?", "1234567890");
?>

    
```php

asigna `2` a la variable `$var`, ya que el string "42" es el segmento inicial del parámetro `string` cuyos caracteres están contenidos en "1234567890".

## Parámetros

`string`  
El string a analizar.

`characters`  
La lista de caracteres autorizados.

`offset`  
La posición en el string `string` a partir de la cual se debe buscar.

Si `offset` es proporcionado y no es negativo, entonces `strspn` comenzará a analizar el string `string` en la posición `offset`. Por ejemplo, en el string '`abcdef`', el carácter en la posición `0` es '`a`', el carácter en la posición `2` es '`c`', y así sucesivamente.

Si `offset` es proporcionado y es negativo, entonces `strspn` comenzará a analizar el string `string` en la posición `offset` desde el final del string `string`.

`length`  
La longitud del string a analizar.

Si `length` es proporcionado y no es negativo, entonces `string` será examinado sobre `length` caracteres después de la posición de inicio.

Si `length` es proporcionado y es negativo, entonces `string` será examinado sobre `length` caracteres desde el final del string `string`.

## Valores devueltos

Retorna el tamaño del segmento inicial del string `string` que está enteramente constituido de caracteres contenidos en `characters`.

> [!NOTE]
> Cuando el parámetro `offset` está definido, la longitud retornada es contada a partir de esta posición, y no desde el inicio del parámetro `string`.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `length` es ahora nullable. |

## Ejemplos

Ejemplo con `strspn`

```
<?php
// El sujeto no comienza con uno de los caracteres desde la máscara
var_dump(strspn("foo", "o"));

// Examina 2 caracteres desde el inicio del sujeto, en la posición 1
var_dump(strspn("foo", "o", 1, 2));

// Examina un carácter desde el inicio del sujeto, en la posición 1
var_dump(strspn("foo", "o", 1, 1));
?>

    
```php

El ejemplo anterior mostrará:

    int(0)
    int(2)
    int(1)

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`strcspn`
