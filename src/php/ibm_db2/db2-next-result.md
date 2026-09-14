---
title: db2_next_result
description: Solicita el siguiente conjunto de resultados de la recurso indicado
source_url: https://www.php.net/manual/es/function.db2-next-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-next-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30940
---

db2_next_result

Solicita el siguiente conjunto de resultados de la recurso indicado

## Descripción

```php
db2_next_result(resource $stmt): resource
```php

Un procedimiento de registro puede devolver ningún o múltiples conjuntos de resultados. El primer conjunto de resultados debe manejarse de la misma manera que los resultados devueltos por una simple consulta SELECT. Para obtener el segundo o los siguientes resultados, debe llamarse a la función `db2_next_result` y almacenar el resultado en una variable PHP.

## Parámetros

`stmt`  
Una consulta preparada devuelta por `db2_exec` o `db2_execute`.

## Valores devueltos

Devuelve un nuevo recurso que contiene el siguiente conjunto de resultados si el procedimiento contenía otro conjunto de resultados. Devuelve `false` si el procedimiento no tenía más conjuntos de resultados para devolver.

## Ejemplos

Ejemplo con `db2_next_result`

En el siguiente ejemplo, se llama a un procedimiento que devuelve tres conjuntos de resultados. El primer conjunto de resultados se recupera directamente de la misma recurso sobre la cual se invocó una consulta CALL, mientras que el segundo y tercer conjuntos de resultados se recuperan de las recursos devueltas por la llamada a la función `db2_next_result`.

```
<?php
$conn = db2_connect($database, $user, $password);

if ($conn) {
  $stmt = db2_exec($conn, 'CALL multiResults()');

  print "Recuperación del primer conjunto de resultados\n";
  while ($row = db2_fetch_array($stmt)) {
    var_dump($row);
  }

  print "\nRecuperación del segundo conjunto de resultados\n";
  $res = db2_next_result($stmt);
  if ($res) {
    while ($row = db2_fetch_array($res)) {
      var_dump($row);
    }
  }

  print "\nRecuperación del tercer conjunto de resultados\n";
  $res2 = db2_next_result($stmt);
  if ($res2) {
    while ($row = db2_fetch_array($res2)) {
      var_dump($row);
    }
  }

  db2_close($conn);
}
?>

   
```php

El ejemplo anterior mostrará:

    Recuperación del primer conjunto de resultados
    array(2) {
      [0]=>
      string(16) "Bubbles         "
      [1]=>
      int(3)
    }
    array(2) {
      [0]=>
      string(16) "Gizmo           "
      [1]=>
      int(4)
    }

    Recuperación del segundo conjunto de resultados
    array(4) {
      [0]=>
      string(16) "Sweater         "
      [1]=>
      int(6)
      [2]=>
      string(5) "lama"
      [3]=>
      string(6) "150.00"
    }
    array(4) {
      [0]=>
      string(16) "Smarty          "
      [1]=>
      int(2)
      [2]=>
      string(5) "cheval"
      [3]=>
      string(6) "350.00"
    }

    Recuperación del tercer conjunto de resultados
    array(1) {
      [0]=>
      string(16) "Bubbles         "
    }
    array(1) {
      [0]=>
      string(16) "Gizmo           "
    }
