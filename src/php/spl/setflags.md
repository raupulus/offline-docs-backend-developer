---
title: ArrayIterator::setFlags
description: Define los flags de comportamientos
source_url: https://www.php.net/manual/es/arrayiterator.setflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/setflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81290
---

ArrayIterator::setFlags

Define los flags de comportamientos

## Descripción

```php
public ArrayIterator::setFlags(int $flags): void
```php

Define los flags que modifican el comportamiento de ArrayIterator.

## Parámetros

`flags`  
El nuevo comportamiento de ArrayIterator. Puede ser un bit-mask o constantes nombradas. Se recomienda encarecidamente el uso de constantes nombradas para asegurar la compatibilidad con futuras versiones.

Los flags de comportamiento disponibles se enumeran a continuación. El comportamiento real de estos flags se describe en las constantes predefinidas [predefined constants](#arrayiterator.constants).

| value | constant |
|----|----|
| 1 | [ArrayIterator::STD_PROP_LIST](#arrayiterator.constants.std-prop-list) |
| 2 | [ArrayIterator::ARRAY_AS_PROPS](#arrayiterator.constants.array-as-props) |

Los flags de comportamiento ArrayIterator

## Valores devueltos

No se retorna ningún valor.

## Véase también

ArrayIterator::getFlags
