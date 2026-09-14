---
title: str_getcsv
description: Analiza una string CSV en un array
source_url: https://www.php.net/manual/es/function.str-getcsv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-getcsv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89130
---

str_getcsv

Analiza una string CSV en un array

## Descripción

```php
str_getcsv(string $string, [string $separator], [string $enclosure], [string $escape]): array
```php

Analiza una cadena de caracteres que representa campos en formato CSV y devuelve un array que contiene todos los campos leídos.

## Parámetros

`string`  
La cadena a analizar.

> [!WARNING]
> Cuando `escape` se define con un valor diferente a una cadena vacía (`""`), puede resultar en un CSV que no sea compatible con [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) o que no pueda sobrevivir a un ciclo de ida y vuelta a través de las funciones CSV de PHP. El valor predeterminado de `escape` es `"\\"`, por lo que se recomienda definirlo explícitamente como cadena vacía. El valor predeterminado cambiará en una futura versión de PHP, no antes de PHP 9.0.

## Valores devueltos

Devuelve un array que contiene los campos leídos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora lanza una ValueError si `separator`, `enclosure`, o `escape` es inválido. Esto imita el comportamiento de `fgetcsv` y `fputcsv`. |
| 7.4.0 | El argumento `escape` interpreta ahora una cadena vacía como señal para desactivar el mecanismo de escape propio. Anteriormente, una cadena vacía era tratada como el valor por defecto del argumento. |

## Ejemplos

Ejemplo con `str_getcsv`

```
<?php

$string = 'PHP,Java,Python,Kotlin,Swift';
$data = str_getcsv($string, escape: '\\');

var_dump($data);
?>

    
```php

El ejemplo anterior mostrará:

    array(5) {
      [0]=>
      string(3) "PHP"
      [1]=>
      string(4) "Java"
      [2]=>
      string(6) "Python"
      [3]=>
      string(6) "Kotlin"
      [4]=>
      string(5) "Swift"
    }

Ejemplo de `str_getcsv` con una cadena vacía

> [!CAUTION]
> Con una cadena vacía, esta función devuelve `[null]` en lugar de un array vacío.

```
<?php

$string = '';
$data = str_getcsv($string, escape: '\\');

var_dump($data);
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      [0]=>
      NULL
    }

## Véase también

`fputcsv`, `fgetcsv`, SplFileObject::fgetcsv, SplFileObject::fputcsv, SplFileObject::setCsvControl, SplFileObject::getCsvControl
