---
title: getcwd
description: Devuelve el directorio de trabajo actual
source_url: https://www.php.net/manual/es/function.getcwd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/functions/getcwd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_reviewed: false
translation_revision: 62126c55f
order: 12040
---

getcwd

Devuelve el directorio de trabajo actual

## Descripción

```php
getcwd(): string
```php

Devuelve el directorio de trabajo actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el directorio de trabajo actual en caso de éxito o `false` en caso de fallo.

En algunas versiones de Unix, `getcwd` puede devolver `false` si todos los directorios padres no tienen el modo escritura o el modo búsqueda definido, incluso si el directorio actual los tiene. Ver la función `chmod` para más información sobre los modos de permisos.

## Ejemplos

Ejemplo con `getcwd`

```
<?php

// directorio actual
echo getcwd() . "\n";

chdir('cvs');

// directorio actual
echo getcwd() . "\n";

?>

     
```php

Resultado del ejemplo anterior es similar a:

    /home/didou
    /home/didou/cvs

## Notas

> [!CAUTION]
> Si el intérprete PHP ha sido compilado con ZTS activado (Zend Thread Safety), el directorio de trabajo actual, devuelto por la función `getcwd` puede ser diferente del devuelto por las interfaces del sistema. Las bibliotecas externas (llamadas a través de [FFI](#book.ffi)), que dependen del directorio de trabajo actual, se verán afectadas.

## Véase también

`chdir`, `chmod`
