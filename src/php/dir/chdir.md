---
title: chdir
description: Cambia de directorio
source_url: https://www.php.net/manual/es/function.chdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/functions/chdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_reviewed: false
translation_revision: dec1f8445
order: 12000
---

chdir

Cambia de directorio

## Descripción

```php
chdir(string $directory): bool
```php

Cambia el directorio actual de PHP a `directorio`.

## Parámetros

`directorio`  
El nuevo directorio actual.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` en caso de error.

## Ejemplos

`chdir` ejemplo

```
<?php

// directorio actual
echo getcwd() . "\n";

chdir('public_html');

// directorio actual
echo getcwd() . "\n";

?>

    
```php

Resultado del ejemplo anterior es similar a:

    /home/vincent
    /home/vincent/public_html

## Notas

> [!CAUTION]
> Si el intérprete de PHP ha sido compilado con ZTS (Seguridad de Hilos Zend) habilitada, cualquier cambio en el directorio actual realizado mediante `chdir` será invisible para el sistema operativo. Todas las funciones integradas de PHP seguirán respetando el cambio en el directorio actual; pero las funciones de bibliotecas externas llamadas mediante [FFI](#book.ffi) no lo harán. Puedes saber si la copia de PHP fue compilada con ZTS habilitada usando `php -i` o la constante incorporada `PHP_ZTS`.

## Véase también

`getcwd`
