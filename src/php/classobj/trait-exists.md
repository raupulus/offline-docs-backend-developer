---
title: trait_exists
description: Verifica si un trait existe
source_url: https://www.php.net/manual/es/function.trait-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/trait-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 42bd1bfed
order: 6920
---

trait_exists

Verifica si un trait existe

## Descripción

```php
trait_exists(string $trait, [bool $autoload]): bool
```php

## Parámetros

`trait`  
Nombre del trait a verificar

`autoload`  
Si debe o no [cargar automáticamente](#language.oop5.autoload) si no ha sido ya cargado.

## Valores devueltos

Retorna `true` si el trait existe, y `false` en caso contrario.
