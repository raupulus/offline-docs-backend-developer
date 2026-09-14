---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/mongodb.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48830
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [mongodb.debug](#ini.mongodb.debug) | "" | `INI_ALL` |  |

mongodb Opciones de configuración

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`mongodb.debug` `string`  
Esta opción puede usarse para activar o desactivar el registro de depuración a nivel de traza en la extensión (y en libmongoc).

Especifique una cadena vacía, `"0"`, `"off"`, `"no"` o `"false"` para desactivar el registro.

Especifique `"stderr"` o `"stdout"` para registrar en `stderr` o `stdout`, respectivamente.

Especifique `"1"`, `"on"`, `"yes"` o `"true"` para registrar en un nuevo fichero temporal dentro del directorio temporal del sistema por omisión (es decir, `sys_get_temp_dir`).

Especifique cualquier otra cadena para registrar en un nuevo fichero temporal dentro de ese directorio. Si el directorio no puede usarse, se usará el directorio temporal del sistema por omisión.

> [!NOTE]
> Tenga en cuenta que el registro de depuración puede contener información sensible, como credenciales del servidor MongoDB y documentos completos escritos o leídos del servidor. Revise cualquier registro de depuración antes de compartirlos con otras personas.
