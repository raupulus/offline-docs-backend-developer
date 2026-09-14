---
title: Collator::sort
description: Ordena un array usando el comparador especificado
source_url: https://www.php.net/manual/es/collator.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e290572f2
order: 39490
---

Collator::sort

collator_sort

Ordena un array usando el comparador especificado

## Descripción

Estilo orientado a objetos

```php
public Collator::sort(array $array, [int $flags]): bool
```php

Estilo procedimental

```php
collator_sort(Collator $object, array $array, [int $flags]): bool
```

Esta función ordena un array según las reglas de la configuración regional actual.

Equivalente a la función estándar de PHP `sort`.

## Parámetros

`object`  
Objeto `Collator`.

`array`  
Array de strings a ordenar.

`flags`  
Tipo de ordenación opcional, uno de los siguientes:

- `Collator::SORT_REGULAR` - compara los elementos normalmente (no cambia los tipos)

- `Collator::SORT_NUMERIC` - compara los elementos numéricamente

- `Collator::SORT_STRING` - compara los elementos como strings

El tipo de ordenación por omisión es `Collator::SORT_REGULAR`. También se utiliza si se especifica un valor no válido para `flags`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `collator_sort`

```php
<?php
$coll = collator_create( 'en_US' );
$arr  = array( 'at', 'às', 'as' );

var_export( $arr );
collator_sort( $coll, $arr );
var_export( $arr );
?>

    
```

El ejemplo anterior mostrará:

    array (
      0 => 'at',
      1 => 'às',
      2 => 'as',
    )array (
      0 => 'as',
      1 => 'às',
      2 => 'at',
    )

## Véase también

[Constantes de Collator](#intl.collator-constants), `collator_asort`, `collator_sort_with_sort_keys`
