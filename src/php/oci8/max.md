---
title: OCICollection::max
description: Retorna el número máximo de valores de una colección Oracle
source_url: https://www.php.net/manual/es/ocicollection.max.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocicollection/max.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57760
---

OCICollection::max

Retorna el número máximo de valores de una colección Oracle

## Descripción

```php
public OCICollection::max(): int
```php

Retorna el número máximo de valores de una colección Oracle.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna el número máximo, en forma de `int`, o `false` si ocurre un error.

Si el valor retornado es 0, entonces el número de elementos no está limitado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Collection` ha sido renombrada a `OCICollection` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocicollection.size)
