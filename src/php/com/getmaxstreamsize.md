---
title: COMPersistHelper::GetMaxStreamSize
description: Devuelve el tamaño máximo del stream
source_url: https://www.php.net/manual/es/compersisthelper.getmaxstreamsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/compersisthelper/getmaxstreamsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 49ff12041
order: 7560
---

COMPersistHelper::GetMaxStreamSize

Devuelve el tamaño máximo del stream

## Descripción

```php
public COMPersistHelper::GetMaxStreamSize(): int
```php

Devuelve el tamaño del stream (en bytes) necesario para guardar el objeto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tamaño del stream (en bytes) necesario para guardar el objeto.

## Errores/Excepciones

Se lanza una excepción `com_exception` si el objeto asociado no implementa la interfaz COM IPersistStream ni IPersistStreamInit, o cuando la llamada al método IPersistStream::GetSizeMax ha fallado.
