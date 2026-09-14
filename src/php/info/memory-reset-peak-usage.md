---
title: memory_reset_peak_usage
description: Reinicia el uso máximo de memoria
source_url: https://www.php.net/manual/es/function.memory-reset-peak-usage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/memory-reset-peak-usage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 57015edfe
order: 39110
---

memory_reset_peak_usage

Reinicia el uso máximo de memoria

## Descripción

```php
memory_reset_peak_usage(): void
```php

Reinicia el uso máximo de memoria devuelto por la función `memory_get_peak_usage`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `memory_reset_peak_usage`

```
<?php

var_dump(memory_get_peak_usage());

$a = str_repeat("Hello", 424242);
var_dump(memory_get_peak_usage());

unset($a);
memory_reset_peak_usage();

$a = str_repeat("Hello", 2424);
var_dump(memory_get_peak_usage());

?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(422440)
    int(2508672)
    int(399208)

## Véase también

`memory_get_peak_usage`
