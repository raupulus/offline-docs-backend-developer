---
title: Gestión de la conexión OCI8 y la cola de espera
source_url: https://www.php.net/manual/es/oci8.connection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/connection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 5e41012cf
order: 57120
---

## Gestión de la conexión OCI8 y la cola de espera

## Funciones de conexión

La extensión oci8 proporciona tres funciones diferentes para conectarse a Oracle. La función de conexión estándar es la función `oci_connect`. Esta función crea una conexión a la base de datos Oracle y devuelve un recurso utilizado por las futuras llamadas a la base de datos.

La conexión a un servidor Oracle es una operación razonablemente costosa en términos de tiempo. La función `oci_pconnect` utiliza un caché persistente de conexiones que puede ser reutilizado a través de diferentes scripts. Esto significa que una sola conexión será utilizada por proceso PHP (o un hijo Apache).

Si su aplicación se conecta a Oracle utilizando un juego diferente de derechos de base de datos para cada usuario web, el caché persistente utilizado por la función `oci_pconnect` se vuelve menos apropiado ya que el aumento del número de usuarios concurrentes afectará el rendimiento del servidor Oracle, ya que deberá mantener demasiadas conexiones en caché. Si su aplicación es de este tipo, se recomienda optimizar su aplicación utilizando las opciones de configuración [oci8.max_persistent](#ini.oci8.max-persistent) y [oci8.persistent_timeout](#ini.oci8.persistent-timeout) (estas opciones le dan control sobre el tamaño y la vida útil del caché de conexiones persistentes) o utilizar el pool de conexiones residentes de Oracle (para las bases de datos Oracle 11g y posteriores), o bien, utilizar la función `oci_connect`.

Las funciones `oci_connect` y `oci_pconnect` emplean un caché de conexiones; si se realizan múltiples llamadas a `oci_connect`, utilizando los mismos parámetros en un script dado, la segunda llamada y las siguientes devolverán el manejador de conexión existente. El caché utilizado por la función `oci_connect` se limpia al final de la ejecución del script o cuando se cierra explícitamente el manejador de conexión. `oci_pconnect` tiene un comportamiento sustancialmente idéntico, con la diferencia de que el caché se mantiene por separado y se conserva entre las peticiones HTTP.

Es importante recordar esta funcionalidad de caché, ya que da la apariencia de que los dos manejadores no están aislados a nivel de transacciones (en realidad representan el mismo manejador de conexión, por lo que no están aislados en absoluto). Si su conexión necesita dos conexiones separadas, aisladas a nivel de transacciones, debe utilizar la función `oci_new_connect`.

El caché de la función `oci_pconnect` se borra y todas las conexiones a la base de datos se cierran cuando el proceso PHP termina, por lo que las conexiones persistentes solo tienen interés cuando PHP se utiliza como módulo Apache o con FPM o similar. Las conexiones persistentes no tienen ningún interés a través de `oci_connect` cuando PHP se utiliza como CGI o en línea de comandos.

`oci_new_connect` siempre crea una nueva conexión al servidor Oracle, independientemente de la existencia de otras conexiones. Las aplicaciones web de alto tráfico deben evitar utilizar `oci_new_connect`, especialmente en las secciones más cargadas de la aplicación.

Las conexiones persistentes pueden ahora ser cerradas por el usuario, permitiendo un mejor control de los recursos de conexión. Las conexiones persistentes pueden ahora ser cerradas automáticamente cuando ninguna variable PHP las referencia, como podría ser el caso al final de un contexto de una función de usuario PHP. Esto invalidará todas las transacciones no confirmadas. Estos cambios en las conexiones persistentes hacen que funcionen como las funciones no persistentes, simplificando la interfaz, permitiendo una mayor coherencia de la aplicación y previsibilidad. Defina la directiva [oci8.old_oci_close_semantics](#ini.oci8.old-oci-close-semantics) a *On* para recuperar el comportamiento histórico.

El restablecimiento automático de las conexiones persistentes PHP después del reinicio de un proceso Apache o FPM hace que los triggers `LOGON` sean únicamente recomendados para definir los atributos de sesión y no las peticiones de conexión de usuarios por aplicación.

## Pool de conexión DRCP

PHP soporta el pool de conexiones residentes Oracle (DRCP). DRCP permite utilizar más eficientemente la memoria de la base de datos y permite una mejor escalabilidad. Se requieren pocos o ningún cambio para aprovechar DRCP.

DRCP está previsto para aplicaciones que se conectan utilizando poco esquema de base de datos, y que mantienen las conexiones abiertas durante un corto período de tiempo. Las otras aplicaciones deben utilizar el proceso dedicado a la base de datos Oracle, o utilizar los servidores compartidos.

DRCP se beneficia de las 3 funciones de conexión, pero solo la función `oci_pconnect` ofrece el mayor rendimiento.

Para hacer DRCP disponible con OCI8, la versión de las bibliotecas clientes Oracle utilizadas por PHP así como la versión de la base de datos Oracle deben ser 11g o superiores.

La documentación sobre DRCP puede encontrarse en los diferentes manuales Oracle. Por ejemplo, consulte la [configuración del pool de conexiones residentes a la base de datos](https://docs.oracle.com/en/database/oracle/oracle-database/23/jjdbc/database-resident-connection-pooling.html) de la documentación Oracle para un ejemplo de uso. Un [libro blanco sobre DRCP](https://www.oracle.com/technetwork/topics/php/whatsnew/php-scalability-ha-twp-128842.pdf) contiene varias informaciones internas sobre DRCP.

Para utilizar DRCP, instale la extensión OCI8 y las bibliotecas Oracle 11g (o posterior), luego, siga estos pasos:

- Utilizando los privilegios de administrador de la base de datos, utilice un programa como SQL\*Plus para iniciar un pool de conexiones a la base de datos:

          SQL> execute dbms_connection_pool.start_pool;

- Opcionalmente, utilice `dbms_connection_pool.alter_param()` para configurar las opciones DRCP. Las opciones comunes del pool pueden encontrarse utilizando la vista `DBA_CPOOL_INFO`.

- Actualice las cadenas de conexión utilizadas. Para las aplicaciones PHP que actualmente se conectan mediante un nombre de conexión de red como `MYDB`:

          $c = oci_pconnect("myuser", "mypassword", "MYDB");

  modifique el archivo tnsnames.ora y añada una cláusula `(SERVER=POOLED)`, por ejemplo:

          MYDB = (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp) (HOST=myhost.dom.com)
                 (PORT=1521))(CONNECT_DATA=(SERVICE_NAME=sales)
                 (SERVER=POOLED)))

  De lo contrario, puede modificar la sintaxis de conexión fácil en PHP y añadir `:POOLED` después del nombre del servicio:

          $c = oci_pconnect("myuser", "mypassword", "myhost.dom.com:1521/sales:POOLED");

- Edite `php.ini` y elija el nombre de la clase de conexión. Este nombre indica una división lógica del pool de conexión y puede ser utilizado para aislar el pool de diferentes aplicaciones. Todas las aplicaciones PHP utilizando el mismo usuario así como el mismo valor de clase de conexión podrán compartir el pool de conexiones, permitiendo así obtener una mayor disponibilidad.

          oci8.connection_class = "MY_APPLICATION_NAME"

- Ejecute su aplicación, conéctese a la base de datos 11g (o superior).

> [!NOTE]
> Las aplicaciones que utilizan las bibliotecas cliente Oracle 10g que necesitan el rendimiento de las conexiones persistentes, pueden reducir la cantidad de memoria asignada al servidor de la base de datos utilizando los servidores compartidos Oracle (conocidos anteriormente como servidores multihilo). Consulte la documentación Oracle para obtener más información.

> [!NOTE]
> La modificación de una contraseña durante conexiones DRCP fallará con el error "*ORA-56609: Usage not supported with DRCP*". Esto es una restricción documentada de la base de datos Oracle 11g.
