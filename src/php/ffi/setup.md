---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/ffi.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 23110
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere que la [biblioteca libffi](https://sourceware.org/libffi/) esté instalada.

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [ffi.enable](#ini.ffi.enable) | "preload" | `INI_SYSTEM` |  |
| [ffi.preload](#ini.ffi.preload) | "" | `INI_SYSTEM` |  |

FFI Opciones de configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`ffi.enable` `string`  
Permite activar (`"true"`) o desactivar (`"false"`) el uso de la API FFI, o restringirlo únicamente a la interfaz CLI SAPI y a los ficheros pre-cargados (`"preload"`).

Las restricciones de la API FFI afectan solo a la clase `FFI`, pero no a las funciones sobrecargadas de los objetos `FFI\CData`. Esto significa que es posible crear ciertos objetos `FFI\CData` en ficheros pre-cargados y luego utilizarlos directamente en scripts PHP.

`ffi.preload` `string`  
Permite la pre-carga de las ligaduras FFI al inicio, lo cual no es posible con FFI::load si [opcache.preload_user](#ini.opcache.preload-user) está definido. Esta directiva acepta una lista de nombres de ficheros delimitada por `DIRECTORY_SEPARATOR`. Las ligaduras pre-cargadas son accesibles llamando a FFI::scope.
