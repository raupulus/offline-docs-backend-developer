---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/datetime.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 11450
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [date.default_latitude](#ini.date.default-latitude) | "31.7667" | `INI_ALL` |  |
| [date.default_longitude](#ini.date.default-longitude) | "35.2333" | `INI_ALL` |  |
| [date.sunrise_zenith](#ini.date.sunrise-zenith) | "90.833333" | `INI_ALL` | Antes de PHP 8.0.0, el valor por omisión era "90.583333" |
| [date.sunset_zenith](#ini.date.sunset-zenith) | "90.833333" | `INI_ALL` | Antes de PHP 8.0.0, el valor por omisión era "90.583333" |
| [date.timezone](#ini.date.timezone) | "UTC" | `INI_ALL` | Desde PHP 8.2, se emite una advertencia si la opción se define con un valor inválido o una cadena vacía. |

Opciones de configuración para fechas y horas

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`date.default_latitude` `float`  
La latitud por omisión que va desde `0` en el ecuador, hasta `+90` en dirección norte, y `-90` en dirección sur.

`date.default_longitude` `float`  
La longitud por omisión que va desde `0` en el meridiano de origen, hasta `+180` en dirección este, y `-180` en dirección oeste.

`date.sunrise_zenith` `float`  
La hora de salida del sol por omisión.

El valor por omisión es 90°50'. Los 50' adicionales se deben a dos componentes: el radio del Sol, que es de 16', y la refracción atmosférica, que es de 34'.

`date.sunset_zenith` `float`  
La hora de puesta del sol por omisión.

`date.timezone` `string`  
La zona horaria por omisión utilizada por todas las funciones de fecha/hora. El orden de las zonas horarias utilizadas si ninguna se especifica está descrito explícitamente en la página de documentación de la función `date_default_timezone_get`. Ver [???](#timezones) para una lista completa de las zonas horarias soportadas.

> [!NOTE]
> Las cuatro primeras opciones de configuración se utilizan actualmente únicamente por las funciones `date_sunrise` y `date_sunset`.
