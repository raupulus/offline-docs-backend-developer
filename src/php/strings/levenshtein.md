---
title: levenshtein
description: Calcula la distancia Levenshtein entre dos strings
source_url: https://www.php.net/manual/es/function.levenshtein.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/levenshtein.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 873f4a3d5
order: 88850
---

levenshtein

Calcula la distancia Levenshtein entre dos strings

## Descripción

```php
levenshtein(string $string1, string $string2, [int $insertion_cost], [int $replacement_cost], [int $deletion_cost]): int
```php

La distancia Levenshtein se define como el número mínimo de caracteres que deben ser reemplazados, insertados o eliminados para transformar el string `string1` en `string2`. La complejidad del algoritmo es de `O(m*n)`, donde `n` y `m` son los tamaños respectivos de `string1` y `string2`: es bastante buena, en comparación con `similar_text`, que es de `O(max(n,m)**3)`, pero sigue siendo muy costosa.

Si `insertion_cost`, `replacement_cost` y/o `deletion_cost` son diferentes de `1`, el algoritmo se adapta para elegir la transformación menos costosa. Por ejemplo, si `$insertion_cost + $deletion_cost < $replacement_cost`, no se realizará ningún reemplazo, sino inserciones y eliminaciones.

## Parámetros

`string1`  
Uno de los strings a evaluar.

`string2`  
Uno de los strings a evaluar.

`insertion_cost`  
Define el costo de la inserción.

`replacement_cost`  
Define el costo del reemplazo.

`deletion_cost`  
Define el costo de la eliminación.

## Valores devueltos

Esta función devuelve la distancia Levenshtein entre dos strings.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Antes de esta versión, `levenshtein` debía ser llamada con dos o cinco argumentos. |
| 8.0.0 | Antes de esta versión, `levenshtein` devolvía `-1` si alguno de los strings de los argumentos superaba los 255 caracteres. |

## Ejemplos

Ejemplo con `levenshtein`

```
<?php
// palabra mal escrita
$input = 'carrrot';

// array de palabras a verificar
$words  = array('apple','pineapple','banana','orange',
                'radish','carrot','pea','bean','potato');

// ninguna distancia encontrada por el momento
$shortest = -1;

// bucle sobre las palabras para encontrar la más cercana
foreach ($words as $word) {

    // calcula la distancia con la palabra ingresada,
    // y la palabra actual
    $lev = levenshtein($input, $word);

    // busca una coincidencia exacta
    if ($lev == 0) {

        // la palabra más cercana es esta (coincidencia exacta)
        $closest = $word;
        $shortest = 0;

        // se sale del bucle; se ha encontrado una coincidencia exacta
        break;
    }

    // Si la distancia es más pequeña que la siguiente distancia encontrada
    // O, si la siguiente palabra más cercana aún no ha sido encontrada
    if ($lev <= $shortest || $shortest < 0) {
        // definición de la palabra más cercana y la distancia
        $closest  = $word;
        $shortest = $lev;
    }
}

echo "Palabra ingresada: $input\n";
if ($shortest == 0) {
    echo "Coincidencia exacta encontrada: $closest\n";
} else {
    echo "¿Quiso decir: $closest?\n";
}

?>

    
```php

El ejemplo anterior mostrará:

    Palabra ingresada: carrrot
    ¿Quiso decir: carrot?

## Véase también

`soundex`, `similar_text`, `metaphone`
