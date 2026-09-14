---
title: DateTimeImmutable::getLastErrors
description: Devuelve las advertencias y errores
source_url: https://www.php.net/manual/es/datetimeimmutable.getlasterrors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeimmutable/getlasterrors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10630
---

DateTimeImmutable::getLastErrors

Devuelve las advertencias y errores

## Descripción

```php
public static DateTimeImmutable::getLastErrors(): array
```php

Devuelve un array de advertencias y errores encontrados mientras se analizaba una cadena de fecha/hora.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array que contiene información sobre advertencias y errores, o `false` si no hay ni advertencias ni errores.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Antes de PHP 8.2.0, esta función no devolvía `false` cuando no había advertencias ni errores. En su lugar, siempre devolvía la estructura de array documentada. |

## Ejemplos

`DateTimeImmutable::getLastErrors` example

```
<?php
try {
    $date = new DateTimeImmutable('asdfasdf');
} catch (Exception $e) {
    // Solo para fines de demostración...
    print_r(DateTimeImmutable::getLastErrors());

    // La forma correcta de hacer esto con programación orientada a objetos es
    echo $e->getMessage();
}
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [warning_count] => 1
        [warnings] => Array
            (
                [6] => Double timezone specification
            )

        [error_count] => 1
        [errors] => Array
            (
                [0] => The timezone could not be found in the database
            )
    )
    Failed to parse time string (asdfasdf) at position 0 (a): The timezone could not be found in the database

       

Los índices 6, y 0 en la salida de ejemplo se refieren al índice de caracteres en la cadena donde ocurrió el error.

Detectando fechas desbordadas

```
<?php
$date = DateTimeImmutable::createFromFormat('!Y-m-d', '2020-02-30');
print_r(DateTimeImmutable::getLastErrors());

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [warning_count] => 1
        [warnings] => Array
            (
                [10] => The parsed date was invalid
            )

        [error_count] => 0
        [errors] => Array
            (
            )
    )
