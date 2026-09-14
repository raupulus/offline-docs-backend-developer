---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/igbinary.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/igbinary/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: igbinary
translation_status: ready
translation_reviewed: false
translation_revision: 43dd38b94
order: 31320
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [igbinary.compact_strings](#ini.igbinary.compact-strings) | 1 | `INI_ALL` |  |

Igbinary Opciones de configuración

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [session.save_handler](#ini.igbinary.save-handler) | "files" | `INI_ALL` |  |

Opciones de configuración de sesión que afectan al comportamiento de igbinary

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`igbinary.compact_strings` `bool`  
Activa o no el compactado de strings duplicados. El valor por omisión es On.

`session.save_handler` `string`  
Igbinary es utilizado como gestor de sesión al establecer el valor de esta opción a `igbinary`.
