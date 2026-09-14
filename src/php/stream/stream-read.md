---
title: streamWrapper::stream_read
description: Lee desde el flujo
source_url: https://www.php.net/manual/es/streamwrapper.stream-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 906db3b3f
order: 88470
---

streamWrapper::stream_read

Lee desde el flujo

## Descripción

```php
public streamWrapper::stream_read(int $count): string
```php

Este método es llamado en respuesta a `fread` y `fgets`.

> [!NOTE]
> No olvide modificar la posición de lectura y escritura del número de bytes que han podido ser leídos.

## Parámetros

`count`  
El número de bytes que han podido ser leídos, a partir de la posición actual.

## Valores devueltos

Si hay menos que `count` bytes disponibles, tantos como sea posible deberían ser retornados. Si no hay más datos disponibles, un string vacío debe ser retornado. Para señalar un error de lectura `false` debe ser retornado.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si la llamada a este método falla (i.e. no implementado).

> [!NOTE]
> Si el valor de retorno es mayor que `count`, se emitirá una advertencia `E_WARNING`, y los datos excedentes se perderán.

## Notas

> [!NOTE]
> streamWrapper::stream_eof es llamado directamente después de streamWrapper::stream_read para verificar si se ha alcanzado EOF. Si la función no está implementada, se utilizará EOF.

> [!WARNING]
> Al leer completamente un fichero (por ejemplo, mediante la función `file_get_contents`), PHP llamará a la función streamWrapper::stream_read seguida de la función streamWrapper::stream_eof en un bucle, pero mientras la función streamWrapper::stream_read retorne un string no vacío, el valor retornado de la función streamWrapper::stream_eof será ignorado.

## Véase también

`fread`, `fgets`
