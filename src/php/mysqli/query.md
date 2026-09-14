---
title: mysqli::query
description: Ejecuta una consulta en la base de datos
source_url: https://www.php.net/manual/es/mysqli.query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: d470f625f
order: 55260
---

mysqli::query

mysqli_query

Ejecuta una consulta en la base de datos

## Descripción

Estilo orientado a objetos

```php
public mysqli::query(string $query, [int $result_mode]): mysqli_result
```php

Estilo procedimental

```php
mysqli_query(mysqli $mysql, string $query, [int $result_mode]): mysqli_result
```

Ejecuta una consulta en la base de datos.

> [!WARNING]
> Si la consulta contiene alguna entrada de variable, entonces se deben usar [sentencias preparadas parametrizadas](#mysqli.quickstart.prepared-statements) en su lugar. Alternativamente, los datos deben estar correctamente formateados y todas las cadenas deben ser escapadas usando la función `mysqli_real_escape_string` .

Para consultas no-DML (que no son un INSERT, un UPDATE o un DELETE), esta función es similar a llamar a `mysqli_real_query` seguida de `mysqli_use_result` o `mysqli_store_result`.

> [!NOTE]
> Si se pasa una consulta a `mysqli_query` que es más larga que `max_allowed_packet`, los códigos de error devueltos serán diferentes según si se utiliza MySQL Native Driver (`mysqlnd`) o la MySQL Client Library (`libmysqlclient`). El comportamiento se define como sigue:
>
> - `mysqlnd` en Linux devuelve un código de error 1153. El mensaje de error será “got a packet bigger than `max_allowed_packet` bytes”.
>
> - `mysqlnd` en Windows devuelve un código de error 2006. El mensaje será del tipo “server has gone away”.
>
> - `libmysqlclient` en cualquier plataforma devuelve el código de error 2006. El mensaje será del tipo “server has gone away”.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`query`  
La consulta, en forma de `string`.

`result_mode`  
El modo de resultado puede ser una de las 3 constantes que indican cómo el resultado será devuelto por el servidor MySQL.

`MYSQLI_STORE_RESULT` (por omisión) - devuelve un objeto `mysqli_result` con un conjunto de resultados almacenados en búfer.

`MYSQLI_USE_RESULT` - devuelve un objeto `mysqli_result` con un conjunto de resultados no almacenados en búfer. Mientras haya registros pendientes de ser recuperados, la línea de conexión estará ocupada y todas las llamadas siguientes devolverán el error `Commands out of sync`. Para evitar el error, todos los registros deben ser recuperados del servidor o el conjunto de resultados debe ser descartado llamando a la `mysqli_free_result`.

`MYSQLI_ASYNC` (disponible con mysqlnd) - la consulta se ejecuta de manera asíncrona y ningún conjunto de resultados es devuelto inmediatamente. `mysqli_poll` se utiliza entonces para obtener los resultados de tales consultas. Utilizada en combinación con la constante `MYSQLI_STORE_RESULT` o `MYSQLI_USE_RESULT`.

## Valores devueltos

Devuelve `false` en caso de fallo. Para consultas exitosas que producen un conjunto de resultados como `SELECT, SHOW, DESCRIBE` o `EXPLAIN`, `mysqli_query` devolverá un objeto `mysqli_result`. Para otros tipos de consultas exitosas, `mysqli_query` devolverá `true`.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo con mysqli::query

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* "Create table" no devolverá ningún conjunto de resultados */
$mysqli->query("CREATE TEMPORARY TABLE myCity LIKE City");
printf("Tabla myCity creada con éxito.\n");

/* Consulta "Select" devuelve un conjunto de resultados */
$result = $mysqli->query("SELECT Name FROM City LIMIT 10");
printf("Select ha devuelto %d líneas.\n", $result->num_rows);

/* Si tenemos que recuperar muchos datos, utilizamos MYSQLI_USE_RESULT */
$result = $mysqli->query("SELECT * FROM City", MYSQLI_USE_RESULT);

/* Tenga en cuenta que no podemos ejecutar ninguna función que actúe en el servidor mientras
   el conjunto de resultados no esté cerrado. Todas las llamadas devolverán un 'out of sync' */
$mysqli->query("SET @a:='this will not work'");

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* "Create table" no devolverá ningún conjunto de resultados */
mysqli_query($link, "CREATE TEMPORARY TABLE myCity LIKE City");
printf("Tabla myCity creada con éxito.\n");

/* Consulta "Select" devuelve un conjunto de resultados */
$result = mysqli_query($link, "SELECT Name FROM City LIMIT 10");
printf("Select ha devuelto %d líneas.\n", mysqli_num_rows($result));

/* Si tenemos que recuperar muchos datos, utilizamos MYSQLI_USE_RESULT */
$result = mysqli_query($link, "SELECT * FROM City", MYSQLI_USE_RESULT);

/* Tenga en cuenta que no podemos ejecutar ninguna función que actúe en el servidor mientras
   el conjunto de resultados no esté cerrado. Todas las llamadas devolverán un 'out of sync' */
mysqli_query($link, "SET @a:='this will not work'");

   
```

Los ejemplos anteriores mostrarán:

    Tabla myCity creada con éxito.
    Select ha devuelto 10 líneas.
    Fatal error: Uncaught mysqli_sql_exception: Commands out of sync; you can't run this command now in...

## Véase también

`mysqli_execute_query`, `mysqli_real_query`, `mysqli_multi_query`, `mysqli_prepare`, `mysqli_free_result`
