---
title: dba_key_split
description: Transforma una representación de clave DBA por cadena en una representación
  por array
source_url: https://www.php.net/manual/es/function.dba-key-split.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-key-split.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11590
---

dba_key_split

Transforma una representación de clave DBA por cadena en una representación por array

## Descripción

```php
dba_key_split(string $key): array
```php

`dba_key_split` transforma una representación de clave DBA por cadena en una representación por array.

## Parámetros

`key`  
La clave en forma de string.

## Valores devueltos

Devuelve un array en la forma `array(0 => grupo, 1 => nombre_valor)`. Esta función devuelve `false` si `key` es `null` o `false`.

## Historial de cambios

| Versión | Descripción                                          |
|---------|------------------------------------------------------|
| 8.4.0   | Pasar `null` o `false` a `key` está ahora deprecado. |

## Véase también

dba_firstkey

dba_nextkey

dba_fetch
