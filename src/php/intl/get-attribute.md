---
title: Collator::getAttribute
description: Obtener el valor de un atributo de ordenación
source_url: https://www.php.net/manual/es/collator.getattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/get-attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e290572f2
order: 39400
---

Collator::getAttribute

collator_get_attribute

Obtener el valor de un atributo de ordenación

## Descripción

Estilo orientado a objetos

```php
public Collator::getAttribute(int $attribute): int
```php

Estilo procedimental

```php
collator_get_attribute(Collator $object, int $attribute): int
```

Obtiene un valor de un atributo entero de ordenación.

## Parámetros

`object`  
Objeto `Collator`.

`attribute`  
Atributo para el cual obtener el valor.

## Valores devueltos

Valor del atributo, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `collator_get_attribute`

```php
<?php
$coll = collator_create( 'en_CA' );
$val = collator_get_attribute( $coll, Collator::NUMERIC_COLLATION );
if( $val === false )
{
    // Manejar error.
}
?>

    
```

## Véase también

[Constantes de Collator](#intl.collator-constants), `collator_set_attribute`, `collator_get_strength`
