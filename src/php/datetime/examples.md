---
title: Ejemplos
source_url: https://www.php.net/manual/es/datetime.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: cd8b964b8
order: 10920
---

## Ejemplos

## Aritmética con DateTime

Los ejemplos siguientes muestran algunos problemas de la aritmética de DateTime en lo que respecta a las transiciones DST y los meses con diferente número de días.

DateTimeImmutable::add/sub añadir un intervalo de tiempo transcurrido

Añadir PT24H más allá de una transición DST parecerá añadir 23/25 horas (para la mayoría de los husos horarios).

```php
<?php
$dt = new DateTimeImmutable("2015-11-01 00:00:00", new DateTimeZone("America/New_York"));
echo "Inicio: ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;
$dt = $dt->add(new DateInterval("PT3H"));
echo "Fin:    ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;

    
```

El ejemplo anterior mostrará:

    Inicio:2015-11-01 00:00:00 -04:00
    Fin:2015-11-01 02:00:00 -05:00

DateTimeImmutable::modify y strtotime incrementar o decrementar valores individuales

Añadir +24 horas más allá de una transición DST puede añadir exactamente 24 horas como se ve con la cadena fecha/hora (excepto si la hora de inicio o fin está en un punto de transición).

```php
<?php
$dt = new DateTimeImmutable("2015-11-01 00:00:00", new DateTimeZone("America/New_York"));
echo "Inicio: ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;
$dt = $dt->modify("+24 hours");
echo "Fin:    ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;

    
```

El ejemplo anterior mostrará:

    Inicio:2015-11-01 00:00:00 -04:00
    Fin:2015-11-02 00:00:00 -05:00

La adición o sustracción de fechas/horas puede exceder (en más o en menos) fechas

Como para 31 de Enero + 1 mes dará como resultado 2 de Marzo (año bisiesto) o 3 de Marzo (año normal).

```php
<?php
echo "Año normal:\n"; // febrero tiene 28 días
$dt = new DateTimeImmutable("2015-01-31 00:00:00", new DateTimeZone("America/New_York"));
echo "Inicio: ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;
$dt = $dt->modify("+1 month");
echo "Fin:    ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;

echo "Año bisiesto:\n"; // febrero tiene 29 días
$dt = new DateTimeImmutable("2016-01-31 00:00:00", new DateTimeZone("America/New_York"));
echo "Inicio: ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;
$dt = $dt->modify("+1 month");
echo "Fin:    ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;

    
```

El ejemplo anterior mostrará:

    Año normal:
    Inicio:2015-01-31 00:00:00 -05:00
    Fin:2015-03-03 00:00:00 -05:00
    Año bisiesto:
    Inicio:2016-01-31 00:00:00 -05:00
    Fin:2016-03-02 00:00:00 -05:00

        

Para obtener el último día del mes próximo (es decir, para prever el excedente), el formato `last day of` está disponible.

```php
<?php
echo "Año normal:\n"; // febrero tiene 28 días
$dt = new DateTimeImmutable("2015-01-31 00:00:00", new DateTimeZone("America/New_York"));
echo "Inicio: ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;
$dt = $dt->modify("last day of next month");
echo "Fin:    ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;

echo "Año bisiesto:\n"; // febrero tiene 29 días
$dt = new DateTimeImmutable("2016-01-31 00:00:00", new DateTimeZone("America/New_York"));
echo "Inicio: ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;
$dt = $dt->modify("last day of next month");
echo "Fin:    ", $dt->format("Y-m-d H:i:s P"), PHP_EOL;

    
```

El ejemplo anterior mostrará:

    Año normal:
    Inicio:2015-01-31 00:00:00 -05:00
    Fin:2015-02-28 00:00:00 -05:00
    Año bisiesto:
    Inicio:2016-01-31 00:00:00 -05:00
    Fin:2016-02-29 00:00:00 -05:00
