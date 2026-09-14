---
title: XSLTProcessor::registerPHPFunctions
description: Activa el uso de PHP en las hojas de estilo XSLT
source_url: https://www.php.net/manual/es/xsltprocessor.registerphpfunctions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/registerphpfunctions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 01904e809
order: 104160
---

XSLTProcessor::registerPHPFunctions

Activa el uso de PHP en las hojas de estilo XSLT

## Descripción

```php
public XSLTProcessor::registerPHPFunctions([array $functions]): void
```php

Este método permite utilizar las funciones PHP como funciones XSLT en las hojas de estilo XSL.

## Parámetros

`functions`  
Utilice este parámetro para restringir las funciones PHP accesibles desde XSLT.

Este parámetro puede ser uno de los siguientes: un `string` (nombre de una función), un `array` indexado que contiene nombres de funciones, o un `array` asociativo donde las claves representan el nombre de la función y el valor asociado es un `callable`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora es posible utilizar `callable` como callbacks cuando se utiliza `functions` con entradas de tipo `array`. |

## Ejemplos

Sencilla llamada a una función PHP desde una hoja de estilo

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
     xmlns:php="http://php.net/xsl">
<xsl:output method="html" encoding="utf-8" indent="yes"/>
 <xsl:template match="allusers">
  <html><body>
    <h2>Users</h2>
    <table>
    <xsl:for-each select="user">
      <tr><td>
        <xsl:value-of
             select="php:function('ucfirst',string(uid))"/>
      </td></tr>
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
$proc->registerPHPFunctions();
$proc->importStyleSheet($xsldoc);
echo $proc->transformToXML($xmldoc);
?>

    
```php

## Véase también

DOMXPath::registerPhpFunctions
