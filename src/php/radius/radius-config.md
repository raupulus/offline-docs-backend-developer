---
title: radius_config
description: Solicita a la biblioteca que lea un archivo de configuración dado
source_url: https://www.php.net/manual/es/function.radius-config.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-config.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67580
---

radius_config

Solicita a la biblioteca que lea un archivo de configuración dado

## Descripción

```php
radius_config(resource $radius_handle, string $file): bool
```php

Antes de cualquier petición Radius, la biblioteca debe conocer el servidor a contactar. La manera sencilla de configurar la biblioteca es llamar a la función `radius_config`. `radius_config` solicita a la biblioteca que lea un archivo de configuración cuyo formato se describe en la página [radius.conf](http://www.freebsd.org/cgi/man.cgi?query=radius.conf).

## Parámetros

`radius_handle`  

`file`  
La ruta hacia el archivo de configuración se pasa como argumento a la función `radius_config`. La biblioteca puede ser configurada también llamando a la función `radius_add_server`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

radius_add_server
