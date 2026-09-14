---
title: El soporte de la reanudación transparente de aplicación (TAF) de OCI8
source_url: https://www.php.net/manual/es/oci8.taf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/taf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: f4c44b869
order: 58540
---

## El soporte de la reanudación transparente de aplicación (TAF) de OCI8

TAF es una funcionalidad de la base de datos Oracle que proporciona alta disponibilidad. Permite que las aplicaciones PHP OCI8 se reconecten automáticamente a una base de datos preconfigurada cuando la conectividad a la base de datos falla debido a una falla de instancia o de red.

En un sistema de base de datos Oracle configurado, TAF ocurre cuando la aplicación PHP detecta que la instancia de la base de datos está fuera de servicio o inalcanzable. Establece una conexión a otro nodo en una configuración Oracle [RAC](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-DEF850F6-27E9-428E-B8FC-530230D78AD2), una base de datos de respaldo en caliente, o la misma instancia de la base de datos ella misma. Consulte el [Guía del programador de la interfaz de llamada Oracle](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-F7817CD2-4A2C-4D37-BD36-56DBABD4725F) para más información sobre OCI TAF.

Una función de retrollamada de aplicación puede ser registrada con `oci_register_taf_callback`. Durante la reanudación, el procesamiento normal de la aplicación se detiene y la retrollamada registrada es invocada. La función de retrollamada notifica a la aplicación de los eventos de reanudación. Si la reanudación tiene éxito, el procesamiento normal se reanudará. Si la reanudación es abandonada, todas las operaciones de base de datos siguientes en la aplicación fallarán debido a la falta de una conexión disponible.

Cuando la conexión falla en otra base de datos, la función de retrollamada puede restablecer cualquier estado de conexión necesario, por ejemplo, rejugando los comandos ALTER SESSION necesarios si el servicio de base de datos no tenía -failover_restore activado.

Una función de retrollamada de aplicación puede ser eliminada llamando a `oci_unregister_taf_callback`.

## Configuración de la reanudación transparente de aplicación

TAF puede ser configurado del lado PHP OCI8 o en la configuración de la base de datos. Si ambos están configurados, los parámetros del lado de la base de datos tienen prioridad.

Configurar TAF en PHP OCI8 (el lado cliente) incluyendo el parámetro FAILOVER_MODE en la parte CONNECT_DATA de un descriptor de conexión. Consulte la sección Configuración de la reanudación transparente de aplicación del [ Guía del administrador de Oracle Database Net Services](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-8F532535-C401-4B51-BE0B-04FD74BB0621) para más información sobre la configuración del lado cliente de TAF.

Un ejemplo de tnsnames.ora para configurar TAF reconectando a la misma instancia de la base de datos:

        ORCL =
          (DESCRIPTION =
            (ADDRESS = (PROTOCOL = TCP)(HOST = 127.0.0.1)(PORT = 1521))
            (CONNECT_DATA =
              (SERVICE_NAME = orclpdb1)
              (FAILOVER_MODE =
                (TYPE = SELECT)
                (METHOD = BASIC)
                (RETRIES = 20)
                (DELAY = 15))))

También es posible configurar TAF del lado de la base de datos modificando el servicio objetivo con [srvctl](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-8DC4D5E0-CA9D-47BC-BAD0-8769405AFEC5) (para RAC) o la procedimiento empaquetado [ DBMS_SERVICE.MODIFY_SERVICE](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-C11449DC-EEDE-4BB8-9D2C-0A45198C1928) (para bases de datos de instancia única).

## Uso de las funciones de retrollamada TAF en OCI8

Una función de retrollamada TAF es una función de aplicación que puede ser registrada para ser llamada durante la reanudación. Es llamada varias veces durante la reanudación de la conexión de la aplicación.

La función de retrollamada es llamada por primera vez cuando se detecta una pérdida de conexión. Esto permite que la aplicación actúe en consecuencia para los retrasos venideros de la reanudación. Si la reanudación tiene éxito, la función de retrollamada es invocada después de que la conexión sea restablecida y utilizable. En ese momento, la aplicación puede resincronizar los parámetros de sesión y tomar acciones tales como informar al usuario que una reanudación ha ocurrido. Si la reanudación es infructuosa, una retrollamada ocurre para informar a la aplicación que una reanudación no ha ocurrido y que la conexión no es utilizable.

La interfaz de una función de retrollamada TAF definida por el usuario es la siguiente:

```php
userCallbackFn(resource $connection, int $event, int $type): int
```php

`connection`  
La conexión Oracle en la que la retrollamada TAF ha sido registrada vía `oci_register_taf_callback`. La conexión no es válida hasta que la reanudación no termine con éxito.

`event`  
El evento de reanudación indica el estado actual de la reanudación.

- `OCI_FO_BEGIN` indica que la reanudación ha detectado una pérdida de conexión y que la reanudación comienza.

- `OCI_FO_END` indica que la reanudación ha tenido éxito.

- `OCI_FO_ABORT` indica que la reanudación ha fallado y que no hay opción de reintentar.

- `OCI_FO_ERROR` indica asimismo que la reanudación ha fallado, pero da a la aplicación la oportunidad de manejar el error y devolver OCI_FO_RETRY para reintentar la reanudación.

- `OCI_FO_REAUTH` indica que un usuario Oracle ha sido reautenticado.

`type`  
El tipo de reanudación. Esto permite a la retrollamada saber qué tipo de reanudación la aplicación ha solicitado. Los valores habituales son los siguientes:

- `OCI_FO_SESSION` indica que el usuario ha solicitado únicamente la reanudación de sesión. Por ejemplo, si la conexión de un usuario se pierde, una nueva sesión es automáticamente creada para el usuario en la base de datos de respaldo. Este tipo de reanudación no intenta recuperar los SELECT.

- `OCI_FO_SELECT` indica que el usuario ha solicitado la reanudación SELECT asimismo. Permite a los usuarios con cursores abiertos continuar recuperándolos después de una falla.

`valor de retorno`  
- `0` indica que los pasos de reanudación deben continuar normalmente.

- `OCI_FO_RETRY` indica que la reanudación debe ser intentada nuevamente por Oracle. En caso de error al reanudar a una nueva conexión, TAF es capaz de reintentar la reanudación. En general, el código de la aplicación debe dormir durante un cierto tiempo antes de devolver OCI_FO_RETRY.

Registro de una función de retrollamada TAF

```
<?php

// Definición de la función de retrollamada del espacio de usuario
class MyClass {
    public static $retry_count;
    public static function TAFCallback($conn, $event, $type)
    {
        switch ($event) {
            case OCI_FO_BEGIN:
                printf(" Reanudando ... Por favor, espere\n");
                printf(" El tipo de reanudación se encontró que era %s \n",
                       (($type==OCI_FO_SESSION) ? "SESSION"
                        :(($type==OCI_FO_SELECT) ? "SELECT" : "UNKNOWN!")));
                self::$retry_count = 0;
                break;
            case OCI_FO_ABORT:
                // La aplicación no puede continuar utilizando la base de datos
                printf(" Reanudación abortada. La reanudación no tendrá lugar.\n");
                break;
            case OCI_FO_END:
                // Reanudación exitosa. Informar a los usuarios que una reanudación ha ocurrido.
                printf(" Reanudación terminada ... reanudando servicios\n");
                break;
            case OCI_FO_REAUTH:
                printf(" Usuario reanudado ... reanudando servicios\n");
                // Rejugar todas las comandos ALTER SESSION asociadas a esta conexión
                // por ejemplo oci_parse($conn, 'ALTER SESSION ...');
                break;
            case OCI_FO_ERROR:
                // Detener los intentos si ya se ha intentado 20 veces.
                if (self::$retry_count >= 20)
                    return 0;
                printf(" Error de reanudación recibido. Durmiendo...\n");
                sleep(10);
                self::$retry_count++;
                return OCI_FO_RETRY; // reintentar reanudación
                break;
            default:
                printf("Evento de reanudación incorrecto: %d.\n", $event);
                break;
        }
        return 0;
    }
}

$fn_name = 'MyClass::TAFCallback';

$conn = oci_connect('hr', 'welcome', 'orcl');
$sysconn = oci_connect('system', 'oracle', 'orcl');

// Usar una conexión privilegiada para construir una instrucción SQL que iniciará la reanudación
$sql = <<< 'END'
select unique 'alter system disconnect session '''||sid||','||serial#||''''
from v$session_connect_info
where sid = sys_context('USERENV', 'SID')
END;

$s = oci_parse($conn, $sql);
oci_execute($s);
$r = oci_fetch_array($s);
$disconnectssql = $r[0];

oci_register_taf_callback($conn, $fn_name); // Registrar TAFCallback a Oracle TAF

print "Analizando consulta de usuario\n";
$sql = "select systimestamp from dual";
$stmt = oci_parse($conn, $sql);

// Por ejemplo, si una pérdida de conexión ocurre en este momento, oci_execute() detectará
// la pérdida y la reanudación comenzará. Durante la reanudación, oci_execute() invocará
// la función de retrollamada TAF varias veces. Si la reanudación tiene éxito,
// una nueva conexión es creada de manera transparente y oci_execute() continuará como
// de costumbre. Los parámetros de sesión de la conexión pueden ser restablecidos en la función de retrollamada TAF.
// Si la reanudación es abandonada, oci_execute() devolverá un error
// ya que una conexión válida no está disponible.

// Desconectar al usuario, lo que inicia la reanudación
print "Desconectando al usuario\n";
$discsql = oci_parse($sysconn, $disconnectssql);
oci_execute($discsql);

print "Ejecutando consulta de usuario\n";
$e = oci_execute($stmt);
if (!$e) {
    $m = oci_error($stmt);
    trigger_error("No se pudo ejecutar la sentencia: ". $m['message'], E_USER_ERROR);
}
$row = oci_fetch_array($stmt);
print $row[0] . "\n";

// hacer otras instrucciones SQL con la nueva conexión, si es válida
// $stmt = oci_parse($conn,  . . .);

?>

   
```php

## Véase también

oci_register_taf_callback

oci_unregister_taf_callback
