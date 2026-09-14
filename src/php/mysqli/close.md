---
title: mysqli::close
description: Cierra una conexión
source_url: https://www.php.net/manual/es/mysqli.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: f78180344
order: 54940
---

mysqli::close

mysqli_close

Cierra una conexión

## Descripción

Estilo orientado a objetos

```php
public mysqli::close(): true
```php

Estilo procedimental

```php
mysqli_close(mysqli $mysql): true
```

Cierra la conexión especificada por el parámetro `link`.

Las conexiones MySQL no persistentes y los conjuntos de resultados serán cerrados automáticamente cuando sus objetos sean destruidos. Cerrar explícitamente las conexiones abiertas y liberar los conjuntos de resultados es opcional. Sin embargo, es una buena idea cerrar la conexión tan pronto como el script termine de realizar todas sus operaciones de base de datos, si aún tiene mucho procesamiento por hacer después de haber recuperado los resultados.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ahora siempre devuelve `true`. Anteriormente, devolvía `false` en caso de fallo. |

## Ejemplos

Ejemplo de mysqli::close

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$result = $mysqli->query("SELECT Name, CountryCode FROM City ORDER BY ID LIMIT 3");

/* Cerrar la conexión tan pronto como ya no sea necesaria */
$mysqli->close();

foreach ($result as $row) {
    /* Procesamiento de los datos recuperados de la base de datos */
}

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

$result = mysqli_query($mysqli, "SELECT Name, CountryCode FROM City ORDER BY ID LIMIT 3");

/* Cerrar la conexión tan pronto como ya no sea necesaria */
mysqli_close($mysqli);

foreach ($result as $row) {
    /* Procesamiento de los datos recuperados de la base de datos */
}

   
```

## Notas

> [!NOTE]
> `mysqli_close` no cierra las conexiones persistentes. Para más detalles, ver la página del manual sobre las [conexiones persistentes](#features.persistent-connections).

## Véase también

mysqli::\_\_construct, `mysqli_init`, `mysqli_real_connect`, `mysqli_free_result`
