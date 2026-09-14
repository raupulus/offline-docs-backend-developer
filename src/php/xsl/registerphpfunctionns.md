---
title: XSLTProcessor::registerPHPFunctionNS
description: Registra una función PHP como una función XSLT en un espacio de nombres
source_url: https://www.php.net/manual/es/xsltprocessor.registerphpfunctionns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/registerphpfunctionns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_reviewed: true
translation_revision: 01904e809
order: 104150
---

XSLTProcessor::registerPHPFunctionNS

Registra una función PHP como una función XSLT en un espacio de nombres

## Descripción

```php
public XSLTProcessor::registerPHPFunctionNS(string $namespaceURI, string $name, callable $callable): void
```php

Este método permite usar una función PHP como una función XSLT en hojas de estilo XSL.

## Parámetros

`namespaceURI`  
El URI del espacio de nombres.

`name`  
La función local dentro del espacio de nombres.

`callable`  
La función PHP a llamar cuando se invoca la función XSL en la hoja de estilo. Cuando se pasa una lista de nodos como parámetro a la función de devolución de llamada, el argumento se convierte en un array que contiene los nodos DOM correspondientes.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Llamada simple a una función PHP desde una hoja de estilo

```
<?php
$xml = <<<EOB
<allusers>
<user>
 <uid>bob</uid>
</user>
<user>
 <uid>joe</uid>
</user>
</allusers>
EOB;
$xsl = <<<EOB

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:my="urn:my.ns">
<xsl:output method="html" encoding="utf-8" indent="yes"/>
<xsl:template match="allusers">
 <html><body>
   <h2><xsl:value-of select="my:count(user/uid)" /> users</h2>
   <table>
   <xsl:for-each select="user">
     <tr>
      <td>
       <xsl:value-of select="my:uppercase(string(uid))"/>
      </td>
     </tr>
   </xsl:for-each>
   </table>
 </body></html>
</xsl:template>
</xsl:stylesheet>
EOB;
$xmldoc = new DOMDocument();
$xmldoc->loadXML($xml);
$xsldoc = new DOMDocument();
$xsldoc->loadXML($xsl);

$proc = new XSLTProcessor();
$proc->registerPHPFunctionNS('urn:my.ns', 'uppercase', strtoupper(...));
$proc->registerPHPFunctionNS('urn:my.ns', 'count', fn (array $arg1) => count($arg1));
$proc->importStyleSheet($xsldoc);
echo $proc->transformToXML($xmldoc);
?>

   
```php

## Véase también

DOMXPath::registerPhpFunctionNS

DOMXPath::registerPhpFunctions

XSLTProcessor::registerPhpFunctions
