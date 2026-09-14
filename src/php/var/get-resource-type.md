---
title: get_resource_type
description: Devuelve el tipo de recurso
source_url: https://www.php.net/manual/es/function.get-resource-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/get-resource-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: d816a0fad
order: 100520
---

get_resource_type

Devuelve el tipo de recurso

## Descripción

```php
get_resource_type(resource $resource): string
```php

Esta función devuelve el tipo del recurso dado.

## Parámetros

`resource`  
El gestor de recursos a evaluar.

## Valores devueltos

Si el argumento `resource` es un recurso, esta función devolverá un string que representa su tipo. Si el tipo no es identificado por esta función, el valor de retorno será el string `Unknown`.

Esta función devolverá `null` y generará un error si `resource` no es una `resource`.

## Ejemplos

Ejemplo con `get_resource_type`

```
<?php

$fp = fopen("foo", "w");
echo get_resource_type($fp) . "\n";
?>

    
```php

Resultado del ejemplo anterior en PHP 7:

```
stream

    
```php

## Véase también

`get_resource_id`
