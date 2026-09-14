---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/image.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_revision: d4d5216e7
order: 32560
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [gd.jpeg_ignore_warning](#ini.gd.jpeg-ignore-warning) | "1" | `INI_ALL` |  |

Opciones de configuración de Imagen

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`gd.jpeg_ignore_warning` `bool`  
Ignora las advertencias (pero no los errores) creadas por libjpeg(-turbo).

| Versión | Descripción |
|----|----|
| 7.1.0 | El valor predeterminado de gd.jpeg_ignore_warning ha cambiado de 0 a 1. |

Registro de cambios para `gd.jpeg_ignore_warning`

Véase también las directivas de configuración de [exif](#exif.configuration).

> [!WARNING]
> Las funciones de imagen consumen mucha memoria. Asegúrese de establecer [memory_limit](#ini.memory-limit) con un valor bastante alto, si está utilizando la versión incluida de la biblioteca GD.
