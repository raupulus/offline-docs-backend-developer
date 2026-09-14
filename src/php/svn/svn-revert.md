---
title: svn_revert
description: Deshace los cambios en la copia de trabajo
source_url: https://www.php.net/manual/es/function.svn-revert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-revert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_revision: 997700a58
order: 90330
---

svn_revert

Deshace los cambios en la copia de trabajo

## Descripción

```php
svn_revert(string $path, [bool $recursive]): bool
```php

Deshace cualquier cambio local de la ruta en la copia de trabajo.

## Parámetros

`path`  
La ruta del repositorio de trabajo.

`recursive`  
Hacer cambios de forma recursiva, opcional.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

svn_delete

svn_export
