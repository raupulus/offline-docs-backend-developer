---
title: OCICollection::assignElem
description: Asigna un valor a un elemento de una colección Oracle
source_url: https://www.php.net/manual/es/ocicollection.assignelem.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocicollection/assignElem.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57730
---

OCICollection::assignElem

Asigna un valor a un elemento de una colección Oracle

## Descripción

```php
public OCICollection::assignElem(int $index, string $value): bool
```php

Asigna un valor al elemento cuyo índice es `index`.

## Parámetros

`index`  
El índice del elemento. El primero vale 0.

`value`  
Puede ser una `string` o un número.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Collection` ha sido renombrada a `OCICollection` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocicollection.getelem)
