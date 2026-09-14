---
title: zend_version
description: Lee la versión actual del motor Zend
source_url: https://www.php.net/manual/es/function.zend-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/zend-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 017824544
order: 39260
---

zend_version

Lee la versión actual del motor Zend

## Descripción

```php
zend_version(): string
```php

Devuelve una cadena que contiene el número de versión del motor de análisis Zend actualmente en uso.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de versión del motor Zend, en forma de `string`.

## Ejemplos

Ejemplo con `zend_version`

```
<?php
echo "Versión del motor Zend: " . zend_version();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Versión del motor Zend: 2.2.0

## Véase también

`phpinfo`, `phpcredits`, `phpversion`
