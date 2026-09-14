---
title: date
description: Da formato a una marca de tiempo de Unix (Unix timestamp)
source_url: https://www.php.net/manual/es/function.date.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 11220
---

date

Da formato a una marca de tiempo de Unix (Unix timestamp)

## Descripción

```php
date(string $format, [int $timestamp]): string
```php

Devuelve una cadena formateada según el formato indicado usando el integer `timestamp` (Unix timestamp) dado, o el momento actual si no se da una marca de tiempo. En otras palabras, `timestamp` es opcional y por defecto es el valor de `time`.

> [!WARNING]
> Las marcas de tiempo de Unix no manejan zonas horarias. Usa la clase `DateTimeImmutable`, y su método DateTimeInterface::format para formatear fecha/hora incluyendo la información de zona horaria.

## Parámetros

`format`  
Formato aceptado por DateTimeInterface::format.

> [!NOTE]
> `date` generará siempre `000000` como microsegundos ya que toma un tipo `int` como parámetro, mientras que DateTimeInterface::format soporta microsegundos, si el objeto del tipo DateTimeInterface es creado con microsegundos.

`timestamp`  
El parámetro opcional `timestamp` es un `int` timestamp Unix que por defecto es la hora local actual si `timestamp` se omite o es `null`. En otras palabras, por defecto toma el valor de `time`.

## Valores devueltos

Devuelve una cadena de fecha formateada.

## Errores/Excepciones

Cada llamada a una función de fecha/hora generará un diagnóstico de tipo `E_WARNING` si la zona horaria no es válida. Ver también `date_default_timezone_set`

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `timestamp` ahora es nullable. |

## Ejemplos

Ejemplos de `date`

```
<?php
// Establecer la zona horaria por omisión
date_default_timezone_set('UTC');

// Imprime algo como: Monday
echo date("l") . "\n";

// Imprime algo como: Monday 8th of August 2005 03:12:46 PM
echo date('l jS \of F Y h:i:s A') . "\n";

// Imprime: 1 de julio de 2000 cae en sábado
echo "1 de julio de 2000 cae en " . date("l", mktime(0, 0, 0, 7, 1, 2000)) . "\n";

/* Usar las constantes en el parámetro de formato */
// Imprime algo como: Wed, 25 Sep 2013 15:28:57 -0700
echo date(DATE_RFC2822) . "\n";

// Imprime algo como: 2000-07-01T00:00:00+00:00
echo date(DATE_ATOM, mktime(0, 0, 0, 7, 1, 2000));

    
```php

Puede prevenir que un carácter reconocido en la cadena de formato sea expandido escapándolo con una barra invertida precedente. Si el carácter con una barra invertida es ya una secuencia especial, necesitará escapar también la barra invertida.

Escapando caracteres en `date`

```
<?php
// Imprime algo como: Wednesday the 15th
echo date('l \t\h\e jS');

    
```php

Algunos ejemplos de formatear `date`. Observe que debería escapar cualesquiera otros caracteres, ya que cualquiera que tenga actualmente un significado especial producirá resultados no deseados, y a otros caracteres se les pueden asignar significado en futuras versiones de PHP. Cuando se escapa un carácter, asegúrese de usar comillas simples para prevenir que caracteres como \n se conviertan en nuevas líneas.

Dando formato con `date`

```
<?php
// Asumiendo que hoy es 10 de marzo de 2001, 5:16:18 pm, y que estamos en la
// zona horaria Mountain Standard Time (MST)
date_default_timezone_set("America/Phoenix");

echo date("F j, Y, g:i a") . "\n";                 // March 10, 2001, 5:16 pm
echo date("m.d.y") . "\n";                         // 03.10.01
echo date("j, n, Y") . "\n";                       // 10, 3, 2001
echo date("Ymd") . "\n";                           // 20010310
echo date('h-i-s, j-m-y, it is w Day') . "\n";     // 05-16-18, 10-03-01, 1631 1618 6 Satpm01
echo date('\i\t \i\s \t\h\e jS \d\a\y.') . "\n";   // es el día 10.
echo date("D M j G:i:s T Y") . "\n";               // Sat Mar 10 17:16:18 MST 2001
echo date('H:m:s \m \i\s\ \m\o\n\t\h') . "\n";     // 17:03:18 m es el mes
echo date("H:i:s") . "\n";                         // 17:16:18
echo date("Y-m-d H:i:s") . "\n";                   // 2001-03-10 17:16:18 (el formato DATETIME de MySQL)

    
```php

Para formatear fechas en otros lenguajes, debería usar IntlDateFormatter::format en vez de `date`.

## Notas

> [!NOTE]
> Para generar una marca de tiempo desde una cadena que representa la fecha, puede usar `strtotime`. Además, algunas bases de datos tienen funciones para convertir formatos de fecha en marcas de tiempo (como la función [UNIX_TIMESTAMP](http://dev.mysql.com/doc/mysql/en/date-and-time-functions.html) de MySQL).

> [!TIP]
> La marca de tiempo del inicio de una petición está disponible en `$_SERVER['REQUEST_TIME']`.

## Véase también

DateTimeImmutable::\_\_construct, DateTimeInterface::format, `gmdate`, `idate`, `getdate`, `getlastmod`, `mktime`, IntlDateFormatter::format, `time`, [Constantes Predefinidas de DateTime](#datetimeinterface.constants.types)
