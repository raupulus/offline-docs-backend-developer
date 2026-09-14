---
title: xhprof_enable
description: Inicia perfil xhprof
source_url: https://www.php.net/manual/es/function.xhprof-enable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xhprof/functions/xhprof-enable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xhprof
translation_status: ready
translation_reviewed: false
translation_revision: af5f2f87b
order: 102320
---

xhprof_enable

Inicia perfil xhprof

## Descripción

```php
xhprof_enable([int $flags], [array $options]): void
```php

Inicia perfiles xhprof.

## Parámetros

`flags`  
Flags opcionales para añadir información adicional a la creación de perfiles. Véase las [constantes XHprof](#xhprof.constants) Para obtener más información acerca de estos flags, p. ej., `XHPROF_FLAGS_MEMORY` para permitir perfiles de memoria.

`options`  
Un `array` de opciones opcionales, es decir, la opción 'ignored_functions' para pasar en las funciones que se ignoraron durante el perfilado.

## Valores devueltos

`null`

## Historial de cambios

| Versión           | Descripción                                   |
|-------------------|-----------------------------------------------|
| PECL xhprof 0.9.2 | El parámetro opcional `options` fué agregado. |

## Ejemplos

Ejemplos de `xhprof_enable`

```
<?php
// 1. tiempo transcurrido + memoria + perfiles CPU; e ignorar las funciones integradas (internas)
xhprof_enable(XHPROF_FLAGS_NO_BUILTINS | XHPROF_FLAGS_CPU | XHPROF_FLAGS_MEMORY);

// 2. perfil tiempo transcurrido; ignorando call_user_func* durante el perfilado
xhprof_enable(
    0,
    array('ignored_functions' =>  array('call_user_func',
                                        'call_user_func_array')));

// 3. tiempo transcurrido + perfil de memoria; ignorando call_user_func* durante el perfilado
xhprof_enable(
    XHPROF_FLAGS_MEMORY,
    array('ignored_functions' =>  array('call_user_func',
                                        'call_user_func_array')));
?>

   
```php

## Véase también

xhprof_disable

xhprof_sample_enable

memory_get_usage

getrusage
