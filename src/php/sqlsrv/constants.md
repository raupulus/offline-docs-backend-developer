---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/sqlsrv.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_revision: 6047c10c1
order: 86060
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SQLSRV_FETCH_ASSOC` (`int`)  
Obliga a `sqlsrv_fetch_array` a devolver un array asociativo cuando se le pasa como argumento.

`SQLSRV_FETCH_NUMERIC` (`int`)  
Obliga a `sqlsrv_fetch_array` a devolver un array indexado numéricamente cuando se le pasa como argumento.

`SQLSRV_FETCH_BOTH` (`int`)  
Obliga a `sqlsrv_fetch_array` a devolver un array asociativo y un array indexado numéricamente cuando se le pasa como argumento (comportamiento por defecto).

`SQLSRV_ERR_ALL` (`int`)  
Obliga a `sqlsrv_errors` a devolver los errores y advertencias cuando se le pasa como argumento (comportamiento por defecto).

`SQLSRV_ERR_ERRORS` (`int`)  
Obliga a `sqlsrv_errors` a devolver solo los errores (no las advertencias) cuando se le pasa como argumento.

`SQLSRV_ERR_WARNINGS` (`int`)  
Obliga a `sqlsrv_errors` a devolver solo las advertencias (no los errores) cuando se le pasa como argumento.

`SQLSRV_LOG_SYSTEM_ALL` (`int`)  
Activa los logs de todos los subsistemas cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SYSTEM_CONN` (`int`)  
Activa los logs de toda la actividad de las conexiones cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SYSTEM_INIT` (`int`)  
Activa los logs de toda la actividad de las inicializaciones cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SYSTEM_OFF` (`int`)  
Desactiva los logs de todos los subsistemas cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SYSTEM_STMT` (`int`)  
Activa los logs de las consultas cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SYSTEM_UTIL` (`int`)  
Activa los logs de los errores de función cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SEVERITY_ALL` (`int`)  
Activa los logs de los errores, advertencias y notas cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SEVERITY_ERROR` (`int`)  
Especifica que los errores serán registrados cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SEVERITY_NOTICE` (`int`)  
Especifica que las notas serán registradas cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_LOG_SEVERITY_WARNING` (`int`)  
Especifica que las advertencias serán registradas cuando se le pasa a la función `sqlsrv_configure` como argumento.

`SQLSRV_NULLABLE_YES` (`int`)  
Indica que una columna puede ser nula.

`SQLSRV_NULLABLE_NO` (`int`)  
Indica que una columna no puede ser nula.

`SQLSRV_NULLABLE_UNKNOWN` (`int`)  
Indica si se conoce que una columna es nula.

`SQLSRV_PARAM_IN` (`int`)  
Indica un parámetro de entrada cuando se le pasa a la función `sqlsrv_query` o a la función `sqlsrv_prepare`.

`SQLSRV_PARAM_INOUT` (`int`)  
Indica un parámetro de entrada o salida cuando se le pasa a la función `sqlsrv_query` o a la función `sqlsrv_prepare`.

`SQLSRV_PARAM_OUT` (`int`)  
Indica un parámetro de salida cuando se le pasa a la función `sqlsrv_query` o a la función `sqlsrv_prepare`.

`SQLSRV_PHPTYPE_INT` (`int`)  
Especifica un dato de tipo entero PHP. Para más información, ver [Cómo especificar los tipos PHP](http://msdn.microsoft.com/en-us/library/cc296208.aspx).

`SQLSRV_PHPTYPE_DATETIME` (`int`)  
Especifica un dato de tipo datetime (fecha y hora) PHP. Para más información, ver [Cómo especificar los tipos PHP](http://msdn.microsoft.com/en-us/library/cc296208.aspx).

`SQLSRV_PHPTYPE_FLOAT` (`int`)  
Especifica un dato de tipo número de punto flotante PHP. Para más información, ver [Cómo especificar los tipos PHP](http://msdn.microsoft.com/en-us/library/cc296208.aspx).

`SQLSRV_PHPTYPE_STREAM` (`int`)  
Especifica un dato de tipo flujo de PHP. Esta constante funciona como una función y acepta una constante codificada. Ver las constantes SQLSRV_ENC\_\*. Para más información, reportez-vous a [Cómo especificar los tipos PHP](http://msdn.microsoft.com/en-us/library/cc296208.aspx).

`SQLSRV_PHPTYPE_STRING` (`int`)  
Especifica un dato de tipo string PHP. Esta constante funciona como una función y acepta una constante codificada. Ver las constantes SQLSRV_ENC\_\*. Para más información, reportez-vous a [Cómo especificar los tipos PHP](http://msdn.microsoft.com/en-us/library/cc296208.aspx).

`SQLSRV_ENC_BINARY` (`int`)  
Especifica que el dato es devuelto en forma de flujo bruto de bytes desde el servidor sin realizar un codificación o transformación. Para más información, reportez-vous a [Cómo especificar los tipos PHP](http://msdn.microsoft.com/en-us/library/cc296208.aspx).

`SQLSRV_ENC_CHAR` (`int`)  
El dato es devuelto en forma de caracteres de 8 bits, tal como se especifica en la página de códigos Windows local, definida en el sistema. Cualquier carácter multibyte o caracteres que no correspondan a esta página de código serán sustituidos con un signo de interrogación de un byte (?). Es la codificación por defecto. Para más información, reportez-vous a [Cómo especificar los tipos PHP](http://msdn.microsoft.com/en-us/library/cc296208.aspx).

`SQLSRV_SQLTYPE_BIGINT` (`int`)  
Describe el tipo de datos bigint de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_BINARY` (`int`)  
Describe el tipo de datos binario de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_BIT` (`int`)  
Describe el tipo de datos bit de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_CHAR` (`int`)  
Describe el tipo de datos carácter de SQL Server. Esta constante funciona como una función y acepta un argumento indicando el número de caracteres. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_DATE` (`int`)  
Describe el tipo de datos date de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_DATETIME` (`int`)  
Describe el tipo de datos datetime de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_DATETIME2` (`int`)  
Describe el tipo de datos datetime2 de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_DATETIMEOFFSET` (`int`)  
Describe el tipo de datos datetimeoffset de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_DECIMAL` (`int`)  
Describe el tipo de datos decimal. Esta constante funciona como una función y acepta 2 argumentos indicando (en orden) la precisión y la escala. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_FLOAT` (`int`)  
Describe el tipo de datos número de punto flotante de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_IMAGE` (`int`)  
Describe el tipo de datos image de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_INT` (`int`)  
Describe el tipo de datos entero de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_MONEY` (`int`)  
Describe el tipo de datos moneda de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_NCHAR` (`int`)  
Describe el tipo de datos nchar de SQL Server. Esta constante funciona como una función y acepta un solo argumento indicando el número de caracteres. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_NUMERIC` (`int`)  
Describe el tipo de datos numérico de SQL Server. Esta constante funciona como una función y acepta 2 argumentos (en orden), la precisión y la escala. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_NVARCHAR` (`int`)  
Describe el tipo de datos nvarchar de SQL Server. Esta constante funciona como una función y acepta un solo argumento indicando el número de caracteres. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_NVARCHAR('max')` (`int`)  
Describe el tipo de datos nvarchar(MAX) de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_NTEXT` (`int`)  
Describe el tipo de datos ntext de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_REAL` (`int`)  
Describe el tipo de datos real de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_SMALLDATETIME` (`int`)  
Describe el tipo de datos smalldatetime de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_SMALLINT` (`int`)  
Describe el tipo de datos smallint de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_SMALLMONEY` (`int`)  
Describe el tipo de datos smallmoney de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_TEXT` (`int`)  
Describe el tipo de datos texto de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_TIME` (`int`)  
Describe el tipo de datos time de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_TIMESTAMP` (`int`)  
Describe el tipo de datos timestamp de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_TINYINT` (`int`)  
Describe el tipo de datos tinyint de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_UNIQUEIDENTIFIER` (`int`)  
Describe el tipo de datos uniqueidentifier de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_UDT` (`int`)  
Describe el tipo de datos UDT de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_VARBINARY` (`int`)  
Describe el tipo de datos varbinary de SQL Server. Esta constante funciona como una función y acepta un solo argumento indicando el número de bytes. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_VARBINARY('max')` (`int`)  
Describe el tipo de datos varbinary(MAX) de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_VARCHAR` (`int`)  
Describe el tipo de datos varchar de SQL Server. Esta constante funciona como una función y acepta un solo argumento indicando el número de caracteres. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_VARCHAR('max')` (`int`)  
Describe el tipo de datos varchar(MAX) de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_SQLTYPE_XML` (`int`)  
Describe el tipo de datos XML de SQL Server. Para más información, reportez-vous a [Cómo especificar los tipos SQL](http://msdn.microsoft.com/en-us/library/cc626305.aspx).

`SQLSRV_TXN_READ_UNCOMMITTED` (`int`)  
Indica un nivel de aislamiento de la transacción a READ UNCOMMITTED. Este valor se utiliza para definir el nivel de aislamiento de la transacción en el array \$connectionOptions pasado a la función `sqlsrv_connect`.

`SQLSRV_TXN_READ_COMMITTED` (`int`)  
Indica un nivel de aislamiento de la transacción a READ COMMITTED. Este valor se utiliza para definir el nivel de aislamiento de la transacción en el array \$connectionOptions pasado a la función `sqlsrv_connect`.

`SQLSRV_TXN_REPEATABLE_READ` (`int`)  
Indica un nivel de aislamiento de la transacción a REPEATABLE READ. Este valor se utiliza para definir el nivel de aislamiento de la transacción en el array \$connectionOptions pasado a la función `sqlsrv_connect`.

`SQLSRV_TXN_SNAPSHOT` (`int`)  
Indica un nivel de aislamiento de la transacción a SNAPSHOT. Este valor se utiliza para definir el nivel de aislamiento de la transacción en el array \$connectionOptions pasado a la función `sqlsrv_connect`.

`SQLSRV_TXN_READ_SERIALIZABLE` (`int`)  
Indica un nivel de aislamiento de la transacción a SERIALIZABLE. Este valor se utiliza para definir el nivel de aislamiento de la transacción en el array \$connectionOptions pasado a la función `sqlsrv_connect`.

`SQLSRV_CURSOR_FORWARD` (`int`)  
Indica un cursor de tipo "solo hacia adelante". Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_CURSOR_STATIC` (`int`)  
Indica un cursor de tipo "estático". Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_CURSOR_DYNAMIC` (`int`)  
Indica un cursor de tipo "dinámico". Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_CURSOR_KEYSET` (`int`)  
Indica un cursor de tipo "keyset". Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_CURSOR_BUFFERED` (`int`)  
Crea una consulta de cursor del lado del cliente. Esto permite acceder a las filas en cualquier orden. Para más información sobre su uso, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_SCROLL_NEXT` (`int`)  
Especifica la fila a seleccionar en un conjunto de resultados. Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_SCROLL_PRIOR` (`int`)  
Especifica la fila a seleccionar en un conjunto de resultados. Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_SCROLL_FIRST` (`int`)  
Especifica la fila a seleccionar en un conjunto de resultados. Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_SCROLL_LAST` (`int`)  
Especifica la fila a seleccionar en un conjunto de resultados. Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_SCROLL_ABSOLUTE` (`int`)  
Especifica la fila a seleccionar en un conjunto de resultados. Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).

`SQLSRV_SCROLL_RELATIVE` (`int`)  
Especifica la fila a seleccionar en un conjunto de resultados. Para más información, reportez-vous a la sección sobre [la especificación de un tipo de cursor y la selección de filas](http://msdn.microsoft.com/en-us/library/ee376927.aspx).
