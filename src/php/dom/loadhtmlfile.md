---
title: DOMDocument::loadHTMLFile
description: Carga HTML desde un fichero
source_url: https://www.php.net/manual/es/domdocument.loadhtmlfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/loadhtmlfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c22cca782
order: 13160
---

DOMDocument::loadHTMLFile

Carga HTML desde un fichero

## Descripción

```php
public DOMDocument::loadHTMLFile(string $filename, [int $options]): bool
```php

Esta función analiza el documento HTML del fichero llamado `filename`. A diferencia de cargar XML, HTML no tiene que estar bien formado para cargarse.

> [!WARNING]
> Utilice `Dom\HTMLDocument` para analizar y tratar el HTML moderno en lugar de `DOMDocument`.
>
> Esta función analiza la entrada utilizando un analizador HTML 4. Las reglas de análisis del HTML 5, que son las utilizadas por los navegadores web modernos, son diferentes. Según la entrada, esto puede resultar en una estructura DOM diferente. Por lo tanto, esta función no puede ser utilizada de forma segura para la sanitización del HTML.
>
> El comportamiento durante el análisis del HTML puede depender de la versión de `libxml` que se utilice, especialmente en lo que respecta a los casos límite y el manejo de errores. Para un análisis conforme a la especificación HTML5, utilice Dom\HTMLDocument::createFromString o Dom\HTMLDocument::createFromFile, añadidos en PHP 8.4.
>
> Por ejemplo, algunos elementos HTML cerrarán implícitamente un elemento padre cuando sean encontrados. Las reglas de cierre automático de elementos padres difieren entre HTML 4 y HTML 5, y por lo tanto, la estructura DOM que `DOMDocument` ve puede ser diferente de la que un navegador web ve, lo que puede permitir potencialmente a un atacante comprometer el HTML resultante.

## Parámetros

`filename`  
La ruta al fichero HTML.

`options`  
[Operación a nivel de bits `OR`](#language.operators.bitwise) de las [constantes de opción libxml](#libxml.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si se pasa una cadena vacía a `filename` o se nombra un fichero vacío, se generará una advertencia. Esta advertencia no es generada por libxml y no puede ser controlada utilizando las [funciones de manejo de errores de libxml](#function.libxml-use-internal-errors).

Aunque el HTML mal-formado debería cargarse con éxito, esta función puede generar una advertencia de tipo `E_WARNING` cuando encuentre una mala etiqueta.[Las funciones de manejo de errores libxml](#function.libxml-use-internal-errors)pueden ser utilizadas para manejar estos errores.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Esta función ahora tiene un tipo de retorno `bool` tentativo. |
| 8.0.0 | Llamar a esta función de forma estática ahora lanzará un `Error`. Anteriormente, se emitía un `E_DEPRECATED`. |

## Ejemplos

Creando un Documento

```
<?php
$doc = new DOMDocument();
$doc->loadHTMLFile("filename.html");
echo $doc->saveHTML();
?>

    
```php

## Véase también

DOMDocument::loadHTML, DOMDocument::saveHTML, DOMDocument::saveHTMLFile
