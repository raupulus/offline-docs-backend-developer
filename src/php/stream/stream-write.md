---
title: streamWrapper::stream_write
description: Escribir en un flujo
source_url: https://www.php.net/manual/es/streamwrapper.stream-write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: af4410a7e
order: 88530
---

streamWrapper::stream_write

Escribir en un flujo

## Descripción

```php
public streamWrapper::stream_write(string $data): int
```php

Este método es llamado en respuesta a `fwrite`.

> [!NOTE]
> Recuerde actualizar la posición actual del flujo por el número de bytes que fueron escritos con éxito.

## Parámetros

`data`  
Esta información debería ser almacenada en el flujo subyacente.

> [!NOTE]
> Si no hay espacio suficiente en el flujo subyacente, guardar lo más posible.

## Valores devueltos

Debería devolver el número de bytes que fueron almacenados con éxito, o 0 si no se puede almacenar nada.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

> [!NOTE]
> Si el valor devuelto es mayor que la longitud de `data`, se emitirá un `E_WARNING` y el valor devuelto será truncado a su longitud.

## Véase también

`fwrite`
