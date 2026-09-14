---
title: xml_set_external_entity_ref_handler
description: Configura el gestor XML de referencias externas
source_url: https://www.php.net/manual/es/function.xml-set-external-entity-ref-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-set-external-entity-ref-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: false
translation_revision: 18aa2012f
order: 102830
---

xml_set_external_entity_ref_handler

Configura el gestor XML de referencias externas

## Descripción

```php
xml_set_external_entity_ref_handler(XMLParser $parser, callable $handler): true
```php

Establece el gestor de entidad externa del analizador XML `parser`.

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
handler(XMLParser $parser, string $open_entity_names, string $base, string $system_id, string $public_id): bool
```

`parser`  
El analizador XML que llama al controlador.

`open_entity_names`  
La lista de nombres de entidades, separados por espacios. Estas entidades son accesibles al análisis por esta entidad (incluyendo el nombre de la entidad referenciada).

`base`  
La raíz para la resolución del identificador de sistema (`system_id`) de la entidad externa.

`system_id`  
El identificador de sistema tal como se especifica en la declaración de entidad.

`public_id`  
El identificador público tal como se especifica en la declaración de entidad, o una cadena vacía, si no se ha especificado ninguna declaración. El espacio en el identificador público será normalizado como se especifica en las especificaciones XML.

El gestor debería devolver `true` si la entidad ha sido gestionada, de lo contrario `false`. Cuando se devuelve `false` el analizador XML detendrá el análisis y `xml_get_error_code` devolverá `XML_ERROR_EXTERNAL_ENTITY_HANDLING`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar un valor no `callable` de tipo `string` a `handler` ahora está obsoleto; utilice un callable apropiado para los métodos, o `null` para reinicializar el gestor. |
| 8.4.0 | La validez de `handler` como `callable` ahora se verifica al definir el gestor en lugar de verificarse al invocarlo. |
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |
| 7.3.0 | El valor de retorno de `handler` ya no es ignorado cuando la extensión ha sido compilada contra libxml. Anteriormente, el valor de retorno era ignorado y el análisis nunca se detenía. |
