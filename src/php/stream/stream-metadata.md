---
title: streamWrapper::stream_metadata
description: Cambiar los metadatos del flujo
source_url: https://www.php.net/manual/es/streamwrapper.stream-metadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/streamwrapper/stream-metadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 86e6094e8
order: 88450
---

streamWrapper::stream_metadata

Cambiar los metadatos del flujo

## Descripción

```php
public streamWrapper::stream_metadata(string $path, int $option, mixed $value): bool
```php

Este método es llamado para establecer metadatos en el flujo. Se invoca cuando una de las siguientes funciones es llamada sobre un URL de flujo: `touch`, `chmod`, `chown`, `chgrp` Observe que algunas de estas operaciones pueden no estar disponibles en su sistema.

## Parámetros

`path`  
La ruta del fichero o el URL a establecer los metadatos. Observe que en caso de ser un URL, debe ser un URL delimitado por ://. No se admiten otros formatos de URL.

`option`  
Una de las siguientes opciones: `STREAM_META_TOUCH` (El método fue llamado en respuesta a `touch`), `STREAM_META_OWNER_NAME` (El método fue llamado en respuesta a `chown` con parámetro de tipo string), `STREAM_META_OWNER` (El método fue llamado en respuesta a `chown`), `STREAM_META_GROUP_NAME` (El método fue llamado en respuesta a `chgrp`), `STREAM_META_GROUP` (El método fue llamado en respuesta a `chgrp`), `STREAM_META_ACCESS` (El método fue llamado en respuesta a `chmod`)

`value`  
Si el parámetro `option` es `STREAM_META_TOUCH`: `Array` que consiste en dos argumentos de la función `touch`., `STREAM_META_OWNER_NAME` o `STREAM_META_GROUP_NAME`: El nombre del usuario/grupo propietario como `string`., `STREAM_META_OWNER` o `STREAM_META_GROUP`: El valor del argumento del usuario/grupo propietario como `int`., `STREAM_META_ACCESS`: El argumento de la función `chmod` como `int`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si `option` no se implementa, debería devolver `false`.

## Véase también

`touch`, `chmod`, `chown`, `chgrp`
