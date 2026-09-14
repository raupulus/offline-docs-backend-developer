---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/geoip.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26290
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [geoip.custom_directory](#ini.geoip.custom-directory) | "" | `INI_ALL` |  |

GeoIP Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`geoip.custom_directory` `string`  
Vacío por omisión, pero puede ser utilizado para cargar una base de datos diferente de la incluida en la biblioteca.
