---
title: DateTimeInterface::format
description: Retorna una fecha formateada según el formato proporcionado
source_url: https://www.php.net/manual/es/datetime.format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface/format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10750
---

DateTimeInterface::format

DateTimeImmutable::format

DateTime::format

date_format

Retorna una fecha formateada según el formato proporcionado

## Descripción

Estilo orientado a objetos

```php
public DateTimeInterface::format(string $format): string
```php

```php
public DateTimeImmutable::format(string $format): string
```

```php
public DateTime::format(string $format): string
```php

Estilo procedimental

```php
date_format(DateTimeInterface $object, string $format): string
```

Retorna una fecha formateada según el formato proporcionado.

## Parámetros

`object`  
Solo en estilo procedimental: un objeto `DateTime` retornado por `date_create`

`format`  
El formato de la fecha deseada en forma de `string`. Ver las opciones de formato a continuación. Existen también numerosas [constantes de fechas](#datetimeinterface.constants.types) que pueden ser utilizadas, lo que hace que `DATE_RSS` reemplace el formato `"D, d M Y H:i:s"`.

| Caracteres para el parámetro `format` | Descripción | Ejemplos de valores retornados |
|----|----|----|
| *Día* | --- | --- |
| `d` | Día del mes, en dos dígitos (con un cero inicial) | `01` a `31` |
| `D` | Día de la semana, en tres letras (y en inglés - por defecto: en inglés, o sino, en el idioma local del servidor) | `Mon` a `Sun` |
| `j` | Día del mes sin los ceros iniciales | `1` a `31` |
| `l` ('L' minúscula) | Día de la semana, textual, versión larga, en inglés | `Sunday` a `Saturday` |
| `N` | Representación numérica ISO 8601 del día de la semana | `1` (para Lunes) a `7` (para Domingo) |
| `S` | Sufijo ordinal de un número para el día del mes, en inglés, en dos letras | `st`, `nd`, `rd` o `th`. Funciona bien con `j` |
| `w` | Día de la semana en formato numérico | `0` (para domingo) a `6` (para sábado) |
| `z` | Día del año | `0` a `365` |
| *Semana* | --- | --- |
| `W` | Número de semana en el año ISO 8601, las semanas comienzan el lunes | Ejemplo: `42` (la 42ª semana del año) |
| *Mes* | --- | --- |
| `F` | Mes, textual, versión larga; en inglés, como `January` o `December` | `January` a `December` |
| `m` | Mes en formato numérico, con ceros iniciales | `01` a `12` |
| `M` | Mes, en tres letras, en inglés | `Jan` a `Dec` |
| `n` | Mes sin los ceros iniciales | `1` a `12` |
| `t` | Número de días en el mes | `28` a `31` |
| *Año* | --- | --- |
| `L` | ¿Es el año bisiesto? | `1` si es bisiesto, `0` si no. |
| `o` | Año de numeración de semanas ISO 8601. Es el mismo valor que `Y`, excepto si el número de semana ISO (`W`) pertenece al año anterior o siguiente, este año será utilizado en su lugar. | Ejemplos: `1999` o `2003` |
| `X` | Una representación numérica completa extendida de un año, de al menos 4 dígitos, con un `-` para los años antes de la era común y un `+` para los años de la era común. | Ejemplos: `-0055`, `+0787`, `+1999`, `+10191` |
| `x` | Una representación numérica completa extendida si es necesario, o una representación numérica completa estándar si es posible (como `Y`). Al menos cuatro dígitos. Los años anteriores a la era común son prefijados por un `-`. Los años más allá (y incluyendo) del `10000` son prefijados por un `+`. | Ejemplos: `-0055`, `0787`, `1999`, `+10191` |
| `Y` | Una representación numérica completa de un año, al menos 4 dígitos, con `-` para los años av. J.-C. | Ejemplos: `-0055`, `0787`, `1999`, `2003`, `10191` |
| `y` | Año en 2 dígitos | Ejemplos: `99` o `03` |
| *Hora* | --- | --- |
| `a` | Ante meridiem y Post meridiem en minúsculas | `am` o `pm` |
| `A` | Ante meridiem y Post meridiem en mayúsculas | `AM` o `PM` |
| `B` | Hora Internet Swatch | `000` a `999` |
| `g` | Hora, en formato 12h, sin los ceros iniciales | `1` a `12` |
| `G` | Hora, en formato 24h, sin los ceros iniciales | `0` a `23` |
| `h` | Hora, en formato 12h, con los ceros iniciales | `01` a `12` |
| `H` | Hora, en formato 24h, con los ceros iniciales | `00` a `23` |
| `i` | Minutos con ceros iniciales | `00` a `59` |
| `s` | Segundos con ceros iniciales | `00` a `59` |
| `u` | Microsegundos. Tenga en cuenta que la función `date` generará siempre `000000` ya que toma un parámetro de tipo `int`, mientras que el método DateTimeInterface::format soporta microsegundos si un objeto de tipo DateTimeInterface fue creado con microsegundos. | Ejemplo: `654321` |
| `v` | Milisegundos. Misma nota que para `u`. | Ejemplo: `654` |
| *Zona horaria* | --- | --- |
| `e` | El identificador de la zona horaria | Ejemplos: `UTC`, `GMT`, `Atlantic/Azores` |
| `I` (i mayúscula) | La hora de verano está activada o no | `1` si sí, `0` si no. |
| `O` | Diferencia de horas con la hora de Greenwich (GMT), sin dos puntos entre las horas y los minutos | Ejemplo: `+0200` |
| `P` | Diferencia con la hora Greenwich (GMT) con un dos puntos entre las horas y los minutos | Ejemplo: `+02:00` |
| `p` | Idéntico a `P`, pero retorna `Z` en lugar de `+00:00` (disponible a partir de PHP 8.0.0) | Ejemplos: `Z` o `+02:00` |
| `T` | Abreviación de la zona horaria, si es conocida; sino, desplazamiento desde GMT | Ejemplos: `EST`, `MDT`, `+05` |
| `Z` | Desplazamiento horario en segundos. El desplazamiento de zonas al oeste de la zona UTC es negativo, y al este, es positivo. | `-43200` a `50400` |
| *Fecha y Hora completa* | --- | --- |
| `c` | Fecha en formato ISO 8601. Solo compatible con el formato no expandido (hasta el año 9999). Las fechas posteriores generarán una cadena no válida. Para fechas posteriores y el formato expandido, consulte `x` y `X`. | 2004-02-12T15:19:21+00:00 |
| `r` | Formato de fecha [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822)/[RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322) | Ejemplo: `Thu, 21 Dec 2000 16:01:070200` |
| `U` | Segundos desde la época Unix (1 de Enero de 1970, 0h00 00s GMT) | Ver también `time` |

Los siguientes caracteres son reconocidos en el parámetro `format`

Los caracteres no reconocidos serán impresos tal cual. "`Z`" retornará siempre `0` cuando se utiliza con `gmdate`.

> [!NOTE]
> Sabiendo que esta función solo acepta timestamps de tipo `int`, el carácter `u` solo es útil al utilizar la función `date_format` con un timestamp de usuario creado con la función `date_create`.

## Valores devueltos

Retorna la fecha formateada, en forma de string, en caso de éxito.

## Historial de cambios

| Versión | Descripción                                            |
|---------|--------------------------------------------------------|
| 8.2.0   | Los caracteres de formato `X` o `x` han sido añadidos. |
| 8.0.0   | El carácter de formato `p` ha sido añadido.            |

## Ejemplos

Ejemplo con `DateTime::format`

Estilo orientado a objetos

```php
<?php
$date = new DateTimeImmutable('2000-01-01');
echo $date->format('Y-m-d H:i:s');
?>

    
```

El ejemplo anterior mostrará:

    2000-01-01 00:00:00

        

Estilo procedimental

```php
<?php
$date = date_create('2000-01-01');
echo date_format($date, 'Y-m-d H:i:s');
?>

    
```

El ejemplo anterior mostrará:

    2000-01-01 00:00:00

Más ejemplos

```php
<?php
// establece la zona horaria predeterminada a usar.
date_default_timezone_set('UTC');

// ahora
$date = new DateTimeImmutable();

// Imprime algo como: Wednesday
echo $date->format('l'), "\n";

// Imprime algo como: Wednesday 19th of October 2022 08:40:48 AM
echo $date->format('l jS \o\f F Y h:i:s A'), "\n";

/* usa las constantes en el parámetro de formato */
// imprime algo como: Wed, 19 Oct 2022 08:40:48 +0000
echo $date->format(DateTimeInterface::RFC2822), "\n";
?>

    
```

Es posible evitar que un carácter reconocido en la cadena de formato se expanda escapándolo con un backslash (barra invertida). Si el carácter con backslash es ya una secuencia especial, será necesario también escapar el backslash.

Escape de caracteres durante el formato

```php
<?php
$date = new DateTimeImmutable();

// imprime algo como: Wednesday the 19th
echo $date->format('l \t\h\e jS');
?>

    
```

Para formatear fechas en otros idiomas, IntlDateFormatter::format puede ser utilizada en lugar de DateTimeInterface::format.

## Notas

Este método no utiliza locales. Todos los despliegues serán en inglés.

## Véase también

IntlDateFormatter::format
