---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/swoole.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: true
translation_revision: d4854f421
order: 90670
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [swoole.enable_library](#ini.swoole.enable-library) | On | `INI_ALL` |  |
| [swoole.enable_fiber_mock](#ini.swoole.enable-fiber-mock) | Off | `INI_ALL` |  |
| [swoole.enable_preemptive_scheduler](#ini.swoole.enable-preemptive-scheduler) | Off | `INI_ALL` |  |
| [swoole.display_errors](#ini.swoole.display-errors) | On | `INI_ALL` |  |
| [swoole.use_shortname](#ini.swoole.use-shortname) | On | `INI_SYSTEM` |  |
| [swoole.unixsock_buffer_size](#ini.swoole.unixsock-buffer-size) | 8388608 | `INI_ALL` |  |

Opciones de configuración de Swoole

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`swoole.enable_library` `string`  
Activa o desactiva la biblioteca integrada de la extensión.

`swoole.enable_fiber_mock` `string`  
Activa o desactiva el uso de la extensión xdebug para depurar programas Swoole.

`swoole.enable_preemptive_scheduler` `string`  
Impide que ciertas corrutinas consuman demasiado tiempo de CPU en un bucle cerrado (10 ms de tiempo CPU), lo que podría impedir la planificación de otras corrutinas.

`swoole.display_errors` `string`  
Activa o desactiva la visualización de los mensajes de error de Swoole.

`swoole.use_shortname` `string`  
Activa o desactiva los alias cortos.

`swoole.unixsock_buffer_size` `int`  
Define el tamaño del búfer Socket para la comunicación interprocesos.
