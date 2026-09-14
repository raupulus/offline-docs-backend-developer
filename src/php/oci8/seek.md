---
title: OCILob::seek
description: Desplaza el puntero interno de un LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57940
---

OCILob::seek

Desplaza el puntero interno de un LOB Oracle

## Descripción

```php
public OCILob::seek(int $offset, [int $whence]): bool
```php

Desplaza el puntero interno de un LOB Oracle.

## Parámetros

`offset`  
Indica la distancia de desplazamiento. El tipo de desplazamiento se especifica con `whence`.

`whence`  
Puede ser una constante entre: `OCI_SEEK_SET` - desplaza el puntero a la posición `offset`., `OCI_SEEK_CUR` - añade `offset` bytes a la posición actual., `OCI_SEEK_END` - añade `offset` bytes al final del LOB (utilice un valor negativo para obtener una posición antes del final del LOB).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinear con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.rewind), [???](#ocilob.tell), [???](#ocilob.eof)
