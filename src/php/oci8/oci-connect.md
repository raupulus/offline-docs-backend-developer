---
title: oci_connect
description: Establece una conexión con un servidor Oracle
source_url: https://www.php.net/manual/es/function.oci-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 5e41012cf
order: 57240
---

oci_connect

Establece una conexión con un servidor Oracle

## Descripción

```php
oci_connect(string $username, string $password, [string $connection_string], [string $encoding], [int $session_mode]): resource
```php

Devuelve un identificador de conexión, necesario para la mayoría de las llamadas OCI8.

Para mejorar el rendimiento, la mayoría de las aplicaciones deberían utilizar conexiones persistentes con `oci_pconnect` en lugar de `oci_connect`. Consulte la sección sobre [la gestión de conexiones](#oci8.connection) para obtener información general sobre la gestión de conexiones y el agrupamiento de conexiones.

Las llamadas siguientes (tras la primera) a la función `oci_connect` con los mismos parámetros devolverán el manejador de conexión devuelto en la primera llamada. Esto significa que las transacciones realizadas sobre un manejador estarán activas en los demás, siempre que utilicen la *misma* conexión subyacente. Si 2 manejadores deben tener transacciones aisladas, utilice en su lugar la función `oci_new_connect`.

## Parámetros

`username`  
El nombre de usuario de Oracle.

`password`  
La contraseña del usuario.

`connection_string`  
Contiene la instancia `Oracle` a la que debemos conectarnos. Esto puede ser una [cadena de conexión rápida](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-E5358DEA-D619-4B7B-A799-3D2F802500F1), un nombre de conexión del fichero `tnsnames.ora`, o el nombre de una instancia local Oracle.

Si no se especifica o es `null`, PHP utiliza variables de entorno como `TWO_TASK` (en Linux) o `LOCAL` (en Windows) y `ORACLE_SID` para determinar la instancia `Oracle` a la que debemos conectarnos.

Para usar el método de conexión rápida, PHP debe estar vinculado con la biblioteca cliente Oracle 10*g* o superior. La cadena de conexión rápida para Oracle 10*g* o superior es de la forma: *\[//\]host_name\[:port\]\[/service_name\]*. Desde Oracle 11*g*, la sintaxis es: *\[//\]host_name\[:port\]\[/service_name\]\[:server_type\]\[/instance_name\]*. Opciones adicionales fueron introducidas con Oracle 19c Los nombres de los servicios pueden ser encontrados ejecutando la utilidad Oracle `lsnrctl status` en la máquina que ejecuta la base de datos.

El fichero `tnsnames.ora` puede estar en el camino de búsqueda de Oracle Net, que incluye `/your/path/to/instantclient/network/admin`, `$ORACLE_HOME/network/admin` y `/etc`. Una solución alternativa sería definir `TNS_ADMIN` para que el fichero `$TNS_ADMIN/tnsnames.ora` sea leído. Asegúrese de que el demonio que ejecuta el servidor web tenga acceso de lectura a este fichero.

`encoding`  
Determina el juego de caracteres utilizado por la biblioteca cliente Oracle. El juego de caracteres no necesita ser idéntico al utilizado por la base de datos. Si no coincide, Oracle hará lo mejor posible para convertir los datos desde el juego de caracteres de la base de datos. Dependiendo de los juegos de caracteres, el resultado puede no ser perfecto. Además, esta conversión requiere un poco de tiempo del sistema.

Si no se especifica, la biblioteca cliente Oracle determinará un juego de caracteres desde la variable de entorno `NLS_LANG`.

Pasar este parámetro puede reducir el tiempo de conexión.

`session_mode`  
Este parámetro está disponible a partir de PHP 5 (PECL OCI8 1.1) y acepta los siguientes valores: `OCI_DEFAULT`, `OCI_SYSOPER` y `OCI_SYSDBA`. Si bien la constante `OCI_SYSOPER` o la constante `OCI_SYSDBA` es especificada, esta función intentará establecer una conexión privilegiada usando identidades externas. Las conexiones privilegiadas están desactivadas por defecto. Para activarlas, debe definir la opción [oci8.privileged_connect](#ini.oci8.privileged-connect) a `On`.

PHP 5.3 (PECL OCI8 1.3.4) introducen el valor de modo `OCI_CRED_EXT`. Este modo solicita a Oracle usar una identificación externa o bien del sistema operativo, que debe ser configurada en la base de datos. El flag `OCI_CRED_EXT` solo puede ser usado con el nombre de usuario "/" asociado a una contraseña vacía. La opción [oci8.privileged_connect](#ini.oci8.privileged-connect) puede ser definida a `On` o `Off`.

`OCI_CRED_EXT` puede ser combinado con el modo `OCI_SYSOPER` o el modo `OCI_SYSDBA`.

`OCI_CRED_EXT` no es soportado en Windows por razones de seguridad.

## Valores devueltos

Devuelve un identificador de conexión o `false` si ocurre un error.

## Historial de cambios

| Versión                | Descripción                            |
|------------------------|----------------------------------------|
| 8.0.0, PECL OCI8 3.0.0 | `connection_string` ahora es nullable. |

## Ejemplos

Ejemplo con `oci_connect` utilizando la sintaxis simplificada

```
<?php

// Conexión al servicio XE (es decir, la base de datos) en la máquina "localhost"
$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM employees');
oci_execute($stid);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>" . ($item !== null ? htmlentities($item, ENT_QUOTES) : "") . "</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

?>

    
```php

Ejemplo con `oci_connect` utilizando un nombre de conexión de red

```
<?php

// Conexión a la base de datos MYDB descrita en el archivo tnsnames.ora,
// Un ejemplo de entrada tnsnames.ora para MYDB podría ser:
//   MYDB =
//     (DESCRIPTION =
//       (ADDRESS = (PROTOCOL = TCP)(HOST = mymachine.oracle.com)(PORT = 1521))
//       (CONNECT_DATA =
//         (SERVER = DEDICATED)
//         (SERVICE_NAME = XE)
//       )
//     )

$conn = oci_connect('hr', 'welcome', 'MYDB');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM employees');
oci_execute($stid);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>" . ($item !== null ? htmlentities($item, ENT_QUOTES) : "") . "</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

?>

    
```php

Ejemplo con `oci_connect` utilizando un juego de caracteres específico

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE', 'AL32UTF8');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM employees');
oci_execute($stid);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>" . ($item !== null ? htmlentities($item, ENT_QUOTES) : "") . "</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

?>

    
```php

Ejemplo con múltiples llamadas a la función `oci_connect`

```
<?php

$c1 = oci_connect("hr", "welcome", 'localhost/XE');
$c2 = oci_connect("hr", "welcome", 'localhost/XE');

// Tanto $c1 como $c2 muestran el mismo identificador de recursos PHP, lo que significa
// que se trata de la misma conexión a la base de datos
echo "c1 is $c1<br>\n";
echo "c2 is $c2<br>\n";

function create_table($conn)
{
    $stmt = oci_parse($conn, "create table hallo (test varchar2(64))");
    oci_execute($stmt);
    echo "Created table<br>\n";
}

function drop_table($conn)
{
    $stmt = oci_parse($conn, "drop table hallo");
    oci_execute($stmt);
    echo "Dropped table<br>\n";
}

function insert_data($connname, $conn)
{
    $stmt = oci_parse($conn, "insert into hallo
              values(to_char(sysdate,'DD-MON-YY HH24:MI:SS'))");
    oci_execute($stmt, OCI_DEFAULT);
    echo "$connname inserted row without committing<br>\n";
}

function rollback($connname, $conn)
{
    oci_rollback($conn);
    echo "$connname rollback<br>\n";
}

function select_data($connname, $conn)
{
    $stmt = oci_parse($conn, "select * from hallo");
    oci_execute($stmt, OCI_DEFAULT);
    echo "$connname ----selecting<br>\n";
    while (oci_fetch($stmt)) {
        echo "    " . oci_result($stmt, "TEST") . "<br>\n";
    }
    echo "$connname ----done<br>\n";
}

create_table($c1);

insert_data('c1', $c1);   // Inserta una fila utilizando c1
sleep(2);                 // Se espera para ver un timestamp diferente para la segunda fila
insert_data('c2', $c2);   // Inserta una fila utilizando c2

select_data('c1', $c1);   // Se devuelven los resultados de las 2 inserciones
select_data('c2', $c2);   // Se devuelven los resultados de las 2 inserciones

rollback('c1', $c1);      // Revertir la transacción utilizando c1

select_data('c1', $c1);   // Las 2 inserciones han sido revertidas
select_data('c2', $c2);

drop_table($c1);

// El cierre de una conexión hace que las variables PHP sean inaccesibles, pero las demás
// pueden seguir siendo utilizadas
oci_close($c1);
echo "c1 is $c1<br>\n";
echo "c2 is $c2<br>\n";

// Salida:
//    c1 is Resource id #5
//    c2 is Resource id #5
//    Created table
//    c1 inserted row without committing
//    c2 inserted row without committing
//    c1 ----selecting
//        09-DEC-09 12:14:43
//        09-DEC-09 12:14:45
//    c1 ----done
//    c2 ----selecting
//        09-DEC-09 12:14:43
//        09-DEC-09 12:14:45
//    c2 ----done
//    c1 rollback
//    c1 ----selecting
//    c1 ----done
//    c2 ----selecting
//    c2 ----done
//    Dropped table
//    c1 is
//    c2 is Resource id #5

?>

    
```php

## Notas

> [!NOTE]
> Si ha ocurrido un problema durante la instalación de la extensión OCI8, una de las manifestaciones será un problema durante la conexión. Consulte la sección [Instalación/Configuración](#oci8.setup) para obtener más información en caso de errores.

## Véase también

`oci_pconnect`, `oci_new_connect`, `oci_close`
