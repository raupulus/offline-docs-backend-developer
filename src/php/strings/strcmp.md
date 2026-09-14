---
title: strcmp
description: Comparación binaria de strings
source_url: https://www.php.net/manual/es/function.strcmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strcmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 873f4a3d5
order: 89260
---

strcmp

Comparación binaria de strings

## Descripción

```php
strcmp(string $string1, string $string2): int
```php

Se debe tener en cuenta que esta comparación distingue entre mayúsculas y minúsculas. Para una comparación que no distinga entre mayúsculas y minúsculas, vea `strcasecmp`.

Se debe tener en cuenta que esta comparación no tiene en cuenta la configuración regional. Para una comparación con la configuración regional, vea `strcoll` o Collator::compare

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

Ejemplo de uso de `strcmp`

```
<?php
$var1 = "Bonjour";
$var2 = "bonjour";
if (strcmp($var1, $var2) !== 0) {
    echo "$var1 no es igual a $var2 en una comparación sensible a mayúsculas y minúsculas.";
}
?>

    
```php

## Véase también

- Comparación completa de string

  strcasecmp
  Collator::compare
  strcoll

- Comparación parcial de string

  substr_compare
  strncmp
  strstr

- Comparación similar / otra de string

  preg_match
  levenshtein
  metaphone
  similar_text
  soundex
