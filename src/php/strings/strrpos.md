---
title: strrpos
description: Busca la posición de la última ocurrencia de una subcadena en una cadena
source_url: https://www.php.net/manual/es/function.strrpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strrpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 4b72b2351
order: 89440
---

strrpos

Busca la posición de la última ocurrencia de una subcadena en una cadena

## Descripción

```php
strrpos(string $haystack, string $needle, [int $offset]): int
```php

Busca la posición numérica de la última ocurrencia de `needle` en la cadena `haystack`.

## Parámetros

`haystack`  
La cadena en la que buscar.

`needle`  
La cadena a buscar.

Anterior a PHP 8.0.0, si `needle` no es una cadena de caracteres, se convierte en un entero y se aplica como valor ordinal de un carácter. Este comportamiento está obsoleto a partir de PHP 7.3.0, y confiar en él está fuertemente desaconsejado. Dependiendo del comportamiento esperado, `needle` debe ser explícitamente convertido a una cadena de caracteres, o debe realizarse una llamada explícita a `chr`.

`offset`  
Si es cero o positivo, la búsqueda se realiza de izquierda a derecha omitiendo los primeros `offset` bytes de `haystack`.

Si es negativo, la búsqueda comienza a `offset` bytes de la derecha en lugar de desde el inicio de `haystack`. La búsqueda se realiza de derecha a izquierda, buscando la primera ocurrencia de `needle` desde el byte seleccionado.

> [!NOTE]
> Esto es efectivamente equivalente a buscar la última ocurrencia de `needle` en o antes de los últimos `offset` bytes.

## Valores devueltos

Devuelve la posición de la última ocurrencia de `needle` en relación con el inicio de la cadena `haystack` (independientemente de la dirección de búsqueda o del offset).

> [!NOTE]
> Las posiciones de los `string` comienzan en 0, y no en 1.

Devuelve `false` si `needle` no ha sido encontrado.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

- Si `offset` es mayor que la longitud de `haystack`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción                                                     |
|---------|-----------------------------------------------------------------|
| 8.0.0   | `needle` acepta ahora una cadena vacía.                         |
| 8.0.0   | Pasar un `int` como `needle` ya no está soportado.              |
| 7.3.0   | Pasar un `int` como `before_needle` ha sido declarado obsoleto. |

## Ejemplos

Verifica si una ocurrencia es encontrada en una cadena

Es fácil cometer un error con respecto al valor devuelto entre "carácter encontrado en la posición 0" y "carácter no encontrado". A continuación se muestra cómo detectar esta diferencia:

```
<?php
$mystring = 'Elephpant';

$pos = strrpos($mystring, "b");
if ($pos === false) { // nota: 3 signos "="
    // no encontrado...
}

?>

    
```php

Búsqueda con posiciones

```
<?php
$foo = "0123456789a123456789b123456789c";

// Buscar '0' desde el byte 0 (desde el inicio)
var_dump(strrpos($foo, '0', 0));

// Buscar '0' desde el primer byte (después del byte "0")
var_dump(strrpos($foo, '0', 1));

// Buscar '7' desde el byte 21 (después del byte 20)
var_dump(strrpos($foo, '7', 20));

// Buscar '7' desde el byte 29 (después del byte 28)
var_dump(strrpos($foo, '7', 28));

// Buscar '7' de derecha a izquierda desde el quinto byte desde el final
var_dump(strrpos($foo, '7', -5));

// Buscar 'c' de derecha a izquierda desde el segundo byte desde el final
var_dump(strrpos($foo, 'c', -2));

// Buscar '9c' de derecha a izquierda desde el segundo byte desde el final
var_dump(strrpos($foo, '9c', -2));
?>

    
```php

El ejemplo anterior mostrará:

    int(0)
    bool(false)
    int(27)
    bool(false)
    int(17)
    bool(false)
    int(29)

## Véase también

`strpos`, `stripos`, `strripos`, `strrchr`, `substr`
