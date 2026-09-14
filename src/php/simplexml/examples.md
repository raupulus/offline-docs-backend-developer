---
title: Ejemplos
source_url: https://www.php.net/manual/es/simplexml.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_revision: bdc3ab31f
order: 74380
---

## Ejemplos

## Uso básico de SimpleXML

Varios ejemplos de este capítulo requieren una cadena XML. En lugar de repetirla en cada ejemplo, se colocará en un archivo que se incluirá en cada uno de ellos. El contenido de este archivo se ilustra con el ejemplo que sigue. De lo contrario, puede crearse un documento XML y leerse con `simplexml_load_file`.

Ejemplo de archivo incluido examples/simplexml-data.php con una cadena XML

```php
<?php
$xmlstr = <<<XML

<movies>
 <movie>
  <title>PHP: Behind the Parser</title>
  <characters>
   <character>
    <name>Ms. Coder</name>
    <actor>Onlivia Actora</actor>
   </character>
   <character>
    <name>Mr. Coder</name>
    <actor>El Act&#211;r</actor>
   </character>
  </characters>
  <plot>
   So, this language. It's like, a programming language. Or is it a
   scripting language? All is revealed in this thrilling horror spoof
   of a documentary.
  </plot>
  <great-lines>
   <line>PHP solves all my web problems</line>
  </great-lines>
  <rating type="thumbs">7</rating>
  <rating type="stars">5</rating>
 </movie>
</movies>
XML;
?>

    
```

La simplicidad de SimpleXML se hace más evidente cuando se intenta extraer una cadena o un número de un documento XML básico.

Lectura de `<plot>`

```php
<?php
include 'examples/simplexml-data.php';

$movies = new SimpleXMLElement($xmlstr);

echo $movies->movie[0]->plot;
?>

    
```

El ejemplo anterior mostrará:

       So, this language. It's like, a programming language. Or is it a
       scripting language? All is revealed in this thrilling horror spoof
       of a documentary.

El acceso a los elementos de un documento XML que contiene caracteres no permitidos según la convención de nombres de PHP (por ejemplo, palabras clave) es posible encapsulando el nombre del elemento entre corchetes y comillas simples.

Recuperación de `<line>`

```php
<?php
include 'examples/simplexml-data.php';

$movies = new SimpleXMLElement($xmlstr);

echo $movies->movie->{'great-lines'}->line;
?>

    
```

El ejemplo anterior mostrará:

    PHP solves all my web problems

Acceder a un elemento no único con SimpleXML

Cuando existen múltiples instancias de un elemento como hijos de un elemento padre único, pueden aplicarse las técnicas normales de iteración.

```php
<?php
include 'examples/simplexml-data.php';

$movies = new SimpleXMLElement($xmlstr);

/* Para cada <character>, se muestra un <name>. */
foreach ($movies->movie->characters->character as $character) {
   echo $character->name, ' played by ', $character->actor, PHP_EOL;
}

?>

    
```

El ejemplo anterior mostrará:

    Ms. Coder played by Onlivia Actora
    Mr. Coder played by El ActÓr

> [!NOTE]
> Las propiedades (`$movies->movie` en nuestro ejemplo anterior) no son arrays. Son objetos [iterables](#class.iterator) y [accesibles](#class.arrayaccess).

Uso de atributos

Hasta ahora, solo se ha cubierto la lectura de los nombres de los elementos y sus valores. SimpleXML también puede acceder a sus atributos. El acceso a los atributos de un elemento se realiza de la misma manera que el acceso a los elementos de un array.

```php
<?php
include 'examples/simplexml-data.php';

$movies = new SimpleXMLElement($xmlstr);

/* Acceso al nodo <rating> del primer <movie>.
 * Mostrar también los atributos de <rating>. */
foreach ($movies->movie[0]->rating as $rating) {
    switch((string) $rating['type']) { // Obtener atributos como índices de elementos
    case 'thumbs':
        echo $rating, ' thumbs up';
        break;
    case 'stars':
        echo $rating, ' stars';
        break;
    }
}
?>

    
```

El ejemplo anterior mostrará:

    7 thumbs up5 stars

Comparación de elementos y atributos con texto

Para comparar un elemento o un atributo con una cadena de caracteres o para pasarlo a una función que requiera una cadena de caracteres, debe convertirse en una cadena utilizando `(string)`. De lo contrario, PHP tratará el elemento como un objeto.

```php
<?php
include 'examples/simplexml-data.php';

$movies = new SimpleXMLElement($xmlstr);

if ((string) $movies->movie->title == 'PHP: Behind the Parser') {
    print 'My favorite movie.';
}

echo htmlentities((string) $movies->movie->title);
?>

    
```

El ejemplo anterior mostrará:

    My favorite movie.PHP: Behind the Parser

Comparación de 2 elementos

Dos objetos `SimpleXMLElement` se consideran diferentes incluso si apuntan al mismo elemento.

```php
<?php
include 'examples/simplexml-data.php';

$movies1 = new SimpleXMLElement($xmlstr);
$movies2 = new SimpleXMLElement($xmlstr);
var_dump($movies1 == $movies2);
?>

    
```

El ejemplo anterior mostrará:

    bool(false)

Uso de XPath

SimpleXML incluye soporte integrado para XPath. Para encontrar todos los elementos `<character>`.

'`//`' actúa como comodín. Para especificar una ruta absoluta, se elimina una barra.

```php
<?php
include 'examples/simplexml-data.php';

$movies = new SimpleXMLElement($xmlstr);

foreach ($movies->xpath('//character') as $character) {
    echo $character->name, ' played by ', $character->actor, PHP_EOL;
}
?>

    
```

El ejemplo anterior mostrará:

    Ms. Coder played by Onlivia Actora
    Mr. Coder played by El ActÓr

Asignación de valores

Los datos en SimpleXML no tienen que ser constantes. El objeto permite la manipulación de todos estos elementos.

```php
<?php
include 'examples/simplexml-data.php';
$movies = new SimpleXMLElement($xmlstr);

$movies->movie[0]->characters->character[0]->name = 'Miss Coder';

echo $movies->asXML();
?>

    
```

El ejemplo anterior mostrará:

    <movies>
     <movie>
      <title>PHP: Behind the Parser</title>
      <characters>
       <character>
        <name>Miss Coder</name>
        <actor>Onlivia Actora</actor>
       </character>
       <character>
        <name>Mr. Coder</name>
        <actor>El Act&#xD3;r</actor>
       </character>
      </characters>
      <plot>
       So, this language. It's like, a programming language. Or is it a
       scripting language? All is revealed in this thrilling horror spoof
       of a documentary.
      </plot>
      <great-lines>
       <line>PHP solves all my web problems</line>
      </great-lines>
      <rating type="thumbs">7</rating>
      <rating type="stars">5</rating>
     </movie>
    </movies>

Añadir elementos y atributos

SimpleXML es capaz de añadir fácilmente hijos y atributos.

```php
<?php
include 'examples/simplexml-data.php';
$movies = new SimpleXMLElement($xmlstr);

$character = $movies->movie[0]->characters->addChild('character');
$character->addChild('name', 'Mr. Parser');
$character->addChild('actor', 'John Doe');

$rating = $movies->movie[0]->addChild('rating', 'PG');
$rating->addAttribute('type', 'mpaa');

echo $movies->asXML();
?>

    
```

El ejemplo anterior mostrará:

    <movies>
     <movie>
      <title>PHP: Behind the Parser</title>
      <characters>
       <character>
        <name>Ms. Coder</name>
        <actor>Onlivia Actora</actor>
       </character>
       <character>
        <name>Mr. Coder</name>
        <actor>El Act&#xD3;r</actor>
       </character>
      <character><name>Mr. Parser</name><actor>John Doe</actor></character></characters>
      <plot>
       So, this language. It's like, a programming language. Or is it a
       scripting language? All is revealed in this thrilling horror spoof
       of a documentary.
      </plot>
      <great-lines>
       <line>PHP solves all my web problems</line>
      </great-lines>
      <rating type="thumbs">7</rating>
      <rating type="stars">5</rating>
     <rating type="mpaa">PG</rating></movie>
    </movies>

Interoperabilidad DOM

PHP tiene un mecanismo para convertir nodos XML entre los formatos SimpleXML y DOM. Este ejemplo muestra cómo cambiar un elemento DOM a SimpleXML.

```php
<?php
$dom = new DOMDocument;
$dom->loadXML('<books><book><title>blah</title></book></books>');
if (!$dom) {
    echo 'Error al analizar el documento';
    exit;
}

$books = simplexml_import_dom($dom);

echo $books->book[0]->title;
?>

    
```

El ejemplo anterior mostrará:

    blah

Uso de espacios de nombres

```php
     
<?php
$data = <<<XML
<movies xmlns="http://default" xmlns:a="http://a">
 <movie xml:id="movie1" a:link="IMDB">
  <a:actor>Onlivia Actora</a:actor>
 </movie>
</movies>
XML;

$movies = simplexml_load_string($data);

// El espacio de nombres http://www.w3.org/XML/1998/namespace está disponible bajo el nombre "xml".
echo $movies->movie->attributes("xml", true)["id"] . "\n";

// Los atributos con espacio de nombres pueden recuperarse con attributes().
echo $movies->movie->attributes("a", true)["link"] . "\n";

// El uso de la URI del espacio de nombres permite usar cualquier alias en el documento.
echo $movies->movie->attributes("http://a")["link"] . "\n";

// Los hijos pueden recuperarse con children().
echo $movies->movie->children("http://a")->actor . "\n";

// El uso de xpath() con un espacio de nombres requiere registrarlo primero.
$movies->registerXPathNamespace("a", "http://a");
echo count($movies->xpath("//a:actor")) . "\n";

// Incluso el espacio de nombres por defecto debe registrarse.
$movies->registerXPathNamespace("default", "http://default");
echo count($movies->xpath("//default:movie")) . "\n";

// Esto está vacío.
echo count($movies->xpath("//movie")) . "\n";
?>

        
```

## Manejo de errores XML

El manejo de errores XML al cargar un documento es una tarea sencilla. Utilizando las funcionalidades [libxml](#book.libxml), es posible suprimir todos los errores XML al cargar un documento, y luego recorrerlos.

El objeto `LibXMLError`, devuelto por la función `libxml_get_errors`, contiene varias propiedades como el [mensaje](#libxmlerror.props.message), la [línea](#libxmlerror.props.line) y la [columna](#libxmlerror.props.column) (posición) del error.

Carga de cadenas XML rotas

```php
<?php
libxml_use_internal_errors(true);
$sxe = simplexml_load_string("<?xml version='1.0'><broken><xml></broken>");
if ($sxe === false) {
    echo "Error al cargar el XML\n";
    foreach(libxml_get_errors() as $error) {
        echo "\t", $error->message;
    }
}
?>

    
```

El ejemplo anterior mostrará:

    Error al cargar el XML
        Blank needed here
        parsing XML declaration: '?>' expected
        Opening and ending tag mismatch: xml line 1 and broken
        Premature end of data in tag broken line 1

### Véase también

`libxml_use_internal_errors`, `libxml_get_errors`, [???](#class.libxmlerror)
