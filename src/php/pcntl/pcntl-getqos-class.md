---
title: pcntl_getqos_class
description: Obtiene la clase de calidad de servicio del hilo actual
source_url: https://www.php.net/manual/es/function.pcntl-getqos-class.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-getqos-class.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_revision: 28192e830
order: 61280
---

pcntl_getqos_class

Obtiene la clase de calidad de servicio del hilo actual

## Descripción

```php
pcntl_getqos_class(): Pcntl\QosClass
```php

Recupera la clase de calidad de servicio (QoS) del hilo actual.

> [!NOTE]
> Esta función solo está disponible en plataformas Apple.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la clase QoS actual como un Pcntl\QosClass.

## Errores/Excepciones

Lanza un Error si la llamada subyacente a `pthread_get_qos_class_np()` falla.

## Véase también

pcntl_setqos_class

Pcntl\QosClass
