---
title: xml_set_element_handler
description: Establece los gestores de inicio y fin de etiqueta XML
source_url: https://www.php.net/manual/es/function.xml-set-element-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-set-element-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: false
translation_revision: 18aa2012f
order: 102810
---

xml_set_element_handler

Establece los gestores de inicio y fin de etiqueta XML

## Descripción

```php
xml_set_element_handler(XMLParser $parser, callable $start_handler, callable $end_handler): true
```php

Establece los gestores de inicio y fin del analizador XML `parser`.

`start_handler` es llamado cuando un nuevo elemento XML es abierto. `end_handler` es llamado cuando un elemento XML es cerrado.

## Parámetros

`parser`  
El analizador XML.

`start_handler`  
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
start_element_handler(XMLParser $parser, string $name, array $attributes): void
```

`parser`  
El analizador XML que llama al controlador.

`name`  
Contiene el nombre del elemento que provocó la llamada del gestor. Si el analizador gestiona la [caja](#xml.case-folding), este elemento estará en mayúsculas.

`attributes`  
Un array asociativo con los atributos del elemento. El array estará vacío si no hay atributos. Las claves de este array serán los nombres de los atributos, y los valores serán los valores correspondientes de los atributos. Los nombres de los atributos estarán en mayúsculas si el analizador gestiona la [caja](#xml.case-folding). Los valores de los atributos *permanecerán inalterados*.

El orden en el que `attributes` es recorrido es idéntico al orden en el que los atributos fueron declarados.

`end_handler`  
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
end_element_handler(XMLParser $parser, string $name): void
```php

`parser`  
El analizador XML que llama al controlador.

`name`  
Contiene el nombre del elemento que provocó la llamada del gestor. Si el analizador gestiona la [caja](#xml.case-folding), este elemento estará en mayúsculas.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar un valor no `callable` de tipo `string` a `handler` ahora está obsoleto; utilice un callable apropiado para los métodos, o `null` para reinicializar el gestor. |
| 8.4.0 | La validez de `handler` como `callable` ahora se verifica al definir el gestor en lugar de verificarse al invocarlo. |
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |
