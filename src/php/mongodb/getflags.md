---
title: MongoDB\BSON\Regex::getFlags
description: Devuelve los flags de la REGEX
source_url: https://www.php.net/manual/es/mongodb-bson-regex.getflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/regex/getflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48280
---

MongoDB\BSON\Regex::getFlags

Devuelve los flags de la REGEX

## Descripción

```php
final public MongoDB\BSON\Regex::getFlags(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los flags de la REGEX.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `BSON\Regex::getFlags`

```
<?php

$regex = new MongoDB\BSON\Regex('regex', 'i');
var_dump($regex->getFlags());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "i"

## Véase también

Los tipos BSON

Los flags soportados de las expresiones regulares
