---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/imap.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_revision: d4d5216e7
order: 38690
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) | "0" | `INI_SYSTEM` | Disponible a partir de PHP 7.1.25, 7.2.13 y 7.3.0. Anteriormente, estaba activado implícitamente. |

IMAP Opciones de configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`imap.enable_insecure_rsh` `bool`  
Establecer una conexión a un servidor puede invocar comandos `rsh` o `ssh`, a menos que esta opción `php.ini` esté desactivada.

> [!WARNING]
> Ni PHP ni la biblioteca IMAP filtran los nombres de los buzones antes de pasarlos a los comandos `rsh` o `ssh`, por lo tanto, pasar datos no fiables a esta función sin desactivar esta opción `php.ini` es *peligroso*.
