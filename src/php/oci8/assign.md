---
title: OCICollection::assign
description: Asigna un valor a una colección desde otra colección Oracle
source_url: https://www.php.net/manual/es/ocicollection.assign.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocicollection/assign.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57720
---

OCICollection::assign

Asigna un valor a una colección desde otra colección Oracle

## Descripción

```php
public OCICollection::assign(OCICollection $from): bool
```php

Asigna un valor a una colección, a partir de la colección `from`. Las dos colecciones deben haber sido creadas con `oci_new_collection` antes de utilizar esta función.

## Parámetros

`from`  
Una instancia OCICollection.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Collection` ha sido renombrada a `OCICollection` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocicollection.append)
