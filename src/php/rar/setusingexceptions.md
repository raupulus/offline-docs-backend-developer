---
title: RarException::setUsingExceptions
description: Activar y desactivar el manejador de errores con excepciones
source_url: https://www.php.net/manual/es/rarexception.setusingexceptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarexception/setusingexceptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68660
---

RarException::setUsingExceptions

Activar y desactivar el manejador de errores con excepciones

## Descripción

```php
public static RarException::setUsingExceptions(bool $using_exceptions): void
```php

Si y sólo si el argumento es `true`, entonces, en lugar de emitir advertencias y devolver un valor especial indicando error cuando la biblioteca UnRAR encuentre un error, una excepción de tipo `RarException` será lanzada.

Las excepciones también será lanzado para los siguientes errores, que se producen fuera de la biblioteca (su código de error será -1):

- intentar algunas operaciones en un objeto `RarArchive` cerrado o un objeto `RarEntry` relativo al primero;

- intentar obtener una entrada que no existe con RarArchive::getEntry.

## Parámetros

`using_exceptions`  
Debe ser `true` para activar lanzamiento de excepciones, `false` para descativarlo (el valor por defecto).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `RarException::setUsingExceptions`

```
<?php
var_dump(RarException::isUsingExceptions());
$arch = RarArchive::open("does_not_exist.rar");
var_dump($arch);

RarException::setUsingExceptions(true);
var_dump(RarException::isUsingExceptions());
$arch = RarArchive::open("does_not_exist.rar");
var_dump($arch); //not reached
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)

    Warning: RarArchive::open(): Failed to open does_not_exist.rar: ERAR_EOPEN (file open error) in C:\php_rar\trunk\tests\test.php on line 3
    bool(false)
    bool(true)

    Fatal error: Uncaught exception 'RarException' with message 'unRAR internal error: Failed to open does_not_exist.rar: ERAR_EOPEN (file open error)' in C:\php_rar\trunk\tests\test.php:8
    Stack trace:
    #0 C:\php_rar\trunk\tests\test.php(8): RarArchive::open('does_not_exist....')
    #1 {main}
      thrown in C:\php_rar\trunk\tests\test.php on line 8

## Véase también

RarException::isUsingExceptions
