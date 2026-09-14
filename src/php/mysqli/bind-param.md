---
title: mysqli_stmt::bind_param
description: Vincula variables a una consulta MySQL
source_url: https://www.php.net/manual/es/mysqli-stmt.bind-param.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/bind-param.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55750
---

mysqli_stmt::bind_param

mysqli_stmt_bind_param

Vincula variables a una consulta MySQL

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::bind_param(string $types, mixed $var, mixed ...$vars): bool
```php

Estilo procedimental

```php
mysqli_stmt_bind_param(mysqli_stmt $statement, string $types, mixed $var, mixed ...$vars): bool
```

Vincula variables para los marcadores de parámetro en la consulta preparada por `mysqli_prepare` o `mysqli_stmt_prepare`.

> [!NOTE]
> Si el tamaño de los datos supera el tamaño máximo de un paquete, (`max_allowed_packet`), se debe especificar el carácter `b` en el parámetro `types` y utilizar la función `mysqli_stmt_send_long_data` para enviar el mensaje por paquetes.

> [!NOTE]
> Se debe tener precaución al utilizar `mysqli_stmt_bind_param` con la función `call_user_func_array`. Tenga en cuenta que `mysqli_stmt_bind_param` requiere que sus parámetros sean pasados por referencia, mientras que la función `call_user_func_array` puede aceptar como parámetro una lista de variables que pueden representar referencias o valores.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

`types`  
Una `string` que contiene uno o más caracteres que especifican el tipo de la variable a vincular:

| Carácter | Descripción |
|----|----|
| i | corresponde a una variable de tipo `int` |
| d | corresponde a una variable de tipo `float` |
| s | corresponde a una variable de tipo `string` |
| b | corresponde a una variable de tipo BLOB, que será enviada por paquetes |

Carácter de especificación de tipos {#mysqli-stmt.bind-param.parameters}

`var`; `vars`  
El número de variables y la longitud de la `string` `types` deben corresponder a los parámetros de la consulta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo con mysqli_stmt::bind_param

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli('localhost', 'my_user', 'my_password', 'world');

$stmt = $mysqli->prepare("INSERT INTO CountryLanguage VALUES (?, ?, ?, ?)");
$stmt->bind_param('sssd', $code, $language, $official, $percent);

$code = 'DEU';
$language = 'Bavarian';
$official = "F";
$percent = 11.2;

$stmt->execute();

printf("%d fila insertada.\n", $stmt->affected_rows);

/* Limpiar tabla CountryLanguage */
$mysqli->query("DELETE FROM CountryLanguage WHERE Language='Bavarian'");
printf("%d fila eliminada.\n", $mysqli->affected_rows);

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect('localhost', 'my_user', 'my_password', 'world');

$stmt = mysqli_prepare($link, "INSERT INTO CountryLanguage VALUES (?, ?, ?, ?)");
mysqli_stmt_bind_param($stmt, 'sssd', $code, $language, $official, $percent);

$code = 'DEU';
$language = 'Bavarian';
$official = "F";
$percent = 11.2;

mysqli_stmt_execute($stmt);

printf("%d fila insertada.\n", mysqli_stmt_affected_rows($stmt));

/* Limpiar tabla CountryLanguage */
mysqli_query($link, "DELETE FROM CountryLanguage WHERE Language='Bavarian'");
printf("%d fila eliminada.\n", mysqli_affected_rows($link));

   
```

Los ejemplos anteriores mostrarán:

    1 fila insertada.
    1 fila eliminada.

Uso de `...` para proporcionar argumentos

El operador `...` puede ser utilizado para proporcionar una lista de argumentos de longitud variable, por ejemplo, en una cláusula `WHERE IN`.

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli('localhost', 'my_user', 'my_password', 'world');

$stmt = $mysqli->prepare("SELECT Language FROM CountryLanguage WHERE CountryCode IN (?, ?)");
/* Usando ... para proporcionar argumentos */
$stmt->bind_param('ss', ...['DEU', 'POL']);
$stmt->execute();
$stmt->store_result();

printf("%d filas encontradas.\n", $stmt->num_rows());

   
```

Los ejemplos anteriores mostrarán:

    10 filas encontradas.

## Véase también

`mysqli_stmt_bind_result`, `mysqli_stmt_execute`, `mysqli_stmt_fetch`, `mysqli_prepare`, `mysqli_stmt_send_long_data`, `mysqli_stmt_errno`, `mysqli_stmt_error`
