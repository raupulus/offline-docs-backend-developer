---
title: Ejemplos
source_url: https://www.php.net/manual/es/xml.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: b47e4bea1
order: 102660
---

## Ejemplos

## Ejemplo de estructura XML

Este primer ejemplo muestra la estructura del elemento de inicio en un documento con indentación.

Mostrar una estructura XML

```php
<?php
$file = "examples/book.xml";
$depth = 0;

function startElement($parser, $name, $attrs)
{
    global $depth;

    global $depth;

    for ($i = 0; $i < $depth; $i++) {
        echo "  ";
    }
    echo "$name\n";
    $depth++;
}

function endElement($parser, $name)
{
    global $depth;
    $depth--;
}

$xml_parser = xml_parser_create();
xml_set_element_handler($xml_parser, "startElement", "endElement");
if (!($fp = fopen($file, "r"))) {
    die("could not open XML input");
}

while ($data = fread($fp, 4096)) {
    if (!xml_parse($xml_parser, $data, feof($fp))) {
        die(sprintf("Error XML: %s en la línea %d",
                    xml_error_string(xml_get_error_code($xml_parser)),
                    xml_get_current_line_number($xml_parser)));
    }
}
?>

    
```

## Conversión XML -\> HTML

Conversión XML -\> HTML

Este ejemplo reemplaza las etiquetas XML de un documento por etiquetas HTML. Los elementos desconocidos serán ignorados. Por supuesto, este ejemplo se aplicará a un tipo específico de archivos XML.

```php
<?php
$file = "examples/book.xml";
$map_array = array(
    "BOLD"     => "B",
    "EMPHASIS" => "I",
    "LITERAL"  => "TT"
);

function startElement($parser, $name, $attrs)
{
    global $map_array;
    if (isset($map_array[$name])) {
        echo "<$map_array[$name]>";
    }
}

function endElement($parser, $name)
{
    global $map_array;
    if (isset($map_array[$name])) {
        echo "</$map_array[$name]>";
    }
}

function characterData($parser, $data)
{
    echo $data;
}

$xml_parser = xml_parser_create();
// Utilizamos el manejo de mayúsculas y minúsculas, para asegurarnos de encontrar la etiqueta en $map_array
xml_parser_set_option($xml_parser, XML_OPTION_CASE_FOLDING, true);
xml_set_element_handler($xml_parser, "startElement", "endElement");
xml_set_character_data_handler($xml_parser, "characterData");
if (!($fp = fopen($file, "r"))) {
    die("could not open XML input");
}

while ($data = fread($fp, 4096)) {
    if (!xml_parse($xml_parser, $data, feof($fp))) {
        die(sprintf("Error XML: %s en la línea %d",
                    xml_error_string(xml_get_error_code($xml_parser)),
                    xml_get_current_line_number($xml_parser)));
    }
}
?>

    
```

## Entidad externa

Este ejemplo utiliza las referencias externas de XML: es posible usar un manejador de entidad externa para incluir y analizar documentos, así como las instrucciones ejecutables pueden servir para incluir y analizar otros documentos, y también proporcionar una indicación de confianza (ver más abajo).

El documento XML que se utiliza en este ejemplo se proporciona más adelante en el ejemplo (`xmltest.xml` y `xmltest2.xml`).

Entidad externa

```php
<?php
$file = "xmltest.xml";

function trustedFile($file)
{
    // solo confíe en archivos locales de los que sea propietario
    if (!preg_match("@^([a-z][a-z0-9+.-]*)\:\/\/@i", $file)
        && fileowner($file) == getmyuid()) {
            return true;
    }
    return false;
}

function startElement($parser, $name, $attribs)
{
    echo "&lt;<font color=\"#0000cc\">$name</font>";
    if (count($attribs)) {
        foreach ($attribs as $k => $v) {
            echo " <font color=\"#009900\">$k</font>=\"<font
                   color=\"#990000\">$v</font>\"";
        }
    }
    echo "&gt;";
}

function endElement($parser, $name)
{
    echo "&lt;/<font color=\"#0000cc\">$name</font>&gt;";
}

function characterData($parser, $data)
{
    echo "<b>$data</b>";
}

function PIHandler($parser, $target, $data)
{
    switch (strtolower($target)) {
        case "php":
            global $parser_file;
            // si el documento analizado es de confianza, se declara que es seguro
            // ejecutar el código PHP que contiene. Si no es así, el código se muestra
            // en su lugar.
            if (trustedFile($parser_file[$parser])) {
                eval($data);
            } else {
                printf("Código PHP no confiable: <i>%s</i>",
                        htmlspecialchars($data));
            }
            break;
    }
}

function defaultHandler($parser, $data)
{
    if (substr($data, 0, 1) == "&" && substr($data, -1, 1) == ";") {
        printf('<font color="#aa00aa">%s</font>',
                htmlspecialchars($data));
    } else {
        printf('<font size="-1">%s</font>',
                htmlspecialchars($data));
    }
}

function externalEntityRefHandler($parser, $openEntityNames, $base, $systemId,
                                  $publicId) {
    if ($systemId) {
        if (!list($parser, $fp) = new_xml_parser($systemId)) {
            printf("No se pudo abrir la entidad %s en %s\n", $openEntityNames,
                   $systemId);
            return false;
        }
        while ($data = fread($fp, 4096)) {
            if (!xml_parse($parser, $data, feof($fp))) {
                printf("Error XML: %s en la línea %d mientras se analiza la entidad %s\n",
                       xml_error_string(xml_get_error_code($parser)),
                       xml_get_current_line_number($parser), $openEntityNames);
                return false;
            }
        }
        return true;
    }
    return false;
}

function new_xml_parser($file)
{
    global $parser_file;

    $xml_parser = xml_parser_create();
    xml_parser_set_option($xml_parser, XML_OPTION_CASE_FOLDING, 1);
    xml_set_element_handler($xml_parser, "startElement", "endElement");
    xml_set_character_data_handler($xml_parser, "characterData");
    xml_set_processing_instruction_handler($xml_parser, "PIHandler");
    xml_set_default_handler($xml_parser, "defaultHandler");
    xml_set_external_entity_ref_handler($xml_parser, "externalEntityRefHandler");

    if (!($fp = @fopen($file, "r"))) {
        return false;
    }
    if (!is_array($parser_file)) {
        settype($parser_file, "array");
    }
    $parser_file[$xml_parser] = $file;
    return array($xml_parser, $fp);
}

if (!(list($xml_parser, $fp) = new_xml_parser($file))) {
    die("could not open XML input");
}

echo "<pre>";
while ($data = fread($fp, 4096)) {
    if (!xml_parse($xml_parser, $data, feof($fp))) {
        die(sprintf("Error XML: %s en la línea %d\n",
                    xml_error_string(xml_get_error_code($xml_parser)),
                    xml_get_current_line_number($xml_parser)));
    }
}
echo "</pre>";
echo "análisis completo\n";

?>

    
```

xmltest.xml

```php
<!DOCTYPE chapter SYSTEM "/just/a/test.dtd" [
<!ENTITY plainEntity "FOO entity">
<!ENTITY systemEntity SYSTEM "xmltest2.xml">
]>
<chapter>
 <TITLE>Title &plainEntity;</TITLE>
 <para>
  <informaltable>
   <tgroup cols="3">
    <tbody>
     <row><entry>a1</entry><entry morerows="1">b1</entry><entry>c1</entry></row>
     <row><entry>a2</entry><entry>c2</entry></row>
     <row><entry>a3</entry><entry>b3</entry><entry>c3</entry></row>
    </tbody>
   </tgroup>
  </informaltable>
 </para>
 &systemEntity;
 <section id="about">
  <title>About this Document</title>
  <para>
   <!-- this is a comment -->
   <?php echo 'Hi!  This is PHP version ' . phpversion(); ?>
  </para>
 </section>
</chapter>

    
```

Este archivo se incluye desde `xmltest.xml`:

xmltest2.xml

```php
<!DOCTYPE foo [
<!ENTITY testEnt "test entity">
]>
<foo>
   <element attrib="value"/>
   &testEnt;
   <?php echo "Esto es código PHP que se ejecuta."; ?>
</foo>

    
```

## Análisis XML con una clase

Este ejemplo muestra cómo utilizar una clase con manejadores.

Mostrar la estructura de los elementos XML

```php
<?php
$file = "examples/book.xml";

class CustomXMLParser
{
    private $fp;
    private $parser;
    private $depth = 0;

    function __construct(string $file)
    {
        if (!($this->fp = fopen($file, 'r'))) {
            throw new RunTimeException("imposible abrir el archivo XML '{$file}'");
        }

        $this->parser = xml_parser_create();

        xml_set_element_handler($this->parser, self::startElement(...), self::endElement(...));
        xml_set_character_data_handler($this->parser, self::cdata(...));
    }

    private function startElement($parser, $name, $attrs)
    {
        for ($i = 0; $i < $this->depth; $i++) {
            echo "  ";
        }
        echo "$name\n";
        $this->depth++;
    }

    private function endElement($parser, $name)
    {
        $this->depth--;
    }

    private function cdata($parser, $cdata)
    {
        if (trim($cdata) === '') {
            return;
        }
        for ($i = 0; $i < $this->depth; $i++) {
            echo "  ";
        }
        echo trim($cdata), "\n";
    }

    public function parse()
    {
        while ($data = fread($this->fp, 4096)) {
            if (!xml_parse($this->parser, $data, feof($this->fp))) {
                throw new RunTimeException(
                    sprintf(
                        "Error XML: %s en la línea %d",
                        xml_error_string(xml_get_error_code($this->parser)),
                        xml_get_current_line_number($this->parser)
                    )
                );
            }
        }
    }
}

$xmlParser = new CustomXMLParser($file);
$xmlParser->parse();
?>

    
```
