---
title: Collator::asort
description: Ordena un array manteniendo la asociación de índices
source_url: https://www.php.net/manual/es/collator.asort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/asort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e290572f2
order: 39360
---

Collator::asort

collator_asort

Ordena un array manteniendo la asociación de índices

## Descripción

Estilo orientado a objetos

```php
public Collator::asort(array $array, [int $flags]): bool
```php

Estilo procedimental

```php
collator_asort(Collator $object, array $array, [int $flags]): bool
```

Esta función ordena un array de modo que los índices mantengan su correlación con los elementos del array con los que están asociados. Se usa principalmente al ordenar arrays asociativos donde el orden real de los elementos es significativo. Los elementos del array tendrán un orden de clasificación según las reglas de configuración regional actuales.

Equivalente a la función estándar de PHP `asort`.

## Parámetros

`object`  
Objeto `Collator`.

`array`  
Array de strings a ordenar.

`flags`  
Tipo de ordenación opcional, uno de los siguientes:

- `Collator::SORT_REGULAR` - compara elementos normalmente (no cambia los tipos)

- `Collator::SORT_NUMERIC` - compara elementos numéricamente

- `Collator::SORT_STRING` - compara elementos como strings

El valor por omisión de `flags` es `Collator::SORT_REGULAR`. También se usa si se especifica un valor de `flags` no válido.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `collator_asort`

```php
<?php
$coll = collator_create( 'en_US' );
$arr = array(
     'a' => '100',
     'b' => '50',
     'c' => '7'
);
collator_asort( $coll, $arr, Collator::SORT_NUMERIC );
var_export( $arr );

collator_asort( $coll, $arr, Collator::SORT_STRING );
var_export( $arr );
?>

    
```

El ejemplo anterior mostrará:

    array (
      'c' => '7',
      'b' => '50',
      'a' => '100',
    )array (
      'a' => '100',
      'b' => '50',
      'c' => '7',
    )

## Véase también

[Constantes de Collator](#intl.collator-constants), `collator_sort`, `collator_sort_with_sort_keys`
