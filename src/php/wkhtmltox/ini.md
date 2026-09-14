---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/wkhtmltox.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wkhtmltox/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wkhtmltox
translation_status: ready
translation_reviewed: false
translation_revision: '373591548'
order: 101860
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [wkhtmltox.graphics](#ini.wkhtmltox.graphics) | Off | `INI_SYSTEM`\|`INI_PERDIR` | \>= 0.3.2 |

wkhtmltox Opciones de configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`wkhtmltox.graphics` `bool`  
Permite que libwkhtmltox utilice gráficos.
