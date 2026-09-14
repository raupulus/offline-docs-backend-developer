---
title: SessionHandlerInterface::open
description: Inicializar una sesión
source_url: https://www.php.net/manual/es/sessionhandlerinterface.open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandlerinterface/open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 601f6f4ce
order: 74070
---

SessionHandlerInterface::open

Inicializar una sesión

## Descripción

```php
public SessionHandlerInterface::open(string $path, string $name): bool
```php

Reinicializa una sesión existente, o crea una nueva. Llamado cuando una sesión se inicia o cuando se invoca a `session_start`.

## Parámetros

`path`  
La ruta donde almacenar/recuperar la sesión.

`name`  
El nombre de la sesión.

## Valores devueltos

El valor devuelto (habitualmente `true` en caso de éxito, `false` si ocurre un error). Tenga en cuenta que este valor es devuelto internamente a PHP para análisis.

## Véase también

`session_name`, La directiva de configuración [session.auto-start](#ini.session.auto-start).
