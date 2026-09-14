---
title: ReflectionFunction::__toString
description: Devuelve una representación textual del objeto ReflectionFunction
source_url: https://www.php.net/manual/es/reflectionfunction.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionfunction/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ca840c9a6
order: 70450
---

ReflectionFunction::\_\_toString

Devuelve una representación textual del objeto ReflectionFunction

## Descripción

```php
public ReflectionFunction::__toString(): string
```php

Obtiene una representación textual legible por humanos de la función, sus argumentos y su valor de retorno.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La cadena.

## Ejemplos

Ejemplo para ReflectionFunction::\_\_toString

```
<?php
function title($title, $name)
{
    return sprintf("%s. %s\r\n", $title, $name);
}

echo new ReflectionFunction('title');
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Function [ <user> function title ] {
      @@ Command line code 1 - 1

      - Parameters [2] {
        Parameter #0 [ <required> $title ]
        Parameter #1 [ <required> $name ]
      }
    }

## Véase también

ReflectionFunction::export, [\_\_toString()](#object.tostring)
