---
title: yaz_schema
description: Especifica el esquema para la recuperación
source_url: https://www.php.net/manual/es/function.yaz-schema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-schema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107930
---

yaz_schema

Especifica el esquema para la recuperación

## Descripción

```php
yaz_schema(resource $id, string $schema): void
```php

`yaz_schema` especifica el esquema para la recuperación.

Esta función debe ser llamada antes de `yaz_search` o `yaz_present`.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`schema`  
Debe ser especificado como un OID (identificador de objeto) notación de puntos sin tratar (como `1.2.840.10003.13.4`) o como uno de los esquemas conocidos registrados: `GILS-schema`, `Holdings`, `Zthes`, ...

## Valores devueltos

No se retorna ningún valor.
