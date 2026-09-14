---
title: strcasecmp
description: Comparación insensible a mayúsculas/minúsculas de strings binarios
source_url: https://www.php.net/manual/es/function.strcasecmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strcasecmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 9b68bf2b6
order: 89240
---

strcasecmp

Comparación insensible a mayúsculas/minúsculas de strings binarios

## Descripción

```php
strcasecmp(string $string1, string $string2): int
```php

Comparación insensible a mayúsculas/minúsculas de strings binarios. La comparación no tiene en cuenta la configuración regional; solo las letras ASCII se comparan de manera insensible a mayúsculas/minúsculas.

## Parámetros

`string1`  
El primer string.

`string2`  
El segundo string.

## Valores devueltos

Devuelve un valor inferior a 0 si `string1` es inferior a `string2`; un valor superior a 0 si `string1` es superior a `string2`, y `0` si son iguales. No se puede deducir ningún significado particular de este valor, excepto su signo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Esta función ya no garantiza retornar `strlen($string1) - strlen($string2)` cuando las longitudes de las strings no son iguales, y puede retornar `-1` o `1` en su lugar. |

## Ejemplos

Ejemplo con `strcasecmp`

```
<?php
$var1 = "Hello";
$var2 = "hello";
if (strcasecmp($var1, $var2) == 0) {
   echo '$var1 es igual a $var2 (comparación insensible a mayúsculas/minúsculas)';
}
?>

    
```php

## Véase también

`strcmp`, `preg_match`, `substr_compare`, `strncasecmp`, `stristr`, `substr`
