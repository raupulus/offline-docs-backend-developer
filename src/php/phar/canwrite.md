---
title: Phar::canWrite
description: Determina si la extensión phar soporta la creación y escritura de archivos
  phar
source_url: https://www.php.net/manual/es/phar.canwrite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/canWrite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63940
---

Phar::canWrite

Determina si la extensión phar soporta la creación y escritura de archivos phar

## Descripción

```php
final public static Phar::canWrite(): bool
```php

Este método estático determina si el acceso en escritura ha sido desactivado en el php.ini del sistema mediante la variable INI [phar.readonly](#ini.phar.readonly).

## Parámetros

## Valores devueltos

`true` si el acceso en escritura es posible, `false` en caso contrario.

## Ejemplos

Un ejemplo con `Phar::canWrite`

```
<?php
if (Phar::canWrite()) {
    file_put_contents('phar://monphar.phar/fichero.txt', 'coucou');
}
?>

    
```php

## Véase también

[phar.readonly](#ini.phar.readonly), `Phar::isWritable`
