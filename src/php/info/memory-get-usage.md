---
title: memory_get_usage
description: Indica la cantidad de memoria utilizada por PHP
source_url: https://www.php.net/manual/es/function.memory-get-usage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/memory-get-usage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 9af43469f
order: 39100
---

memory_get_usage

Indica la cantidad de memoria utilizada por PHP

## Descripción

```php
memory_get_usage([bool $real_usage]): int
```php

Devuelve la cantidad de memoria asignada a PHP en este momento.

## Parámetros

`real_usage`  
Definir como `true` para obtener el tamaño total de la memoria asignada por el sistema. Si este argumento no está definido o es `false`, solo se retornará la memoria utilizada.

> [!NOTE]
> PHP solo puede rastrear la memoria asignada por `emalloc()`

## Valores devueltos

Devuelve la cantidad de memoria, en bytes.

## Ejemplos

Ejemplo con `memory_get_usage`

```
<?php
// Esto es solo un ejemplo. Los números a continuación
// variarán según los sistemas y las configuraciones

echo memory_get_usage() . "\n"; // 36640

$a = str_repeat("Hello", 4242);

echo memory_get_usage() . "\n"; // 57960

unset($a);

echo memory_get_usage() . "\n"; // 36744

?>

    
```php

## Véase también

`memory_get_peak_usage`, [memory_limit](#ini.memory-limit)
