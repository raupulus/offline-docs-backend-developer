---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/iconv.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: d4d5216e7
order: 31280
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [iconv.input_encoding](#ini.iconv.input-encoding) | "" | `INI_ALL` | Deprecado en PHP 5.6.0. |
| [iconv.output_encoding](#ini.iconv.output-encoding) | "" | `INI_ALL` | Deprecado en PHP 5.6.0. |
| [iconv.internal_encoding](#ini.iconv.internal-encoding) | "" | `INI_ALL` | Deprecado en PHP 5.6.0. |

Opciones de configuración iconv

Aquí hay una aclaración sobre el uso de las directivas de configuración.

> [!WARNING]
> Algunos sistemas (como IBM AIX) utilizan `"ISO8859-1"` en lugar de `"ISO-8859-1"`, por lo que este valor debe ser utilizado en las opciones de configuración así como en los argumentos de las funciones.

`iconv.input_encoding` `string`  
> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 5.6.0. Depender de esta funcionalidad está altamente desaconsejado.

Los usuarios de PHP 5.6 y versiones posteriores deben dejar esta opción vacía y definir en su lugar la opción [input_encoding](#ini.input-encoding).

`iconv.output_encoding` `string`  
> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 5.6.0. Depender de esta funcionalidad está altamente desaconsejado.

Los usuarios de PHP 5.6 y versiones posteriores deben dejar esta opción vacía y definir en su lugar la opción [output_encoding](#ini.output-encoding).

`iconv.internal_encoding` `string`  
> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 5.6.0. Depender de esta funcionalidad está altamente desaconsejado.

Los usuarios de PHP 5.6 y versiones posteriores deben dejar esta opción vacía y definir en su lugar la opción [`default_charset`](#ini.default-charset).
