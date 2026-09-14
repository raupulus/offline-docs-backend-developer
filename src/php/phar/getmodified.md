---
title: Phar::getModified
description: Indica si el archivo phar ha sido modificado
source_url: https://www.php.net/manual/es/phar.getmodified.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/getModified.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64110
---

Phar::getModified

Indica si el archivo phar ha sido modificado

## Descripción

```php
public Phar::getModified(): bool
```php

Determina si un archivo phar ha tenido algún fichero interno eliminado o si el contenido de un fichero ha cambiado de alguna manera.

## Parámetros

No se admiten argumentos.

## Valores devueltos

`true` si el phar ha sido modificado desde su apertura, `false` en caso contrario.
