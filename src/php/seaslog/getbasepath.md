---
title: SeasLog::getBasePath
description: Devuelve la ruta base de SeasLog
source_url: https://www.php.net/manual/es/seaslog.getbasepath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/getbasepath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73240
---

SeasLog::getBasePath

Devuelve la ruta base de SeasLog

## Descripción

```php
public static Seaslog::getBasePath(): string
```php

Utilizar la función SeasLog::getBasePath para obtener el valor de [seaslog.default_basepath](#ini.seaslog.default-basepath) configurado en php.ini (seaslog.ini).

Si se utiliza Seaslog::setBasePath, el resultado será modificado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve [seaslog.default_basepath](#ini.seaslog.default-basepath) como string.

## Ejemplos

Ejemplo de SeasLog::getBasePath

```
<?php

var_dump(SeasLog::getBasePath());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(12) "/var/log/www"
