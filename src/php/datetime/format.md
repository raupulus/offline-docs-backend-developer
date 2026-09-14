---
title: DateInterval::format
description: Formatea el intervalo
source_url: https://www.php.net/manual/es/dateinterval.format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateinterval/format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10240
---

DateInterval::format

Formatea el intervalo

## Descripción

```php
public DateInterval::format(string $format): string
```php

Formatea el intervalo.

## Parámetros

`format`  
| Carácter `format` | Descripción | Valores de ejemplo |
|----|----|----|
| `%` | Literal `%` | `%` |
| `Y` | Años, numérico, al menos 2 dígitos con 0 a la izquierda | `01`, `03` |
| `y` | Años, numérico | `1`, `3` |
| `M` | Meses, numérico, al menos 2 dígitos con 0 a la izquierda | `01`, `03`, `12` |
| `m` | Meses, numérico | `1`, `3`, `12` |
| `D` | Días, numérico, al menos 2 dígitos con 0 a la izquierda | `01`, `03`, `31` |
| `d` | Días, numérico | `1`, `3`, `31` |
| `a` | Número total de días como resultado de una operación con DateTime::diff, o de lo contrario `(unknown)` | `4`, `18`, `8123` |
| `H` | Horas, numérico, al menos 2 dígitos con 0 a la izquierda | `01`, `03`, `23` |
| `h` | Horas, numérico | `1`, `3`, `23` |
| `I` | Minutos, numérico, al menos 2 dígitos con 0 a la izquierda | `01`, `03`, `59` |
| `i` | Minutos, numérico | `1`, `3`, `59` |
| `S` | Segundos, numérico, al menos 2 dígitos con 0 a la izquierda | `01`, `03`, `57` |
| `s` | Segundos, numérico | `1`, `3`, `57` |
| `F` | Microsegundos, numérico, al menos 6 dígitos con 0 a la izquierda 0 | `007701`, `052738`, `428291` |
| `f` | Microsegundos, numérico | `7701`, `52738`, `428291` |
| `R` | Signo "`-`" cuando es negativo, "`+`" cuando es positivo | `-`, `+` |
| `r` | Signo "`-`" cuando es negativo, vacío cuando es positivo | `-`, `` |

Los siguientes caracteres están reconocidos en el parámetro de cadena `format`. Cada carácter de formato debe ser prefijado con un signo de porcentaje (`%`).

## Valores devueltos

Devuelve el intervalo formateado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.12 | Los caracteres de formato `F` y `f` ahora siempre serán positivos. |
| 7.1.0 | Se han añadido los caracteres de formato `F` y `f`. |

## Ejemplos

Ejemplo de `DateInterval`

```
<?php
$interval = new DateInterval('P2Y4DT6H8M');
echo $interval->format('%d days');

    
```php

El ejemplo anterior mostrará:

```
4 days

    
```php

`DateInterval` y excesos

```
     
<?php
$interval = new DateInterval('P32D');
echo $interval->format('%d days');

    
```php

El ejemplo anterior mostrará:

```
32 days

    
```php

`DateInterval` y DateTime::diff con los modificadores %a y %d

```
     
<?php
$january = new DateTime('2010-01-01');
$february = new DateTime('2010-02-01');
$interval = $february->diff($january);

// %a imprimirá el múmero total de días.
echo $interval->format('%a total days')."\n";

// Mientras que %d sólo imprimirá el múmero total de días no cubiertos por el
// mes.
echo $interval->format('%m month, %d days');

    
```php

El ejemplo anterior mostrará:

```
31 total days
1 month, 0 days

    
```php

## Notas

> [!NOTE]
> El método DateInterval::format no recalcula los desbordamientos en los strings de tiempo ni en los segmentos de fecha. Esto se espera porque no es posible desbordar valores como `"32 días"` que podrían interpretarse en algo como, desde `"1 mes y 4 días"` hasta `"1 mes y 1 día"`.

## Véase también

DateTime::diff
