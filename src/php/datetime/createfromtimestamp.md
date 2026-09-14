---
title: DateTime::createFromTimestamp
description: Crea una instancia a partir de una marca de tiempo Unix
source_url: https://www.php.net/manual/es/datetime.createfromtimestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetime/createfromtimestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 726154e3c
order: 10450
---

DateTime::createFromTimestamp

Crea una instancia a partir de una marca de tiempo Unix

## Descripción

```php
public static DateTime::createFromTimestamp(int $timestamp): static
```php

Crea una instancia a partir de una marca de tiempo Unix.

## Parámetros

`timestamp`  
Marca de tiempo Unix que representa la fecha. También se acepta un valor `float`, lo que permite una precisión de microsegundos.

## Valores devueltos

Devuelve una nueva instancia de `DateTime`.

## Errores/Excepciones

Si `timestamp` está fuera del rango \[`PHP_INT_MIN`, `PHP_INT_MAX`\], se lanza una DateRangeError.

## Ejemplos

Ejemplo de DateTime::createFromTimestamp

```
<?php
$date = DateTime::createFromTimestamp(123.456789);
echo $date->format('Y-m-d H:i:s.u');
?>

   
```php

El ejemplo anterior mostrará:

    1970-01-01 00:02:03.456789
