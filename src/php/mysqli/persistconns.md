---
title: La extensión mysqli y las conexiones persistentes
source_url: https://www.php.net/manual/es/mysqli.persistconns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/persistconns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: a714378ed
order: 56060
---

## La extensión mysqli y las conexiones persistentes

La idea detrás de las conexiones persistentes es que las conexiones entre los clientes y la base de datos pueden ser reutilizadas por otro proceso cliente, en lugar de ser destruidas y recreadas numerosas veces. Esto reduce el coste de creación de conexiones cada vez que una de ellas es requerida, ya que las conexiones se almacenan en caché para ser recicladas.

A diferencia de la extensión MySQL, MySQLi no proporciona una función separada para abrir conexiones persistentes. Para abrir una conexión persistente, se debe añadir `p:` al nombre del host al conectar.

El problema de las conexiones persistentes es que pueden ser dejadas en un estado impredecible por los clientes. Por ejemplo, un bloqueo de tabla puede haber sido puesto antes de que el cliente se desconecte inesperadamente. Un nuevo cliente tomará entonces la conexión, pero “tal cual”. Sería necesario entonces que el nuevo cliente realice una limpieza en profundidad de la conexión antes de poder reutilizarla sin interferencias, lo cual es una desventaja para el programador.

La conexión persistente de la extensión `mysqli` proporciona un método de limpieza automática. La limpieza es realizada por `mysqli` e incluye:

- La cancelación de las transacciones activas.

- El cierre y destrucción de las tablas temporales.

- El desbloqueo de las tablas.

- La restauración de los valores por defecto de las variables de sesión.

- La liberación de las sentencias preparadas (esto siempre ocurre con PHP).

- El cierre del manejador.

- La liberación de los bloqueos puestos por `GET_LOCK`.

Esto asegura que la conexión persistente está en una condición correcta antes de ser devuelta al grupo de conexiones, y que un cliente diferente la retome.

La extensión `mysqli` realiza esta limpieza llamando automáticamente a la función C `mysql_change_user()`.

La limpieza automática tiene sus ventajas e inconvenientes. La ventaja es que el programador no necesita preocuparse por ello, ya que es llamada automáticamente. Sin embargo, el inconveniente es que este código puede *finalmente* ser un poco más lento, ya que debe ser llamado cada vez que la conexión es devuelta al grupo de espera.

Es posible desactivar la limpieza del código, compilando PHP con la opción `MYSQLI_NO_CHANGE_USER_ON_PCONNECT`.

> [!NOTE]
> La extensión `mysqli` soporta las conexiones persistentes con el MySQL Native Driver y con la biblioteca MySQL.
