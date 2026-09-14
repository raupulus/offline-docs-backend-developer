---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/tidy.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: true
translation_revision: d4d5216e7
order: 93960
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [tidy.default_config](#ini.tidy.default-config) | "" | `INI_SYSTEM` |  |
| [tidy.clean_output](#ini.tidy.clean-output) | "0" | `INI_USER` |  |

Opciones de Configuración de Tidy

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`tidy.default_config` `string`  
Ruta por defecto al archivo de configuración tidy.

`tidy.clean_output` `bool`  
Activa/Desactiva la reparación del HTML por Tidy.

> [!WARNING]
> No active `tidy.clean_output` si usted está generando contenido distinto al html, como por ejemplo imágenes dinámicas.
