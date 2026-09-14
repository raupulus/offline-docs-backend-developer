---
title: xhprof_sample_enable
description: Iniciar el analisis de XHProf en modo de muestreo
source_url: https://www.php.net/manual/es/function.xhprof-sample-enable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xhprof/functions/xhprof-sample-enable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xhprof
translation_status: ready
translation_revision: 3f0325b86
order: 102340
---

xhprof_sample_enable

Iniciar el analisis de XHProf en modo de muestreo

## Descripción

```php
xhprof_sample_enable(): void
```php

Inicia la creación de perfiles en modo de muestra, que es una versión más ligera de peso de `xhprof_enable` . El intervalo de muestreo es 0,1 segundos, y las muestras de registro de la pila de llamadas de función completa. El caso de uso principal es en gastos indirectos más bajos se requiere cuando se hace la supervisión del rendimiento y de diagnóstico.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`null`

## Véase también

xhprof_sample_disable

xhprof_enable

memory_get_usage

getrusage
