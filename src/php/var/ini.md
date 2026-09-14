---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/var.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_revision: d4d5216e7
order: 100810
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [unserialize_callback_func](#ini.unserialize-callback-func) | `null` | `INI_ALL` |  |
| [unserialize_max_depth](#ini.unserialize-max-depth) | "4096" | `INI_ALL` | Disponible desde PHP 7.4.0. |

Opciones de configuración de variables

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`unserialize_callback_func` `string`  
La función indicada es llamada cuando `unserialize` intenta utilizar una clase no definida. Aparece una advertencia si la función indicada no está definida o si la función no logra definir la clase faltante.

Véase también `unserialize` y [Autocarga de clases](#language.oop5.autoload).

`unserialize_max_depth` `int`  
La profundidad máxima de estructuras permitida durante la deserialización cuando se utiliza `unserialize`, y está destinada a evitar desbordamientos de pila. Esto se puede desactivar estableciendo `unserialize_max_depth=0`.

Véase también `unserialize` y [Autocarga de clases](#language.oop5.autoload).
