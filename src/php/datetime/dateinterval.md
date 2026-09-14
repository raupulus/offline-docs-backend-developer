---
title: La clase DateInterval
source_url: https://www.php.net/manual/es/class.dateinterval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateinterval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 4d17b7b49
order: 10250
---

## Introducción

Representa un intervalo de fechas.

Un intervalo de fechas almacena o bien una cantidad fija de instantes (en años, meses, días, horas, etc.) o bien una cadena con un instante relativo en el formato que admiten los constructores de `DateTimeImmutable` y `DateTime`.

Más especificamente, la información en un objeto de la clase `DateInterval` es una instrucción para llegar de un instante de fecha/hora a otro instante de fecha/hora. Este proceso no es siempre reversible.

Un modo común de crear un objeto `DateInterval` es calculando la diferencia entre dos objetos de fecha/hora a través de DateTimeInterface::diff.

Dado que no hay una forma bien definida de comparar intervalos de fechas, las instancias de `DateInterval` son [incomparables](#language.operators.comparison.incomparable).

## Sinopsis de la clase

DateInterval

Propiedades

public

int

y

public

int

m

public

int

d

public

int

h

public

int

i

public

int

s

public

float

f

public

int

invert

public

mixed

days

public

bool

from_string

public

string

date_string

Métodos

## Propiedades

> [!WARNING]
> El listado de propiedades disponibles que se muestra a continuación depende de la versión de PHP, y deben considerarse como de *solo lectura*.

`y`  
Número de años.

`m`  
Número de meses.

`d`  
Número de días.

`h`  
Número de horas.

`i`  
Número de minutos.

`s`  
Número de segundos.

`f`  
Número de microsegundos, como fracción de un segundo.

`invert`  
Es `1` si el intervalo representa un periodo de tiempo negativo y `0` en caso contrario. Véase DateInterval::format.

`days`  
Si el objeto DateInterval fue creado por DateTimeImmutable::diff o DateTime::diff, entonces este es el número total de días completos entre las fechas de inicio y fin. En caso contrario, `days` será `false`.

`from_string`  
Si el objeto DateInterval fue creado por DateInterval::createFromDateString, entonces esta propiedad tendrá el valor `true`, y será establecida la propiedad `date_string`. De lo contrario, el valor será `false`, y serán establecidas las propiedades `y` a `f`, `invert`, y `days`.

`date_string`  
La cadena usada como argumento en DateInterval::createFromDateString.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Se han añadido las propiedades `from_string` y `date_string` para las instancias de `DateInterval` que fueron creadas usando el método DateInterval::createFromDateString. |
| 8.2.0 | Solo las propiedades `y` a `f`, `invert`, y `days` serán visibles. |
| 7.4.0 | Ahora las instancias de `DateInterval` son incomparables; anteriormente, todas las instancias de `DateInterval` se consideraban iguales. |
| 7.1.0 | Se ha añadido la propiedad `f`. |
