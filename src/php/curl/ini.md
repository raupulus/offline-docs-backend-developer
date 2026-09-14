---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/curl.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: d4d5216e7
order: 10160
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [curl.cainfo](#ini.curl.cainfo) | NULL | `INI_SYSTEM` |  |

Opciones de Configuración de cURL

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`curl.cainfo` `string`  
Define un valor predeterminado para la opción `CURLOPT_CAINFO`. Debe especificarse una ruta absoluta.
