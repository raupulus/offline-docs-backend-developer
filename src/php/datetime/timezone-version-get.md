---
title: timezone_version_get
description: Lee la versión de la timezonedb
source_url: https://www.php.net/manual/es/function.timezone-version-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/timezone-version-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11440
---

timezone_version_get

Lee la versión de la timezonedb

## Descripción

```php
timezone_version_get(): string
```php

Devuelve la versión actual de la timezonedb.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` en formato `YYYY.increment`, como `2022.2`.

Si se tiene una versión antigua de la base de datos de zonas horarias (por ejemplo, no muestra el año actual), se pueden actualizar las informaciones de zona horaria actualizando la versión de PHP o instalando el paquete PECL [ timezonedb](https://pecl.php.net/package/timezonedb) PECL.

Algunas distribuciones Linux corrigen el soporte de fecha/hora de PHP para usar una fuente alternativa para las informaciones de zona horaria. En este caso, esta función devolverá `0.system`. Asimismo, se recomienda instalar el paquete PECL [timezonedb](https://pecl.php.net/package/timezonedb) en este caso.

## Ejemplos

Lectura de la versión de la timezonedb

```
<?php
echo timezone_version_get();

    
```php

Resultado del ejemplo anterior es similar a:

    2022.2

## Véase también

[Lista de zonas horarias válidas](#timezones)
