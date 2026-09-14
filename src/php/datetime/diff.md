---
title: DateTimeInterface::diff
description: Devuelve la diferencia entre dos objetos DateTime
source_url: https://www.php.net/manual/es/datetime.diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface/diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10740
---

DateTimeInterface::diff

DateTimeImmutable::diff

DateTime::diff

date_diff

Devuelve la diferencia entre dos objetos DateTime

## Descripción

Estilo orientado a objetos

```php
public DateTimeInterface::diff(DateTimeInterface $targetObject, [bool $absolute]): DateInterval
```php

```php
public DateTimeImmutable::diff(DateTimeInterface $targetObject, [bool $absolute]): DateInterval
```

```php
public DateTime::diff(DateTimeInterface $targetObject, [bool $absolute]): DateInterval
```php

Estilo procedimental

```php
date_diff(DateTimeInterface $baseObject, DateTimeInterface $targetObject, [bool $absolute]): DateInterval
```

Devuelve la diferencia entre dos objetos `DateTimeInterface`.

## Parámetros

`datetime`  
La fecha a comparar.

`absolute`  
¿Debería el intervalo forzado a ser positivo?

## Valores devueltos

El objeto `DateInterval` que representa la diferencia entre dos fechas.

El parámetro `absolute` solo afecta a la propiedad `invert` de un objeto `DateInterval`.

El valor devuelto más especificamente, representa el intervalo de tiempo que habría que aplicar al objeto original (`$this` o `$originObject`) para llegar a `$targetObject`. Este proceso no siempre es reversible.

El método tiene en cuenta los cambios de horario de verano y, por lo tanto, puede devolver un intervalo de `24 horas y 30 minutos`, como en uno de los ejemplos. Si quieres calcular un tiempo absoluto, debes comvertir ambos `$this`/`$baseObject`, y `$targetObject` primero a UTC.

## Ejemplos

Ejemplo de `DateTime::diff`

Estilo orientado a objetos

```php
<?php
$origin = new DateTimeImmutable('2009-10-11');
$target = new DateTimeImmutable('2009-10-13');
$interval = $origin->diff($target);
echo $interval->format('%R%a days');

   
```

El ejemplo anterior mostrará:

    +2 days

       

Estilo procedimental

```php
<?php
$origin = date_create('2009-10-11');
$target = date_create('2009-10-13');
$interval = date_diff($origin, $target);
echo $interval->format('%R%a days');

   
```

El ejemplo anterior mostrará:

    +2 days

DateTimeInterface::diff durante el cambio de horario de verano

```php
<?php
$originalTime = new DateTimeImmutable("2021-10-30 09:00:00 Europe/London");
$targetTime = new DateTimeImmutable("2021-10-31 08:30:00 Europe/London");
$interval = $originalTime->diff($targetTime);
echo $interval->format("%H:%I:%S (Días completos: %a)"), "\n";

   
```

El ejemplo anterior mostrará:

    24:30:00 (Días completos: 0)

Rango de DateTimeInterface::diff

El valor devuelto es la cantidad de tiempo exacto entre `$this` y `$targetObject`. Comparando del 1 de enero al 31 de diciembre devuelve 364 días, y no 365 (para años no bisiestos).

```php
<?php
$originalTime = new DateTimeImmutable("2023-01-01 UTC");
$targetTime = new DateTimeImmutable("2023-12-31 UTC");
$interval = $originalTime->diff($targetTime);
echo "Días completos: ", $interval->format("%a"), "\n";

   
```

El ejemplo anterior mostrará:

    Días completos: 364

Comparación de objetos `DateTime`

> [!NOTE]
> Los objetos `DateTimeImmutable` y `DateTime` se pueden comparar usando los [operadores de comparación](#language.operators.comparison).

```php
<?php
$date1 = new DateTime("now");
$date2 = new DateTime("tomorrow");

var_dump($date1 == $date2);
var_dump($date1 < $date2);
var_dump($date1 > $date2);

   
```

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
    bool(false)

## Véase también

DateInterval::format

DateTime::add

DateTime::sub
