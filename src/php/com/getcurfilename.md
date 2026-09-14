---
title: COMPersistHelper::GetCurFileName
description: Devuelve el nombre del fichero actual
source_url: https://www.php.net/manual/es/compersisthelper.getcurfilename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/compersisthelper/getcurfilename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 49ff12041
order: 7550
---

COMPersistHelper::GetCurFileName

Devuelve el nombre del fichero actual

## Descripción

```php
public COMPersistHelper::GetCurFileName(): string
```php

Devuelve el nombre del fichero actual asociado al objeto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del fichero actual asociado al objeto.

## Errores/Excepciones

Se lanza una excepción `com_exception` si el objeto asociado no implementa la interfaz COM IPersistFile, o cuando la llamada al método IPersistFile::GetCurFile ha fallado.
