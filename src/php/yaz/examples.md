---
title: Ejemplos
source_url: https://www.php.net/manual/es/yaz.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: af4410a7e
order: 107730
---

## Ejemplos

PHP/YAZ mantiene la vía de conexión con los objetivos de las (Asociaciones-Z). Un recurso representa una conexión a objetivo.

El código debajo demuestra las características de la búsqueda en paralelo del API. Cuando se invoca sin argumentos imprime una consulta de formulario; sino (los argumentos son suministrados) busca los objetivos como son dados en el arreglo del `anfitrión`.

Busqueda Paralela usando YAZ

```php
<?php
$host=$_REQUEST["anfitrion"];
$query=$_REQUEST["consulta"];
$num_hosts = count($host);
if (empty($query) || count($host) == 0) {
    echo '<form method="get">
    <input type="checkbox"
    name="host[]" value="bagel.indexdata.dk/gils" />
        Prueba GILS
    <input type="checkbox"
    name="host[]" value="localhost:9999/Default" />
        Prueba local
    <input type="checkbox" checked="checked"
    name="host[]" value="z3950.loc.gov:7090/voyager" />
        Congresos de librería
    <br />
    RPN Query:
    <input type="text" size="30" name="query" />
    <input type="submit" name="action" value="Buscar" />
    </form>
    ';
} else {
    echo 'Se encontro para ' . htmlspecialchars($query) . '<br />';
    for ($i = 0; $i < $num_hosts; $i++) {
        $id[] = yaz_connect($host[$i]);
        yaz_syntax($id[$i], "usmarc");
        yaz_range($id[$i], 1, 10);
        yaz_search($id[$i], "rpn", $query);
    }
    yaz_wait();
    for ($i = 0; $i < $num_hosts; $i++) {
        echo '<hr />' . $host[$i] . ':';
        $error = yaz_error($id[$i]);
        if (!empty($error)) {
            echo "Error: $error";
        } else {
            $hits = yaz_hits($id[$i]);
            echo "Conteo de Resultado $hits";
        }
        echo '<dl>';
        for ($p = 1; $p <= 10; $p++) {
            $rec = yaz_record($id[$i], $p, "string");
            if (empty($rec)) continue;
            echo "<dt><b>$p</b></dt><dd>";
            echo nl2br($rec);
            echo "</dd>";
        }
        echo '</dl>';
    }
}
?>

   
```
