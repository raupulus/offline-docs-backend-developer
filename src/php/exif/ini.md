---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/exif.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exif/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exif
translation_status: ready
translation_revision: 6a08181be
order: 20720
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

Exif soporta automáticamente la conversión de codificaciones de caracteres Unicode y JIS de comentarios de usuario cuando el módulo [mbstring](#ref.mbstring) está disponible. Ésto se realiza primero decodificando el comentario utilizando el conjunto de caracteres especificado. El resultado después es codificado con otro conjunto de caracteres que debería de coincidir con su salida `HTTP`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [exif.encode_unicode](#ini.exif.encode-unicode) | "ISO-8859-15" | `INI_ALL` |  |
| [exif.decode_unicode_motorola](#ini.exif.decode-unicode-motorola) | "UCS-2BE" | `INI_ALL` |  |
| [exif.decode_unicode_intel](#ini.exif.decode-unicode-intel) | "UCS-2LE" | `INI_ALL` |  |
| [exif.encode_jis](#ini.exif.encode-jis) | "" | `INI_ALL` |  |
| [exif.decode_jis_motorola](#ini.exif.decode-jis-motorola) | "JIS" | `INI_ALL` |  |
| [exif.decode_jis_intel](#ini.exif.decode-jis-intel) | "JIS" | `INI_ALL` |  |

Opciones de configuración de Exif

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`exif.encode_unicode` `string`  
`exif.encode_unicode` define el conjunto de caracteres UNICODE de los comentarios de usuario que se están tratando. Por defecto es ISO-8859-15 lo que debería funcionar para la mayoría de los países no asiáticos. La configuración puede estar vacía o debe ser una codificacion soportada por mbstring. Si está vacía se usa la codificación interna actual de mbstring.

`exif.decode_unicode_motorola` `string`  
`exif.decode_unicode_motorola` define el conjunto de caracteres interno de la imagen para comentarios de usuario codificados con Unicode si la imagen está con el orden de byte de motorola (big-endian). Esta configuración no puede estar vacía pero puede especificar una lista de codificaciones soportadas por mbstring. El valor por defecto es UCS-2BE.

`exif.decode_unicode_intel` `string`  
`exif.decode_unicode_intel` define el conjunto de caracteres interno de la imagen para comentarios de usuario codificados con Unicode si la imagen está con el orden de byte de intel (little-endian). Esta configuración no puede estar vacía pero puede especificar una lista de codificaciones soportadas por mbstring. El valor por defecto es UCS-2LE.

`exif.encode_jis` `string`  
`exif.encode_jis` define el conjunto de caracteres JIS de los comentarios de usuario que se están tratando. Por defecto está vacía lo que fuerza a las funciones a usar la codificación interna actual de mbstring.

`exif.decode_jis_motorola` `string`  
`exif.decode_jis_motorola` define el conjunto de caracteres interno de la imagen para los comentarios de usuario codificados con JIS si la imagen está con el orden de byte de motorola (big-endian). Esta configuración no puede estar vacía pero puede especificar una lista de codificaciones soportadas por mbstring. El valor por defecto es JIS.

`exif.decode_jis_intel` `string`  
`exif.decode_jis_intel` define el conjunto de caracteres interno de la imagen para los comentarios de usuario codificados con JIS si la imagen está con el orden de byte de intel (little-endian). Esta configuración no puede estar vacía pero puede especificar una lista de codificaciones soportadas por mbstring. El valor por defecto es JIS.
