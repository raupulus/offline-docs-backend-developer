---
title: OCILob::size
description: Devuelve el tamaño de un LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57960
---

OCILob::size

Devuelve el tamaño de un LOB Oracle

## Descripción

```php
public OCILob::size(): int
```php

Devuelve el tamaño de un LOB Oracle.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tamaño del LOB o `false` si ocurre un error. Los objetos vacíos tienen un tamaño de 0.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |
