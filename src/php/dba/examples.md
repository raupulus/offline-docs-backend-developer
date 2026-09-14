---
title: Ejemplos
source_url: https://www.php.net/manual/es/dba.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11510
---

## Ejemplos

## Utilización

Ejemplo con DBA

```php
<?php

$id = dba_open("/tmp/test.db", "n", "db2");

if (!$id) {
    echo "dba_open ha fallado\n";
    exit;
}

dba_replace("key", "¡Esto es un ejemplo!", $id);

if (dba_exists("key", $id)) {
    echo dba_fetch("key", $id);
    dba_delete("key", $id);
}

dba_close($id);
?>

   
```

DBA gestiona datos binarios y no tiene límites arbitrarios. Sin embargo, hereda todas las limitaciones definidas por la implementación de la base de datos accedida.

Todas las bases de datos basadas en ficheros deben proporcionar una forma de definir el modo de fichero de las nuevas bases creadas. Este modo se pasa generalmente como cuarto argumento de las funciones `dba_open` o `dba_popen`.

Se puede acceder a todas las entradas de la base de datos de forma lineal, utilizando las funciones `dba_firstkey` y `dba_nextkey`. No se puede modificar la base de datos mientras se está leyendo.

Lectura de una base de datos

```php
<?php

// ...apertura de la base de datos...

$key = dba_firstkey($id);

while ($key !== false) {
    if (true) {          // se retiene la clave para realizar otras acciones más tarde
        $handle_later[] = $key;
    }
    $key = dba_nextkey($id);
}

foreach ($handle_later as $val) {
    dba_delete($val, $id);
}

?>

   
```
