---
title: Modos de recuperación
source_url: https://www.php.net/manual/es/pdo.constants.fetch-modes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/constants.fetch-modes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 61760
---

## Modos de recuperación

Véase [constantes de cursor](#pdo.constants.cursors) para las constantes de cursor `PDO::FETCH_ORI_*`.

## Modos básicos de recuperación

| Modo de recuperación | Resumen |
|----|----|
| `PDO::FETCH_DEFAULT` | Valor especial para usar el modo de recuperación por omisión actual. |
| `PDO::FETCH_ASSOC` | Array indexado solo por el nombre de la columna. |
| `PDO::FETCH_BOTH` (por defecto) | Array indexado tanto por el número de columna como por el nombre. |
| `PDO::FETCH_NAMED` | Variante de `PDO::FETCH_ASSOC` que conserva las columnas duplicadas. |
| `PDO::FETCH_NUM` | Array indexado solo por el número de columna. |
| `PDO::FETCH_COLUMN` | Una sola columna. |
| `PDO::FETCH_KEY_PAIR` | Pares clave-valor, indexados por la primera columna. |
| `PDO::FETCH_FUNC` | Una una función para crear el valor de retorno. (solamente con PDOStatement::fetchAll) |
| `PDO::FETCH_OBJ` | Objeto anónimo (`stdClass`). |
| `PDO::FETCH_CLASS` | Un objeto de la clase especificada. |

## Opciones de PDO::FETCH_CLASS

Estos modos se utilizan para implementar opciones al usar `PDO::FETCH_CLASS`.

| Modo de recuperación | Resumen |
|----|----|
| `PDO::FETCH_CLASSTYPE` | Usa la primera columna como nombre de la clase. |
| `PDO::FETCH_PROPS_LATE` | Llama al constructor antes de establecer las propiedades. |
| `PDO::FETCH_SERIALIZE` | Usa datos serializados de PHP. Obsoleto a partir de PHP 8.1.0. |

## Modos de resultado único

Los siguientes modos no pueden ser utilizados con PDOStatement::fetchAll.

| Modo de recuperación | Resumen |
|----|----|
| `PDO::FETCH_BOUND` | Asigna valores a las variables especificadas. |
| `PDO::FETCH_INTO` | Actualiza un objeto existente. |
| `PDO::FETCH_LAZY` | Recuperación diferida mediante `PDORow` para acceso similar a arrays y objetos. |

## Flags de comportamiento especiales para PDOStatement::fetchAll

Los siguientes modos especiales para resultados múltiples solo funcionan con PDOStatement::fetchAll y no funcionan con algunos otros modos de recuperación. Consulta la documentación completa para más detalles.

| Modo de recuperación | Resumen |
|----|----|
| `PDO::FETCH_GROUP` | Los resultados se agrupan por la primera columna. |
| `PDO::FETCH_UNIQUE` | Los resultados se indexan (únicamente) por la primera columna. |

## Manejo de nombres duplicados de columnas

Es posible que los resultados contengan varias columnas con el mismo nombre. Por ejemplo, al combinar dos tablas que contienen una columna con el mismo nombre.

Debido a que las estructuras de PHP, como los arrays y los objetos, no admiten varias claves o propiedades con el mismo nombre, el array o el objeto devuelto contendrá solo uno de los valores con el mismo nombre.

El valor que se devuelve para un nombre duplicado determinado debe considerarse indefinido.

Para evitar este problema, asigne nombres explícitos a las columnas mediante un alias. Por ejemplo:

```php
SELECT table1.created_at AS t1_created_at,
       table2.created_at AS t2_created_at
FROM table1
JOIN table2 ON table1.table2id = table2.id

   
```

Véase también `PDO::FETCH_NAMED`, `PDO::ATTR_FETCH_TABLE_NAMES` y `PDO::ATTR_FETCH_CATALOG_NAMES`.

## Estableciendo el modo de recuperación predeterminado

Es posible establecer el modo de recuperación predeterminado para todas las consultas usando `PDO::ATTR_DEFAULT_FETCH_MODE` con PDO::\_\_construct o PDO::setAttribute.

El modo de recuperación predeterminado para una sentencia específica se puede establecer usando PDOStatement::setFetchMode. Esto afecta a la reutilización como sentencia preparada y a la iteración (usando [`foreach`](#control-structures.foreach)).

> [!CAUTION]
> PDOStatement::setAttribute no se puede usar para establecer el modo de recuperación predeterminado. Solo acepta atributos específicos del controlador y, de forma silenciosa, ignora los atributos que no reconoce.

## PDO::FETCH_DEFAULT (`int`)

Disponible a partir de PHP 8.0.7.

Este es un valor especial que utiliza el modo de recuperación predeterminado actual para un `PDOStatement`. Es especialmente útil como valor predeterminado para los parámetros de método al extender `PDOStatement` para su uso con `PDO::ATTR_STATEMENT_CLASS`.

Este valor no se puede usar con `PDO::ATTR_DEFAULT_FETCH_MODE`.

## PDO::FETCH_ASSOC (`int`)

`PDO::FETCH_ASSOC` devuelve un array indexada únicamente por nombre de columna.

```php
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users");
$row = $stmt->fetch(\PDO::FETCH_ASSOC);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [userid] => 104
        [name] => Chris
        [country] => Ukraine
    )

## PDO::FETCH_BOTH (`int`)

Este es el modo de recuperación predeterminado.

`PDO::FETCH_BOTH` devuelve un array indexada tanto por número de columna como por nombre. Esto significa que cada valor devuelto se duplica para cada fila de resultados.

El número de columna comienza en 0 y se determina por el orden de las columnas de la consulta, no (por ejemplo) por el orden en que se definen las columnas en la tabla.

> [!NOTE]
> No se recomienda utilizar el índice de columna numérico, ya que esto puede cambiar cuando se cambie la consulta, o cuando se cambie el esquema de la tabla al usar `SELECT *`.

> [!NOTE]
> Es posible que el número de entradas indexadas por nombre no coincida con el número de entradas indexadas por número en los casos en que varias columnas devueltas utilicen el mismo nombre.

```php
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users");
$row = $stmt->fetch(\PDO::FETCH_BOTH);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [id] => 104,
        [0] => 104,
        [name] => Chris,
        [1] => Chris,
        [country] => Ukraine,
        [2] => Ukraine
    )

## PDO::FETCH_NAMED (`int`)

`PDO::FETCH_NAMED` devuelve resultados en el mismo formato que `PDO::FETCH_ASSOC` excepto que, cuando varias columnas usan el mismo nombre, todos los valores se devuelven como una lista.

Para obtener más información sobre el manejo de nombres de columnas duplicados y alternativas, consulte la sección [manejo de nombres duplicados](#pdo.fetch-modes.duplicate-names) anterior.

El orden en el que se devuelven los valores duplicados debe considerarse indefinido. No hay forma de saber de dónde proviene cada valor.

```php
<?php
$stmt = $pdo->query(
    "SELECT users.*, referrer.name
     FROM users
     LEFT JOIN users AS referrer ON users.referred_by = referrer.userid
     WHERE userid = 109"
);
$row = $stmt->fetch(\PDO::FETCH_NUM);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [userid] => 109
        [name] => Array
            (
                [0] => Toni
                [1] => Chris
            )
        [country] => Germany
        [referred_by] = 104
    )

## PDO::FETCH_NUM (`int`)

`PDO::FETCH_NUM` devuelve un array indexada únicamente por número de columna. El número de columna comienza en 0 y se determina por el orden de las columnas de resultados en la consulta, no (por ejemplo) por el orden en que se definen las columnas en la tabla.

> [!NOTE]
> No se recomienda utilizar el índice de columna numérico, ya que esto puede cambiar cuando se cambie la consulta, o cuando se cambie el esquema de la tabla al usar `SELECT *`.

```php
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users");
$row = $stmt->fetch(\PDO::FETCH_NUM);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => 104
        [1] => Chris
        [2] => Ukraine
    )

## PDO::FETCH_COLUMN (`int`)

`PDO::FETCH_COLUMN` devuelve los valores de una sola columna. Utilice el segundo argumento de PDOStatement::setFetchMode o PDOStatement::fetchAll para especificar la columna que se devuelve.

Si la columna especificada no existe, se lanzará un `ValueError`.

```php
<?php
$stmt = $pdo->query("SELECT name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_COLUMN);
print_r($row);

$stmt = $pdo->query("SELECT name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_COLUMN, 1);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => Chris
        [1] => Jamie
        [2] => Robin
    )

    Array
    (
        [0] => Ukraine
        [1] => England
        [2] => Germany
    )

## PDO::FETCH_KEY_PAIR (`int`)

`PDO::FETCH_KEY_PAIR` devuelve pares de valores, indexados por la primera columna. Los resultados deben contener solo dos columnas. Este modo de recuperación solo tiene sentido con PDOStatement::fetchAll.

> [!NOTE]
> Si la primera columna no es única, se perderán valores. Qué valor(es) se perderán debe considerarse indefinido.

```php
<?php
$stmt = $pdo->query("SELECT name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_KEY_PAIR);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [Chris] => Ukraine
        [Jamie] => England
        [Robin] => Germany
    )

## PDO::FETCH_FUNC (`int`)

Especifique una función para crear el valor devuelto. Este modo solo se puede usar con PDOStatement::fetchAll.

La función recibe los valores como parámetros. No es posible recuperar el nombre de la columna a la que estaba asociado un valor dado. Es crucial asegurarse de que el orden de las columnas en la consulta coincida con el orden de los parámetros de la función.

> [!NOTE]
> Los efectos de `PDO::FETCH_GROUP` y `PDO::FETCH_UNIQUE` se aplican a los resultados antes de que se llame a la función.

```php
<?php
function valueCreator($col1, $col2, $col3)
{
    return [
        'col1' => $col1,
        'col2' => strtoupper($col2),
        'col3' => $col3,
        'customKey' => 'customValue',
    ];
}

$stmt = $pdo->query("SELECT userid, name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_FUNC, valueCreator(...));
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [col1] => 104
                [col2] => SAM
                [col3] => Ukraine
                [customKey] => customValue
            )

        [1] => Array
            (
                [col1] => 105
                [col2] => JAMIE
                [col3] => England
                [customKey] => customValue
            )

        [2] => Array
            (
                [col1] => 107
                [col2] => ROBIN
                [col3] => Germany
                [customKey] => customValue
            )

    )

## PDO::FETCH_OBJ (`int`)

`PDO::FETCH_OBJ` devuelve un objeto `stdClass`.

Véase también PDOStatement::fetchObject y `PDO::FETCH_CLASS`.

```php
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users");
$row = $stmt->fetch(\PDO::FETCH_OBJ);
print_r($row);

   
```

El ejemplo anterior mostrará:

    stdClass Object
    (
        [userid] => 104
        [name] => Chris
        [country] => Ukraine
    )

## PDO::FETCH_CLASS (`int`)

Devuelve un objeto de una clase específica. Para conocer comportamientos adicionales, consulte las [opciones flags](#pdo.fetch-modes.class-flags).

Si una propiedad no existe con el nombre de una columna devuelta, se declarará dinámicamente. Este comportamiento está obsoleto y provocará un error a partir de PHP 9.0.

Véase también PDOStatement::fetchObject.

```php
<?php
class TestEntity
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;

    public function __construct()
    {
        print "Constructor called with ". count(func_get_args()) ." args\n";
        print "Properties set when constructor called? "
            . (isset($this->name) ? 'Yes' : 'No') . "\n";
    }
}

$stmt = $db->query(
    "SELECT userid, name, country, referred_by_userid FROM users"
);
$stmt->setFetchMode(PDO::FETCH_CLASS, TestEntity::class);
$result = $stmt->fetch();
var_dump($result);

   
```

Resultado del ejemplo anterior es similar a:

    Constructor called with 0 args
    Properties set when constructor called? Yes
    object(TestEntity)#3 (4) {
      ["userid"]=>
      int(104)
      ["name"]=>
      string(5) "Chris"
      ["country"]=>
      string(7) "Ukraine"
      ["referred_by_userid"]=>
      NULL
    }

## PDO::FETCH_CLASSTYPE (`int`)

Este modo de recuperación solo se puede usar combinado con `PDO::FETCH_CLASS` (y [sus otras opciones](#pdo.fetch-modes.class-flags)).

Cuando se utiliza este modo de recuperación, PDO utilizará la primera columna devuelta como nombre de la clase que se devolverá.

Si no se encuentra la clase especificada, se devolverá un objeto `stdClass`, sin advertencia ni error.

```php
<?php
class TestEntity
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;

    public function __construct()
    {
        print "Constructor called with ". count(func_get_args()) ." args\n";
        print "Properties set when constructor called? "
            . (isset($this->name) ? 'Yes' : 'No') . "\n";
    }
}

$stmt = $db->query(
    "SELECT 'TestEntity', userid, name, country, referred_by_userid FROM users"
);
$stmt->setFetchMode(PDO::FETCH_CLASS | PDO::FETCH_CLASSTYPE);
$result = $stmt->fetch();
var_dump($result);

   
```

Resultado del ejemplo anterior es similar a:

    Constructor called with 0 args
    Properties set when constructor called? Yes
    object(TestEntity)#3 (4) {
      ["userid"]=>
      int(104)
      ["name"]=>
      string(5) "Chris"
      ["country"]=>
      string(7) "Ukraine"
      ["referred_by_userid"]=>
      NULL
    }

## PDO::FETCH_PROPS_LATE (`int`)

Este modo de recuperación solo se puede usar combinado con `PDO::FETCH_CLASS` (y [sus otras opciones](#pdo.fetch-modes.class-flags)).

Cuando se utiliza este modo de recuperación, se llamará al constructor antes de que se establezcan las propiedades.

```php
<?php
class TestEntity
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;

    public function __construct()
    {
        print "Constructor called with ". count(func_get_args()) ." args\n";
        print "Properties set when constructor called? "
            . (isset($this->name) ? 'Yes' : 'No') . "\n";
    }
}

$stmt = $db->query(
    "SELECT userid, name, country, referred_by_userid FROM users"
);
$stmt->setFetchMode(PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, TestEntity::class);
$result = $stmt->fetch();
var_dump($result);

   
```

Resultado del ejemplo anterior es similar a:

    Constructor called with 0 args
    Properties set when constructor called? No
    object(TestEntity)#3 (4) {
      ["userid"]=>
      int(104)
      ["name"]=>
      string(5) "Chris"
      ["country"]=>
      string(7) "Ukraine"
      ["referred_by_userid"]=>
      NULL
    }

## PDO::FETCH_SERIALIZE (`int`)

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.0.0. Depender de esta característica está altamente desaconsejado.

Este modo de recuperación solo se puede usar combinado con `PDO::FETCH_CLASS` (y [sus otras opciones](#pdo.fetch-modes.class-flags)).

Cuando se utiliza este modo de recuperación, la clase especificada debe ser Serializable.

> [!CAUTION]
> Esta función no admite un string que contenga un objeto serializado completo (con `serialize`).

> [!CAUTION]
> Este modo de recuperación no llama al constructor.

```php
<?php
class TestEntity implements Serializable
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;

    public function __construct()
    {
        print "Constructor llamado con " . count(func_get_args()) . " argumentos\n";
        print "¿Propiedades establecidas cuando se llama al constructor? "
            . (isset($this->name) ? 'Sí' : 'No') . "\n";
    }

    public function serialize()
    {
        return join(
            "|",
            [$this->userid, $this->name, $this->country, $this->referred_by_userid]
        );
    }

    public function unserialize(string $data)
    {
        $parts = explode("|", $data);
        $this->userid = (int) $parts[0];
        $this->name = $parts[1];
        $this->country = $parts[2];

        $refId = $parts[3];
        $this->referred_by_userid = ($refId === "" ? null : (int) $refId);
    }
}

print "Establecer registro (constructor llamado manualmente):\n";
$db->exec(
    "CREATE TABLE serialize (
        sdata TEXT
    )"
);

$origObj = new TestEntity();
$origObj->userid = 200;
$origObj->name = 'Seri';
$origObj->country = 'Syria';
$origObj->referred_by_userid = null;

$insert = $db->prepare("INSERT INTO serialize (sdata) VALUES (:sdata)");
$insert->execute(['sdata' => $origObj->serialize()]);

print "\nObtener resultados:\n";
$query = "SELECT sdata FROM serialize";
$stmt = $db->query($query);
// NOTA: El constructor nunca se llama!
$stmt->setFetchMode(PDO::FETCH_CLASS | PDO::FETCH_SERIALIZE, TestEntity::class);
$result = $stmt->fetch();
var_dump($result);

   
```

Resultado del ejemplo anterior es similar a:

    Deprecated: TestEntity implements the Serializable interface, which is deprecated. Implement __serialize() and __unserialize() instead (or in addition, if support for old PHP versions is necessary) in Standard input code on line 2
    Establecer registro (constructor llamado manualmente):
    Constructor llamado con 0 argumentos
    ¿Propiedades establecidas cuando se llama al constructor? No

    Obtener resultados:
    Deprecated: PDOStatement::setFetchMode(): The PDO::FETCH_SERIALIZE mode is deprecated in Standard input code on line 58

    Deprecated: PDOStatement::fetch(): The PDO::FETCH_SERIALIZE mode is deprecated in Standard input code on line 59
    object(TestEntity)#5 (4) {
      ["userid"]=>
      int(200)
      ["name"]=>
      string(4) "Seri"
      ["country"]=>
      string(5) "Syria"
      ["referred_by_userid"]=>
      NULL
    }

## PDO::FETCH_BOUND (`int`)

Este modo de recuperación no se puede utilizar con PDOStatement::fetchAll.

Este modo de recuperación no devuelve directamente un resultado, sino que asigna valores a las variables especificadas con PDOStatement::bindColumn. El método de recuperación llamado devuelve `true`.

> [!NOTE]
> Cuando se utilizan sentencias preparadas, para que funcionen correctamente, las variables deben enlazarse después de que se ejecute la consulta.

```php
<?php
$query = "SELECT users.userid, users.name, users.country, referrer.name
    FROM users
    LEFT JOIN users AS referrer ON users.referred_by_userid = referrer.userid";
$stmt = $db->prepare($query);
$stmt->execute();

$stmt->bindColumn('userid', $userId);
$stmt->bindColumn('name', $name);
$stmt->bindColumn('country', $country);
// Se utiliza la posición de la columna para resolver nombres de columna duplicados.
// Para evitar que esto falle si se modifica la consulta, se recomienda usar un alias SQL.
// Por ejemplo: referrer.name AS referrer_name
$stmt->bindColumn(4, $referrerName);

while ($stmt->fetch(\PDO::FETCH_BOUND)) {
    print join("\t", [$userId, $name, $country, ($referrerName ?? 'NULL')]) . "\n";
}

  
```

El ejemplo anterior mostrará:

    104 Chris   Ukraine NULL
    105 Jamie   England NULL
    107 Robin   Germany Chris
    108 Sean    Ukraine NULL
    109 Toni    Germany NULL
    110 Toni    Germany NULL

      

## PDO::FETCH_INTO (`int`)

Este modo de recuperación no se puede utilizar con PDOStatement::fetchAll.

Este modo de recuperación actualiza las propiedades del objeto especificado. El objeto se devuelve si la operación se realiza correctamente.

Si una propiedad no existe con el nombre de una columna devuelta, se declarará dinámicamente. Este comportamiento está obsoleto y provocará un error a partir de PHP 9.0.

Las propiedades deben ser `public` y no pueden ser `readonly`.

> [!CAUTION]
> No hay forma de cambiar el objeto que se va a actualizar sin usar PDOStatement::setFetchMode entre la recuperación de cada registro.

```php
<?php

class TestEntity
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;
}

$obj = new TestEntity();

$stmt = $db->query("SELECT userid, name, country, referred_by_userid FROM users");

$stmt->setFetchMode(\PDO::FETCH_INTO, $obj);
$result = $stmt->fetch();

var_dump($result);

   
```

Resultado del ejemplo anterior es similar a:

    object(TestEntity)#3 (4) {
      ["userid"]=>
      int(104)
      ["name"]=>
      string(5) "Chris"
      ["country"]=>
      string(7) "Ukraine"
      ["referred_by_userid"]=>
      NULL
    }

## PDO::FETCH_LAZY (`int`)

Este modo de recuperación no se puede utilizar con PDOStatement::fetchAll.

Este modo de obtención recuperación un objeto `PDORow` que proporciona acceso a los valores tanto como arrays como objetos (es decir, combina el comportamiento de `PDO::FETCH_BOTH` y `PDO::FETCH_OBJ`), recuperados de forma diferida.

Esto permite un acceso eficiente en memoria (en el lado de PHP) a los resultados sin almacenar en búfer en el servidor de la base de datos. El uso o no de almacenamiento en búfer del lado del cliente por parte de PDO depende del controlador específico de la base de datos que se utilice (y de su configuración).

> [!CAUTION]
> `PDORow` devolverá `null` sin mostrar ningún error ni advertencia al acceder a propiedades o claves no definidas. Esto puede dificultar la detección y depuración de errores como erratas o consultas que no devuelven los datos esperados.

> [!CAUTION]
> El objeto `PDORow` devuelto se actualiza cada vez que se recupera un resultado.

```php
<?php
$stmt = $db->query("SELECT userid, name, country, referred_by_userid FROM users");
$result = $stmt->fetch(\PDO::FETCH_LAZY);

print "ID: ". $result[0] ."\n";
print "Nombre: {$result->name}\n";
print "País: " . $result['country'] ."\n";
// Devuelve NULL. No se genera ninguna advertencia ni error.
print "No existe: " . var_export($result->does_not_exist, true) . "\n";

$differentResult = $stmt->fetch(\PDO::FETCH_LAZY);
// El PDOrow recuperado previamente ahora apunta al resultado recién recuperado.
print "ID: ". $result[0] ."\n";

  
```

El ejemplo anterior mostrará:

    ID: 104
    Nombre: Chris
    País: Ukraine
    No existe: NULL
    ID: 105

      

## PDO::FETCH_GROUP (`int`)

`PDO::FETCH_GROUP` devuelve listas de arrays asociativos, indexados por una columna (no única). Este modo de obtención solo funciona con PDOStatement::fetchAll.

Cuando se combina con `PDO::FETCH_UNIQUE`, ambos modos utilizarán la misma columna, lo que hace que la combinación de estos modos sea inútil.

Esta recuperación debe combinarse con una de `PDO::FETCH_ASSOC`, `PDO::FETCH_BOTH`, `PDO::FETCH_NAMED`, `PDO::FETCH_NUM`, `PDO::FETCH_COLUMN` o `PDO::FETCH_FUNC`.

Si no se proporciona ningún modo de recuperación de la lista anterior, se utilizará el modo de recuperación predeterminado actual para `PDOStatement`.

```php
<?php
$stmt = $pdo->query("SELECT country, userid, name FROM users");
$row = $stmt->fetchAll(\PDO::FETCH_GROUP | \PDO::FETCH_ASSOC);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [Ukraine] => Array
            (
                [0] => Array
                    (
                        [userid] => 104
                        [name] => Chris
                    )

                [1] => Array
                    (
                        [userid] => 108
                        [name] => Sean
                    )

            )
        [England] => Array
            (
                [0] => Array
                    (
                        [userid] => 105
                        [name] => Jamie
                    )

            )

        [Germany] => Array
            (
                [0] => Array
                    (
                        [userid] => 107
                        [name] => Robin
                    )

                [1] => Array
                    (
                        [userid] => 109
                        [name] => Toni
                    )
            )
    )

En el ejemplo anterior, cabe señalar que la primera columna se omite del array en cada fila y solo está disponible como clave. Se puede incluir repitiendo la columna, como en el siguiente ejemplo:

```php
<?php
$stmt = $pdo->query("SELECT country, userid, name, country FROM users");
$row = $stmt->fetchAll(\PDO::FETCH_GROUP | \PDO::FETCH_ASSOC);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [Ukraine] => Array
            (
                [0] => Array
                    (
                        [userid] => 104
                        [name] => Chris
                        [country] => Ukraine
                    )

                [1] => Array
                    (
                        [userid] => 108
                        [name] => Sean
                        [country] => Ukraine
                    )

            )
        [England] => Array
            (
                [0] => Array
                    (
                        [userid] => 105
                        [name] => Jamie
                        [country] => England
                    )

            )

        [Germany] => Array
            (
                [0] => Array
                    (
                        [userid] => 107
                        [name] => Robin
                        [country] => Germany
                    )

                [1] => Array
                    (
                        [userid] => 109
                        [name] => Toni
                        [country] => Germany
                    )
            )
    )

## PDO::FETCH_UNIQUE (`int`)

`PDO::FETCH_UNIQUE` utiliza la primera columna para indexar los registros, devolviendo un registro por cada valor de índice. Este modo de recuperación solo funciona con PDOStatement::fetchAll.

Cuando se combina con `PDO::FETCH_GROUP`, ambos modos utilizarán la misma columna, lo que hace que la combinación de estos modos sea inútil.

Esta recuperación debe combinarse con uno de `PDO::FETCH_ASSOC`, `PDO::FETCH_BOTH`, `PDO::FETCH_NAMED`, `PDO::FETCH_NUM`, `PDO::FETCH_COLUMN` o `PDO::FETCH_FUNC`.

Si no se proporciona ningún modo de recuperación de la lista anterior, se utilizará el modo de recuperación predeterminado actual para `PDOStatement`.

Cuando se utiliza con una columna que se sabe que es única (como el ID del registro), este modo proporciona la capacidad de devolver rápidamente resultados indexados por ese valor.

> [!NOTE]
> Si la primera columna no es única, se perderán valores. Qué valor(es) se perderán se considera indefinido.

> [!CAUTION]
> Siempre que sea posible, se recomienda filtrar los registros mediante SQL. La base de datos utilizará índices para optimizar este proceso y devolver únicamente los registros necesarios. Seleccionar más registros de los necesarios puede aumentar significativamente el uso de memoria y el tiempo de consulta para conjuntos de resultados grandes.

```php
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_UNIQUE | \PDO::FETCH_ASSOC);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [104] => Array
            (
                [name] => Chris
                [country] => Ukraine
            )

        [105] => Array
            (
                [name] => Jamie
                [country] => England
            )

        [107] => Array
            (
                [name] => Robin
                [country] => Germany
            )

    )

En el ejemplo anterior, cabe señalar que la primera columna se omite del array en cada fila y solo está disponible como clave. Se puede incluir repitiendo la columna, como en el siguiente ejemplo:

```php
<?php
$stmt = $pdo->query("SELECT userid, userid, name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_UNIQUE | \PDO::FETCH_ASSOC);
print_r($row);

   
```

El ejemplo anterior mostrará:

    Array
    (
        [104] => Array
            (
                [userid] => 104
                [name] => Chris
                [country] => Ukraine
            )

        [105] => Array
            (
                [userid] => 105
                [name] => Jamie
                [country] => England
            )

        [107] => Array
            (
                [userid] => 107
                [name] => Robin
                [country] => Germany
            )

    )
