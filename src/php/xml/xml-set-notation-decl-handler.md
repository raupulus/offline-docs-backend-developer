---
title: xml_set_notation_decl_handler
description: Configura el gestor XML de notaciones
source_url: https://www.php.net/manual/es/function.xml-set-notation-decl-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-set-notation-decl-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 18aa2012f
order: 102840
---

xml_set_notation_decl_handler

Configura el gestor XML de notaciones

## Descripción

```php
xml_set_notation_decl_handler(XMLParser $parser, callable $handler): true
```php

Establece los gestores de inicio y fin del analizador XML `parser`.

Una notación es una parte del DTD del documento, que tiene el formato siguiente:

```
<!NOTATION <parameter>name</parameter>
{ <parameter>systemId</parameter> | <parameter>publicId</parameter>? }

   
```php

Consulte la sección [de las especificaciones XML 1.0](http://www.w3.org/TR/1998/REC-xml-19980210#Notations) para conocer las notaciones de las entidades externas.

## Parámetros

`parser`  
El analizador XML.

`handler`  
Si `null` se pasa, el controlador se reinicia a su estado predeterminado.

> [!WARNING]
> Una cadena vacía también reiniciará el controlador, sin embargo esta funcionalidad está deprecada a partir de PHP 8.4.0.

Si `handler` es un `callable`, el callable se define como el controlador.

Si `handler` es una `string`, puede ser el nombre de un método de un objeto definido con `xml_set_object`.

> [!WARNING]
> Esta funcionalidad está deprecada a partir de PHP 8.4.0.

> [!WARNING]
> A partir de PHP 8.4.0, se verifica la validez del callable durante la configuración del controlador, y no en el momento de su llamada. Esto significa que `xml_set_object` debe ser llamado antes de definir un método como cadena como devolución de llamada. Sin embargo, como este comportamiento también está deprecado a partir de PHP 8.4.0, se recomienda utilizar un `callable` adecuado para el método.

La firma del gestor debe ser:

```php
handler(XMLParser $parser, string $notation_name, string $base, string $system_id, string $public_id): void
```

`parser`  
El analizador XML que llama al controlador.

`notation_name`  
El nombre de la notación, como se especifica en el formato de notación anterior.

`base`  
La raíz para la resolución del identificador de sistema (`system_id`) de la entidad externa.

`system_id`  
Identificador de sistema para esta entidad externa.

`public_id`  
Identificador público para esta entidad externa.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar un valor no `callable` de tipo `string` a `handler` ahora está obsoleto; utilice un callable apropiado para los métodos, o `null` para reinicializar el gestor. |
| 8.4.0 | La validez de `handler` como `callable` ahora se verifica al definir el gestor en lugar de verificarse al invocarlo. |
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |
