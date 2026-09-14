---
title: odbc_next_result
description: Verifica si hay múltiples resultados disponibles
source_url: https://www.php.net/manual/es/function.odbc-next-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-next-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: false
translation_revision: ed1aff136
order: 98950
---

odbc_next_result

Verifica si hay múltiples resultados disponibles

## Descripción

```php
odbc_next_result(Odbc\Result $statement): bool
```php

Verifica si hay más conjuntos de resultados disponibles accesibles mediante las funciones `odbc_fetch_array`, `odbc_fetch_row`, `odbc_result`, etc.

## Parámetros

`statement`  
The ODBC result object.

## Valores devueltos

Devuelve `true` si hay más conjuntos de resultados, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `odbc_next_result`

```
<?php
$r_Connection = odbc_connect($dsn, $username, $password);

$s_SQL = <<<END_SQL
SELECT 'A'
SELECT 'B'
SELECT 'C'
END_SQL;

$r_Results = odbc_exec($r_Connection, $s_SQL);

$a_Row1 = odbc_fetch_array($r_Results);
$a_Row2 = odbc_fetch_array($r_Results);
echo "Muestra el primer conjunto de resultados: ";
var_dump($a_Row1, $a_Row2);

echo "Recuperación del segundo conjunto de resultados: ";
var_dump(odbc_next_result($r_Results));

$a_Row1 = odbc_fetch_array($r_Results);
$a_Row2 = odbc_fetch_array($r_Results);
echo "Muestra el segundo conjunto de resultados: ";
var_dump($a_Row1, $a_Row2);

echo "Recuperación del tercer conjunto de resultados: ";
var_dump(odbc_next_result($r_Results));

$a_Row1 = odbc_fetch_array($r_Results);
$a_Row2 = odbc_fetch_array($r_Results);
echo "Muestra el tercer conjunto de resultados: ";
var_dump($a_Row1, $a_Row2);

echo "Intento de recuperar un cuarto conjunto de resultados: ";
var_dump(odbc_next_result($r_Results));
?>

    
```php

El ejemplo anterior mostrará:

    Muestra el primer conjunto de resultados: array(1) {
      ["A"]=>
      string(1) "A"
    }
    bool(false)
    Recuperación del segundo conjunto de resultados:bool(true)
    Muestra el segundo conjunto de resultados: array(1) {
      ["B"]=>
      string(1) "B"
    }
    bool(false)
    Recuperación del tercer conjunto de resultados: bool(true)
    Muestra el tercer conjunto de resultados: array(1) {
      ["C"]=>
      string(1) "C"
    }
    bool(false)
    Intento de recuperar un cuarto conjunto de resultados: bool(false)
