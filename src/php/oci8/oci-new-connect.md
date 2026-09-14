---
title: oci_new_connect
description: Conexión al servidor Oracle utilizando una sola conexión
source_url: https://www.php.net/manual/es/function.oci-new-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-new-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: ed6de1ae2
order: 57470
---

oci_new_connect

Conexión al servidor Oracle utilizando una sola conexión

## Descripción

```php
oci_new_connect(string $username, string $password, [string $connection_string], [string $encoding], [int $session_mode]): resource
```php

Establece una nueva conexión al servidor Oracle e identifica.

A diferencia de las funciones `oci_connect` y `oci_pconnect`, `oci_new_connect` no almacena en caché las conexiones y siempre devuelve un manejador de conexión recién abierto. Esto es muy útil si la aplicación necesita aislamiento transaccional entre dos conjuntos de consultas.

## Parámetros

`username`  
El nombre de usuario de Oracle.

`password`  
La contraseña para el usuario.

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

Devuelve un identificador de conexión, o `false` si ocurre un error.

## Historial de cambios

| Versión                | Descripción                            |
|------------------------|----------------------------------------|
| 8.0.0, PECL OCI8 3.0.0 | `connection_string` ahora es nullable. |

## Ejemplos

A continuación se muestra cómo separar transacciones.

Ejemplo con `oci_new_connect`

```
<?php

// Creación de la tabla mytab (mycol number);

function query($name, $c)
{
    echo "Querying $name\n";
    $s = oci_parse($c, "select * from mytab");
    oci_execute($s, OCI_NO_AUTO_COMMIT);
    $row = oci_fetch_array($s, OCI_ASSOC);
    if (!$row) {
        echo "No rows\n";
    } else {
        do {
            foreach ($row as $item)
                echo $item . " ";
            echo "\n";
        } while (($row = oci_fetch_array($s, OCI_ASSOC)) != false);
    }
}

$c1 = oci_connect("hr", "welcome", "localhost/orcl");
$c2 = oci_new_connect("hr", "welcome", "localhost/orcl");

$s = oci_parse($c1, "insert into mytab values(1234)");
oci_execute($s, OCI_NO_AUTO_COMMIT);

query("basic connection", $c1);
query("new connection", $c2);
oci_commit($c1);
query("new connection after commit", $c2);

// Muestra:
//   Querying basic connection
//   1234
//   Querying new connection
//   No rows
//   Querying new connection after commit
//   1234

?>

    
```php

Ver la función `oci_connect` para más ejemplos sobre el uso de este parámetro.

## Véase también

`oci_connect`, `oci_pconnect`
