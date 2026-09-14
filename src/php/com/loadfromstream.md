---
title: COMPersistHelper::LoadFromStream
description: Carga un objeto desde un stream
source_url: https://www.php.net/manual/es/compersisthelper.loadfromstream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/compersisthelper/loadfromstream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 49ff12041
order: 7590
---

COMPersistHelper::LoadFromStream

Carga un objeto desde un stream

## Descripción

```php
public COMPersistHelper::LoadFromStream(resource $stream): bool
```php

Inicializa un objeto a partir del stream donde fue guardado previamente.

## Parámetros

`stream`  
El stream `resource` desde el cual cargar el objeto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una excepción `com_exception` si el objeto asociado no implementa la interfaz COM IPersistStream, o cuando la llamada al método IPersistStream::Load falla.
