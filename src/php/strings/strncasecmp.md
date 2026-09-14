---
title: strncasecmp
description: Comparación binaria de strings insensible a mayúsculas/minúsculas
source_url: https://www.php.net/manual/es/function.strncasecmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strncasecmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 9b68bf2b6
order: 89370
---

strncasecmp

Comparación binaria de strings insensible a mayúsculas/minúsculas

## Descripción

```php
strncasecmp(string $string1, string $string2, int $length): int
```php

`strncasecmp` es similar a `strcasecmp`, con la diferencia de que permite limitar el número de caracteres utilizados para comparar `string1` y `string2`, mediante el argumento `length`.

## Parámetros

`string1`  
El primer string.

`string2`  
El segundo string.

`length`  
La longitud de los strings a utilizar en la comparación.

## Valores devueltos

Devuelve un valor inferior a 0 si `string1` es inferior a `string2`; un valor superior a 0 si `string1` es superior a `string2`, y `0` si son iguales. No se puede deducir ningún significado particular de este valor, excepto su signo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Esta función ya no garantiza retornar `strlen($string1) - strlen($string2)` cuando las longitudes de las strings no son iguales, y puede retornar `-1` o `1` en su lugar. |

## Ejemplos

Ejemplo con `strncasecmp`

```
<?php

$var1 = 'Hello John';
$var2 = 'hello Doe';
if (strncasecmp($var1, $var2, 5) === 0) {
    echo 'Los 5 primeros caracteres de $var1 y $var2 son iguales en una comparación de strings insensible a mayúsculas/minúsculas.';
}
?>

    
```php

## Véase también

`strncmp`, `preg_match`, `substr_compare`, `strcasecmp`, `stristr`, `substr`
