---
title: get_resource_id
description: Devuelve un entero que identifica un recurso
source_url: https://www.php.net/manual/es/function.get-resource-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/get-resource-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: false
translation_revision: 77887dc8e
order: 100510
---

get_resource_id

Devuelve un entero que identifica un recurso

## Descripción

```php
get_resource_id(resource $resource): int
```php

Esta función proporciona un método seguro para generar un entero que identifica un recurso.

## Parámetros

`resource`  
El gestor del recurso a identificar.

## Valores devueltos

El `int` que identifica el `resource` pasado como argumento.

Esta función es una conversión de tipo de `resource` a un `int` para facilitar la recuperación del ID de un recurso.

## Ejemplos

`get_resource_id` produce el mismo resultado que una conversión a `int`

```
<?php

$handle = fopen("php://stdout", "w");

echo (int) $handle . "\n";

echo get_resource_id($handle);

?>

    
```php

Resultado del ejemplo anterior es similar a:

```
698
698

    
```php

## Véase también

`get_resource_type`
