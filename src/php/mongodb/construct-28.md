---
title: MongoDB\Driver\ServerApi::__construct
description: Crear una nueva instancia de ServerApi
source_url: https://www.php.net/manual/es/mongodb-driver-serverapi.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverapi/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51160
---

MongoDB\Driver\ServerApi::\_\_construct

Crear una nueva instancia de ServerApi

## Descripción

```php
final public MongoDB\Driver\ServerApi::__construct(string $version, [bool $strict], [bool $deprecationErrors])
```php

Crear una nueva instancia de `MongoDB\Driver\ServerApi` utilizada para declarar una versión de API al crear un `MongoDB\Driver\Manager`.

## Parámetros

`version`  
Una versión de API de servidor.

Las versiones de API admitidas se proporcionan como constantes en `MongoDB\Driver\ServerApi`. La única versión de API admitida es `MongoDB\Driver\ServerApi::V1`.

`strict`  
Si el parámetro `strict` se establece en `true`, el servidor devolverá un error para cualquier comando que no forme parte de la versión de API especificada. Si no se proporciona ningún valor, se utiliza el valor predeterminado del servidor (`false`).

`deprecationErrors`  
Si el parámetro `deprecationErrors` se establece en `true`, el servidor devolverá un error al utilizar un comando que está obsoleto en la versión de API especificada. Si no se proporciona ningún valor, se utiliza el valor predeterminado del servidor (`false`).
