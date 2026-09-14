---
title: OCILob::writeTemporary
description: Escribe un LOB Oracle temporal
source_url: https://www.php.net/manual/es/ocilob.writetemporary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/writeTemporary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 58000
---

OCILob::writeTemporary

Escribe un LOB Oracle temporal

## Descripción

```php
public OCILob::writeTemporary(string $data, [int $type]): bool
```php

Crea un LOB temporal y escribe los datos `data` en él.

Se debe utilizar la función [???](#ocilob.close) cuando se ha terminado de trabajar con el LOB.

## Parámetros

`data`  
Los datos a escribir.

`type`  
Puede tomar uno de los siguientes valores: `OCI_TEMP_BLOB` se utiliza para crear un BLOB temporal., `OCI_TEMP_CLOB` se utiliza para crear un CLOB temporal.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.close)
