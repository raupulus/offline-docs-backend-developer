---
title: strripos
description: Busca la posición de la última ocurrencia de un string contenido en otro,
  de forma insensible a mayúsculas y minúsculas
source_url: https://www.php.net/manual/es/function.strripos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strripos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 95d055464
order: 89430
---

strripos

Busca la posición de la última ocurrencia de un string contenido en otro, de forma insensible a mayúsculas y minúsculas

## Descripción

```php
strripos(string $haystack, string $needle, [int $offset]): int
```php

Busca la posición numérica de la última ocurrencia de `needle` en el string `haystack`.

A diferencia de la función `strrpos`, `strripos` es insensible a mayúsculas y minúsculas.

## Parámetros

`haystack`  
El string en el que se debe buscar.

`needle`  
El string a buscar.

Anterior a PHP 8.0.0, si `needle` no es una cadena de caracteres, se convierte en un entero y se aplica como valor ordinal de un carácter. Este comportamiento está obsoleto a partir de PHP 7.3.0, y confiar en él está fuertemente desaconsejado. Dependiendo del comportamiento esperado, `needle` debe ser explícitamente convertido a una cadena de caracteres, o debe realizarse una llamada explícita a `chr`.

`offset`  
Si es cero o positivo, la búsqueda se realiza de izquierda a derecha omitiendo los primeros `offset` bytes de `haystack`.

Si es negativo, la búsqueda se realiza de derecha a izquierda omitiendo los últimos `offset` bytes de `haystack` y buscando la primera ocurrencia de `needle`.

> [!NOTE]
> Esto es efectivamente buscar la última ocurrencia de `needle` antes de los últimos `offset` bytes.

## Valores devueltos

Devuelve la posición donde existe `needle` en relación con el comienzo del string `haystack` (independientemente de la dirección de búsqueda o `offset`).

> [!NOTE]
> Las posiciones de los `string` comienzan en 0, y no en 1.

Devuelve `false` si `needle` no ha sido encontrado.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

- Si `offset` es mayor que la longitud de `haystack`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El case folding ya no depende de la configuración local definida con `setlocale`. Solo se realizará el case folding ASCII. Los octetos no-ASCII serán comparados por su valor de octeto. |
| 8.0.0 | `needle` acepta ahora una cadena vacía. |
| 8.0.0 | Pasar un `int` como `needle` ya no está soportado. |
| 7.3.0 | Pasar un `int` como `before_needle` ha sido declarado obsoleto. |

## Ejemplos

Ejemplo con `strripos`

```
<?php

$haystack = 'ababcd';
$needle   = 'aB';

$pos      = strripos($haystack, $needle);

if ($pos === false) {
    echo "Lo sentimos, no se pudo encontrar `$needle` en `$haystack`";
} else {
    echo "¡Felicidades!\n";
    echo "Hemos encontrado el último `$needle` en `$haystack` en la posición `$pos`";
}

?>

    
```php

El ejemplo anterior mostrará:

    ¡Felicidades!
    Hemos encontrado el último `aB` en `ababcd` en la posición `2`

## Véase también

`strpos`, `stripos`, `strrpos`, `strrchr`, `stristr`, `substr`
