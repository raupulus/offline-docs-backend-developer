---
title: IntlBreakIterator::getPartsIterator
description: Crea un iterador para navegar en los fragmentos entre los límites
source_url: https://www.php.net/manual/es/intlbreakiterator.getpartsiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlbreakiterator/getpartsiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: 0f83ceff0
order: 40100
---

IntlBreakIterator::getPartsIterator

Crea un iterador para navegar en los fragmentos entre los límites

## Descripción

```php
public IntlBreakIterator::getPartsIterator([int $type]): IntlPartsIterator
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`type`  
Tipo de clave (opcional). Los valores posibles son : `IntlPartsIterator::KEY_SEQUENTIAL` - El valor por omisión. Enteros secuencialmente crecientes utilizados como claves., `IntlPartsIterator::KEY_LEFT` - Desplazamiento de octeto a la izquierda de la parte actual utilizada como clave., `IntlPartsIterator::KEY_RIGHT` - Desplazamiento de octeto a la derecha de la parte actual utilizada como clave.

## Valores devueltos
