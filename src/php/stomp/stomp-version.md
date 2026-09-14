---
title: stomp_version
description: Obtiene la versión actual de la extensión stomp
source_url: https://www.php.net/manual/es/function.stomp-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/functions/stomp-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87500
---

stomp_version

Obtiene la versión actual de la extensión stomp

## Descripción

```php
stomp_version(): string
```php

Devuelve una cadena que contiene la versión actual de la extensión stomp.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta devuelve la versión actual de la extensión stomp

## Ejemplos

Ejemplo de `stomp_version`

```
<?php

var_dump(stomp_version());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(5) "0.2.0"
