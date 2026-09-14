---
title: tidy::getOptDoc
description: Devuelve la documentación correspondiente a un nombre de opción dado
source_url: https://www.php.net/manual/es/tidy.getoptdoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/getoptdoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: false
translation_revision: 8bcc6238e
order: 94060
---

tidy::getOptDoc

tidy_get_opt_doc

Devuelve la documentación correspondiente a un nombre de opción dado

## Descripción

Estilo orientado a objetos

```php
public tidy::getOptDoc(string $option): string
```php

Estilo procedimental

```php
tidy_get_opt_doc(tidy $tidy, string $option): string
```

Devuelve la documentación `tidy_get_opt_doc` para el nombre de opción dado.

> [!NOTE]
> Se requiere al menos la librería libtidy del 25 de abril del 2005 para que la función esté disponible.

## Parámetros

`tidy`  
El objeto `Tidy`

`option`  
El nombre de la opción

## Valores devueltos

Devuelve una cadena si la opción existe y tiene documentación disponible, o `false` de otro modo.

## Ejemplos

Imprimir todas las opciones, junto con su documentación y sus valores por omisión

```php
<?php

$tidy = new tidy;
$config = $tidy->getConfig();

ksort($config);

foreach ($config as $opt => $val) {

    if (!$doc = $tidy->getOptDoc($opt))
        $doc = 'no documentation available!';

    $val = ($tidy->getOpt($opt) === true)  ? 'true'  : $val;
    $val = ($tidy->getOpt($opt) === false) ? 'false' : $val;

    echo "<p><b>$opt</b> (default: '$val')<br />".
         "$doc</p><hr />\n";
}

?>

    
```

## Véase también

`tidy::getConfig`, `tidy::getOpt`
