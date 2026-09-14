---
title: strncmp
description: Comparación binaria de los n primeros caracteres
source_url: https://www.php.net/manual/es/function.strncmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strncmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 9b68bf2b6
order: 89380
---

strncmp

Comparación binaria de los n primeros caracteres

## Descripción

```php
strncmp(string $string1, string $string2, int $length): int
```php

Idéntica a la función `strcmp`, con la diferencia de que se puede especificar el número máximo de caracteres a utilizar para la comparación de `string1` con `string2` mediante el parámetro `length`.

Tenga en cuenta que esta comparación es sensible a mayúsculas y minúsculas.

## Parámetros

`string1`  
El primer string.

`string2`  
El segundo string.

`length`  
Número de caracteres a utilizar para la comparación.

## Valores devueltos

Devuelve un valor inferior a 0 si `string1` es inferior a `string2`; un valor superior a 0 si `string1` es superior a `string2`, y `0` si son iguales. No se puede deducir ningún significado particular de este valor, excepto su signo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Esta función ya no garantiza retornar `strlen($string1) - strlen($string2)` cuando las longitudes de las strings no son iguales, y puede retornar `-1` o `1` en su lugar. |

## Ejemplos

Ejemplo con `strncmp`

```
<?php

$var1 = 'Hello John';
$var2 = 'Hello Doe';
if (strncmp($var1, $var2, 5) === 0) {
    echo 'Los 5 primeros caracteres de $var1 y $var2 son iguales en una comparación de strings sensibles a mayúsculas y minúsculas.';
}
?>

    
```php

## Véase también

`strncasecmp`, `preg_match`, `substr_compare`, `strcmp`, `strstr`, `substr`
