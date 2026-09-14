---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/odbc.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: 6b194e05a
order: 99110
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [odbc.allow_persistent](#ini.uodbc.allow-persistent) | "1" | `INI_SYSTEM` |  |
| [odbc.check_persistent](#ini.uodbc.check-persistent) | "1" | `INI_SYSTEM` |  |
| [odbc.max_persistent](#ini.uodbc.max-persistent) | "-1" | `INI_SYSTEM` |  |
| [odbc.max_links](#ini.uodbc.max-links) | "-1" | `INI_SYSTEM` |  |
| [odbc.defaultlrl](#ini.uodbc.defaultlrl) | "4096" | `INI_ALL` |  |
| [odbc.defaultbinmode](#ini.uodbc.defaultbinmode) | "1" | `INI_ALL` |  |
| [odbc.default_cursortype](#ini.uodbc.defaultcursortype) | "3" | `INI_ALL` |  |

Opciones de configuración UODBC

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`odbc.default_db` `string`  
La fuente de datos ODBC si no se especifica ninguna en las funciones `odbc_connect` o `odbc_pconnect`.

`odbc.default_user` `string`  
Nombre de usuario a utilizar si no se especifica ninguno en las funciones `odbc_connect` o `odbc_pconnect`.

`odbc.default_pw` `string`  
Contraseña a utilizar si no se especifica ninguna en las funciones `odbc_connect` o `odbc_pconnect`.

`odbc.allow_persistent` `bool`  
¿Se permiten las conexiones ODBC persistentes o no?

`odbc.check_persistent` `bool`  
Verifica que la conexión sea válida antes de utilizarla.

`odbc.max_persistent` `int`  
Número máximo de conexiones persistentes por proceso.

`odbc.max_links` `int`  
El número máximo de conexiones ODBC por proceso, incluyendo las conexiones persistentes.

`odbc.defaultlrl` `int`  
Gestión de campos de tipo LONG. Especifica el número de bytes devueltos en las variables. Consulte `odbc_longreadlen` para más información.

Cuando se utiliza un `int`, el valor se mide en bytes. También se puede usar la notación abreviada, como se describe en [esta FAQ](#faq.using.shorthandbytes).

`odbc.defaultbinmode` `int`  
Gestión de datos binarios. Consulte `odbc_binmode` para más información.

`odbc.default_cursortype` `int`  
Controla el modelo de cursor ODBC. Valores posibles: `SQL_CURSOR_FORWARD_ONLY`, `SQL_CURSOR_KEYSET_DRIVEN`, `SQL_CURSOR_DYNAMIC` y `SQL_CURSOR_STATIC` (por defecto).
