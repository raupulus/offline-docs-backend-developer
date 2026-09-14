---
title: XMLWriter::setIndent
description: Activa o no la indentación
source_url: https://www.php.net/manual/es/xmlwriter.setindent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/setindent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 78a71e92e
order: 103700
---

XMLWriter::setIndent

xmlwriter_set_indent

Activa o no la indentación

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::setIndent(bool $enable): bool
```php

Estilo procedimental

```php
xmlwriter_set_indent(XMLWriter $writer, bool $enable): bool
```

Activa o no la indentación.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`enable`  
Si se debe activar la indentación o no.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |

## Ejemplos

XMLWriter::setIndent y diversos contenidos

La activación de la indentación no es recomendada para contenido diverso, ya que el carácter de indentación también se insertará antes de los elementos en línea.

```php
<?php
$writer = new XMLWriter();
$writer->openMemory();
$writer->setIndent(true);
$writer->startDocument();
$writer->startElement('p');
$writer->text('before');
$writer->writeElement('a', 'element');
$writer->text('after');
$writer->endElement();
$writer->endDocument();
echo $writer->outputMemory();
?>

   
```

El ejemplo anterior mostrará:

    <p>before <a>element</a>
    after</p>

## Notas

> [!NOTE]
> La indentación se reinicia cuando se abre un XMLWriter.

## Véase también

XMLWriter::setIndentString
