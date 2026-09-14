---
title: streamWrapper::stream_flush
description: Vuelca la salida
source_url: https://www.php.net/manual/es/streamwrapper.stream-flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 8ba145b34
order: 88430
---

streamWrapper::stream_flush

Vuelca la salida

## Descripción

```php
public streamWrapper::stream_flush(): bool
```php

Este método es llamado en respuesta a `fflush` y cuando el flujo está siendo cerrado mientras cualquier dato no volcado haya sido escrito en él antes.

Si se tiene información en la caché del flujo pero aún no se ha guardado en el almacenamiento subyacente, se debería hacer ahora.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Debería devolver `true` si la información en la caché se almacenó con éxito (o si no había información que almacenar), o `false` si la información podría no estar almacenada.

## Notas

> [!NOTE]
> Si no está implementado, se asume que el valor devuelto es `false`.

## Véase también

`fflush`
