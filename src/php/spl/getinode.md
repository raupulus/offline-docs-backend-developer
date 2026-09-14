---
title: SplFileInfo::getInode
description: Obtiene el i-nodo de el fichero
source_url: https://www.php.net/manual/es/splfileinfo.getinode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getinode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84090
---

SplFileInfo::getInode

Obtiene el i-nodo de el fichero

## Descripción

```php
public SplFileInfo::getInode(): int
```php

Obtiene el número de i-nodo de el objeto filesystem.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de i-nodo de el objeto filesystem en caso de éxito, o `false` en caso de error.

## Errores/Excepciones

Lanza una `RuntimeException` en caso de error.

## Véase también

`fileinode`
