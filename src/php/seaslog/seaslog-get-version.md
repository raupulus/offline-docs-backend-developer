---
title: seaslog_get_version
description: Devuelve la versión de SeasLog.
source_url: https://www.php.net/manual/es/function.seaslog-get-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/functions/seaslog-get-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73110
---

seaslog_get_version

Devuelve la versión de SeasLog.

## Descripción

```php
seaslog_get_version(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la versión de SeasLog (SEASLOG_VERSION) como string.

## Ejemplos

Ejemplo de `seaslog_get_version`

```
<?php

var_dump(seaslog_get_version());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(5) "1.8.4"
