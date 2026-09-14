---
title: yaz_range
description: Específica un rango de registros a recuperar
source_url: https://www.php.net/manual/es/function.yaz-range.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-range.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107890
---

yaz_range

Específica un rango de registros a recuperar

## Descripción

```php
yaz_range(resource $id, int $start, int $number): void
```php

Específica un rango de registros a recuperar.

Esta función debería ser llamada antes de `yaz_search` o `yaz_present`.

## Parámetros

`id`  
El recurso de conexión retornado por `yaz_connect`.

`start`  
Especifíca la posición del primer registro a ser recuperado. Los registros numéricos van de 1 a `yaz_hits`.

`number`  
Específica un rango de registros a recuperar.

## Valores devueltos

No se retorna ningún valor.
