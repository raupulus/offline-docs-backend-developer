---
title: easter_date
description: Retorna el timestamp Unix para la medianoche local el día de Pascua de
  un año dado
source_url: https://www.php.net/manual/es/function.easter-date.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/easter-date.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: false
translation_revision: 7706c4d38
order: 6570
---

easter_date

Retorna el timestamp Unix para la medianoche local el día de Pascua de un año dado

## Descripción

```php
easter_date([int $year], [int $mode]): int
```php

Retorna un timestamp UNIX para Pascua, a medianoche, para un año dado.

La fecha de Pascua fue establecida por el concilio de Nicea, en 325 de nuestra era, como siendo el domingo después de la primera luna llena que sigue al equinoccio de primavera. El equinoccio de primavera es considerado como siendo siempre el 21 de marzo, lo cual reduce el problema al cálculo de la fecha de la luna llena que sigue, y el domingo siguiente. El algoritmo fue introducido hacia 532, por Dionysius Exiguus. Con el calendario Juliano, (para los años antes de 1753), un ciclo de 19 años es suficiente para conocer las fechas de las fases de la luna. Con el calendario Gregoriano, (a partir de los años 1753, diseñado por Clavius y Lilius, luego introducido por el papa Gregorio XIII en octubre de 1582, y en Gran Bretaña y sus colonias en septiembre de 1752), dos factores de corrección fueron añadidos para hacer el ciclo más preciso.

## Parámetros

`year`  
El año, debe ser un número comprendido entre 1970 y 2037 para los sistemas de 32 bits, o entre 1970 y 2 000 000 000 para los sistemas de 64 bits. Si se omite o es `null`, el valor por omisión será el año actual según la hora local.

`mode`  
Permite calcular la fecha de Pascua según el calendario Juliano cuando se define como `CAL_EASTER_ALWAYS_JULIAN`. Ver también [las constantes de calendario](#calendar.constants).

## Valores devueltos

La fecha para Pascua, en forma de timestamp unix.

## Errores/Excepciones

Se genera una `ValueError` si el año es anterior a 1970 o posterior a 2037 al ejecutarse en un sistema de 32 bits, o posterior a 2 000 000 000 en un sistema de 64 bits.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | En los sistemas de 64 bits, el argumento `year` ahora acepta valores en el rango de 1970 a 2 000 000 000. |
| 8.0.0 | `year` ahora es nullable. |
| 8.0.0 | Ahora se genera una `ValueError` cuando `year` está fuera del rango permitido. Anteriormente, se generaba una advertencia `E_WARNING` y la función retornaba `false`. |

## Ejemplos

Ejemplo con `easter_date`

```
<?php

echo date("M-d-Y", easter_date(1999));        // Apr-04-1999
echo date("M-d-Y", easter_date(2000));        // Apr-23-2000
echo date("M-d-Y", easter_date(2001));        // Apr-15-2001

?>

    
```php

Uso de `easter_date` con `DateTime`

```
<?php

$timestamp = easter_date(2023);

$datetime = new \DateTime();
$datetime->setTimestamp($timestamp);

echo $datetime->format('M-d-Y'); // Apr-09-2023

?>

    
```php

## Notas

> [!NOTE]
> La función `easter_date` se basa en las funciones de la biblioteca C time del sistema, en lugar de las funciones date y time internas de PHP. Además, la función `easter_date` utiliza la variable de entorno `TZ` para determinar la zona horaria a utilizar, en lugar de la [zona horaria por defecto](#ini.date.timezone) de PHP, lo cual puede llevar a un comportamiento no deseado al utilizar esta función con otras funciones date de PHP.
>
> Como solución alternativa, puede utilizarse la función `easter_days` con las clases `DateTime` y `DateInterval` para calcular el día de Pascua en la zona horaria de PHP, de la siguiente manera:
>
> <div class="informalexample">
>
> ```
> <?php
> function get_easter_datetime($year) {
>     $base = new DateTime("$year-03-21");
>     $days = easter_days($year);
>
>     return $base->add(new DateInterval("P{$days}D"));
> }
>
> foreach (range(2012, 2015) as $year) {
>     printf("Pascua, en %d, cae el %s\n",
>            $year,
>            get_easter_datetime($year)->format('d F'));
> }
> ?>
>
>     
> ```
>
> El ejemplo anterior mostrará:
>
>     Pascua, en 2012, cae el 08 Abril
>     Pascua, en 2013, cae el 31 Marzo
>     Pascua, en 2014, cae el 20 Abril
>     Pascua, en 2015, cae el 05 Abril
>
>         
>
> </div>

## Véase también

`easter_days` para el cálculo de Pascua antes de 1970 y después de 2037
