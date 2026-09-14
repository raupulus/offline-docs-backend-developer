---
title: Collator::getStrength
description: Obtener la fuerza de ordenación actual
source_url: https://www.php.net/manual/es/collator.getstrength.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/get-strength.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e290572f2
order: 39450
---

Collator::getStrength

collator_get_strength

Obtener la fuerza de ordenación actual

## Descripción

Estilo orientado a objetos

```php
public Collator::getStrength(): int
```php

Estilo procedimental

```php
collator_get_strength(Collator $object): int
```

## Parámetros

`object`  
Objeto `Collator`.

## Valores devueltos

Devuelve la fuerza de ordenación actual, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `collator_get_strength`

```php
<?php
$coll     = collator_create( 'en_US' );
$strength = collator_get_strength( $coll );
?>

    
```

## Véase también

[Constantes de Collator](#intl.collator-constants), `collator_set_strength`, `collator_get_attribute`
