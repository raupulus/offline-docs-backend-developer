---
title: Collator::sortWithSortKeys
description: Ordenar un array usando el comparador especificado y claves de ordenación
source_url: https://www.php.net/manual/es/collator.sortwithsortkeys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/sort-with-sort-keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e290572f2
order: 39480
---

Collator::sortWithSortKeys

collator_sort_with_sort_keys

Ordenar un array usando el comparador especificado y claves de ordenación

## Descripción

Estilo orientado a objetos

```php
public Collator::sortWithSortKeys(array $array): bool
```php

Estilo procedimental

```php
collator_sort_with_sort_keys(Collator $object, array $array): bool
```

Similar a `collator_sort` pero utiliza claves de ordenación de ICU producidas por ucol_getSortKey() para ganar más velocidad en arrays grandes.

## Parámetros

`object`  
Objeto `Collator`.

`array`  
Array de strings a ordenar

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `collator_sort_with_sort_keys`

```php
<?php
$arr  = array( 'Köpfe', 'Kypper', 'Kopfe' );
$coll = collator_create( 'sv' );

collator_sort_with_sort_keys( $coll, $arr );
var_export( $arr );
?>

    
```

El ejemplo anterior mostrará:

    array (
      0 => 'Kopfe',
      1 => 'Kypper',
      2 => 'Köpfe',
    )

## Véase también

[Constantes de Collator](#intl.collator-constants), `collator_sort`, `collator_asort`
