---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/ibm-db2.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 31130
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [ibm_db2.binmode](#ini.ibm-db2.binmode) | "1" | `INI_ALL` |  |
| [ibm_db2.i5_all_pconnect](#ini.ibm-db2.i5-all-pconnect) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.6.5. |
| [ibm_db2.i5_allow_commit](#ini.ibm-db2.i5-allow-commit) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.4.9. |
| [ibm_db2.i5_blank_userid](#ini.ibm-db2.i5-blank-userid) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.9.7. |
| [ibm_db2.i5_char_trim](#ini.ibm-db2.i5-char-trim) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 2.1.0. |
| [ibm_db2.i5_dbcs_alloc](#ini.ibm-db2.i5-dbcs-alloc) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.5.0. |
| [ibm_db2.i5_guard_profile](#ini.ibm-db2.i5-guard-profile) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.9.7. |
| [ibm_db2.i5_ignore_userid](#ini.ibm-db2.i5-ignore-userid) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.8.0. |
| [ibm_db2.i5_job_sort](#ini.ibm-db2.i5-job-sort) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.8.4. |
| [ibm_db2.i5_log_verbose](#ini.ibm-db2.i5-log-verbose) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.9.7. |
| [ibm_db2.i5_max_pconnect](#ini.ibm-db2.i5-max-pconnect) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.9.7. |
| [ibm_db2.i5_override_ccsid](#ini.ibm-db2.i5-override-ccsid) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.9.7. |
| [ibm_db2.i5_servermode_subsystem](#ini.ibm-db2.i5-servermode-subsystem) | NULL | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.9.7. |
| [ibm_db2.i5_sys_naming](#ini.ibm-db2.i5-sys-naming) | "0" | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.9.7. |
| [ibm_db2.instance_name](#ini.ibm-db2.instance-name) | NULL | `INI_SYSTEM` | Disponible a partir de ibm_db2 1.0.2. |

Opciones de configuración DB2

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`ibm_db2.binmode` (`int`)  
Esta opción controla el modo utilizado para convertir desde o hacia los datos binarios en la aplicación PHP.

- 1 (DB2_BINARY)

- 2 (DB2_CONVERT)

- 3 (DB2_PASSTHRU)

`ibm_db2.i5_all_pconnect` (`int`)  
Esta opción fuerza todas las conexiones a ser persistentes en IBM i. Fundamentalmente, todas las llamadas a `db2_connect` se convierten automáticamente en llamadas a `db2_pconnect`. Por omisión, esta opción es `0`. Esta opción se proporciona por conveniencia en los casos donde las conexiones persistentes son más rápidas. No debería utilizarse en nuevas aplicaciones.

- 0 - Se pueden establecer conexiones persistentes y no persistentes.

- 1 - Todas las conexiones son persistentes.

`ibm_db2.i5_allow_commit` `int`  
Esta opción controla el modo de aislamiento de la transacción utilizado. Por omisión, esta opción es `0`, por lo que no se utiliza el control de compromiso. Esta opción puede ser reemplazada durante la conexión si la clave del array `i5_commit` está definida en el array de opciones de conexión pasado a `db2_connect` o `db2_pconnect`.

- 0 - No se utiliza el control de compromiso.

- 1 - Lectura no comprometida, lectura sucia posible.

- 2 - Lectura comprometida, lectura sucia imposible.

- 3 - Lectura repetible, lectura sucia y lectura no repetible son imposibles.

- 4 - Serializable, lectura sucia, lectura no repetible y fantasma son imposibles.

`ibm_db2.i5_blank_userid` `int`  
Esto controla si se debe permitir un identificador de usuario vacío en IBM i. Por omisión, esta opción es `0`. A diferencia de `ibm_db2.i5_ignore_userid`, esta opción no fuerza a que todos los identificadores de usuario sean vacíos o a modificar el comportamiento del trabajo, sino que simplemente permite pasar un identificador de usuario vacío, para conectarse a Db2 como usuario actual.

- 0 - No permite pasar un identificador de usuario vacío.

- 1 - Permite pasar un identificador de usuario vacío.

`ibm_db2.i5_char_trim` `int`  
Esta opción controla si se recorta el final de las cadenas en IBM i. Dado que muchas tablas utilizan tamaños de columnas fijos rellenos de espacios, esto se proporciona por conveniencia. Por omisión, esta opción es `0`.

- 0 - Las columnas no se recortan.

- 1 - Los espacios al final de las columnas de caracteres devueltas se eliminan.

`ibm_db2.i5_dbcs_alloc` (`int`)  
Esta opción afecta a la estrategia de asignación de memoria de búfer interno en IBM i. Por omisión, esta opción es `0`. Cuando esta opción está definida, los búferes se asignan con un tamaño mucho mayor, en caso de que la base de datos subestime el tamaño de una cadena durante la conversión entre codificaciones. Esta opción utiliza seis veces más memoria para los búferes (para tener en cuenta las secuencias UTF-8 más grandes posibles), pero puede ser necesaria si se devuelven datos truncados.

- 0 - Se asignan búferes de tamaño mínimo.

- 1 - Se asignan búferes de tamaño mayor.

`ibm_db2.i5_guard_profile` `int`  
Esta opción verifica si el perfil de usuario de la base de datos ha sido cambiado durante la conexión a una conexión de base de datos persistente en IBM i, y si es así, se desconecta de la base de datos. Por omisión, esta opción está definida en `0`.

- 0 - No verificar cambios de perfil.

- 1 - Verificar cambios de perfil y desconectarse en caso necesario.

`ibm_db2.i5_log_verbose` `int`  
Esta opción define si los mensajes de diagnóstico SQL como advertencias y errores son siempre enviados al registro de errores PHP en IBM i. Normalmente, solo se envía un breve mensaje en caso de fallo (como "la ejecución de la sentencia falló") en el registro de errores PHP, ya que esta opción está definida en `0` por omisión. Tenga en cuenta que siempre y cuando debe llamar, por ejemplo, `db2_stmt_errormsg` manualmente para verificar si las funciones fallan.

- 0 - Solo se registran mensajes breves.

- 1 - Se registra el mensaje de diagnóstico SQL además del mensaje breve.

`ibm_db2.i5_ignore_userid` (`int`)  
Esta opción ignora el ID de usuario al conectarse a la base de datos al ejecutarse en IBM i, y ejecuta la funcionalidad SQL/CLI dentro del trabajo PHP, en lugar de un trabajo separado. Por omisión, esta opción es `0`. Cuando está activada, ya no utiliza un trabajo de servidor de base de datos separado, y siempre utiliza el perfil de usuario actual para la base de datos, ignorando el nombre de usuario y la contraseña pasados a `db2_connect` y `db2_pconnect`.

- 0 : db2\_(p)connect con un identificador de usuario y contraseña específicos 0 - Utiliza las credenciales especificadas y utiliza un trabajo de servidor SQL/CLI.

- 1 : db2\_(p)connect con un identificador de usuario y contraseña vacíos 1 - Siempre utiliza credenciales vacías y ejecuta SQL/CLI en el trabajo PHP.

`ibm_db2.i5_job_sort` `int`  
Controla la opción de ordenación de trabajos en IBM i. Por omisión, esta opción es `0`. Esto corresponde al atributo `SQL_ATTR_CONN_SORT_SEQUENCE` de IBM i SQL/CLI.

- 0 - Utiliza la opción de ordenación `*HEX`, ordenando por bytes.

- 1 - Utiliza la secuencia de ordenación de trabajo definida para el trabajo PHP.

- 2 - Utiliza la secuencia de ordenación de trabajo definida para el trabajo de base de datos.

`ibm_db2.i5_max_pconnect` `int`  
Esto afectará cuántas veces se puede reutilizar una conexión persistente al ejecutarse en IBM i. Por omisión, esto está configurado en `0`, lo que significa que una conexión persistente siempre puede ser reutilizada. Esta opción puede ayudar a evitar problemas en un trabajo de base de datos de larga duración (es decir, si un procedimiento pierde memoria), pero obviamente no es una solución a largo plazo.

`ibm_db2.i5_override_ccsid` `int`  
El CCSID PASE a utilizar para las conversiones de caracteres EBCDIC en IBM i. Por omisión, es `0`, lo que seleccionará el CCSID de trabajo PASE por defecto, procedente de los parámetros de localización PASE. Por ejemplo, al configurarlo en `1208`, se utilizará el UTF-8. Solo debe modificarse si el CCSID del trabajo PASE no es el CCSID esperado, y la localización no puede ser modificada.

Para obtener más información sobre los CCSID en IBM i, consulte la [documentación de IBM](https://www.ibm.com/docs/en/i/7.5?topic=information-ccsid-reference). Para saber cómo las localizaciones en IBM i PASE se mapean a los CCSID, consulte la [documentación de IBM](https://www.ibm.com/docs/en/i/7.5?topic=ssw_ibm_i_75/apis/pase_locales.html).

`ibm_db2.i5_sys_naming` `int`  
Esta opción controla el modo de nombrado al conectarse a un sistema IBM i. Por omisión, esta opción es `0`. El modo de nombrado afecta a la resolución de nombres y la sintaxis permitida para los nombres. Cuando está configurado en `0`, utiliza puntos para calificar los nombres y utiliza la biblioteca o el identificador de usuario por defecto para resolver los nombres. Cuando está configurado en `1`, utiliza barras diagonales para calificar los nombres y utiliza la lista de bibliotecas de trabajo para resolver los nombres.

- 0 - Utiliza el modo de nombrado SQL ("SCHEMA.TABLE").

- 1 - Utiliza el modo de nombrado del sistema ("LIBRARY/FILE").

Para obtener más información sobre los modos de nombrado en IBM i, consulte la [documentación de IBM](https://www.ibm.com/docs/en/i/7.5?topic=application-naming-distributed-relational-database-objects).

`ibm_db2.i5_servermode-subsystem` `string`  
Esta opción modifica el subsistema bajo el cual se ejecutan los trabajos del servidor de base de datos en IBM i. Por omisión, esta opción es `null`, por lo que los trabajos se ejecutarán bajo el subsistema por defecto para los trabajos QSQSRVR.

`ibm_db2.instance_name` `string`  
En los sistemas operativos Linux y UNIX, esta opción define el nombre de la instancia a utilizar para las conexiones de base de datos catalogadas. Por omisión, esta opción es `null`. Si esta opción está definida, su valor reemplaza la configuración de la variable de entorno `DB2INSTANCE`.

Esta opción se ignora en los sistemas operativos Windows.
