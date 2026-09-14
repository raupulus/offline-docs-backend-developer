---
title: Ordenación de arrays
source_url: https://www.php.net/manual/es/array.sorting.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/sorting.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: d1df62fe7
order: 6020
---

## Ordenación de arrays

PHP dispone de numerosas funciones para ordenar arrays, y esta sección del manual va a ayudar a comprenderlas.

Las diferencias principales son:

Algunos de los ordenamientos de `array` están basados en las claves, mientras que otros están basados en los valores: `$array['clave'] = 'valor';`, Algunos ordenamientos mantienen la correlación entre las claves y los valores, y otros no, lo que significa que las claves suelen ser reasignadas numéricamente (0,1,2 ...), El orden de la ordenación puede ser: alfabético, ascendente, descendente, numérico, natural, aleatorio, o definido por el usuario., Nota: todas estas funciones de ordenación trabajan sobre el array mismo, a diferencia de la práctica normal que sería devolver el array ordenado., Si una de estas funciones de ordenación evalúa 2 miembros como iguales, entonces conservan el orden original. Anterior a PHP 8.0.0, su orden era indefinido (la ordenación no era estable).

| Nombre de la función | Ordenación por | Asociación clave-valor | Orden de ordenación | Funciones asociadas |
|----|----|----|----|----|
| `array_multisort` | valor | claves `string` sí, claves `int` no | primer array, o bien opciones de ordenación | `array_walk` |
| `asort` | valor | sí | ascendente | `arsort` |
| `arsort` | valor | sí | descendente | `asort` |
| `krsort` | clave | sí | descendente | `ksort` |
| `ksort` | clave | sí | ascendente | `asort` |
| `natcasesort` | valor | sí | natural, insensible a la casilla | `natsort` |
| `natsort` | valor | sí | natural | `natcasesort` |
| `rsort` | valor | no | descendente | `sort` |
| `shuffle` | valor | no | aleatorio | `array_rand` |
| `sort` | valor | no | ascendente | `rsort` |
| `uasort` | valor | sí | Definido por una función de usuario | `uksort` |
| `uksort` | clave | sí | Definido por una función de usuario | `uasort` |
| `usort` | valor | no | Definido por una función de usuario | `uasort` |

Atributos de funciones de ordenación
