---
title: Ejemplos
source_url: https://www.php.net/manual/es/xsl.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 10b60deaa
order: 104080
---

## Ejemplos

## Ficheros collection.xml y collection.xsl de ejemplo

Muchos ejemplos en esta referencia requieren tanto un fichero XML como un XSL. Se usará `collection.xml` y `collection.xsl` que contienen el siguiente código:

collection.xml

```php
<collection>
 <cd>
  <title>Fight for your mind</title>
  <artist>Ben Harper</artist>
  <year>1995</year>
 </cd>
 <cd>
  <title>Electric Ladyland</title>
  <artist>Jimi Hendrix</artist>
  <year>1997</year>
 </cd>
</collection>

    
```

collection.xsl

```php
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:param name="owner" select="'Nicolas Eliaszewicz'"/>
 <xsl:output method="html" encoding="iso-8859-1" indent="no"/>
 <xsl:template match="collection">
  Hey! Welcome to <xsl:value-of select="$owner"/>'s sweet CD collection!
  <xsl:apply-templates/>
 </xsl:template>
 <xsl:template match="cd">
  <h1><xsl:value-of select="title"/></h1>
  <h2>by <xsl:value-of select="artist"/> - <xsl:value-of select="year"/></h2>
  <hr />
 </xsl:template>
</xsl:stylesheet>

    
```

## Manejo de errores con las funciones de manejo de errores de libxml

libxml ofrece una serie de funciones para el manejo de errores, que pueden ser empleadas para capturar y tratar los errores en el procesamiento de XSLT.

fruits.xml

Un archivo XML válido.

```php
<fruits>
 <fruit>Apple</fruit>
 <fruit>Banana</fruit>
 <fruit>Cherry</fruit>
</fruits>

    
```

fruits.xsl

Contiene una expresión selectiva no válida.

```php
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:output method="html" encoding="utf-8" indent="no"/>
 <xsl:template match="fruits">
  <ul>
   <xsl:apply-templates/>
  </ul>
 </xsl:template>
 <xsl:template match="fruit">
  <li><xsl:value-of select="THIS IS A DELIBERATE ERROR!"/></li>
 </xsl:template>
</xsl:stylesheet>

    
```

Errores de compaginación e impresión

El siguiente ejemplo captura y muestra los errores de libxml que se producen al llamar a XSLTProcessor::importStyleSheet con una hoja de estilo que contiene un error.

```php
<?php

$xmldoc = new DOMDocument();
$xsldoc = new DOMDocument();
$xsl = new XSLTProcessor();

$xmldoc->loadXML('fruits.xml');
$xsldoc->loadXML('fruits.xsl');

libxml_use_internal_errors(true);
$result = $xsl->importStyleSheet($xsldoc);
if (!$result) {
    foreach (libxml_get_errors() as $error) {
        echo "Libxml error: {$error->message}\n";
    }
}
libxml_use_internal_errors(false);

if ($result) {
    echo $xsl->transformToXML($xmldoc);
}

?>

    
```

Resultado del ejemplo anterior es similar a:

    Libxml error: Invalid expression

    Libxml error: compilation error: file fruits.xsl line 9 element value-of
    Libxml error: xsl:value-of : could not compile select expression 'THIS IS A DELIBERATE ERROR!'
