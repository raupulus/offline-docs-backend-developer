---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/yaconf.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaconf/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaconf
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 104410
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [yaconf.check_delay](#ini.yaconf.check-delay) | 300 | `INI_SYSTEM` |  |
| [yaconf.directory](#ini.yaconf.directory) | /tmp/conf/ | `INI_SYSTEM` |  |

Yaconf Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`yaconf.check_delay` `int`  
En que intervalo Yaconf detectará el cambio del archivo ini (por el directorio mtime), si se pone a cero, hay que reiniciar el php para recargar las configuraciones.

`yaconf.directory` `string`  
Ruta al directorio en el que se encuentran todos los archivos de configuración INI.
