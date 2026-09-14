---
title: Ejemplos
source_url: https://www.php.net/manual/es/pgsql.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: aa2e1accf
order: 62840
---

## Ejemplos

## Uso básico

Este simple ejemplo muestra cómo conectarse, ejecutar una consulta y mostrar las líneas resultantes y desconectarse de una base de datos PostgreSQL.

Ejemplo general de la extensión PostgreSQL

```php
<?php

// Conexión, selección de la base de datos
$dbconn = pg_connect("host=localhost dbname=publishing user=www password=foo")
    or die('Conexión imposible : ' . pg_last_error());

// Ejecución de la consulta SQL
$query = 'SELECT * FROM authors';
$result = pg_query($dbconn, $query) or die('Fallo en la consulta : ' . pg_last_error());

// Mostrar los resultados en HTML
echo "<table>\n";
while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
    echo "\t<tr>\n";
    foreach ($line as $col_value) {
        echo "\t\t<td>$col_value</td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table>\n";

// Liberar el resultado
pg_free_result($result);

// Cerrar la conexión
pg_close($dbconn);

?>

    
```

## Uso básico

Estos ejemplos contienen funciones definidas por el usuario similares a las funciones anteriores de MySQL.

Ejemplo de funciones PostgreSQL definidas por el usuario

```php
<?php
// Esta función debería ser necesaria, ya que una conexión PostgreSQL se
// vincula a una base de datos.
function pg_list_dbs($db)
{
    assert(is_resource($db));
    $query = '
SELECT
 d.datname as "Name",
 u.usename as "Owner",
 pg_encoding_to_char(d.encoding) as "Encoding"
FROM
 pg_database d LEFT JOIN pg_user u ON d.datdba = u.usesysid
ORDER BY 1;
';
    return pg_query($db, $query);
}

// Listar las tablas.
function pg_list_tables($db)
{
    assert(is_resource($db));
    $query = "
SELECT
 c.relname as \"Name\",
 CASE c.relkind WHEN 'r' THEN 'table' WHEN 'v' THEN 'view' WHEN 'i' THEN 'index' WHEN 'S' THEN 'sequence' WHEN 's' THEN 'special' END as \"Type\",
  u.usename as \"Owner\"
FROM
 pg_class c LEFT JOIN pg_user u ON c.relowner = u.usesysid
WHERE
 c.relkind IN ('r','v','S','')
 AND c.relname !~ '^pg_'
ORDER BY 1;
";
    return pg_query($db, $query);
}

// Ver también pg_meta_data(). Esto devuelve la definición de los campos como array.
function pg_list_fields($db, $table)
{
    assert(is_resource($db));
    $query = "
SELECT
 a.attname,
 format_type(a.atttypid, a.atttypmod),
 a.attnotnull,
 a.atthasdef,
 a.attnum
FROM
 pg_class c,
 pg_attribute a
WHERE
 c.relname = '".$table."'
 AND a.attnum > 0 AND a.attrelid = c.oid
ORDER BY a.attnum;
";
    return pg_query($db, $query);
}
?>

    
```
