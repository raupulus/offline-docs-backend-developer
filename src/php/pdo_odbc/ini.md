---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/pdo-odbc.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_odbc/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_odbc
translation_status: ready
translation_revision: d4d5216e7
order: 62450
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [pdo_odbc.connection_pooling](#ini.pdo-odbc.connection-pooling) | "strict" | `INI_ALL` |  |
| [pdo_odbc.db2_instance_name](#ini.pdo-odbc.db2-instance-name) | NULL | `INI_SYSTEM` | Esta funcionalidad obsoleta *será* ciertamente *eliminada* en el futuro. |

Opciones de configuración de PDO_ODBC

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`pdo_odbc.connection_pooling` `string`  
Si agrupar conexiones de ODBC. Se puede usar `"strict"`, `"relaxed"` o `"off"` (que es igual a `""`). El parámetro describe cómo de estricta debería ser el administrador de conexiones cuando coincidan los parámetros de conexión con conexiones existentes en la agrupación. `strict` es el valor predetermiando recomendado, y dará como resultado en el uso de conexiones almacenadas en caché solamente cuando todos los parámetros de conexión coincidan exactamente. `relaxed` dará como resultado el uso de conexiones almacenadas en caché cuando se utilicen parámetros de conexión similares. Esto puede resultar en el aumento del uso de la caché, con el riesgo de perder información de conexión entre (por ejemplo) hosts virtuales.

Este ajuste solamente se puede cambiar desde el fichero `php.ini`, y afecta al proceso completo; cualquier otro módulo dentro del proceso que utilice las mismas bibliotecas de ODBC también se verá afectado, incluyendo la [Extensión ODBC Unificada](#ref.uodbc).

> [!WARNING]
> `relaxed` no debería usarse en servidores compartidos, por razones de seguridad.

> [!TIP]
> Deje este ajuste a la configuración `strict` predeterminada a menos que tenga una buena razón para cambiarlo.

`pdo_odbc.db2_instance_name` `string`  
Si se compila PDO_ODBC usando el sabor `db2`, este ajuste establece el valor de la variable de entorno DB2INSTANCE en sistemas operativos Linux y UNIX al nombre especificado de la instancia de DB2. También habilita PDO_ODBC para resolver la ubicación de las bibliotecas de DB2 y realizar conexiones catalogadas a bases de datos DB2.

Este ajuste solamente se puede cambiar desde el fichero `php.ini`, y afecta al proceso completo; cualquier otro módulo dentro del proceso que utilice las mismas bibliotescas de ODBC también se verá afectado, incluyendo la [Extensión ODBC Unificada](#ref.uodbc).

Este ajuste no tiene efecto en Windows.
