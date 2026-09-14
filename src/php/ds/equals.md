---
title: Ds\Hashable::equals
description: Determina si un objeto es igual a la instancia actual
source_url: https://www.php.net/manual/es/ds-hashable.equals.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/hashable/equals.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14790
---

Ds\Hashable::equals

Determina si un objeto es igual a la instancia actual

## Descripción

```php
abstract public Ds\Hashable::equals(object $obj): bool
```php

Determina si otro objeto es igual a la instancia actual.

Este método permite utilizar objetos como claves en estructuras tales como `Ds\Map` y `Ds\Set`, o cualquier otra estructura de búsqueda que respete esta interfaz.

> [!NOTE]
> Se garantiza que `obj` es una instancia de la misma clase.

> [!CAUTION]
> Es importante que los objetos que son iguales tengan también el mismo valor de hash. Ver `Ds\Hashable::hash`.

## Parámetros

`obj`  
El objeto a comparar con la instancia actual, que siempre es una instancia de la misma clase.

## Valores devueltos

`true` si los objetos son iguales, de lo contrario `false`.
