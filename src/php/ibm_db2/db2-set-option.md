---
title: db2_set_option
description: Establece opciones para una conexión o recursos
source_url: https://www.php.net/manual/es/function.db2-set-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-set-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: true
translation_revision: 020edc73b
order: 31060
---

db2_set_option

Establece opciones para una conexión o recursos

## Descripción

```php
db2_set_option(resource $resource, array $options, int $type): bool
```php

Establece opciones para un recurso o una conexión. No se pueden establecer opciones para un conjunto de resultados.

## Parámetros

`resource`  
Un recurso válido como el devuelto por `db2_prepare` o una conexión válida como la devuelta por `db2_connect` o `db2_pconnect`.

`options`  
Un array asociativo que contiene opciones de recursos o de conexión válidas. Este parámetro puede ser utilizado para cambiar los valores de autocommit, tipos de cursor (flotante o de avance único) y especificar la capitalización de los nombres de columna (minúscula, mayúscula o natural) que aparecerá en el conjunto de resultados.

`autocommit`  
Pasar `DB2_AUTOCOMMIT_ON` activa el autocommit para la conexión especificada.

Pasar `DB2_AUTOCOMMIT_OFF` desactiva el autocommit para la conexión especificada.

`cursor`  
Pasar `DB2_FORWARD_ONLY` especifica un cursor de avance único para un recurso. Este es el tipo por defecto para un cursor y es soportado por todos los servidores de base de datos.

Pasar `DB2_SCROLLABLE` especifica un cursor flotante para un recurso. Los cursores flotantes permiten que las filas de resultados sean accesibles en un orden no secuencial. Este tipo de cursor es soportado solo por las bases de datos IBM DB2 Universal Database.

`binmode`  
Pasar `DB2_BINARY` especifica que los datos binarios serán devueltos como tales. Este es el modo por defecto. Esto es equivalente a la configuración `ibm_db2.binmode=1` en `php.ini`.

Pasar `DB2_CONVERT` especifica que los datos binarios serán convertidos a codificación hexadecimal y serán devueltos así. Esto es equivalente a la configuración `ibm_db2.binmode=2` en `php.ini`.

Pasar `DB2_PASSTHRU` especifica que los datos binarios serán convertidos a `null`. Esto es equivalente a la configuración `ibm_db2.binmode=3` en `php.ini`.

`db2_attr_case`  
Pasar `DB2_CASE_LOWER` especifica que los nombres de las columnas en el conjunto de resultados serán devueltos en minúsculas.

Pasar `DB2_CASE_UPPER` especifica que los nombres de las columnas en el conjunto de resultados serán devueltos en mayúsculas.

Pasar `DB2_CASE_NATURAL` especifica que los nombres de columnas en el conjunto de resultados serán devueltos en su capitalización natural.

`deferred_prepare`  
Pasar `DB2_DEFERRED_PREPARE_ON` activa la preparación diferida en el recurso de consulta especificado.

Pasar `DB2_DEFERRED_PREPARE_OFF` desactiva la preparación diferida en el recurso de consulta especificado.

Las siguientes nuevas opciones i5/OS están disponibles desde la versión 1.5.1 de ibm_db2. Estas opciones se aplican únicamente cuando PHP e ibm_db2 funcionan de forma nativa en un sistema i5.

`i5_fetch_only`  
`DB2_I5_FETCH_ON`: los cursores son de solo lectura y no pueden ser utilizados para posicionar actualizaciones y eliminaciones. Este es el valor por defecto a menos que la variable de entorno `SQL_ATTR_FOR_FETCH_ONLY` haya sido establecida a `SQL_FALSE`.

`DB2_I5_FETCH_OFF`: los cursores pueden ser posicionados para actualizaciones y eliminaciones.

Las siguientes nuevas opciones están disponibles desde ibm_db2 versión 1.8.0 y posteriores.

`rowcount`  
`DB2_ROWCOUNT_PREFETCH_ON` - El cliente puede solicitar un conteo completo de las filas antes de recuperarlas, lo que significa que la función `db2_num_rows` devuelve el número de filas seleccionadas incluso si se utiliza un cursor `ROLLFORWARD_ONLY`.

`DB2_ROWCOUNT_PREFETCH_OFF` - El cliente no puede solicitar un conteo completo de las filas antes de recuperarlas.

Las siguientes opciones son nuevas y están disponibles desde ibm_db2 versión 1.7.0.

`trusted_user`  
Para cambiar al usuario a un usuario de confianza, indique el identificador de usuario como string del usuario de confianza que desea utilizar. Esta opción puede ser configurada solo a nivel de conexión. Para utilizar esta opción, un contexto de confianza debe estar activado en el recurso de conexión.

`trusted_password`  
La contraseña, como string, que corresponde al usuario de confianza.

Las siguientes opciones son nuevas y están disponibles desde ibm_db2 versión 1.6.0. Estas opciones son útiles para obtener información de seguimiento, accesible a través de `db2_get_option`.

> [!NOTE]
> Cuando el valor de cada opción está a punto de ser definido, algunos servidores pueden no manejar toda la longitud proporcionada y pueden truncar el valor.
>
> Para asegurarse de que los datos especificados en cada opción se convertirán correctamente cuando se transmitan al sistema, utilice solo los caracteres de A a Z, 0 a 9, los guiones bajos (`_`) y los puntos (`.`).

`userid`  
`SQL_ATTR_INFO_USERID`: un puntero a un `string` terminado por `null` utilizado para identificar el ID de usuario del cliente enviado al servidor de base de datos, durante la conexión DB2.

> [!NOTE]
> DB2 para servidores z/OS y OS/390 soporta una longitud mayor a 16 caracteres. El ID de usuario no debe confundirse con el ID de usuario de identificación, se utiliza para los procesos de identificación únicamente y no para los de autorización.

`acctstr`  
`SQL_ATTR_INFO_ACCTSTR`: un puntero a un `string` terminado por `null` utilizado para identificar la cuenta del cliente a enviar al servidor de base de datos durante la conexión DB2.

> [!NOTE]
> DB2 para servidores z/OS y OS/390 soporta una longitud mayor a 200 caracteres.

`applname`  
`SQL_ATTR_INFO_APPLNAME`: un puntero a un `string` terminado por `null` utilizado para identificar el nombre de la aplicación cliente a enviar al servidor de base de datos durante la conexión DB2.

> [!NOTE]
> DB2 para servidores z/OS y OS/390 soporta una longitud mayor a 32 caracteres.

`wrkstnname`  
`SQL_ATTR_INFO_WRKSTNNAME`: un puntero a un `string` terminado por `null` utilizado para identificar el nombre de la estación a enviar al servidor de base de datos durante la conexión DB2.

> [!NOTE]
> DB2 para servidores z/OS y OS/390 soporta una longitud mayor a 18 caracteres.

`type`  
Un `int` que especifica el tipo de recurso que ha sido pasado a la función. El tipo de recurso y valor deben coincidir.

Pasar `1` como valor especifica que un recurso de conexión ha sido pasado a la función.

Pasar cualquier `int` diferente de `1` como valor especifica que un recurso ha sido pasado a la función.

La siguiente tabla especifica qué opciones son compatibles con qué tipos de recursos:

<table>
<caption>Matriz de parámetros de recurso</caption>
<thead>
<tr>
<th style="text-align: center;">Clave</th>
<th style="text-align: center;">Valor</th>
<th colspan="3" style="text-align: center;">Tipo de recurso</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Conexión</td>
<td style="text-align: center;">Consulta</td>
<td style="text-align: center;">Conjunto de resultados</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">autocommit</td>
<td style="text-align: center;"><code>DB2_AUTOCOMMIT_ON</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">autocommit</td>
<td style="text-align: center;"><code>DB2_AUTOCOMMIT_OFF</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">cursor</td>
<td style="text-align: center;"><code>DB2_SCROLLABLE</code></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">cursor</td>
<td style="text-align: center;"><code>DB2_FORWARD_ONLY</code></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">binmode</td>
<td style="text-align: center;"><code>DB2_BINARY</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">binmode</td>
<td style="text-align: center;"><code>DB2_CONVERT</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">binmode</td>
<td style="text-align: center;"><code>DB2_PASSTHRU</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">db2_attr_case</td>
<td style="text-align: center;"><code>DB2_CASE_LOWER</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">db2_attr_case</td>
<td style="text-align: center;"><code>DB2_CASE_UPPER</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">db2_attr_case</td>
<td style="text-align: center;"><code>DB2_CASE_NATURAL</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">deferred_prepare</td>
<td style="text-align: center;"><code>DB2_DEFERRED_PREPARE_ON</code></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">deferred_prepare</td>
<td style="text-align: center;"><code>DB2_DEFERRED_PREPARE_OFF</code></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">i5_fetch_only</td>
<td style="text-align: center;"><code>DB2_I5_FETCH_ON</code></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">rowcount</td>
<td style="text-align: center;"><code>DB2_ROWCOUNT_PREFETCH_ON</code></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">rowcount</td>
<td style="text-align: center;"><code>DB2_ROWCOUNT_PREFETCH_OFF</code></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">trusted_user</td>
<td style="text-align: center;"><code>&lt;USER NAME&gt; (String)</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">trusted_password</td>
<td style="text-align: center;"><code>&lt;PASSWORD&gt; (String)</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">i5_fetch_only</td>
<td style="text-align: center;"><code>DB2_I5_FETCH_OFF</code></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">userid</td>
<td style="text-align: center;"><code>SQL_ATTR_INFO_USERID</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">acctstr</td>
<td style="text-align: center;"><code>SQL_ATTR_INFO_ACCTSTR</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">applname</td>
<td style="text-align: center;"><code>SQL_ATTR_INFO_APPLNAME</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">wrkstnname</td>
<td style="text-align: center;"><code>SQL_ATTR_INFO_WRKSTNNAME</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
</tbody>
</table>

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Establecer un parámetro en un recurso de conexión

```
<?php
/* Parámetros de Conexión */
$database = 'SAMPLE';
$hostname = 'localhost';
$port = 50000;
$protocol = 'TCPIP';
$username = 'db2inst1';
$password = 'ibmdb2';

/* Cadenas de Conexión */
$conn_string = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=$database;";
$conn_string .= "HOSTNAME=$hostname;PORT=$port;PROTOCOL=$protocol;";
$conn_string .= "UID=$username;PWD=$password;";

/* Obtención del Recurso de Conexión */
$conn = db2_connect($conn_string, '', '');

/* Crea el array asociativo de opciones con pares clave-valor válidos */
$options = array('autocommit' => DB2_AUTOCOMMIT_ON);

/* Llamada a la función utilizando el tipo correcto de recurso, el array
* de opciones y el valor type */
$result = db2_set_option($conn, $options, 1);

/* Verifica si todas las opciones pueden ser establecidas correctamente */
if($result)
{
   echo 'Opciones establecidas correctamente';
}
else
{
   echo 'No se pueden establecer las opciones';
}
?>

    
```php

El ejemplo anterior mostrará:

    Opciones establecidas correctamente

Establece múltiples parámetros con un recurso de conexión

```
<?php
/* Parámetros de Conexión */
$database = 'SAMPLE';
$hostname = 'localhost';
$port = 50000;
$protocol = 'TCPIP';
$username = 'db2inst1';
$password = 'ibmdb2';

/* Cadenas de Conexión */
$conn_string = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=$database;";
$conn_string .= "HOSTNAME=$hostname;PORT=$port;PROTOCOL=$protocol;";
$conn_string .= "UID=$username;PWD=$password;";

/* Obtención del Recurso de Conexión */
$conn = db2_connect($conn_string, '', '');

/* Crea el array asociativo de opciones con pares clave-valor válidos */
$options = array('autocommit' => DB2_AUTOCOMMIT_OFF,
'binmode' => DB2_PASSTHRU,
'db2_attr_case' => DB2_CASE_UPPER,
'cursor' => DB2_SCROLLABLE);

/* Llamada a la función utilizando el tipo correcto de recurso, el array
* de opciones y el valor type */
$result = db2_set_option($conn, $options, 1);

/* Verifica si todas las opciones pueden ser establecidas correctamente */
if($result)
{
  echo 'Opciones establecidas correctamente';
}
else
{
  echo 'No se pueden establecer las opciones';
}
?>

    
```php

El ejemplo anterior mostrará:

    Opciones establecidas correctamente

Establece múltiples parámetros con una clave inválida

```
<?php
/* Parámetros de Conexión */
$database = 'SAMPLE';
$hostname = 'localhost';
$port = 50000;
$protocol = 'TCPIP';
$username = 'db2inst1';
$password = 'ibmdb2';

/* Cadenas de Conexión */
$conn_string = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=$database;";
$conn_string .= "HOSTNAME=$hostname;PORT=$port;PROTOCOL=$protocol;";
$conn_string .= "UID=$username;PWD=$password;";

/* Obtención del Recurso de Conexión */
$conn = db2_connect($conn_string, '', '');

/* Crea el array asociativo de opciones con pares clave-valor válidos */
$options = array('autocommit' => DB2_AUTOCOMMIT_OFF,
'MI_CLAVE_INVÁLIDA' => DB2_PASSTHRU,
'db2_attr_case' => DB2_CASE_UPPER,
'cursor' => DB2_SCROLLABLE);

/* Llamada a la función utilizando el tipo correcto de recurso, el array
* de opciones y el valor type */
$result = db2_set_option($conn, $options, 1);

/* Verifica si todas las opciones pueden ser establecidas correctamente */
if($result)
{
   echo 'Opciones establecidas correctamente';
}
else
{
   echo 'No se pueden establecer las opciones';
}
?>

    
```php

El ejemplo anterior mostrará:

    No se pueden establecer las opciones

Establece múltiples parámetros con un valor inválido

```
<?php
/* Parámetros de Conexión */
$database = 'SAMPLE';
$hostname = 'localhost';
$port = 50000;
$protocol = 'TCPIP';
$username = 'db2inst1';
$password = 'ibmdb2';

/* Cadenas de Conexión */
$conn_string = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=$database;";
$conn_string .= "HOSTNAME=$hostname;PORT=$port;PROTOCOL=$protocol;";
$conn_string .= "UID=$username;PWD=$password;";

/* Obtención del Recurso de Conexión */
$conn = db2_connect($conn_string, '', '');

/* Crea el array asociativo de opciones con pares clave-valor válidos */
$options = array('autocommit' => DB2_AUTOCOMMIT_OFF,
'binmode' => 'VALOR_INVÁLIDO',
'db2_attr_case' => DB2_CASE_UPPER,
'cursor' => DB2_SCROLLABLE);

/* Llamada a la función utilizando el tipo correcto de recurso, el array
* de opciones y el valor type */
$result = db2_set_option($conn, $options, 1);

/* Verifica si todas las opciones pueden ser establecidas correctamente */
if($result)
{
   echo 'Opciones establecidas correctamente';
}
else
{
   echo 'No se pueden establecer las opciones';
}
?>

    
```php

El ejemplo anterior mostrará:

    No se pueden establecer las opciones

Establece múltiples parámetros con un recurso de conexión y un tipo incorrecto

```
<?php
/* Parámetros de Conexión */
$database = 'SAMPLE';
$hostname = 'localhost';
$port = 50000;
$protocol = 'TCPIP';
$username = 'db2inst1';
$password = 'ibmdb2';

/* Cadenas de Conexión */
$conn_string = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=$database;";
$conn_string .= "HOSTNAME=$hostname;PORT=$port;PROTOCOL=$protocol;";
$conn_string .= "UID=$username;PWD=$password;";

/* Obtención del Recurso de Conexión */
$conn = db2_connect($conn_string, '', '');

/* Crea el array asociativo de opciones con pares clave-valor válidos */
$options = array('autocommit' => DB2_AUTOCOMMIT_OFF,
'binmode' => DB2_PASSTHRU,
'db2_attr_case' => DB2_CASE_UPPER,
'cursor' => DB2_SCROLLABLE);

/* Llamada a la función utilizando el tipo incorrecto de recurso, el array
* de opciones y el valor type inválido */
$result = db2_set_option($conn, $options, 2);

/* Verifica si todas las opciones pueden ser establecidas correctamente */
if($result)
{
  echo 'Opciones establecidas correctamente';
}
else
{
  echo 'No se pueden establecer las opciones';
}
?>

    
```php

El ejemplo anterior mostrará:

    No se pueden establecer las opciones

Establece múltiples parámetros con un recurso incorrecto

```
<?php
/* Parámetros de Conexión */
$database = 'SAMPLE';
$hostname = 'localhost';
$port = 50000;
$protocol = 'TCPIP';
$username = 'db2inst1';
$password = 'ibmdb2';

/* Cadenas de Conexión */
$conn_string = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=$database;";
$conn_string .= "HOSTNAME=$hostname;PORT=$port;PROTOCOL=$protocol;";
$conn_string .= "UID=$username;PWD=$password;";

/* Obtención del Recurso de Conexión */
$conn = db2_connect($conn_string, '', '');

/* Crea el array asociativo de opciones con pares clave-valor válidos */
$options = array('autocommit' => DB2_AUTOCOMMIT_OFF,
'binmode' => DB2_PASSTHRU,
'db2_attr_case' => DB2_CASE_UPPER,
'cursor' => DB2_SCROLLABLE);

$stmt = db2_prepare($conn, 'SELECT * FROM EMPLOYEE');

/* Llamada a la función utilizando el tipo incorrecto de recurso, pero el array
* de opciones y el valor type válido */
$result = db2_set_option($stmt, $options, 1);

/* Verifica si todas las opciones pueden ser establecidas correctamente */
if($result)
{
  echo 'Opciones establecidas correctamente';
}
else
{
  echo 'No se pueden establecer las opciones';
}
?>

    
```php

El ejemplo anterior mostrará:

    No se pueden establecer las opciones

Todo junto

```
<?php
/* Parámetros de Conexión */
$database = 'SAMPLE';
$hostname = 'localhost';
$port = 50000;
$protocol = 'TCPIP';
$username = 'db2inst1';
$password = 'ibmdb2';

/* Cadenas de Conexión */
$conn_string = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=$database;";
$conn_string .= "HOSTNAME=$hostname;PORT=$port;PROTOCOL=$protocol;";
$conn_string .= "UID=$username;PWD=$password;";

/* Obtención del Recurso de Conexión */
$conn = db2_connect($conn_string, '', '');

/* Crea el array asociativo de opciones con pares clave-valor válidos */
$options = array('db2_attr_case' => DB2_CASE_LOWER,
'cursor' => DB2_SCROLLABLE);

$stmt = db2_prepare($conn, 'SELECT * FROM EMPLOYEE WHERE EMPNO = ? OR EMPNO = ?');

/* Llamada a la función utilizando el tipo correcto de recurso, el array
* de opciones y el valor type */
$option_result = db2_set_option($stmt, $options, 2);
$result = db2_execute($stmt, array('000130', '000140'));

/* Obtiene la fila 2 antes que la fila 1 ya que tenemos un cursor flotante */
print_r(db2_fetch_assoc($stmt, 2));
print '<br /><br />';
print_r(db2_fetch_assoc($stmt, 1));

?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
         [empno] => 000140
         [firstnme] => HEATHER
         [midinit] => A
         [lastname] => NICHOLLS
         [workdept] => C01
         [phoneno] => 1793
         [hiredate] => 1976-12-15
         [job] => ANALYST
         [edlevel] => 18
         [sex] => F
         [birthdate] => 1946-01-19
         [salary] => 28420.00
         [bonus] => 600.00
         [comm] => 2274.00
    )

    Array
    (
         [empno] => 000130
         [firstnme] => DELORES
         [midinit] => M
         [lastname] => QUINTANA
         [workdept] => C01
         [phoneno] => 4578
         [hiredate] => 1971-07-28
         [job] => ANALYST
         [edlevel] => 16
         [sex] => F
         [birthdate] => 1925-09-15
         [salary] => 23800.00
         [bonus] => 500.00
         [comm] => 1904.00
    )

Los cursores i5/OS son de solo lectura

```
<?php
$conn = db2_connect("", "", "", array("i5_lib"=>"nobody"));
$stmt = db2_prepare($conn, 'select * from names where first = ?');
$name = "first2";
db2_bind_param($stmt, 1, "name", DB2_PARAM_IN);
$options = array("i5_fetch_only"=>DB2_I5_FETCH_ON);
db2_set_option($stmt,$options,0);
if (db2_execute($stmt)) {
   while ($row = db2_fetch_array($stmt)) {
      echo "{$row[0]} {$row[1]}";
   }
}
?>

    
```php

El ejemplo anterior mostrará:

    first2 last2

## Véase también

db2_connect

db2_pconnect

db2_exec

db2_prepare

db2_cursor_type
