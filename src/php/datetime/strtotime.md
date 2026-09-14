---
title: strtotime
description: Transforma un texto inglés en timestamp
source_url: https://www.php.net/manual/es/function.strtotime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/strtotime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11340
---

strtotime

Transforma un texto inglés en timestamp

## Descripción

```php
strtotime(string $datetime, [int $baseTimestamp]): int
```php

La función espera recibir una cadena que contiene una fecha en inglés e intentará leerla y transformarla en un timestamp Unix (el número de segundos desde el 1 de enero de 1970 a 00:00:00 UTC), relativo al timestamp `baseTimestamp`, o a la fecha actual si este último es omitido. El análisis de la cadena de fecha está definido en [los formatos de fecha y hora](#datetime.formats) y presenta varias consideraciones sutiles. Se recomienda encarecidamente examinar todos los detalles.

> [!WARNING]
> El timestamp Unix que devuelve esta función no contiene información sobre los husos horarios. Para realizar cálculos con información de fecha/hora, es preferible utilizar `DateTimeImmutable` que es más capaz.

Cada parámetro de la función utiliza el desplazamiento horario por defecto a menos que se especifique explícitamente un desplazamiento horario. Tenga cuidado de no utilizar un desplazamiento horario diferente para cada parámetro a menos que sea lo que se necesita. Consulte la función `date_default_timezone_get` para saber cómo definir un desplazamiento horario por defecto.

## Parámetros

`datetime`  
Una cadena de fecha/hora. Los formatos válidos son explicados en la documentación sobre los [formatos de Fecha y Hora](#datetime.formats).

`baseTimestamp`  
El timestamp, que representa la fecha actual, utilizado para el cálculo relativo de fechas.

## Valores devueltos

Devuelve un timestamp en caso de éxito, `false` en caso contrario.

## Errores/Excepciones

Cada llamada a una función de fecha/hora generará un diagnóstico de tipo `E_WARNING` si la zona horaria no es válida. Ver también `date_default_timezone_set`

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 8.0.0   | `baseTimestamp` ahora es nullable. |

## Ejemplos

Ejemplo con `strtotime`

```
<?php
echo strtotime("now"), "\n";
echo strtotime("10 September 2000"), "\n";
echo strtotime("+1 day"), "\n";
echo strtotime("+1 week"), "\n";
echo strtotime("+1 week 2 days 4 hours 2 seconds"), "\n";
echo strtotime("next Thursday"), "\n";
echo strtotime("last Monday"), "\n";

    
```php

Verificación de error

```
<?php
$str = 'No es válido';

if (($timestamp = strtotime($str)) === false) {
   echo "La cadena ($str) está corrupta";
} else {
   echo "$str == " . date('l dS \o\f F Y h:i:s A', $timestamp);
}

    
```php

## Notas

> [!NOTE]
> En este caso, la fecha "relativa" significa también que si un componente particular del timestamp no es proporcionado, será extraído textualmente de `baseTimestamp`. En otras palabras, `strtotime('February')`, si se ejecuta el 31 de mayo de 2022, será interpretado como el `31 de febrero de 2022`, lo que desbordará a un timestamp el `3 de marzo`. (En un año bisiesto, sería el `2 de marzo`.) El uso de `strtotime('1 February')` o `strtotime('first day of February')` evitaría este problema.

> [!NOTE]
> Si el número de años se especifica en dos dígitos, los valores entre 00-69 corresponden a 2000-2069 y 70-99 a 1970-1999. Consulte las notas posteriores sobre las posibles diferencias entre sistemas de 32 bits (las fechas pueden fallar después del 19/01/2038 a 03:14:07).

> [!NOTE]
> El intervalo de validez de un timestamp va del Viernes 13 de diciembre de 1901 20:45:54 UTC al Martes 19 de enero de 2038 03:14:07 UTC. (Esto corresponde a las fechas máximas y mínimas para un entero de 32 bits firmado).
>
> Para las versiones de 64 bits de PHP, el intervalo válido de un timestamp es realmente infinito, sabiendo que 64 bits puede representar aproximadamente 293 mil millones de años en cualquier dirección.

> [!NOTE]
> El uso de esta función en operaciones matemáticas no está recomendado. Es preferible utilizar en este caso DateTime::add y DateTime::sub.

## Véase también

`DateTimeImmutable`, DateTimeImmutable::createFromFormat, [Los formatos sobre fechas](#datetime.formats), `checkdate`, `strptime`
