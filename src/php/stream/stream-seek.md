---
title: streamWrapper::stream_seek
description: Coloca el puntero de flujo en una posición
source_url: https://www.php.net/manual/es/streamwrapper.stream-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: cf2b27998
order: 88480
---

streamWrapper::stream_seek

Coloca el puntero de flujo en una posición

## Descripción

```php
public streamWrapper::stream_seek(int $offset, int $whence): bool
```php

Este método es llamado en respuesta a `fseek`.

La posición de lectura/escritura debe ser modificada para reflejar la nueva posición `offset` y `whence`.

## Parámetros

`offset`  
La posición a buscar en el flujo.

`whence`  
Los valores posibles son: `SEEK_SET`: la nueva posición es `offset` bytes., `SEEK_CUR`: la nueva posición es la posición actual más `offset`., `SEEK_END`: la nueva posición es el final del fichero más `offset`.

> [!NOTE]
> La implementación actual nunca define `whence` como `SEEK_CUR`; de hecho, estas búsquedas de posición son convertidas internamente a búsquedas de tipo `SEEK_SET`.

## Valores devueltos

Retorna `true` si la posición ha sido actualizada, `false` en caso contrario.

## Notas

> [!NOTE]
> Si no está implementado, `false` será utilizado como valor de retorno.

> [!NOTE]
> En caso de éxito, streamWrapper::stream_tell es llamado directamente después de streamWrapper::stream_seek. Si streamWrapper::stream_tell falla, el valor retornado a la función llamante es `false`.

> [!NOTE]
> Todas las operaciones de desplazamiento en un flujo no requieren necesariamente el uso de esta función. Los flujos PHP tienen la lectura en búfer activada por omisión (ver también la función `stream_set_read_buffer`) así como el desplazamiento en este flujo, que puede ser realizado moviendo el puntero del búfer.

## Véase también

`fseek`
