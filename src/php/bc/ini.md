---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/bc.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_revision: c7e83fbbb
order: 6360
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [bcmath.scale](#ini.bcmath.scale) | "0" | `INI_ALL` |  |

BCmath Opciones de Configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`bcmath.scale` `integer`  
Número de dígitos decimales para todas las funciones bcmath. Ver también `bcscale`.

> [!NOTE]
> `BcMath\Number` no se ve afectado por esta configuración.
