---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/misc.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: e50e79746
order: 47310
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [ignore_user_abort](#ini.ignore-user-abort) | "0" | `INI_ALL` |  |
| [highlight.string](#ini.syntax-highlighting) | "#DD0000" | `INI_ALL` |  |
| [highlight.comment](#ini.syntax-highlighting) | "#FF8000" | `INI_ALL` |  |
| [highlight.keyword](#ini.syntax-highlighting) | "#007700" | `INI_ALL` |  |
| [highlight.default](#ini.syntax-highlighting) | "#0000BB" | `INI_ALL` |  |
| [highlight.html](#ini.syntax-highlighting) | "#000000" | `INI_ALL` |  |
| [browscap](#ini.browscap) | NULL | `INI_SYSTEM` |  |

Opciones de configuración diversos

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`ignore_user_abort` `bool`  
`false` por omisión. Si se cambia a `true` los scripts no se terminarán después de que el cliente anule su conexión.

Ver también `ignore_user_abort`.

`highlight.bg` `string`; `highlight.comment` `string`; `highlight.default` `string`; `highlight.html` `string`; `highlight.keyword` `string`; `highlight.string` `string`  
Colores utilizados para el modo de resaltado sintáctico. Estas opciones pueden tomar cualquier valor válido en `<font color="??????">`.

`browscap` `string`  
Nombre del archivo de descripción de clientes HTML. (ej.: `browscap.ini`) Ver también `get_browser`.
