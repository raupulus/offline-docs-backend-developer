---
title: COMPersistHelper::InitNew
description: Inicializa un objeto en un estado por omisión
source_url: https://www.php.net/manual/es/compersisthelper.initnew.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/compersisthelper/initnew.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 49ff12041
order: 7570
---

COMPersistHelper::InitNew

Inicializa un objeto en un estado por omisión

## Descripción

```php
public COMPersistHelper::InitNew(): bool
```php

Inicializa un objeto en un estado por omisión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una excepción `com_exception` si el objeto asociado no implementa la interfaz COM IPersistStreamInit, o cuando la llamada al método IPersistStreamInit::Init ha fallado.
