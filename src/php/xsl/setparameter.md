---
title: XSLTProcessor::setParameter
description: Define el valor de un parámetro
source_url: https://www.php.net/manual/es/xsltprocessor.setparameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/setparameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 68e72e60b
order: 104180
---

XSLTProcessor::setParameter

Define el valor de un parámetro

## Descripción

```php
public XSLTProcessor::setParameter(string $namespace, string $name, string $value): bool
```php

```php
public XSLTProcessor::setParameter(string $namespace, array $options): bool
```

Especifica el valor de uno o varios parámetros para ser utilizados en una subsecuencia de transformación con `XSLTProcessor`. Si el parámetro no existe en la hoja de estilo, será ignorado.

## Parámetros

`namespace`  
La URI del espacio de nombres del parámetro XSLT.

`name`  
El nombre local del parámetro XSLT.

`value`  
El nuevo valor del parámetro XSLT.

`options`  
Un array de pares `nombre => valor`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Genera una excepción de tipo ValueError si alguno de los argumentos contiene bytes nulos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora lanza una una excepción de tipo ValueError si alguno de los argumentos contiene bytes nulos, en lugar de truncar silenciosamente. |
| 8.4.0 | Ahora es posible definir un valor de parámetro que contenga tanto comillas simples como dobles. Antes de PHP 8.4.0, esto generaba una advertencia. |

## Ejemplos

Modificación del propietario antes de la transformación

```php
<?php

$collections = array(
    'Marc Rutkowski' => 'marc',
    'Olivier Parmentier' => 'olivier'
);

$xsl = new DOMDocument;
$xsl->load('collection.xsl');

// Configurar el transformador
$proc = new XSLTProcessor;
$proc->importStyleSheet($xsl); // adjuntar las reglas xsl

foreach ($collections as $name => $file) {
    // Cargar la fuente XML
    $xml = new DOMDocument;
    $xml->load('collection_' . $file . '.xml');

    $proc->setParameter('', 'owner', $name);
    $proc->transformToURI($xml, 'file:///tmp/' . $file . '.html');
}

?>

    
```

## Véase también

`XSLTProcessor::getParameter`, `XSLTProcessor::removeParameter`
