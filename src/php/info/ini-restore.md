---
title: ini_restore
description: Restaura el valor de la opción de configuración
source_url: https://www.php.net/manual/es/function.ini-restore.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/ini-restore.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: ab36e3826
order: 39070
---

ini_restore

Restaura el valor de la opción de configuración

## Descripción

```php
ini_restore(string $option): void
```php

Restaura el valor original de la opción de configuración `varname`.

## Parámetros

`option`  
El nombre de la opción de configuración.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ini_restore`

```
<?php
$setting = 'html_errors';

echo 'Valor actual de \'' . $setting . '\': ' . ini_get($setting), PHP_EOL;

ini_set($setting, ini_get($setting) ? 0 : 1);
echo 'Nuevo valor de \'' . $setting . '\': ' . ini_get($setting), PHP_EOL;

ini_restore($setting);
echo 'Valor original de \'' . $setting . '\': ' . ini_get($setting), PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    Valor actual de 'html_errors': 1
    Nuevo valor de 'html_errors': 0
    Valor original de 'html_errors': 1

## Véase también

`ini_get`, `ini_get_all`, `ini_set`
