---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/outcontrol.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: false
translation_revision: 2a8768782
order: 59700
---

## Constantes predefinidas

Las constantes listadas aquí están siempre disponibles en PHP.

`PHP_OUTPUT_HANDLER_START` (`int`)  
Indica que el almacenamiento en búfer de salida ha comenzado.

`PHP_OUTPUT_HANDLER_WRITE` (`int`)  
Indica que el búfer de salida ha comenzado a ser mostrado y contiene datos.

`PHP_OUTPUT_HANDLER_FLUSH` (`int`)  
Indica que el búfer ha sido mostrado.

`PHP_OUTPUT_HANDLER_CLEAN` (`int`)  
Indica que el búfer de salida ha sido limpiado.

`PHP_OUTPUT_HANDLER_FINAL` (`int`)  
Indica que es la operación final de almacenamiento en búfer de salida.

`PHP_OUTPUT_HANDLER_CONT` (`int`)  
Indica que el búfer ha sido mostrado, pero el almacenamiento en búfer de salida continúa.

Es un alias de la constante `PHP_OUTPUT_HANDLER_WRITE`.

`PHP_OUTPUT_HANDLER_END` (`int`)  
Indica que el almacenamiento en búfer de salida ha finalizado.

Es un alias de la constante `PHP_OUTPUT_HANDLER_FINAL`.

<!-- -->

`PHP_OUTPUT_HANDLER_CLEANABLE` (`int`)  
Controla si un búfer de salida creado por la función `ob_start` puede ser eliminado por `ob_clean`. Este indicador no controla el comportamiento de `ob_end_clean` o `ob_get_clean`.

`PHP_OUTPUT_HANDLER_FLUSHABLE` (`int`)  
Controla si un búfer de salida creado por la función `ob_start` puede ser enviado a la salida estándar por `ob_flush`. Este indicador no controla el comportamiento de `ob_end_flush` o `ob_get_flush`.

`PHP_OUTPUT_HANDLER_REMOVABLE` (`int`)  
Controla si un búfer de salida creado por la función `ob_start` puede ser eliminado antes del final del script o durante la llamada a `ob_end_clean`, `ob_end_flush`, `ob_get_clean` o `ob_get_flush`.

`PHP_OUTPUT_HANDLER_STDFLAGS` (`int`)  
El conjunto por defecto de indicadores para el búfer de salida; actualmente, equivalente a `PHP_OUTPUT_HANDLER_CLEANABLE` \| `PHP_OUTPUT_HANDLER_FLUSHABLE` \| `PHP_OUTPUT_HANDLER_REMOVABLE`.

<!-- -->

`PHP_OUTPUT_HANDLER_STARTED` (`int`)  
Indica que el controlador de salida ha sido llamado.

`PHP_OUTPUT_HANDLER_DISABLED` (`int`)  
Indica que el controlador de salida está desactivado. Este indicador se define cuando el controlador de salida devuelve `false` o falla durante el procesamiento del búfer. Antes de PHP 8.4.0, este indicador podía estar definido durante el inicio de un búfer de salida.

`PHP_OUTPUT_HANDLER_PROCESSED` (`int`)  
Indica que el controlador de salida ha procesado con éxito el búfer. Disponible desde PHP 8.4.0.
