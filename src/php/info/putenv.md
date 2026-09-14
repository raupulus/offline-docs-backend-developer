---
title: putenv
description: Establece el valor de una variable de entorno
source_url: https://www.php.net/manual/es/function.putenv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/putenv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 39190
---

putenv

Establece el valor de una variable de entorno

## Descripción

```php
putenv(string $assignment): bool
```php

Agrega `setting` al entorno del servidor. La variable de entorno existirá únicamente durante la petición actual. Al final de la petición el entorno es recuperado a su estado original.

## Parámetros

`asignación`  
El parámetro, como p.ej. `"FOO=BAR"`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Definición de una variable de entorno

```
<?php
putenv("UNIQID=$uniqid");
?>

    
```php

## Véase también

`getenv`, `apache_setenv`
