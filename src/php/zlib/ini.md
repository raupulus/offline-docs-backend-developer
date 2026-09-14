---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/zlib.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_revision: d4d5216e7
order: 109030
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

La extensión zlib ofrece la opción de comprimir de manera trasparente las páginas sobre la marcha, si el navegador que hace la solicitud lo soporta. Por lo tanto hay tres opciones en el [archivo de configuración](#configuration.file) `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [zlib.output_compression](#ini.zlib.output-compression) | "0" | `INI_ALL` |  |
| [zlib.output_compression_level](#ini.zlib.output-compression-level) | "-1" | `INI_ALL` |  |
| [zlib.output_handler](#ini.zlib.output-handler) | "" | `INI_ALL` |  |

Opciones de Configuración de Zlib

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`zlib.output_compression` `bool`/`int`  
Para comprimir páginas transparentemente. Si esta opción está configurada en "On" en `php.ini` o en la configuración de Apache, las páginas serán comprimidas si el navegador envía un encabezado "Accept-Encoding: gzip" o "deflate". Los encabezados "Content-Encoding: gzip" (respectivamente "deflate") y "Vary: Accept-Encoding" serán agregados a la salida. En tiempo de ejecución, esto se puede configurar sólo antes de enviar cualquier salida.

Esta opción también acepta valores enteros (integer) en lugar de boolean en "On"/"Off", usando esto se puede configurar el tamaño del buffer de salida (por defecto es 4KB).

> [!NOTE]
> [output_handler](#ini.output-handler) debe estar vacío si ésta se configura en 'On' ! De otra manera se debe usar `zlib.output_handler`.

`zlib.output_compression_level` `int`  
Nivel de compresión usado para la salida de la compresión transparente. Especifica un valor entre 0 (no comprimido) y 9 (máxima compresión). El valor por defecto es -1, que deja que el servidor decida cual nivel utilizar.

`zlib.output_handler` `string`  
No se pueden especificar manejadores adicionales de salida si zlib.output_compression está activada aquí. Esta configuración hace lo mismo que [ output_handler](#ini.output-handler) pero en un orden diferente.
