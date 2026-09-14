---
title: Ejemplos
source_url: https://www.php.net/manual/es/xmlwriter.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: false
translation_revision: 2e8ef0a1b
order: 103530
---

## Ejemplos

## Crear un simple documento XML

Este ejemplo muestra cómo utilizar XMLWriter para crear un documento XML en memoria.

Crear un simple documento XML

```php
<?php

$xw = xmlwriter_open_memory();
xmlwriter_set_indent($xw, 1);
$res = xmlwriter_set_indent_string($xw, ' ');

xmlwriter_start_document($xw, '1.0', 'UTF-8');

// A first element
xmlwriter_start_element($xw, 'tag1');

// Attribute 'att1' for element 'tag1'
xmlwriter_start_attribute($xw, 'att1');
xmlwriter_text($xw, 'valueofatt1');
xmlwriter_end_attribute($xw);

xmlwriter_write_comment($xw, 'this is a comment.');

// Start a child element
xmlwriter_start_element($xw, 'tag11');
xmlwriter_text($xw, 'This is a sample text, ä');
xmlwriter_end_element($xw); // tag11

xmlwriter_end_element($xw); // tag1

// CDATA
xmlwriter_start_element($xw, 'testc');
xmlwriter_write_cdata($xw, "This is cdata content");
xmlwriter_end_element($xw); // testc

xmlwriter_start_element($xw, 'testc');
xmlwriter_start_cdata($xw);
xmlwriter_text($xw, "test cdata2");
xmlwriter_end_cdata($xw);
xmlwriter_end_element($xw); // testc

// A processing instruction
xmlwriter_start_pi($xw, 'php');
xmlwriter_text($xw, '$foo=2;echo $foo;');
xmlwriter_end_pi($xw);

xmlwriter_end_document($xw);

echo xmlwriter_output_memory($xw);

    
```

El ejemplo anterior mostrará:

    <tag1 att1="valueofatt1">
     <!--this is a comment.-->
     <tag11>This is a sample text, ä</tag11>
    </tag1>
    <testc><![CDATA[This is cdata content]]></testc>
    <testc><![CDATA[test cdata2]]></testc>
    <?php $foo=2;echo $foo;?>

## Trabajar con espacios de nombres XML

Este ejemplo muestra cómo crear elementos XML con espacio de nombres.

Trabajar con espacios de nombres XML

```php
<?php

$xw = xmlwriter_open_memory();
xmlwriter_set_indent($xw, 1);
$res = xmlwriter_set_indent_string($xw, ' ');

xmlwriter_start_document($xw, '1.0', 'UTF-8');
// A first element
xmlwriter_start_element_ns($xw,'prefix', 'books', 'uri');
xmlwriter_start_attribute($xw, 'isbn');

xmlwriter_start_attribute_ns($xw, 'prefix', 'isbn', 'uri');
xmlwriter_end_attribute($xw);

xmlwriter_end_attribute($xw);

xmlwriter_text($xw, 'book1');
xmlwriter_end_element($xw);

xmlwriter_end_document($xw);

echo xmlwriter_output_memory($xw);

    
```

El ejemplo anterior mostrará:

    <prefix:books isbn="" prefix:isbn="" xmlns:prefix="uri">book1</prefix:books>

## Trabajando con el OO API

Este ejemplo muestra cómo trabajar con la API orientada a objetos de XMLWriter.

Trabajando con el OO API

```php
<?php

$xw = new XMLWriter();
$xw->openMemory();
$xw->startDocument("1.0");
$xw->startElement("book");
$xw->text("example");
$xw->endElement();
$xw->endDocument();
echo $xw->outputMemory();

    
```

El ejemplo anterior mostrará:

    <book>example</book>
