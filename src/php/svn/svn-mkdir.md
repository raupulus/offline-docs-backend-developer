---
title: svn_mkdir
description: Crea un directorio en la copia de trabajo actual o repositorio
source_url: https://www.php.net/manual/es/function.svn-mkdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-mkdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_revision: 997700a58
order: 90250
---

svn_mkdir

Crea un directorio en la copia de trabajo actual o repositorio

## Descripción

```php
svn_mkdir(string $path, [string $log_message]): bool
```php

Crea un directorio en la copia de trabajo o repositorio.

## Parámetros

`path`  
La ruta a la copia de trabajo o repositorio.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

svn_add

svn_copy
