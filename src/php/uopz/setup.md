---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/uopz.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99470
---

## Instalación/Configuración

## Requisitos

A partir de uopz 5.0, PHP 7.0 es necesario. A partir de uopz 5.1, PHP 7.1+ es necesario.

## Instalación

Las versiones de uopz están alojadas por PECL y el código fuente por [github](https://github.com/krakjoe/uopz); la forma más sencilla de instalarlo es a través de la instalación via PECL : <https://pecl.php.net/package/uopz>.

Los usuarios de Windows pueden descargar los binarios desde el sitio web de [PECL](https://pecl.php.net/package/uopz).

A partir de uopz 5.0.0, la extensión debe ser cargada como una [extensión](#ini.extension). Anterior a esta versión, debe ser cargada como una [zend_extension](#ini.zend-extension).

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [uopz.disable](#ini.uopz.disable) | "0" | `INI_SYSTEM` | Disponible a partir de uopz 5.0.2 |
| [uopz.exit](#ini.uopz.exit) | "0" | `INI_SYSTEM` | Disponible a partir de uopz 6.0.1 |
| [uopz.overloads](#ini.uopz.overloads) | "1" | `INI_SYSTEM` | Disponible a partir de uopz 2.0.2. Eliminado a partir de uopz 5.0.0. |

uopz Opciones de configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`uopz.disable` `bool`  
Si está activado, uopz no debería tener ningún efecto sobre el motor.

`uopz.exit` `bool`  
Permitir o no la ejecución de los códigos de operación (opcodes) de salida. Este parámetro puede ser sobreescrito durante la ejecución llamando a `uopz_allow_exit`.

`uopz.overloads` `bool`  
Activa la posibilidad de utilizar `uopz_overload`.

> [!NOTE]
> Al ejecutar con OPcache activado, puede ser necesario desactivar todas las [optimizaciones OPcache](#ini.opcache.optimization-level) (`opcache.optimization_level=0`).
