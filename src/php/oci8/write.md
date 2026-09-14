---
title: OCILob::write
description: Escribe datos en un LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57990
---

OCILob::write

Escribe datos en un LOB Oracle

## Descripción

```php
public OCILob::write(string $data, [int $length]): int
```php

Escribe los datos de la variable `data` en la posición actual del LOB.

## Parámetros

`data`  
Los datos a escribir en el LOB.

`length`  
Si este argumento es un entero, la escritura se detendrá después de `length` bytes, o al final de la variable `data`.

## Valores devueltos

Devuelve el número de bytes escritos o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | `length` ahora es nullable. |
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.read)
