---
title: SplFileInfo::getFileInfo
description: Obtiene un objeto SplFileInfo para el fichero
source_url: https://www.php.net/manual/es/splfileinfo.getfileinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getfileinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84060
---

SplFileInfo::getFileInfo

Obtiene un objeto SplFileInfo para el fichero

## Descripción

```php
public SplFileInfo::getFileInfo([string $class]): SplFileInfo
```php

Este método obtiene un objeto `SplFileInfo` para el fichero de referencia.

## Parámetros

`class`  
Nombre de una clase `SplFileInfo` derivada de su uso.

## Valores devueltos

Un objeto `SplFileInfo` creado para el fichero.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `class` es ahora anulable. |

## Véase también

SplFileInfo::setInfoClass
