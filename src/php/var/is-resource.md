---
title: is_resource
description: Determina si una variable es un recurso
source_url: https://www.php.net/manual/es/function.is-resource.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/is-resource.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 77887dc8e
order: 100690
---

is_resource

Determina si una variable es un recurso

## Descripción

```php
is_resource(mixed $value): bool
```php

Determina si una variable es un `resource`.

## Parámetros

`value`  
La variable a evaluar.

## Valores devueltos

Retorna `true` si `value` es un `resource`, `false` de lo contrario.

## Ejemplos

Ejemplo con `is_resource`

```
<?php

$handle = fopen("php://stdout", "w");
if (is_resource($handle)) {
    echo '$handle es un recurso';
}
?>

    
```php

El ejemplo anterior mostrará:

```
$handle es un recurso

    
```php

## Notas

> [!NOTE]
> La función `is_resource` no es un método de verificación estricta de tipo: retornará `false` si el argumento `value` es un recurso que ha sido cerrado.

## Véase también

[La `documentación` sobre los recursos](#language.types.resource), `get_resource_type`
