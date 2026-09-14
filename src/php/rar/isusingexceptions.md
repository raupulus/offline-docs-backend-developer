---
title: RarException::isUsingExceptions
description: Comprobar si el manejador de errores con excepciones está en uso
source_url: https://www.php.net/manual/es/rarexception.isusingexceptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarexception/isusingexceptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68650
---

RarException::isUsingExceptions

Comprobar si el manejador de errores con excepciones está en uso

## Descripción

```php
public static RarException::isUsingExceptions(): bool
```php

Comprueba si las funciones RAR emitirán avisos y devolverán valores de error o si ellas lanzarán excepciones en la mayoría de las circunstancias (no incluye algunos errores de programación tales como pasar el tipo incorrecto de argumento).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si las excepciones estan siendo utilizadas, `false` en caso contrario.

## Ejemplos

Ejemplo de `RarException::isUsingExceptions`

```
<?php
//El valor predeterminado es no usar excepciones
var_dump(RarException::isUsingExceptions());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)

## Véase también

RarException::setUsingExceptions
