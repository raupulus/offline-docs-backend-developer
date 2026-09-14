---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/yar.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_revision: d4d5216e7
order: 107480
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [yar.packager](#ini.yar.packager) | php | `INI_SYSTEM` |  |
| [yar.debug](#ini.yar.debug) | Off | `INI_ALL` |  |
| [yar.connect_timeout](#ini.yar.connect-timeout) | 1000 | `INI_ALL` |  |
| [yar.timeout](#ini.yar.timeout) | 5000 | `INI_ALL` |  |
| [yar.expose_info](#ini.yar.expose-info) | On | `INI_SYSTEM` |  |

Yar Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`yar.packager` `string`  
Podría ser php, json, y msgpack (requiere construcción con soporte para msgpack)

`yar.debug` `string`  

`yar.connect_timeout` `int`  
Tiempo de espera en ms

`yar.timeout` `int`  
Tiempo de espera en ms

`yar.expose_info` `bool`  
Si exponer la información del servicio (al acceder al servidor mediante GET)
