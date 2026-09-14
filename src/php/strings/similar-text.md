---
title: similar_text
description: Calcula la similitud entre dos strings
source_url: https://www.php.net/manual/es/function.similar-text.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/similar-text.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 873f4a3d5
order: 89060
---

similar_text

Calcula la similitud entre dos strings

## Descripción

```php
similar_text(string $string1, string $string2, [float $percent]): int
```php

Calcula la similitud entre los dos strings `string1` y `string2`, según el método descrito en Programming Classics: Implementing the World's Best Algorithms by Oliver (ISBN 0-131-00413-1). Se debe tener en cuenta que esta implementación no utiliza el método de pila como en el pseudocódigo de Oliver, sino llamadas recursivas, lo que puede acelerar o no el proceso. Se debe tener en cuenta que la complejidad del algoritmo es de O(N\*\*3) donde N es el tamaño del string más grande.

## Parámetros

`string1`  
El primer string.

`string2`  
El segundo string.

> [!NOTE]
> Invertir `string1` y `string2` puede producir resultados diferentes; ver el ejemplo a continuación.

`percent`  
Al pasar una referencia como tercer argumento, `similar_text` calculará la similitud en porcentaje, dividiendo el resultado de `similar_text` por la media de la longitud de los strings proporcionados multiplicado por `100`.

## Valores devueltos

Devuelve el número de caracteres coincidentes en los dos strings.

El número de caracteres coincidentes se calcula encontrando la primera subcadena común más larga, y luego haciendo esto para los prefijos y sufijos, de forma recursiva. Las longitudes de todas las subcadenas comunes se suman.

## Ejemplos

Ejemplo de `similar_text` invirtiendo los argumentos

Este ejemplo muestra que invertir los argumentos `string1` y `string2` puede producir resultados diferentes.

```
<?php
$sim = similar_text('bafoobar', 'barfoo', $perc);
echo "similaridad: $sim ($perc %)\n";
$sim = similar_text('barfoo', 'bafoobar', $perc);
echo "similaridad: $sim ($perc %)\n";

   
```php

Resultado del ejemplo anterior es similar a:

    similaridad: 5 (71.428571428571 %)
    similaridad: 3 (42.857142857143 %)

## Véase también

`levenshtein`, `metaphone`, `soundex`
