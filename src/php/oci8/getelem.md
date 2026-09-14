---
title: OCICollection::getElem
description: Devuelve el valor de un elemento de una colección Oracle
source_url: https://www.php.net/manual/es/ocicollection.getelem.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocicollection/getElem.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57750
---

OCICollection::getElem

Devuelve el valor de un elemento de una colección Oracle

## Descripción

```php
public OCICollection::getElem(int $index): string
```php

Devuelve el valor del elemento en el índice `index` (comenzando en 0).

## Parámetros

`index`  
El índice del elemento. El primero vale 1.

## Valores devueltos

Devuelve `false` si este elemento no existe; `null`, si el elemento es `null`, un string si la columna es de tipo string, y un número si es un campo numérico.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Collection` ha sido renombrada a `OCICollection` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocicollection.assignelem)
