---
title: Phar::getVersion
description: Devuelve las informaciones de versión del archivo Phar
source_url: https://www.php.net/manual/es/phar.getversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/getVersion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64170
---

Phar::getVersion

Devuelve las informaciones de versión del archivo Phar

## Descripción

```php
public Phar::getVersion(): string
```php

Devuelve la versión de la API de un archivo Phar abierto.

## Parámetros

## Valores devueltos

La versión de la API del archivo abierto. No debe confundirse con la versión de API que la extensión phar cargada utilizará para crear nuevos archivos phar. Cada archivo Phar tiene la versión de API codificada de forma fija en su manifiesto. Para más información, consulte [el formato de archivo Phar](#phar.fileformat).

## Véase también

`Phar::apiVersion`
