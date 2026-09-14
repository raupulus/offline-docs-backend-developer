---
title: cubrid_pconnect_with_url
description: Establece una conexión persistente con un servidor CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-pconnect-with-url.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-pconnect-with-url.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9390
---

cubrid_pconnect_with_url

Establece una conexión persistente con un servidor CUBRID

## Descripción

```php
cubrid_pconnect_with_url(string $conn_url, [string $userid], [string $passwd]): resource
```php

Establece una conexión persistente con un servidor CUBRID.

`cubrid_pconnect_with_url` funciona de manera similar a la función `cubrid_connect_with_url`, con dos diferencias principales.

En primer lugar, al establecer la conexión, la función intentará encontrar un enlace (persistente) ya abierto con el mismo host, en el mismo puerto, en la misma base de datos dbname y utilizando el mismo userid. Si se encuentra una conexión de este tipo, su identificador será devuelto en lugar de abrir una nueva conexión.

A continuación, la conexión al servidor CUBRID no se cerrará cuando finalice el script. En su lugar, la conexión permanecerá abierta para su uso futuro (la función `cubrid_close` o la función `cubrid_disconnect` no cerrarán la conexión establecida por la función `cubrid_pconnect_with_url`).

Este tipo de enlace se denominaba anteriormente 'persistente'.

\<url\> ::= CUBRID:\<host\>:\<db_name\>:\<db_user\>:\<db_password\>:\[?\<properties\>\]

\<properties\> ::= \<property\> \[&\<property\>\]

\<properties\> ::= alhosts=\<alternative_hosts\>\[ &rctime=\<time\>\]

\<properties\> ::= login_timeout=\<milli_sec\>

\<properties\> ::= query_timeout=\<milli_sec\>

\<properties\> ::= disconnect_on_query_timeout=true\|false

\<alternative_hosts\> ::= \<standby_broker1_host\>:\<port\> \[,\<standby_broker2_host\>:\<port\>\]

\<host\> := HOSTNAME \| IP_ADDR

\<time\> := SECOND

\<milli_sec\> := MILLI SECOND

host : Un nombre de host o una dirección IP del servidor maestro de la base de datos

db_name : Un nombre de base de datos

db_user : Un nombre de usuario de la base de datos

db_password : Una contraseña para el usuario de la base de datos

autocommit : El modo auto-commit de la conexión a la base de datos

alhosts : Especifica la información del broker del servidor, que será utilizado como punto de salida cuando no sea posible conectarse al servidor activo. Se pueden especificar varios brokers en este caso, y la conexión a los brokers se intentará en el orden de la configuración alhosts

rctime : Un intervalo de tiempo para esperar antes de intentar una conexión con un broker cuando ocurre un error. Después de que ocurra un error, el sistema intentará conectarse a un broker especificado por althosts, terminará la transacción, y luego intentará conectarse al broker activo del servidor maestro de la base de datos. El valor por omisión es de 600 segundos.

login_timeout : Valor del tiempo máximo de espera (unidad: milisegundo) para la identificación a la base de datos. Por omisión, este valor es 0, lo que significa que se espera indefinidamente.

query_timeout : Valor del tiempo máximo de espera (unidad: milisegundo) para la ejecución de la consulta. Una vez alcanzado este valor, se envía un mensaje para cancelar la consulta enviada al servidor. El valor devuelto puede depender de la configuración de disconnect_on_query_timeout; incluso si el mensaje para cancelar la consulta ha sido enviado al servidor, la consulta puede tener éxito.

disconnect_on_query_timeout : Configura un valor que determina si se debe devolver inmediatamente un error para las funciones ejecutadas después del tiempo máximo de espera. El valor por omisión es

false

.

> [!NOTE]
> Los caracteres `?` y `:` utilizados como identificadores en las URLs de conexión PHP no pueden ser incluidos en la contraseña. A continuación se muestra un ejemplo de contraseña inválida, ya que utiliza los caracteres "`?:`" en la URL de conexión.
>
> \$url = "CUBRID:localhost:33000:tdb:dba:12?:?login_timeout=100";
>
> Las contraseñas que contienen el carácter `?` o el carácter `:` pueden ser pasadas como argumento separado.
>
> \$url = "CUBRID:localhost:33000:tbd:::?login_timeout=100";
>
> \$conn = cubrid_pconnect_with_url (\$url, "dba", "12?");
>
> Si el nombre de usuario o la contraseña están vacíos, no se deben eliminar los "`:`"; a continuación se muestra un ejemplo:
>
> \$url = "CUBRID:localhost:33000:demodb:::";

## Parámetros

`conn_url`  
Un `string` que contiene la información de conexión para el servidor.

`userid`  
Nombre de usuario para la base de datos.

`passwd`  
Contraseña para el usuario.

## Valores devueltos

Identificador de conexión, cuando el proceso tiene éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_pconnect_with_url` sin propiedades

```
<?php
$conn_url = "CUBRID:127.0.0.1:33000:demodb:dba::?althost=10.34.63.132:33088&rctime=100";
$con = cubrid_pconnect_with_url ($conn_url);

if ($con) {
   echo "Conexión exitosa";
   cubrid_execute($con, "create table person(id int,name char(16))");
   $req =cubrid_execute($con, "insert into person values(1,'James')");

   if ($req) {
      cubrid_close_request ($req);
      cubrid_commit ($con);
   } else {
      cubrid_rollback ($con);
   }
   cubrid_disconnect ($con);
}
?>

   
```php

Ejemplo de `cubrid_pconnect_with_url` con URL y propiedades

```
<?php
$conn_url = "CUBRID:127.0.0.1:33000:demodb:dba::?autocommit=off&althost=10.34.63.132:33088&rctime=100";
$con = cubrid_pconnect_with_url ($conn_url);

if ($con) {
   echo "Conexión exitosa";
   $req =cubrid_execute($con, "insert into person values(1,'James')");

   if ($req) {
      cubrid_close_request ($req);
      cubrid_commit ($con);
   } else {
      cubrid_rollback ($con);
   }
   cubrid_disconnect ($con);
}
?>

   
```php

## Véase también

cubrid_connect

cubrid_connect_with_url

cubrid_pconnect

cubrid_disconnect

cubrid_close
