---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/mailparse.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_reviewed: true
translation_revision: 01bd007b0
order: 44450
---

## Instalación/Configuración

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [mailparse.def_charset](#ini.mailparse.def_charset) | "us-ascii" | `INI_SYSTEM` |  |

Mailparse Opciones de configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`mailparse.def_charset` `string`  
El juego de caracteres por omisión.

## Tipos de recursos

Mailparse define el tipo de recurso `mailparse_mail_structure`, que es devuelto por `mailparse_msg_create` y `mailparse_msg_parse_file`.
