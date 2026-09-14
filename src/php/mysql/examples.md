---
title: Ejemplos
source_url: https://www.php.net/manual/es/mysql.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_reviewed: true
translation_revision: 47ce3a593
order: 52020
---

## Ejemplos

## Ejemplo con la extensión MySQL

Este ejemplo simple muestra cómo conectarse, ejecutar una consulta, leer la información obtenida y desconectarse de una base de datos MySQL.

Ejemplo de presentación de la extensión MySQL

```php
<?php
// Conexión y selección de la base de datos
$link = mysql_connect('mysql_host', 'mysql_user', 'mysql_password')
    or die('Imposible conectarse: ' . mysql_error());
echo 'Conectado correctamente';
mysql_select_db('my_database') or die('Imposible seleccionar la base de datos');

// Ejecución de consultas SQL
$query = 'SELECT * FROM my_table';
$result = mysql_query($query) or die('Fallo en la consulta: ' . mysql_error());

// Visualización de los resultados en HTML
echo "<table>\n";
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
    echo "\t<tr>\n";
    foreach ($line as $col_value) {
        echo "\t\t<td>$col_value</td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table>\n";

// Liberación de los resultados
mysql_free_result($result);

// Cierre de la conexión
mysql_close($link);
?>

    
```
