---
title: db2_pconnect
description: Devuelve una conexión persistente a una base de datos
source_url: https://www.php.net/manual/es/function.db2-pconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-pconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30980
---

db2_pconnect

Devuelve una conexión persistente a una base de datos

## Descripción

```php
db2_pconnect(string $database, string $username, string $password, [array $options]): resource
```php

Devuelve una conexión persistente a una base de datos IBM DB2 Universal Database, IBM Cloudscape o Apache Derby.

Para más información sobre las conexiones persistentes, véase [???](#features.persistent-connections).

Al llamar a `db2_close` sobre una conexión persistente, siempre se recibirá `true`, pero las conexiones de los clientes DB2 permanecerán abiertas y esperarán para servir la próxima petición de la función `db2_pconnect`.

Los usuarios de versiones 1.9.0 o superiores de ibm_db2 deben saber que la extensión ejecutará un rollback sobre una transacción en una conexión persistente al final de la consulta, terminando así la transacción. Esto evita un bloqueo transaccional hacia la consulta siguiente sobre la misma conexión si la ejecución del script termina antes de la transacción.

## Parámetros

`database`  
Para una conexión catalogada a una base de datos, `database` representa el alias de la base de datos en el catálogo del cliente DB2.

Para una conexión no catalogada a una base de datos, `database` representa una cadena de conexión completa en el siguiente formato :

DATABASE=`database`;HOSTNAME=`hostname`;PORT=`port`;PROTOCOL=TCPIP;UID=`username`;PWD=`password`;

> [!NOTE]
> Al conectarse a Db2 sobre IBM i, las llamadas al sistema subyacentes [SQLDriverConnect](https://www.ibm.com/docs/en/i/7.5?topic=functions-sqldriverconnect-connect-data-source), solo aceptan DSN, UID y PWD para la [cadena de conexión](https://www.ibm.com/docs/en/i/7.5?topic=functions-sqldriverconnect-connect-data-source#rzadpfndvcon__title__5). Como sigue :
>
> DSN=`database`;UID=`username`;PWD=`password`;

donde los parámetros representan los siguientes valores :

`database`  
El nombre de la base de datos.

`hostname`  
El nombre de host o la dirección IP del servidor de la base de datos.

`port`  
El puerto TCP/IP en el que la base de datos escucha las consultas.

`username`  
El nombre de usuario con el que se conecta a la base de datos.

`password`  
La contraseña con la que se conecta a la base de datos.

`username`  
El nombre de usuario con el que se conecta a la base de datos.

`password`  
La contraseña con la que se conecta a la base de datos.

`options`  
Un array asociativo de opciones de conexión que afectarán el comportamiento de la conexión, donde los valores de las claves incluyen :

`autocommit`  
El valor `DB2_AUTOCOMMIT_ON` activa el autocommit en esta conexión.

El valor `DB2_AUTOCOMMIT_OFF` desactiva el autocommit para esta conexión.

`DB2_ATTR_CASE`  
Pasar el valor `DB2_CASE_NATURAL` especifica que los nombres de columnas serán devueltos en sus casos naturales.

Pasar el valor `DB2_CASE_LOWER` especifica que los nombres de columnas serán devueltos en minúsculas.

Pasar el valor `DB2_CASE_UPPER` especifica que los nombres de columnas serán devueltos en mayúsculas.

`CURSOR`  
Pasar el valor `DB2_FORWARD_ONLY` especifica un cursor solo hacia adelante para un recurso de consulta. Este es el tipo de cursor por defecto y es soportado en todos los servidores de base de datos.

Pasar el valor `DB2_SCROLLABLE` especifica un cursor desplazable para un recurso de consulta. Este modo permite un acceso aleatorio a las filas en un conjunto de resultados, pero actualmente, solo es soportado por la base de datos IBM DB2 Universal.

Las siguientes opciones están disponibles desde ibm_db2 versión 1.7.0.

`trustedcontext`  
Al pasar el valor DB2_TRUSTED_CONTEXT_ENABLE, el contexto de confianza es activado para esta conexión. Este parámetro no puede ser activado con `db2_set_option`.

Esta opción solo funciona si la base está catalogada, incluso si la base es local, o si se especifica un DSN completo al crear la conexión.

Para catalogar la base, utilice el siguiente comando :

db2 catalog tcpip node loopback remote \<SERVERNAME\> server \<SERVICENAME\>\
db2 catalog database \<LOCALDBNAME\> as \<REMOTEDBNAME\> at node loopback\
db2 "update dbm cfg using svcename \<SERVICENAME\>"\
db2set DB2COMM=TCPIP

Las siguientes opciones i5/OS están disponibles desde ibm_db2 versión 1.5.1.

> [!TIP]
> Atributos de conexión contradictorios, en conjunción con una conexión persistente pueden producir resultados indeterminados en i5/OS. La política del sitio debe ser establecida para todas las aplicaciones que utilizan una conexión persistente. El valor por defecto de DB2_AUTOCOMMIT_ON es recomendado con las conexiones persistentes.

`i5_lib`  
Un carácter que indica la biblioteca por defecto que será utilizada para resolver las referencias de ficheros no calificadas. Esta opción no es válida si la conexión utiliza el modo de nombramiento del sistema.

`i5_naming`  
`DB2_I5_NAMING_ON` activa el modo de nombramiento del sistema de DB2 UDB CLI iSeries. Los ficheros son entonces calificados con el delimitador slash (/). Los ficheros no calificados son resueltos utilizando la lista de bibliotecas de la tarea.

`DB2_I5_NAMING_OFF` activa el modo de nombramiento por defecto, que es el nombramiento SQL. Los ficheros son entonces calificados con el punto (.) . Los ficheros no calificados son resueltos con la biblioteca por defecto, o bien el identificador del usuario actual.

`i5_commit`  
El atributo `i5_commit` debe ser configurado antes de la llamada a `db2_pconnect`. Si el valor es cambiado después de la conexión, y la conexión se efectúa sobre datos remotos, entonces este cambio no tendrá efectos, hasta la próxima llamada exitosa a `db2_pconnect`.

> [!NOTE]
> La directiva del `php.ini` `ibm_db2.i5_allow_commit`==0 o `DB2_I5_TXN_NO_COMMIT` es el valor por defecto, pero puede ser reemplazado por la opción `i5_commit`.

`DB2_I5_TXN_NO_COMMIT` : el control de validación no es utilizado.

`DB2_I5_TXN_READ_UNCOMMITTED` : las lecturas inconsistentes, o no repetibles y los fantasmas son posibles.

`DB2_I5_TXN_READ_COMMITTED` : las lecturas son consistentes. Las lecturas no repetibles y los fantasmas son posibles.

`DB2_I5_TXN_REPEATABLE_READ` : las lecturas consistentes y repetibles, pero los fantasmas son posibles.

`DB2_I5_TXN_SERIALIZABLE` : las transacciones son activadas. Las lecturas inconsistentes, o no repetibles y los fantasmas son imposibles.

`i5_query_optimize`  
`DB2_FIRST_IO` : todas las consultas son optimizadas con el objetivo de devolver la primera página lo más rápidamente posible. Este objetivo funciona bien cuando el resultado es controlado por un usuario que tiene buenas probabilidades de cancelar la consulta después de ver las primeras respuestas. Las consultas codificadas con una cláusula `OPTIMIZE FOR nnn ROWS` respetan también este objetivo.

`DB2_ALL_IO` : todas las consultas son optimizadas con el objetivo de procesar la consulta completa lo más rápidamente posible. Esta es una buena opción cuando el resultado de la consulta debe ser escrito en un fichero o un informe, o que la interfaz acumula todos los datos antes de exportarlos. Las consultas codificadas con la cláusula `OPTIMIZE FOR nnn ROWS` respetan también este objetivo. Este es el comportamiento por defecto.

`i5_dbcs_alloc`  
`DB2_I5_DBCS_ALLOC_ON` activa el esquema de asignación DB2 6X para el crecimiento de las tallas de columnas de traducción DBCS.

`DB2_I5_DBCS_ALLOC_OFF` desactiva el esquema de asignación DB2 6X para el crecimiento de las tallas de columnas de traducción DBCS.

> [!NOTE]
> La directiva del `php.ini` `ibm_db2.i5_dbcs_alloc`==0 o `DB2_I5_DBCS_ALLOC_OFF` es el valor por defecto, pero puede ser reemplazado por la opción `i5_dbcs_alloc`.

`i5_date_fmt`  
`DB2_I5_FMT_ISO` : el formato de fecha ISO (`International Organization for Standardization`) es utilizado : `yyyy-mm-dd`. Este es el formato por defecto.

`DB2_I5_FMT_USA` : el formato de los Estados Unidos de América es utilizado : `mm/dd/yyyy`.

`DB2_I5_FMT_EUR` : el formato de fecha europeo `dd.mm.yyyy` es utilizado.

`DB2_I5_FMT_JIS` : el formato estándar industrial japonés `yyyy-mm-dd` es utilizado.

`DB2_I5_FMT_MDY` : el formato de fecha `mm/dd/yyyy` es utilizado.

`DB2_I5_FMT_DMY` : el formato de fecha `dd/mm/yyyy` es utilizado.

`DB2_I5_FMT_YMD` : el formato de fecha `yy/mm/dd` es utilizado.

`DB2_I5_FMT_JUL` : El formato de fecha juliano `yy/ddd` es utilizado.

`DB2_I5_FMT_JOB` : el formato de fecha por defecto es utilizado.

`i5_date_sep`  
`DB2_I5_SEP_SLASH` : un slash ( / ) es utilizado como separador de fecha. Este es el formato por defecto.

`DB2_I5_SEP_DASH` : un guión ( - ) es utilizado como separador de fecha.

`DB2_I5_SEP_PERIOD` : un punto ( . ) es utilizado como separador de fecha.

`DB2_I5_SEP_COMMA` : una coma ( , ) es utilizada como separador de fecha.

`DB2_I5_SEP_BLANK` : un espacio es utilizado como separador de fecha.

`DB2_I5_SEP_JOB` : la configuración por defecto es utilizada

`i5_time_fmt`  
`DB2_I5_FMT_ISO` : el formato de hora ISO (`International Organization for Standardization`) es utilizado : `hh.mm.ss`. Este es el formato por defecto.

`DB2_I5_FMT_USA` : el formato de los Estados Unidos de América es utilizado : `hh:mmxx` es utilizado, donde `xx` vale `AM` o `PM`.

`DB2_I5_FMT_EUR` : el formato de hora europeo `hh.mm.ss` es utilizado.

`DB2_I5_FMT_JIS` : el formato estándar industrial japonés es utilizado `hh:mm:ss`.

`DB2_I5_FMT_HMS` : el formato `hh:mm:ss` es utilizado.

`i5_time_sep`  
`DB2_I5_SEP_COLON` : un dos-puntos ( : ) es utilizado como separador de hora. Este es el defecto.

`DB2_I5_SEP_PERIOD` : un punto ( . ) es utilizado como separador de hora.

`DB2_I5_SEP_COMMA` : una coma ( , ) es utilizada como separador de hora.

`DB2_I5_SEP_BLANK` : un espacio es utilizado como separador de hora.

`DB2_I5_SEP_JOB` : el separador por defecto es utilizado.

`i5_decimal_sep`  
`DB2_I5_SEP_PERIOD` : un punto ( . ) es utilizado como separador decimal. Este es el separador por defecto.

`DB2_I5_SEP_COMMA` : una coma ( , ) es utilizada como separador decimal.

`DB2_I5_SEP_JOB` : el separador por defecto es utilizado.

Las siguientes opciones i5/OS están disponibles desde ibm_db2 versión 1.8.0.

`i5_libl`  
Un carácter que indica la biblioteca que será utilizada para resolver las referencias de ficheros no calificadas. Especifique la lista de bibliotecas en la forma de elementos separados por espacios : `'i5_libl'=>"MYLIB YOURLIB ANYLIB"`.

> [!NOTE]
> i5_libl llama a `qsys2/qcmdexc('cmd',cmdlen)`, que está disponible desde i5/OS V5R4.

## Valores devueltos

Devuelve el recurso de conexión si la tentativa de conexión tiene éxito. `db2_pconnect` intenta reutilizar un recurso de conexión existente que coincide perfectamente con los parámetros tales como la base de datos `database`, el usuario `username` y la contraseña `password`. Si la tentativa de conexión falla, `db2_pconnect` devuelve `false`

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL ibm_db2 1.9.0 | Las transacciones activas sobre conexiones persistentes serán anuladas al final de cada consulta. |
| PECL ibm_db2 1.8.0 | La opción `i5_libl` está disponible para los usuarios de i5/OS. |
| PECL ibm_db2 1.7.0 | La opción `trustedcontext` está disponible. |
| PECL ibm_db2 1.5.1 | Las opciones `i5_lib`, `i5_naming`, `i5_commit`, `i5_query_optimize`, `i5_dbcs_alloc`, `i5_date_fmt`, `i5_date_sep`, `i5_time_fmt`, `i5_time_sep` y `i5_decimal_sep` están disponibles para los usuarios de i5/OS. |

## Ejemplos

Ejemplo de uso de `db2_pconnect`

En el siguiente ejemplo, la primera llamada a `db2_pconnect` devuelve un nuevo recurso de conexión persistente. La segunda llamada a la función `db2_pconnect` devuelve un recurso de conexión persistente que reutiliza el primer recurso de conexión.

```
<?php
$database = 'EJEMPLO';
$user = 'db2inst1';
$password = 'ibmdb2';

$pconn = db2_pconnect($database, $user, $password);

if ($pconn) {
    echo "Conexión persistente exitosa.";
}
else {
    echo "Conexión persistente fallida.";
}

$pconn2 = db2_pconnect($database, $user, $password);
if ($pconn) {
    echo "Segunda conexión persistente exitosa.";
}
else {
    echo "Segunda conexión persistente fallida.";
}
?>

    
```php

El ejemplo anterior mostrará:

    Conexión persistente exitosa.
    Segunda conexión persistente exitosa.

Uso de contextos de confianza DB2

El siguiente ejemplo muestra cómo activar un usuario de confianza, cambiar a él, y obtener un identificador de usuario.

```
<?php

$database = "SAMPLE";
$hostname = "localhost";
$port = 50000;
$authID = "db2inst1";
$auth_pass = "ibmdb2";

$tc_user = "tcuser";
$tc_pass = "tcpassword";

$dsn = "DATABASE=$database;HOSTNAME=$hostname;PORT=$port;
  PROTOCOL=TCPIP;UID=$authID;PWD=$auth_pass;";
$options = array ("trustedcontext" => DB2_TRUSTED_CONTEXT_ENABLE);

$tc_conn = db2_pconnect($dsn, "", "", $options);
if($tc_conn) {
    echo "Conexión de confianza exitosa.\n";

    if(db2_get_option($tc_conn, "trustedcontext")) {
        $userBefore = db2_get_option($tc_conn, "trusted_user");

        //Trabajo por el usuario 1.

        //Cambio al usuario de confianza.
        $parameters = array("trusted_user" => $tc_user,
          "trusted_password" => $tcuser_pass);
        $res = db2_set_option ($tc_conn, $parameters, 1);

        $userAfter = db2_get_option($tc_conn, "trusted_user");
        //Hacer más trabajo como usuario de confianza.

        if($userBefore != $userAfter) {
            echo "Usuario cambiado." . "\n";
        }
    }

    db2_close($tc_conn);
}
else {
    echo "Conexión de confianza fallida.\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    Conexión de confianza exitosa.
    Usuario cambiado

## Véase también

db2_connect
