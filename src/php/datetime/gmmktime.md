---
title: gmmktime
description: Retorna el timestamp UNIX de una fecha GMT
source_url: https://www.php.net/manual/es/function.gmmktime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/gmmktime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11260
---

gmmktime

Retorna el timestamp UNIX de una fecha GMT

## Descripción

```php
gmmktime(int $hour, [int $minute], [int $second], [int $month], [int $day], [int $year]): int
```php

Similar a la función `mktime` excepto que los argumentos opcionales pasados son GMT. `gmmktime` utiliza internamente la función `mktime`, por lo tanto, solo los tiempos válidos en la zona horaria local derivada pueden ser utilizados.

Al igual que `mktime`, los argumentos restantes pueden ser omitidos. En ese caso, tomarán los valores GMT actuales.

Llamar a `gmmktime` sin argumentos no es soportado. Esto resultará en lanzar una `ArgumentCountError`. `time` puede ser utilizado para obtener el timestamp actual.

## Parámetros

`hour`  
El número de horas desde el inicio del día establecido por los parámetros `month`, `day` y `year`. Los valores negativos hacen referencia a las horas antes de la medianoche del día en cuestión. Los valores superiores a 23 hacen referencia a las horas asociadas al(dos) día(s) siguiente(s).

`minute`  
El número de minutos desde el inicio de la hora `hour`. Los valores negativos hacen referencia a los minutos de la hora anterior. Los valores superiores a 59 hacen referencia a los minutos asociados a la(s) hora(s) siguiente(s).

`second`  
El número de segundos desde el inicio del minuto `minute`. Los valores negativos hacen referencia a los segundos del minuto anterior. Los valores superiores a 59 hacen referencia a los segundos asociados a el(la) minuto(s) siguiente(s).

`month`  
El número de meses desde el final del año anterior. Los valores comprendidos entre 1 y 12 hacen referencia a los meses del calendario normal del año en cuestión. Los valores inferiores a 1 (incluyendo los valores negativos) hacen referencia a los meses del año anterior en orden inverso, por lo tanto, 0 corresponde a diciembre, -1 a noviembre, etc. Los valores superiores a 12 hacen referencia al mes correspondiente en el(la) año(s) siguiente(s).

`day`  
El número de días desde el final del mes anterior. Los valores comprendidos entre 1 y 28, 29, 30, 31 (según el mes) hacen referencia a los días normales en el mes actual. Los valores inferiores a 1 (incluyendo los valores negativos) hacen referencia a los días del mes anterior, por lo tanto, 0 corresponde al último día del mes anterior, -1, el día anterior, etc. Los valores superiores al número de días del mes actual hacen referencia a los días correspondientes del(la) mes(es) siguiente(s).

`year`  
El año

## Valores devueltos

Retorna un timestamp Unix de tipo `int`, o `false` si el timestamp no cabe en un entero PHP.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `hour` ya no es opcional. Para obtener un timestamp unix, se deberá utilizar la función `time`. |
| 8.0.0 | `minute`, `second`, `month`, `day` y `year` ahora son nullable. |

## Ejemplos

Ejemplo con `gmmktime`

```
<?php
date_default_timezone_set("Indian/Maldives");

echo "1 de julio de 2000 cae en " . date("l", gmmktime(0, 0, 0, 7, 1, 2000));

    
```php

El ejemplo anterior mostrará:

    1 de julio de 2000 cae en Saturday

## Véase también

La clase `DateTimeImmutable`, `mktime`, `date`, `time`
