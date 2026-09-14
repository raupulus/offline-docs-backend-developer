---
title: gc_enabled
description: Devuelve el estado del colector de referencia circular
source_url: https://www.php.net/manual/es/function.gc-enabled.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/gc-enabled.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_revision: 3dee475a9
order: 38810
---

gc_enabled

Devuelve el estado del colector de referencia circular

## Descripción

```php
gc_enabled(): bool
```php

Devuelve el estado del colector de referencia circular.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el recolector de basura está activado, `false` en caso contrario.

## Ejemplos

Ejemplo de `gc_enabled`

```
<?php
if(gc_enabled()) gc_collect_cycles();
?>

    
```php

## Véase también

[Recolección de Basura](#features.gc)
