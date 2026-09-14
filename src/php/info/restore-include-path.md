---
title: restore_include_path
description: Restaura el valor de la directiva de configuración include_path
source_url: https://www.php.net/manual/es/function.restore-include-path.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/restore-include-path.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: f112cc1ec
order: 39200
---

restore_include_path

Restaura el valor de la directiva de configuración include_path

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
restore_include_path(): void
```php

Restaura el valor de la directiva de configuración [include_path](#ini.include-path) a su valor original al inicio del script, tal como se indica en el `php.ini`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | Esta función ha sido eliminada. |
| 7.4.0   | Esta función está obsoleta.     |

## Ejemplos

Ejemplo con `restore_include_path`

```
<?php

echo get_include_path();  // .:/usr/local/lib/php

set_include_path('/inc');

echo get_include_path();  // /inc

restore_include_path();

// O usar ini_restore()
ini_restore('include_path');

echo get_include_path();  // .:/usr/local/lib/php

?>

    
```php

## Véase también

`ini_restore`, `get_include_path`, `set_include_path`, `include`
