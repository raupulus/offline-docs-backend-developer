---
title: streamWrapper::stream_eof
description: Comprueba si un puntero a un archivo está en el final del archivo (EOF)
source_url: https://www.php.net/manual/es/streamwrapper.stream-eof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-eof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 79cdc519d
order: 88420
---

streamWrapper::stream_eof

Comprueba si un puntero a un archivo está en el final del archivo (EOF)

## Descripción

```php
public streamWrapper::stream_eof(): bool
```php

Este método es llamado en respuesta a `feof`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Debería devolver `true` si la posición de lectura/escritura está al final del flujo y no hay más información disponible para leer, o de otro modo `false`.

## Notas

> [!WARNING]
> Al leer un fichero entero (por ejemplo, con `file_get_contents`), PHP llamará a streamWrapper::stream_read seguido de streamWrapper::stream_eof en un bucle, pero siempre y cuando streamWrapper::stream_read devuelva un texto no vacío, el valor que devuelva streamWrapper::stream_eof será ignorado.

## Véase también

`feof`
