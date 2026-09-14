---
title: __autoload
description: Intenta cargar una clase sin definir
source_url: https://www.php.net/manual/es/function.autoload.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/autoload.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: d88a13cd9
order: 6730
---

\_\_autoload

Intenta cargar una clase sin definir

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0 y ha sido *ELIMINADA* a partir de PHP 8.0.0.

## Descripción

```php
__autoload(string $class): void
```php

Puede definir esta función para habilitar la [carga de clases](#language.oop5.autoload).

## Parámetros

`class`  
Nombre de la clase a cargar

## Valores devueltos

No se retorna ningún valor.

## Véase también

`spl_autoload_register`
