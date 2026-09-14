---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/xhprof.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xhprof/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xhprof
translation_status: ready
translation_revision: d4d5216e7
order: 102350
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [xhprof.output_dir](#ini.xhprof.output-dir) | "" | `INI_ALL` |  |

Xhprof Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`xhprof.output_dir` `string`  
Directorio utilizado por la aplicación por defecto de la interfaz iXHProfRuns (es decir, la clase XHProfRuns_Default) para el almacenamiento XHProf.
