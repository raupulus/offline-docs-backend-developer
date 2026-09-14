---
title: OCILob::load
description: Devuelve el contenido de un LOB
source_url: https://www.php.net/manual/es/ocilob.load.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/load.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57890
---

OCILob::load

Devuelve el contenido de un LOB

## Descripción

```php
public OCILob::load(): string
```php

Lee el contenido de un LOB Oracle. El script puede ser interrumpido debido a [memory_limit](#ini.memory-limit), si este último excede el límite. En la mayoría de los casos, se recomienda utilizar la función [???](#ocilob.read) en su lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido del objeto, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.read)
