---
title: db2_connect
description: Devuelve una conexión a una base de datos
source_url: https://www.php.net/manual/es/function.db2-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30710
---

db2_connect

Devuelve una conexión a una base de datos

## Descripción

```php
db2_connect(string $database, string $username, string $password, [array $options]): resource
```php

Crea una nueva conexión a una base de datos IBM DB2 Universal Database, IBM Cloudscape o Apache Derby.

## Parámetros

`database`  
Para una conexión catalogada de la base de datos, `database` representa el alias de la base de datos en el catálogo cliente DB2

Para una conexión no catalogada de la base de datos, `database` representa una cadena completa de conexión que está en el formato siguiente :

DATABASE=`database`;HOSTNAME=`hostname`;PORT=`port`;PROTOCOL=TCPIP;UID=`username`;PWD=`password`;

> [!NOTE]
> Al conectarse a Db2 en IBM i, las llamadas al sistema subyacentes [SQLDriverConnect](https://www.ibm.com/docs/en/i/7.5?topic=functions-sqldriverconnect-connect-data-source), solo aceptan DSN, UID y PWD para la [cadena de conexión](https://www.ibm.com/docs/en/i/7.5?topic=functions-sqldriverconnect-connect-data-source#rzadpfndvcon__title__5). Como sigue :
>
> DSN=`database`;UID=`username`;PWD=`password`;

donde los parámetros representan los siguientes valores :

`database`  
El nombre de la base de datos.

`hostname`  
La dirección Internet o IP del servidor de base de datos.

`port`  
El puerto TCP/IP en el que la base de datos escucha las conexiones.

`username`  
El nombre de usuario con el que se conecta a la base de datos.

`password`  
La contraseña con la que se conecta a la base de datos.

`username`  
El nombre de usuario con el que se conecta a la base de datos.

Para las conexiones no catalogadas, debe pasar un valor `null` o una cadena vacía.

`password`  
La contraseña con la que se conecta a la base de datos.

Para las conexiones no catalogadas, debe pasar un valor `null` o una cadena vacía.

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

La siguiente nueva opción está disponible para las versiones ibm_db2 1.7.0 y posteriores.

`trustedcontext`  
Pasar el valor DB2_TRUSTED_CONTEXT_ENABLE activa el contexto para este gestor de conexión. Este parámetro no puede ser definido con la función `db2_set_option`.

Esta clave solo funciona si la base de datos está catalogada (incluso si la base de datos es local), o si se especifica el DSN completo al crear la conexión.

Para catalogar la base de datos, utilice los siguientes comandos :

db2 catalog tcpip node loopback remote \<SERVERNAME\> server \<SERVICENAME\>\
db2 catalog database \<LOCALDBNAME\> as \<REMOTEDBNAME\> at node loopback\
db2 "update dbm cfg using svcename \<SERVICENAME\>"\
db2set DB2COMM=TCPIP

Las siguientes nuevas opciones i5/OS están disponibles en las versiones ibm_db2 1.5.1 y posteriores.

`i5_lib`  
Un carácter que indica la biblioteca por defecto que será utilizada para resolver las referencias a los ficheros no calificados. Esto no es válido si la conexión utiliza un modo de sistema de nombres.

`i5_naming`  
El valor `DB2_I5_NAMING_ON` activa el modo sistema de nombres DB2 UDB CLI iSeries. Los ficheros son calificados utilizando el delimitador barra (/). Los ficheros no calificados son resueltos utilizando la lista de bibliotecas para el trabajo.

El valor `DB2_I5_NAMING_OFF` desactiva el modo de nombres por defecto de DB2 UDB CLI, que es la escritura SQL. Los ficheros son calificados utilizando el delimitador punto (.). Los ficheros no calificados son resueltos utilizando la biblioteca por defecto o el ID del usuario actual.

`i5_commit`  
El atributo `i5_commit` debe ser fijado antes de la llamada a `db2_connect`. Si el valor es cambiado después de que la conexión haya sido establecida y la conexión es a una fuente de datos remota, el cambio solo tendrá efecto en la próxima llamada a `db2_connect`.

> [!NOTE]
> La configuración php.ini `ibm_db2.i5_allow_commit`==0 o `DB2_I5_TXN_NO_COMMIT` es por defecto, pero puede ser derivada con la opción `i5_commit`.

`DB2_I5_TXN_NO_COMMIT` : no se utiliza el control de envío.

`DB2_I5_TXN_READ_UNCOMMITTED` : lectura antigua, lectura no repetitiva y ficticia es posible.

`DB2_I5_TXN_READ_COMMITTED` : lectura antigua no posible. La lectura repetitiva y ficticia es posible.

`DB2_I5_TXN_REPEATABLE_READ` : lectura antigua y no repetitiva no es posible. Lectura ficticia es posible.

`DB2_I5_TXN_SERIALIZABLE` : las transacciones son serializadas. Lectura antigua, no repetitiva y ficticia no es posible.

`i5_query_optimize`  
`DB2_FIRST_IO` Todas las consultas son optimizadas con el objetivo de devolver la primera página tan rápido como sea posible. Este objetivo funciona bien cuando la visualización es controlada por un usuario que puede cancelar una consulta después de ver la primera página de los datos. Las consultas son codificadas con una cláusula `"OPTIMIZE nnn ROWS"` para cumplir el objetivo especificado por la cláusula.

`DB2_ALL_IO` Todas las consultas son optimizadas con el objetivo de devolver la consulta completa en el menor intervalo de tiempo. Esta es una buena opción cuando la visualización de una consulta está siendo escrita hacia un fichero o un informe o cuando la interfaz pone en cola los datos. Las consultas son codificadas con una cláusula `"OPTIMIZE FOR nnn ROWS"` para cumplir el objetivo especificado por la cláusula. Esta es la operación por defecto.

`i5_dbcs_alloc`  
El valor `DB2_I5_DBCS_ALLOC_ON` activa el esquema de asignación DB2 6X para el incremento de los tamaños de columnas.

El valor `DB2_I5_DBCS_ALLOC_OFF` desactiva el esquema de asignación DB2 6X para el incremento de los tamaños de columnas.

Nota : la configuración `php.ini` `ibm_db2.i5_dbcs_alloc`==0 o `DB2_I5_DBCS_ALLOC_OFF` es por defecto pero puede ser derivada con la opción `i5_dbcs_alloc`.

`i5_date_fmt`  
`DB2_I5_FMT_ISO` : se utiliza el formato de fecha de la organización internacional de normalización (ISO) `"yyyy-mm-dd"`. Este es el valor por defecto.

`DB2_I5_FMT_USA` : se utiliza el formato de fecha de los Estados Unidos `"mm/dd/yyyy"`.

`DB2_I5_FMT_EUR` : se utiliza el formato de fecha Europeo `"dd.mm.yyyy"`.

`DB2_I5_FMT_JIS` : se utiliza el formato de fecha de la industria japonesa de estándares `"yyyy-mm-dd"`.

`DB2_I5_FMT_MDY` : se utiliza el formato de fecha `"mm/dd/yyyy"`.

`DB2_I5_FMT_DMY` : se utiliza el formato de fecha `"dd/mm/yyyy"`.

`DB2_I5_FMT_YMD` : se utiliza el formato de fecha `"yy/mm/dd"`.

`DB2_I5_FMT_JUL` : se utiliza el formato de fecha Juliano `"yy/ddd"`.

`DB2_I5_FMT_JOB` : se utiliza el valor por defecto.

`i5_date_sep`  
`DB2_I5_SEP_SLASH` : se utiliza una barra ( / ) como separador de fecha. Este es el valor por defecto.

`DB2_I5_SEP_DASH` : se utiliza un guión ( - ) como separador de fecha.

`DB2_I5_SEP_PERIOD` : se utiliza un punto ( . ) como separador de fecha.

`DB2_I5_SEP_COMMA` : se utiliza una coma ( , ) como separador de fecha.

`DB2_I5_SEP_BLANK` : se utiliza un espacio en blanco como separador de fecha.

`DB2_I5_SEP_JOB` : se utiliza el valor por defecto.

`i5_time_fmt`  
`DB2_I5_FMT_ISO` : se utiliza el formato de hora de la organización internacional de normalización `"hh.mm.ss"`. Este es el valor por defecto.

`DB2_I5_FMT_USA` : se utiliza el formato de hora de los Estados Unidos `"hh:mmxx"`, donde `"xx"` vale `"AM"` o `"PM"`.

`DB2_I5_FMT_EUR` : se utiliza el formato de hora Europeo `"hh.mm.ss"`.

`DB2_I5_FMT_JIS` : se utiliza el formato de hora de la industria japonesa de estándares `"hh:mm:ss"`.

`DB2_I5_FMT_HMS` : se utiliza el formato `"hh:mm:ss"`.

`i5_time_sep`  
`DB2_I5_SEP_COLON` : se utiliza un dos puntos ( : ) como separador de tiempo. Este es el valor por defecto.

`DB2_I5_SEP_PERIOD` : se utiliza un punto ( . ) como separador de tiempo.

`DB2_I5_SEP_COMMA` : se utiliza una coma ( , ) como separador de tiempo.

`DB2_I5_SEP_BLANK` : se utiliza un espacio en blanco como separador de tiempo.

`DB2_I5_SEP_JOB` : se utiliza el valor por defecto.

`i5_decimal_sep`  
`DB2_I5_SEP_PERIOD` : se utiliza un punto ( . ) como separador decimal. Este es el valor por defecto.

`DB2_I5_SEP_COMMA` : se utiliza una coma ( , ) como separador decimal.

`DB2_I5_SEP_JOB` : se utiliza el valor por defecto.

La siguiente nueva opción i5/OS está disponible desde la versión ibm_db2 1.8.0 y posteriores.

`i5_libl`  
Una cadena que indica la lista a utilizar para resolver las referencias de ficheros no calificados. Especifique la lista separando los valores con un espacio, como sigue : 'i5_libl'=\>"MYLIB YOURLIB ANYLIB".

> [!NOTE]
> `i5_libl` llama a `qsys2/qcmdexc('cmd',cmdlen)`, que solo está disponible desde i5/OS V5R4.

## Valores devueltos

Devuelve el recurso de conexión si la tentativa de conexión tiene éxito. Si la tentativa de conexión falla, `db2_connect` devuelve `false`.

## Ejemplos

Creación de una conexión catalogada

Las conexiones catalogadas requieren que haya catalogado previamente la base de datos especificada utilizando el procesador de línea de comandos DB2 (`"Command Line Processor"` : cLP) o con el asistente de configuración de DB2.

```
<?php
$database = 'EJEMPLO';
$user = 'db2inst1';
$password = 'ibmdb2';

$conn = db2_connect($database, $user, $password);

if ($conn) {
    echo "Conexión exitosa.";
    db2_close($conn);
}
else {
    echo "Conexión fallida.";
}
?>

    
```php

El ejemplo anterior mostrará:

    Conexión exitosa.

Creación de una conexión no catalogada

Una conexión no catalogada permite conectarse dinámicamente a una base de datos.

```
<?php
$database = 'EJEMPLO';
$user = 'db2inst1';
$password = 'ibmdb2';
$hostname = 'localhost';
$port = 50000;

$conn_string = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=$database;" .
  "HOSTNAME=$hostname;PORT=$port;PROTOCOL=TCPIP;UID=$user;PWD=$password;";
$conn = db2_connect($conn_string, '', '');

if ($conn) {
    echo "Conexión exitosa.";
    db2_close($conn);
}
else {
    echo "Conexión fallida.";
}
?>

    
```php

El ejemplo anterior mostrará:

    Conexión exitosa.

Creación de una conexión con autocommit desactivado por defecto

Pasar un array de opciones a `db2_connect` permite modificar el comportamiento por defecto de la conexión.

```
<?php
$database = 'EJEMPLO';
$user = 'db2inst1';
$password = 'ibmdb2';
$options = array('autocommit' => DB2_AUTOCOMMIT_OFF);

$conn = db2_connect($database, $user, $password, $options);

if ($conn) {
    echo "Conexión exitosa.\n";
    if (db2_autocommit($conn)) {
         echo "Autocommit está activado.\n";
    }
    else {
         echo "Autocommit está desactivado.\n";
    }
    db2_close($conn);
}
else {
    echo "Conexión fallida.";
}
?>

    
```php

El ejemplo anterior mostrará:

    Conexión exitosa.
    Autocommit está desactivado.

Mejor rendimiento i5/OS

Para lograr utilizar el mejor rendimiento de su i5/OS ibm_db2 1.5.1, la aplicación PHP utiliza el host por defecto, el userid y la contraseña para su `db2_connect`.

```
<?php
  $library = "ADC";
  $i5 = db2_connect("", "", "", array("i5_lib"=>"qsys2"));
  $result = db2_exec($i5,
       "select * from systables where table_schema = '$library'");
  while ($row = db2_fetch_both($result)) {
     echo $row['TABLE_NAME']."</br>";
  }
  db2_close($i5);
?>

    
```php

El ejemplo anterior mostrará:

    ANIMALS
    NAMES
    PICTURES

Utilización del contexto

El siguiente ejemplo muestra cómo activar el contexto, cambiar de usuario y recuperar el ID del usuario actual.

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

$tc_conn = db2_connect($dsn, "", "", $options);
if($tc_conn) {
    echo "Conexión de confianza explícita exitosa.\n";

    if(db2_get_option($tc_conn, "trustedcontext")) {
        $userBefore = db2_get_option($tc_conn, "trusted_user");

        //Código como usuario 1.

        //Cambio al usuario de confianza.
        $parameters = array("trusted_user" => $tc_user,
          "trusted_password" => $tcuser_pass);
        $res = db2_set_option ($tc_conn, $parameters, 1);

        $userAfter = db2_get_option($tc_conn, "trusted_user");
        //Código como usuario de confianza.

        if($userBefore != $userAfter) {
            echo "El usuario ha cambiado." . "\n";
        }
    }

    db2_close($tc_conn);
}
else {
    echo "El cambio de contexto de conexión ha fallado.\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    El cambio de contexto de conexión ha fallado.
    El usuario ha cambiado.

## Véase también

db2_close

db2_pconnect
