---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/v8js.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/v8js/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: v8js
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 100310
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [v8js.max_disposed_contexts](#ini.v8js.max-disposed-contexts) | 25 | `INI_ALL` |  |
| [v8js.flags](#ini.v8js.flags) |  | `INI_ALL` |  |

V8js Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`v8js.max_disposed_contexts` `int`  
Establece límite para contextos dispuestas antes de forzar V8 que hacer la recolección de basura.

`v8js.flags` `string`  
Establece V8 opciones de la línea de comandos. La lista de los indicadores disponibles se puede obtener en el modo CLI estableciendo este parámetro en `--help`. Ejemplo:

    $ php -r 'ini_set("v8js.flags", "--help"); new V8Js;' | less

> [!NOTE]
> Por estas banderas para ser eficaz en tiempo de ejecución de la ini_set () llamada se tiene que hacer antes de que los objetos se instancian V8Js!
