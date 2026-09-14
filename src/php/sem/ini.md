---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/sem.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_revision: fd2f14b2e
order: 73630
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [sysvshm.init_mem](#ini.sysvshm.init-mem) | 10000 | `INI_SYSTEM` |  |

Opciones de Configuración del Semáforo

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`sysvshm.init_mem` `int`  
Un tamaño predeterminado del segmento de memoria compartida.
