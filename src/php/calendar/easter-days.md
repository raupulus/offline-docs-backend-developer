---
title: easter_days
description: Retorna el número de días entre el 21 de marzo y Pascua, para un año
  dado
source_url: https://www.php.net/manual/es/function.easter-days.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/easter-days.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 789af8343
order: 6580
---

easter_days

Retorna el número de días entre el 21 de marzo y Pascua, para un año dado

## Descripción

```php
easter_days([int $year], [int $mode]): int
```php

Retorna el número de días entre el 21 de marzo y Pascua, para un año dado. Si el año no está especificado, se utilizará el año actual.

Esta función puede ser utilizada en lugar de `easter_date` para calcular la fecha de Pascua, para los años que caen fuera del intervalo de validez de los timestamps UNIX (es decir, antes de 1970 o después de 2037).

La fecha de Pascua fue fijada por el concilio de Nicea, en 325 de nuestra era, como siendo el domingo después de la primera luna llena que sigue al equinoccio de primavera. El equinoccio de primavera es considerado como siendo siempre el 21 de marzo, lo que reduce el problema al cálculo de la fecha de la luna llena que sigue, y el domingo siguiente. El algoritmo fue introducido hacia 532, por Dionysius Exiguus. Con el calendario Juliano, (para los años antes de 1753), un ciclo de 19 años es suficiente para conocer las fechas de las fases de la luna. Con el calendario Gregoriano, (a partir de los años 1753, diseñado por Clavius y Lilius, luego introducido por el papa Gregorio XIII en octubre de 1582, y en Gran Bretaña y sus colonias en septiembre de 1752), dos factores de corrección fueron añadidos para hacer el ciclo más preciso.

## Parámetros

`year`  
El año, en forma de un número positivo. Si se omite o es `null`, el valor por defecto será el año actual según la hora local.

`mode`  
Permite el cálculo de las fechas de Pascua basándose en el calendario Gregoriano para los años entre 1582 y 1752 cuando se define como `CAL_EASTER_ROMAN`. Ver las [constantes de los calendarios](#calendar.constants) para más constantes válidas.

## Valores devueltos

El número de días entre el 21 de marzo y Pascua, para el año `year` proporcionado.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `year` ahora es nullable. |

## Ejemplos

Ejemplo con `easter_days`

```
<?php

echo easter_days(1999);        // 14, es decir, 4 de abril
echo easter_days(1492);        // 32, es decir, 22 de abril
echo easter_days(1913);        //  2, es decir, 23 de marzo

?>

    
```php

## Véase también

`easter_date`
