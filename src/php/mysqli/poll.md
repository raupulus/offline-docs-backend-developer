---
title: mysqli::poll
description: Verifica el estado de la conexión
source_url: https://www.php.net/manual/es/mysqli.poll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/poll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: c5ccd084c
order: 55240
---

mysqli::poll

mysqli_poll

Verifica el estado de la conexión

## Descripción

Estilo orientado a objetos

```php
public static mysqli::poll(array $read, array $error, array $reject, int $seconds, [int $microseconds]): int
```php

Estilo procedimental

```php
mysqli_poll(array $read, array $error, array $reject, int $seconds, [int $microseconds]): int
```

Verifica el estado de la conexión. El método puede ser utilizado como [estático](#language.oop5.static).

> [!NOTE]
> Disponible solo con [mysqlnd](#book.mysqlnd).

## Parámetros

`read`  
Lista de conexiones para verificar resultados excepcionales que pueden ser leídos.

`error`  
Lista de conexiones en las que se ha producido un error, por ejemplo, fallos en consultas o pérdidas de conexión.

`reject`  
Lista de conexiones rechazadas porque se ejecutaron consultas no asíncronas y para las cuales la función podría devolver resultados.

`seconds`  
Número de segundos de espera máxima, debe ser positivo.

`microseconds`  
Número de microsegundos de espera máxima, debe ser positivo.

## Valores devueltos

Devuelve el número de conexiones disponibles en caso de éxito, `false` en caso contrario.

## Errores/Excepciones

Se lanza una `ValueError` cuando ni el argumento `read` ni el argumento `error` son transmitidos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Ahora lanza una excepción `ValueError` cuando ni el argumento `read` ni el argumento `error` son transmitidos. |

## Ejemplos

Ejemplo con `mysqli_poll`

```php
<?php
$link1 = mysqli_connect();
$link1->query("SELECT 'test'", MYSQLI_ASYNC);
$all_links = array($link1);
$processed = 0;
do {
    $links = $errors = $reject = array();
    foreach ($all_links as $link) {
        $links[] = $errors[] = $reject[] = $link;
    }
    if (!mysqli_poll($links, $errors, $reject, 1)) {
        continue;
    }
    foreach ($links as $link) {
        if ($result = $link->reap_async_query()) {
            print_r($result->fetch_row());
            if (is_object($result))
                mysqli_free_result($result);
        } else die(sprintf("Error MySQLi: %s", mysqli_error($link)));
        $processed++;
    }
} while ($processed < count($all_links));
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => test
    )

## Véase también

`mysqli_query`, `mysqli_reap_async_query`
