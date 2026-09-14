---
title: OCICollection::append
description: Añade un elemento a una colección Oracle
source_url: https://www.php.net/manual/es/ocicollection.append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocicollection/append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57710
---

OCICollection::append

Añade un elemento a una colección Oracle

## Descripción

```php
public OCICollection::append(string $value): bool
```php

Añade un elemento al final de una colección Oracle.

## Parámetros

`value`  
El valor a añadir a la colección.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Collection` ha sido renombrada a `OCICollection` para alinear con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocicollection.assign)
