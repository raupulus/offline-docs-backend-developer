---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/stomp.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87510
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [stomp.default_broker](#ini.stomp.default-broker) | tcp://localhost:61613 | `INI_ALL` |  |
| [stomp.default_connection_timeout_sec](#ini.stomp.default-connection-timeout-sec) | 2 | `INI_ALL` |  |
| [stomp.default_connection_timeout_usec](#ini.stomp.default-connection-timeout-usec) | 0 | `INI_ALL` |  |
| [stomp.default_read_timeout_sec](#ini.stomp.default-read-timeout-sec) | 2 | `INI_ALL` |  |
| [stomp.default_read_timeout_usec](#ini.stomp.default-read-timeout-usec) | 0 | `INI_ALL` |  |

Opciones de configuración Stomp

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`stomp.default_broker` `string`  
La URI broker por defecto a utilizar cuando conectemos a el message broker si otra URI no es especificada.

`stomp.default_connection_timeout_sec` `int`  
Los segundos parte del tiempo de espera de la solicitud de conexión por defecto.

`stomp.default_connection_timeout_usec` `int`  
Los microsegundos parte del tiempo de espera de la solicitud de conexión por defecto.

`stomp.default_read_timeout_sec` `int`  
Los segundos parte del tiempo de espera de lectura por defecto.

`stomp.default_read_timeout_usec` `int`  
Los microsegundos parte del tiempo de espera de lectura por defecto.
