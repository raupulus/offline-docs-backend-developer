---
title: get_cfg_var
description: Devuelve el valor de una opción de PHP
source_url: https://www.php.net/manual/es/function.get-cfg-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-cfg-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 38840
---

get_cfg_var

Devuelve el valor de una opción de PHP

## Descripción

```php
get_cfg_var(string $option): string
```php

Devuelve el valor de la opción `option` de configuración de PHP.

`get_cfg_var` no devuelve las opciones que fueron seleccionadas durante la compilación de PHP, ni lee en el archivo de configuración de Apache.

Para verificar si el sistema utiliza el [archivo de configuración](#configuration.file), intente leer el valor de cfg_file_path. Si este valor está disponible, entonces el archivo de configuración se utiliza.

## Parámetros

`option`  
El nombre de la opción de configuración.

## Valores devueltos

Devuelve el valor actual de la opción PHP `option` o bien `false` si ocurre un error.

## Véase también

`ini_get`, `ini_get_all`
