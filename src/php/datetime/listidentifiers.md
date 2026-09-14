---
title: DateTimeZone::listIdentifiers
description: Devuelve un array numérico que contiene todos los identificadores de
  zonas horarias definidos
source_url: https://www.php.net/manual/es/datetimezone.listidentifiers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimezone/listidentifiers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: c142be811
order: 10900
---

DateTimeZone::listIdentifiers

timezone_identifiers_list

Devuelve un array numérico que contiene todos los identificadores de zonas horarias definidos

## Descripción

Estilo orientado a objetos

```php
public static DateTimeZone::listIdentifiers([int $timezoneGroup], [string $countryCode]): array
```php

Estilo procedimental

```php
timezone_identifiers_list([int $timezoneGroup], [string $countryCode]): array
```

Devuelve la lista de [identificadores de zona horaria de IANA](https://en.wikipedia.org/wiki/Tz_database#Names_of_timezones).

> [!NOTE]
> Es posible detectar la zona horaria del cliente (navegador) con JavaScript usando [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#timezone) o [Temporal.ZonedDateTime](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets).

## Parámetros

`timezoneGroup`  
Una (o una combinación) de las constantes de clase `DateTimeZone`.

`countryCode`  
Un código de país de dos letras (en mayúsculas), compatible con ISO 3166-1.

> [!NOTE]
> Esta opción solo está disponible cuando el argumento `timezoneGroup` toma el valor de `DateTimeZone::PER_COUNTRY`.

## Valores devueltos

Devuelve el `array` de identificadores de zonas horarias. Solo se devuelven los elementos no obsoletos. Para obtener todo, incluyendo los identificadores de zonas horarias obsoletos, utilice `DateTimeZone::ALL_WITH_BC` como valor para `timezoneGroup`.

## Historial de cambios

| Versión | Descripción                                                    |
|---------|----------------------------------------------------------------|
| 8.0.0   | Anterior a esta versión, `false` se devolvía en caso de error. |
| 7.1.0   | `countryCode` ahora es nullable.                               |

## Ejemplos

Lista de identificadores con comentarios de ubicación

```php
<?php
$identifiers = DateTimeZone::listIdentifiers(DateTimeZone::ALL);

foreach ($identifiers as $tzid) {
    $tz = new DateTimeZone($tzid);
    $comments = $tz->getLocation()['comments'];
    echo $tzid . " (" . ($comments ?: 'Toda la región') . ")\n";
}

    
```

Resultado del ejemplo anterior es similar a:

    America/Antigua (Toda la región)
    America/Araguaina (Tocantins)
    America/Argentina/Buenos_Aires (Buenos Aires (BA, CF))
    America/Argentina/Catamarca (Catamarca (CT), Chubut (CH))
    America/Argentina/Cordoba (Argentina (most areas: CB, CC, CN, ER, FM, MN, SE, SF))
    // (Salida recortada debido a la longitud)

Listar identificadores para una región específica

```php
<?php
$timezone_identifiers = DateTimeZone::listIdentifiers( DateTimeZone::ASIA );
for ($i=0; $i < 5; $i++) {
    echo "$timezone_identifiers[$i]\n";
}

    
```

Resultado del ejemplo anterior es similar a:

    Asia/Aden
    Asia/Almaty
    Asia/Amman
    Asia/Anadyr
    Asia/Aqtau

Listar identificadores de múltiples regiones

```php
<?php
$timezone_identifiers = DateTimeZone::listIdentifiers( DateTimeZone::ASIA | DateTimeZone::PACIFIC );
echo join( ', ', $timezone_identifiers );

    
```

Resultado del ejemplo anterior es similar a:

    Asia/Aden, Asia/Almaty, Asia/Amman, Asia/Anadyr, Asia/Aqtau, Asia/Aqtobe,
    Asia/Ashgabat, Asia/Atyrau, Asia/Baghdad, Asia/Bahrain, Asia/Baku,
    Asia/Bangkok, Asia/Barnaul, Asia/Beirut, Asia/Bishkek, Asia/Brunei,
    Asia/Chita, Asia/Choibalsan, Asia/Colombo, Asia/Damascus, Asia/Dhaka,
    Asia/Dili, Asia/Dubai, Asia/Dushanbe, Asia/Famagusta, Asia/Gaza, Asia/Hebron,
    Asia/Ho_Chi_Minh, Asia/Hong_Kong, Asia/Hovd, Asia/Irkutsk, Asia/Jakarta,
    Asia/Jayapura, Asia/Jerusalem, Asia/Kabul, Asia/Kamchatka, Asia/Karachi,
    Asia/Kathmandu, Asia/Khandyga, Asia/Kolkata, Asia/Krasnoyarsk,
    Asia/Kuala_Lumpur, Asia/Kuching, Asia/Kuwait, Asia/Macau, Asia/Magadan,
    Asia/Makassar, Asia/Manila, Asia/Muscat, Asia/Nicosia, Asia/Novokuznetsk,
    Asia/Novosibirsk, Asia/Omsk, Asia/Oral, Asia/Phnom_Penh, Asia/Pontianak,
    Asia/Pyongyang, Asia/Qatar, Asia/Qostanay, Asia/Qyzylorda, Asia/Riyadh,
    Asia/Sakhalin, Asia/Samarkand, Asia/Seoul, Asia/Shanghai, Asia/Singapore,
    Asia/Srednekolymsk, Asia/Taipei, Asia/Tashkent, Asia/Tbilisi, Asia/Tehran,
    Asia/Thimphu, Asia/Tokyo, Asia/Tomsk, Asia/Ulaanbaatar, Asia/Urumqi,
    Asia/Ust-Nera, Asia/Vientiane, Asia/Vladivostok, Asia/Yakutsk, Asia/Yangon,
    Asia/Yekaterinburg, Asia/Yerevan, Pacific/Apia, Pacific/Auckland,
    Pacific/Bougainville, Pacific/Chatham, Pacific/Chuuk, Pacific/Easter,
    Pacific/Efate, Pacific/Fakaofo, Pacific/Fiji, Pacific/Funafuti,
    Pacific/Galapagos, Pacific/Gambier, Pacific/Guadalcanal, Pacific/Guam,
    Pacific/Honolulu, Pacific/Kanton, Pacific/Kiritimati, Pacific/Kosrae,
    Pacific/Kwajalein, Pacific/Majuro, Pacific/Marquesas, Pacific/Midway,
    Pacific/Nauru, Pacific/Niue, Pacific/Norfolk, Pacific/Noumea,
    Pacific/Pago_Pago, Pacific/Palau, Pacific/Pitcairn, Pacific/Pohnpei,
    Pacific/Port_Moresby, Pacific/Rarotonga, Pacific/Saipan, Pacific/Tahiti,
    Pacific/Tarawa, Pacific/Tongatapu, Pacific/Wake, Pacific/Wallis

Listar identificadores de un solo país

```php
<?php
$timezone_identifiers = DateTimeZone::listIdentifiers( DateTimeZone::PER_COUNTRY, "UA" );
foreach( $timezone_identifiers as $identifier ) {
    echo "$identifier\n";
}

    
```

Resultado del ejemplo anterior es similar a:

    Europe/Kyiv
    Europe/Simferopol
    Europe/Uzhgorod
    Europe/Zaporozhye

## Véase también

`timezone_abbreviations_list`
