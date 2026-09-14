---
title: SessionIdInterface::create_sid
description: Crear un ID de sesión
source_url: https://www.php.net/manual/es/sessionidinterface.create-sid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionidinterface/create-sid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 601f6f4ce
order: 74110
---

SessionIdInterface::create_sid

Crear un ID de sesión

## Descripción

```php
public SessionIdInterface::create_sid(): string
```php

Crea un nuevo ID de sesión. Esta función se ejecuta automáticamente cuando debe crearse un nuevo ID de sesión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nuevo ID de sesión. Cabe señalar que este valor se devuelve internamente a PHP para su procesamiento.

## Véase también

SessionHandler::create_sid
