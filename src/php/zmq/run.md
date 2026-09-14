---
title: ZMQDevice::run
description: Ejecutar el nuevo dispositivo
source_url: https://www.php.net/manual/es/zmqdevice.run.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zmq/zmqdevice/run.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zmq
translation_status: ready
translation_reviewed: false
translation_revision: ab5614596
order: 109180
---

ZMQDevice::run

Ejecutar el nuevo dispositivo

## Descripción

```php
public ZMQDevice::run(): void
```php

Ejecuta el dispositivo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una llamada a este método hará que quede en espera hasta que el dispositivo esté en ejecución. No se recomienda que los dispositivos se utilicen desde script interactivos. En caso de fallo, este método lanzará una ZMQDeviceException.
