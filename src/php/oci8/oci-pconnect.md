---
title: oci_pconnect
description: Establece una conexión persistente a un servidor Oracle
source_url: https://www.php.net/manual/es/function.oci-pconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-pconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57540
---

oci_pconnect

Establece una conexión persistente a un servidor Oracle

## Descripción

```php
oci_pconnect(string $username, string $password, [string $connection_string], [string $encoding], [int $session_mode]): resource
```php

Establece una conexión persistente a un servidor Oracle y se identifica.

Las conexiones persistentes se almacenan en caché y se reutilizan entre las consultas, reduciendo así la carga en cada carga de página; una aplicación PHP típica tiene una sola conexión persistente a un servidor Oracle por proceso hijo Apache (o proceso PHP FastCGI/CGI). Ver la sección sobre la [Gestión de Conexiones y el Agrupamiento de Conexiones](#oci8.connection) para más información.

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

Devuelve un identificador de conexión, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_pconnect`

```
<?php

// Conexión al servicio XE (i.e. base de datos) en la máquina "localhost"
$conn = oci_pconnect('hr', 'welcome', 'localhost/XE');
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

Ver la función `oci_connect` para más ejemplos sobre el uso de este parámetro.

## Notas

> [!NOTE]
> La duración y el número máximo de conexiones persistentes Oracle por proceso PHP pueden ajustarse definiendo los siguientes valores de configuración: [oci8.persistent_timeout](#ini.oci8.persistent-timeout), [oci8.ping_interval](#ini.oci8.ping-interval) y [oci8.max_persistent](#ini.oci8.max-persistent).

## Véase también

`oci_connect`, `oci_new_connect`
