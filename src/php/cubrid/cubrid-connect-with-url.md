---
title: cubrid_connect_with_url
description: Establecer el entorno para la conexión al servidor de CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-connect-with-url.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-connect-with-url.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: dfd68fd22
order: 8940
---

cubrid_connect_with_url

Establecer el entorno para la conexión al servidor de CUBRID

## Descripción

```php
cubrid_connect_with_url(string $conn_url, [string $userid], [string $passwd], [bool $new_link]): resource
```php

La función `cubrid_connect_with_url` se usa para establecer el entorno de conexión a su servidor usando la información de conexión pasada con un argumento de cadena de url. Si la característica HA está habilitada en CUBRID, se debe especificar la información de conexión del servidor de emergencia, el cual se usa para la recuperación de fallos cuando sucede uno, en el argumento de cadena de url de esta función. Si el nombre de usuario y la contraseña no se dan se realizará la conexión "PUBLIC" por omisión.

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

host : Un nombre de host o dirección IP de la base de datos maestra

db_name : Un nombre de la base de datos

db_user : Un nombre del usuario de la base de datos

db_password : Una contraseña de usuario de la base de datos

alhosts: Especifica la información del agente del servidor de emergencia, el cual se usa para la recuperación de fallos cuando es imposible conectar al servidor activo. Se pueden especificar múltiples agentes para la recuperación de fallos, y la conexión a los agentes se intenta en el orden listado en alhosts

rctime : Un intervalo entre los intentos de conexión al agente activo en el que ocurrió el fallo. Después de que ocurra un fallo, el sistema se conecta al agente especificado por althosts (recuperación de fallos), finaliza la transacción, y después intenta conectarse al agente activo de la base de datos maestra cada rctime. El valor predeterminado es 600 segundos.

login_timeout : Valor de tiempo de espera (unidad: mseg.) para la identificación en la base de datos. El valor predeterminado es 0, lo que significa un aplazamiento infinito.

query_timeout : Valor de tiempo de espera (unidad: mseg.) para la solicitud de consulta. Cuando finaliza el tiempo de espera, se envía al servidor un mensaje para cancelar la transferencia de la consulta. El valor devuelto puede depender de de la configuración de disconnect_on_query_timeout; incluso si el mensaje para cancelar una petición es enviado al servidor, tal peticioón puede realizarse.

disconnect_on_query_timeout : Configura un valor para establecer si devolver inmediantamente un error de función que está siendo ejecutada al finalizar el tiempo de espera. El valor predeterminado es false.

> [!NOTE]
> `?` y `:`, que son usados como identificadores en el URL de conexión de PHP, no pueden ser incluidos en la contraseña. El siguiente es un ejemplo de una contraseña que no es válida para usarla como URL de conexión ya que contiene "`?:`".
>
> \$url = "CUBRID:localhost:33000:tdb:dba:12?:?login_timeout=100";
>
> Las contraseñas que contengan `?` o `:` se pueden pasar como un parámetro aparte.
>
> \$url = "CUBRID:localhost:33000:tbd:::?login_timeout=100";
>
> \$conn = cubrid_connect_with_url(\$url, "dba", "12?");
>
> Si el usuario o la contraseña están vacíos no se podrá borrar "`:`". He aquí un ejemplo:
>
> \$url = "CUBRID:localhost:33000:demodb:::";

## Parámetros

`conn_url`  
Una cadena de caracteres que contiene la información de conexión al servidor.

`userid`  
El nombre de usuario de la base de datos.

`passwd`  
La contraseña del usuario.

`new_link`  
Si se hace una segunda llamada a `cubrid_connect_with_url` con los mismos argumentos, no se establecerá una nueva conexión, en su lugar, se devolverá el identificador de conexión de la conexión ya abierta. El parámetro `new_link` modifica este comportamiento y hace que `cubrid_connect_with_url` abra siempre una nueva conexión, incluso si `cubrid_connect_with_url` fue llamada antes con los mismos parámetros.

## Valores devueltos

El identificador de conexión, cuando el proceso tiene éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_connect_with_url`, url sin propiedades

```
<?php
$conn_url = "CUBRID:localhost:33000:demodb:dba::";
$con = cubrid_connect_with_url($conn_url);

if ($con) {
   echo "Se conectó con éxito";
   cubrid_execute($con, "create table person(id int,name char(16))");
   $req =cubrid_execute($con, "insert into person values(1,'James')");

   if ($req) {
      cubrid_close_request($req);
      cubrid_commit($con);
   } else {
      cubrid_rollback($con);
   }
   cubrid_disconnect($con);
}
?>

   
```php

Ejemplo de `cubrid_connect_with_url`, url con propiedades

```
<?php
$conn_url = "CUBRID:127.0.0.1:33000:demodb:dba::?login_timeout=100";
$con = cubrid_connect_with_url ($conn_url);

if ($con) {
   echo "Se conectó con éxito";
   cubrid_execute($con, "create table person(id int,name char(16))");
   $req =cubrid_execute($con, "insert into person values(1,'James')");

   if ($req) {
      cubrid_close_request($req);
      cubrid_commit($con);
   } else {
      cubrid_rollback($con);
   }
   cubrid_disconnect($con);
}
?>

   
```php

## Véase también

cubrid_connect

cubrid_pconnect

cubrid_pconnect_with_url

cubrid_disconnect

cubrid_close
