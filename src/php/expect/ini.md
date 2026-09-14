---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/expect.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/expect/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: expect
translation_status: ready
translation_revision: ca6054f60
order: 20790
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

La extensión Expect se configura mediante opciones del [fichero de configuración](#configuration.file) `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [expect.timeout](#ini.expect.timeout) | "10" | `INI_ALL` |  |
| [expect.loguser](#ini.expect.loguser) | "1" | `INI_ALL` |  |
| [expect.logfile](#ini.expect.logfile) | "" | `INI_ALL` |  |
| [expect.match_max](#ini.expect.match-max) | "" | `INI_ALL` |  |

Opciones de configuración de Expect

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`expect.timeout` `int`  
Tiempo de espera de datos, al usar la función `expect_expectl`.

El valor en "-1" deshabilita el tiempo de espera.

> [!NOTE]
> El valor en "0" provoca que `expect_expectl` devuelva el control inmediatamente.

`expect.loguser` `bool`  
Indica si Expect debe enviar alguna salida del proceso creado a la salida estándar. Dado que normalmente los programas interactivos imprimen en pantalla los datos de entrada, esto sería suficiente para poder mostrar los dos lados de la conversación.

`expect.logfile` `string`  
Nombre del fichero en el que se escribirá la salida del proceso creado. Si no existiera, se crearía.

> [!NOTE]
> Si se establece un valor, se escribe la salida independientemente del valor de [expect.loguser](#ini.expect.loguser).

`expect.match_max` `int`  
Cambia el tamaño predeterminado (2000 bytes) del buffer utilizado para que coincida con los asteriscos en el patrón.
