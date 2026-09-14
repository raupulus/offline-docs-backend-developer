---
title: PDOStatement::fetch
description: Recupera la siguiente línea de un conjunto de resultados PDO
source_url: https://www.php.net/manual/es/pdostatement.fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: c142be811
order: 62100
---

PDOStatement::fetch

Recupera la siguiente línea de un conjunto de resultados PDO

## Descripción

```php
public PDOStatement::fetch([int $mode], [int $cursorOrientation], [int $cursorOffset]): mixed
```php

Recupera una línea desde un conjunto de resultados asociado al objeto PDOStatement. El argumento `mode` determina la forma en que PDO devuelve la línea.

## Parámetros

`mode`  
Controla cómo se devolverá la siguiente línea al llamante. Este valor debe ser una de las constantes `PDO::FETCH_*`, y por omisión, vale la constante `PDO::ATTR_DEFAULT_FETCH_MODE` (que por omisión vale la constante `PDO::FETCH_BOTH`).

- `PDO::FETCH_ASSOC`: devuelve un array indexado por el nombre de la columna como se devuelve en el conjunto de resultados

- `PDO::FETCH_BOTH` (por omisión): devuelve un array indexado por los nombres de columnas y también por los números de columnas, comenzando en el índice 0, como se devuelve en el conjunto de resultados

- `PDO::FETCH_BOUND`: devuelve `true` y asigna los valores de las columnas de su conjunto de resultados en las variables PHP a las que están vinculadas con el método PDOStatement::bindColumn

- `PDO::FETCH_CLASS`: devuelve una nueva instancia de la clase solicitada. El objeto se inicializa mapeando las columnas del conjunto de resultados a las propiedades de la clase. Este proceso ocurre antes de que se llame al constructor, permitiendo la población de las propiedades, independientemente de su visibilidad o de su marca como `readonly`. Si una propiedad no existe en la clase, se invocará el método mágico [\_\_set()](#object.set) si existe; de lo contrario, se creará una propiedad pública dinámica. Sin embargo, cuando `PDO::FETCH_PROPS_LATE` también está especificado, el constructor se llama *antes* de que las propiedades sean pobladas. Si `mode` incluye `PDO::FETCH_CLASSTYPE` (p.ej. `PDO::FETCH_CLASS | PDO::FETCH_CLASSTYPE`), el nombre de la clase se determina a partir del valor de la primera columna.

- `PDO::FETCH_INTO` : actualiza una instancia existente de la clase solicitada, vinculando las columnas del conjunto de resultados a los nombres de las propiedades de la clase

- `PDO::FETCH_LAZY` : combina `PDO::FETCH_BOTH` y `PDO::FETCH_OBJ`, y devuelve un objeto `PDORow` que crea los nombres de propiedad del objeto a medida que se acceden.

- `PDO::FETCH_NAMED` : devuelve un array de la misma forma que `PDO::FETCH_ASSOC`, excepto que si hay múltiples columnas con los mismos nombres, el valor apuntado por esta clave será un array de todas las valores de la línea que tiene ese nombre como columna

- `PDO::FETCH_NUM` : devuelve un array indexado por el número de la columna como se devuelve en su conjunto de resultados, comenzando en 0

- `PDO::FETCH_OBJ` : devuelve un objeto anónimo con los nombres de propiedades que corresponden a los nombres de las columnas devueltas en el conjunto de resultados

- `PDO::FETCH_PROPS_LATE` : cuando se usa con `PDO::FETCH_CLASS`, el constructor de la clase es llamado antes de que las propiedades sean asignadas a partir de los valores de columna respectivos.

`cursorOrientation`  
Para un objeto PDOStatement que representa un cursor desplazable, este valor determina qué línea se devolverá al llamante. Este valor debe ser una de las constantes `PDO::FETCH_ORI_*`, y por omisión, vale `PDO::FETCH_ORI_NEXT`. Para solicitar un cursor desplazable para su objeto PDOStatement, debe definir el atributo `PDO::ATTR_CURSOR` a `PDO::CURSOR_SCROLL` cuando prepare la consulta SQL con la función PDO::prepare.

`cursorOffset`  
Para un objeto PDOStatement que representa un cursor desplazable para el cual el argumento `cursorOrientation` está definido a `PDO::FETCH_ORI_ABS`, este valor especifica el número absoluto de la línea en el conjunto de resultados que debe ser recuperada.

Para un objeto PDOStatement que representa un cursor desplazable para el cual el argumento `cursorOrientation` está definido a `PDO::FETCH_ORI_REL`, este valor especifica la línea a recuperar relativamente a la posición del cursor antes de la llamada a la función PDOStatement::fetch.

## Valores devueltos

El valor devuelto por esta función en caso de éxito depende del tipo recuperado. En todos los casos, `false` se devuelve si ocurre un error o si no hay más líneas.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Recuperación de líneas utilizando diferentes métodos

```
<?php
$sth = $dbh->prepare("SELECT nom, couleur FROM fruit");
$sth->execute();

/* estilos PDOStatement::fetch */
print "PDO::FETCH_ASSOC: ";
print "Devuelve la siguiente línea como un array indexado por el nombre de las columnas\n";
$result = $sth->fetch(PDO::FETCH_ASSOC);
print_r($result);
print "\n";

print "PDO::FETCH_BOTH: ";
print "Devuelve la siguiente línea como un array indexado por el nombre y el número de la columna\n";
$result = $sth->fetch(PDO::FETCH_BOTH);
print_r($result);
print "\n";

print "PDO::FETCH_LAZY: ";
print "Devuelve la siguiente línea como objeto PDORow con los nombres de columnas como propiedades\n";
$result = $sth->fetch(PDO::FETCH_LAZY);
print_r($result);
print "\n";

print "PDO::FETCH_OBJ: ";
print "Devuelve la siguiente línea como objeto anónimo con los nombres de columnas como propiedades\n";
$result = $sth->fetch(PDO::FETCH_OBJ);
print $result->name;
print "\n";
?>

    
```php

El ejemplo anterior mostrará:

    PDO::FETCH_ASSOC: Devuelve la siguiente línea como un array indexado por el nombre de las columnas
    Array
    (
        [nom] => apple
        [couleur] => red
    )

    PDO::FETCH_BOTH: Devuelve la siguiente línea como un array indexado por el nombre y el número de la columna
    Array
    (
        [nom] => banana
        [0] => banana
        [couleur] => yellow
        [1] => yellow
    )

    PDO::FETCH_LAZY: Devuelve la siguiente línea como objeto PDORow con los nombres de columnas como propiedades PDORow Object
    (
        [nom] => orange
        [couleur] => orange
    )

    PDO::FETCH_OBJ: Devuelve la siguiente línea como objeto anónimo con los nombres de columnas como propiedades kiwi

Recuperación de líneas con un cursor desplazable

```
<?php
function readDataForwards($dbh) {
    $sql = 'SELECT hand, won, bet FROM mynumbers ORDER BY BET';
    $stmt = $dbh->prepare($sql, array(PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL));
    $stmt->execute();
    while ($row = $stmt->fetch(PDO::FETCH_NUM, PDO::FETCH_ORI_NEXT)) {
        $data = $row[0] . "\t" . $row[1] . "\t" . $row[2] . "\n";
        print $data;
    }
}
function readDataBackwards($dbh) {
    $sql = 'SELECT hand, won, bet FROM mynumbers ORDER BY bet';
    $stmt = $dbh->prepare($sql, array(PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL));
    $stmt->execute();
    $row = $stmt->fetch(PDO::FETCH_NUM, PDO::FETCH_ORI_LAST);
    do {
        $data = $row[0] . "\t" . $row[1] . "\t" . $row[2] . "\n";
        print $data;
    } while ($row = $stmt->fetch(PDO::FETCH_NUM, PDO::FETCH_ORI_PRIOR));
}

print "Lectura hacia adelante :\n";
readDataForwards($conn);

print "Lectura hacia atrás :\n";
readDataBackwards($conn);
?>

    
```php

El ejemplo anterior mostrará:

    Lectura hacia adelante :
    21    10    5
    16    0     5
    19    20    10

    Lectura hacia atrás :
    19    20    10
    16    0     5
    21    10    5

Orden de construcción

Cuando los objetos son recuperados mediante `PDO::FETCH_CLASS`, las propiedades del objeto se asignan primero, luego se llama al constructor de la clase. Sin embargo, cuando `PDO::FETCH_PROPS_LATE` también está especificado, este orden se invierte, es decir, el constructor se llama primero, luego las propiedades son asignadas.

```
<?php
class Person
{
    private $name;

    public function __construct()
    {
        $this->tell();
    }

    public function tell()
    {
        if (isset($this->name)) {
            echo "Soy {$this->name}.\n";
        } else {
            echo "Aún no tengo nombre.\n";
        }
    }
}

$sth = $dbh->query("SELECT * FROM people");
$sth->setFetchMode(PDO::FETCH_CLASS, 'Person');
$person = $sth->fetch();
$person->tell();
$sth->setFetchMode(PDO::FETCH_CLASS|PDO::FETCH_PROPS_LATE, 'Person');
$person = $sth->fetch();
$person->tell();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Soy Alice.
    Soy Alice.
    Aún no tengo nombre.
    Soy Bob.

## Véase también

PDO::prepare, PDOStatement::execute, PDOStatement::fetchAll, PDOStatement::fetchColumn, PDOStatement::fetchObject, PDOStatement::setFetchMode
