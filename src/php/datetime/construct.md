---
title: DateInterval::__construct
description: Crea un nuevo objeto DateInterval
source_url: https://www.php.net/manual/es/dateinterval.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateinterval/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10220
---

DateInterval::\_\_construct

Crea un nuevo objeto DateInterval

## Descripción

```php
public DateInterval::__construct(string $duration)
```php

Crea un nuevo objeto DateInterval.

## Parámetros

`duration`  
Una especificación de intervalo.

El formato empieza con la letra `P`, de “periodo.” Cada periodo de duración está representado por un valor de tipo integer seguido de un indicador de periodo. Si la duración contiene elementos de hora, esa parte de la especificación estará precedida por una letra `T`.

| Indicador de periodo | Descripción |
|----|----|
| `Y` | años |
| `M` | meses |
| `D` | días |
| `W` | semanas; estas se convierten a días, Antes de PHP 8.0.0, no se puede combinar con `D`. |
| `H` | horas |
| `M` | minutos |
| `S` | segundos |

Indicadores de periodo de `duration`

Algunos ejemplos sencillos: Dos días es `P2D`. Dos segundos es `PT2S`. Seis años y cinco minutos es `P6YT5M`.

> [!NOTE]
> Los tipos de unidades deben ser escritos desde la unidad de escala más grande a la izquierda a la unidad de escala más pequeña a la derecha. Así los años van antes que los meses, meses antes que días, días antes que minutos, etc. Así un año y cuatro días debe representarse como `P1Y4D`, y no como `P4D1Y`.

La especificación también puede ser representada como una fecha/hora. Un ejemplo de un año y cuatro días sería `P0001-00-04T00:00:00`. Pero los valores en este formato no pueden exceder el punto de desbordamiento de un periodo (p.ej. `25` horas no es válido).

Estos formatos están basados en la [ especificación de duración ISO 8601](http://en.wikipedia.org/wiki/Iso8601#Durations).

## Errores/Excepciones

Lanza una `DateMalformedIntervalStringException` cuando el `duration` no puede ser analizado como un intervalo. Antes de PHP 8.3, esto era Exception.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza DateMalformedIntervalStringException en lugar de Exception. |
| 8.2.0 | Solo serán visibles las propiedades `y` a `f`, `invert` y `days`, incluyendo una nueva propiedad booleana `from_string`. |
| 8.0.0 | `W` se puede combinar con `D`. |

## Ejemplos

Construyendo y usando objetos `DateInterval`

```
<?php
// Crea una fecha especifica
$someDate = \DateTime::createFromFormat("Y-m-d H:i", "2022-08-25 14:18");

// Crea un intervalo
$interval = new \DateInterval("P7D");

// Añade el intervalo
$someDate->add($interval);

// Convierte el intervalo a string
echo $interval->format("%d");

    
```php

El ejemplo anterior mostrará:

```
7

    
```php

Ejemplo de `DateInterval`

```
<?php
$interval = new DateInterval('P1W2D');
var_dump($interval);

    
```php

Resultado del ejemplo anterior en PHP 8.2:

```
object(DateInterval)#1 (10) {
  ["y"]=>
  int(0)
  ["m"]=>
  int(0)
  ["d"]=>
  int(9)
  ["h"]=>
  int(0)
  ["i"]=>
  int(0)
  ["s"]=>
  int(0)
  ["f"]=>
  float(0)
  ["invert"]=>
  int(0)
  ["days"]=>
  bool(false)
  ["from_string"]=>
  bool(false)
}

    
```php

Resultado del ejemplo anterior en PHP 8:

```
object(DateInterval)#1 (16) {
  ["y"]=>
  int(0)
  ["m"]=>
  int(0)
  ["d"]=>
  int(9)
  ["h"]=>
  int(0)
  ["i"]=>
  int(0)
  ["s"]=>
  int(0)
  ["f"]=>
  float(0)
  ["weekday"]=>
  int(0)
  ["weekday_behavior"]=>
  int(0)
  ["first_last_day_of"]=>
  int(0)
  ["invert"]=>
  int(0)
  ["days"]=>
  bool(false)
  ["special_type"]=>
  int(0)
  ["special_amount"]=>
  int(0)
  ["have_weekday_relative"]=>
  int(0)
  ["have_special_relative"]=>
  int(0)
}

    
```php

Resultado del ejemplo anterior en PHP 7:

```
     
object(DateInterval)#1 (16) {
  ["y"]=>
  int(0)
  ["m"]=>
  int(0)
  ["d"]=>
  int(2)
  ["h"]=>
  int(0)
  ["i"]=>
  int(0)
  ["s"]=>
  int(0)
  ["f"]=>
  float(0)
  ["weekday"]=>
  int(0)
  ["weekday_behavior"]=>
  int(0)
  ["first_last_day_of"]=>
  int(0)
  ["invert"]=>
  int(0)
  ["days"]=>
  bool(false)
  ["special_type"]=>
  int(0)
  ["special_amount"]=>
  int(0)
  ["have_weekday_relative"]=>
  int(0)
  ["have_special_relative"]=>
  int(0)
}

    
```php

## Véase también

`DateInterval::format`, `DateTime::add`, `DateTime::sub`, `DateTime::diff`
