---
title: yaz_syntax
description: Especifica la sintaxis de registro preferida para la recuperación
source_url: https://www.php.net/manual/es/function.yaz-syntax.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-syntax.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107970
---

yaz_syntax

Especifica la sintaxis de registro preferida para la recuperación

## Descripción

```php
yaz_syntax(resource $id, string $syntax): void
```php

`yaz_syntax` especifica la sintaxis de registro preferida para la recuperación

Esta función debe ser llamada antes de `yaz_search` o `yaz_present`.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`syntax`  
La sintaxis debe especificarse como un OID (identificador de objeto) en una notación de puntos sin tratar (como `1.2.840.10003.5.10`) o como una de las sintaxis conocidas (sutrs, usmarc, grs1, xml, etc.).

## Valores devueltos

No se retorna ningún valor.
