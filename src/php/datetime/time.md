---
title: time
description: Devuelve el timestamp UNIX actual
source_url: https://www.php.net/manual/es/function.time.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/time.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 11350
---

time

Devuelve el timestamp UNIX actual

## Descripción

```php
time(): int
```php

Devuelve la hora actual medida en el número de segundos desde el inicio de la época UNIX (1 de enero de 1970 00:00:00 GMT).

> [!NOTE]
> Los timestamps Unix no contienen información alguna sobre el huso horario local. Se recomienda utilizar la clase `DateTimeImmutable` para manipular información relativa a la fecha y la hora, a fin de evitar los problemas asociados a los timestamps Unix.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el timestamp actual.

## Ejemplos

Ejemplo con `time`

```
<?php
echo 'Hoy : '. time();

    
```php

Resultado del ejemplo anterior es similar a:

    Hoy : 1660338149

## Notas

> [!TIP]
> Un timestamp que representa el inicio de la petición está disponible en la variable `$_SERVER['REQUEST_TIME']`.

## Véase también

`DateTimeImmutable`, `date`, `microtime`
