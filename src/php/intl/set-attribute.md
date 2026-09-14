---
title: Collator::setAttribute
description: Establece un atributo de ordenación
source_url: https://www.php.net/manual/es/collator.setattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/set-attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e290572f2
order: 39460
---

Collator::setAttribute

collator_set_attribute

Establece un atributo de ordenación

## Descripción

Estilo orientado a objetos

```php
public Collator::setAttribute(int $attribute, int $value): bool
```php

Estilo procedimental

```php
collator_set_attribute(Collator $object, int $attribute, int $value): bool
```

## Parámetros

`object`  
Objeto `Collator`.

`attribute`  
Atributo.

`value`  
Valor del atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `collator_set_attribute`

```php
<?php
$coll = collator_create('en_CA');
collator_set_attribute($coll, Collator::NORMALIZATION_MODE, Collator::ON);
?>

    
```

## Véase también

[Constantes de Collator](#intl.collator-constants), `collator_get_attribute`, `collator_set_strength`
