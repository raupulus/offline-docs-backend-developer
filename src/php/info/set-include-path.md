---
title: set_include_path
description: Modifica el valor de la directiva de configuración include_path
source_url: https://www.php.net/manual/es/function.set-include-path.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/set-include-path.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 39210
---

set_include_path

Modifica el valor de la directiva de configuración include_path

## Descripción

```php
set_include_path(string $include_path): string
```php

Modifica el valor de la directiva de configuración [include_path](#ini.include-path), durante la ejecución del script en curso.

## Parámetros

`include_path`  
El nuevo valor para la directiva de configuración [include_path](#ini.include-path)

## Valores devueltos

Devuelve el valor anterior de [include_path](#ini.include-path) en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `set_include_path`

```
<?php
set_include_path('/usr/lib/pear');

// O usar ini_set()
ini_set('include_path', '/usr/lib/pear');
?>

    
```php

Añadir al camino de inclusión

Usando la constante `PATH_SEPARATOR`, es posible extender el camino de inclusión según el sistema.

En este ejemplo, se añade `/usr/lib/pear` al final del actual `include_path`.

```
<?php
$path = '/usr/lib/pear';
set_include_path(get_include_path() . PATH_SEPARATOR . $path);
?>

    
```php

## Véase también

`ini_set`, `get_include_path`, `restore_include_path`, `include`
