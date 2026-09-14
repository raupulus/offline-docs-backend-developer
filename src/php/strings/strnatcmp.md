---
title: strnatcmp
description: Comparación de strings con el algoritmo de "orden natural"
source_url: https://www.php.net/manual/es/function.strnatcmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strnatcmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89360
---

strnatcmp

Comparación de strings con el algoritmo de "orden natural"

## Descripción

```php
strnatcmp(string $string1, string $string2): int
```php

Implementa el algoritmo de comparación que ordena los strings como lo haría un ser humano. Tenga en cuenta que esta comparación distingue entre mayúsculas y minúsculas.

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

Un ejemplo de la diferencia de tratamiento con el algoritmo estándar se presenta a continuación:

`strcmp`

```
<?php
$arr1 = $arr2 = array("img12.png", "img10.png", "img2.png", "img1.png");
echo "Ordenación de strings estándar\n";
usort($arr1, "strcmp");
print_r($arr1);
echo "\nOrdenación de strings \"orden natural\"\n";
usort($arr2, "strnatcmp");
print_r($arr2);
?>

    
```php

El ejemplo anterior mostrará:

    Ordenación de strings estándar
    Array
    (
        [0] => img1.png
        [1] => img10.png
        [2] => img12.png
        [3] => img2.png
    )

    Ordenación de strings "orden natural"
    Array
    (
        [0] => img1.png
        [1] => img2.png
        [2] => img10.png
        [3] => img12.png
    )

Para más detalles, consulte [`Natural Order String Comparison`](https://github.com/sourcefrog/natsort) de Martin Pool (en inglés).

## Véase también

`preg_match`, `strcasecmp`, `substr`, `stristr`, `strcmp`, `strncmp`, `strncasecmp`, `strnatcasecmp`, `strstr`, `natsort`, `natcasesort`
