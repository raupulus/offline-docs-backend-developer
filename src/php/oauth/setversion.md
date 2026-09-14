---
title: OAuth::setVersion
description: Configura la versión OAuth
source_url: https://www.php.net/manual/es/oauth.setversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/setversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_revision: bdee7e8c1
order: 56900
---

OAuth::setVersion

Configura la versión OAuth

## Descripción

```php
public OAuth::setVersion(string $version): bool
```php

Establece la versión OAuth para las subsecuentes peticiones

## Parámetros

`version`  
Versión OAuth, el valor por omisión es siempre "1.0"

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
