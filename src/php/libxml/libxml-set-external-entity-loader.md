---
title: libxml_set_external_entity_loader
description: Cambia el cargador de entidades externas por defecto
source_url: https://www.php.net/manual/es/function.libxml-set-external-entity-loader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/functions/libxml-set-external-entity-loader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_reviewed: false
translation_revision: 5b7646656
order: 43700
---

libxml_set_external_entity_loader

Cambia el cargador de entidades externas por defecto

## Descripción

```php
libxml_set_external_entity_loader(callable $resolver_function): true
```php

Cambia el cargador de entidades externas por defecto. Esto puede ser utilizado para reprimir la expansión de entidades externas arbitrarias para prevenir ataques XXE, incluso si `LIBXML_NOENT` ha sido definida para la operación respectiva, y esto es generalmente preferible a llamar a `libxml_disable_entity_loader`.

## Parámetros

`resolver_function`  
Un `callable` con la siguiente firma:

```php
resolver(string $public_id, string $system_id, array $context): resource
```

`public_id`  
El ID público.

`system_id`  
El ID del sistema.

`context`  
Un array que contiene cuatro elementos `"directory"`, `"intSubName"`, `"extSubURI"` y `"extSubSystem"`.

Esta callable debería devolver un `resource`, un `string` a través del cual puede abrirse un recurso. Si se devuelve `null`, la resolución de referencia de entidad fallará.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                    |
|---------|----------------------------------------------------------------|
| 8.5.0   | El tipo de retorno es ahora `true`; anteriormente, era `bool`. |

## Ejemplos

Ejemplo con `libxml_set_external_entity_loader`

```php
<?php
$xml = <<<XML
<!DOCTYPE foo PUBLIC "-//FOO/BAR" "http://example.com/foobar">
<foo>bar</foo>
XML;

$dtd = <<<DTD
<!ELEMENT foo (#PCDATA)>
DTD;

libxml_set_external_entity_loader(
    function ($public, $system, $context) use($dtd) {
        var_dump($public);
        var_dump($system);
        var_dump($context);
        $f = fopen("php://temp", "r+");
        fwrite($f, $dtd);
        rewind($f);
        return $f;
    }
);

$dd = new DOMDocument;
$r  = $dd->loadXML($xml);

var_dump($dd->validate());
?>

    
```

El ejemplo anterior mostrará:

    string(10) "-//FOO/BAR"
    string(25) "http://example.com/foobar"
    array(4) {
        ["directory"]    => NULL
        ["intSubName"]   => NULL
        ["extSubURI"]    => NULL
        ["extSubSystem"] => NULL
    }
    bool(true)

## Véase también

`libxml_disable_entity_loader`, `libxml_get_external_entity_loader`
