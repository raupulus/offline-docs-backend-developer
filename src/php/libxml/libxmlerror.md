---
title: La clase LibXMLError
source_url: https://www.php.net/manual/es/class.libxmlerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/libxmlerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 43730
---

## Introducción

Contiene diversas informaciones sobre los errores emitidos por la biblioteca libxml. Los códigos de error son descritos en la [documentación oficial de la API xmlError](https://gnome.pages.gitlab.gnome.org/libxml2/devhelp/libxml2-xmlerror.html).

## Sinopsis de la clase

LibXMLError

Propiedades

public

int

level

public

int

code

public

int

column

public

string

message

public

string

file

public

int

line

## Propiedades

`level`  
La severidad del error (una de las constantes siguientes : `LIBXML_ERR_WARNING`, `LIBXML_ERR_ERROR` o `LIBXML_ERR_FATAL`)

`code`  
El código del error.

`column`  
La columna en la cual el error ha ocurrido.

> [!NOTE]
> Esta propiedad no está totalmente implementada por la biblioteca libxml; por lo tanto, `0` es a menudo retornado.

`message`  
El mensaje de error, si existe.

`file`  
El nombre del fichero, o vacío si el XML ha sido cargado desde una cadena.

`line`  
La línea desde la cual el error ha ocurrido.
