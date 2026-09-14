---
title: COMPersistHelper::SaveToStream
description: Guarda un objeto en un stream
source_url: https://www.php.net/manual/es/compersisthelper.savetostream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/compersisthelper/savetostream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 49ff12041
order: 7610
---

COMPersistHelper::SaveToStream

Guarda un objeto en un stream

## Descripción

```php
public COMPersistHelper::SaveToStream(resource $stream): bool
```php

Guarda un objeto en el stream especificado.

## Parámetros

`stream`  
El stream `resource` en el cual guardar el objeto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una excepción `com_exception` si el objeto asociado no implementa la interfaz COM IPersistStream, y/o la interfaz IPersistStreamInit, o cuando la llamada al método IPersistStream::Save ha fallado.
