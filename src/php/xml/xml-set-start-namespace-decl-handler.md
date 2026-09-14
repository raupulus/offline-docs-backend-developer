---
title: xml_set_start_namespace_decl_handler
description: Configura el gestor de caracteres
source_url: https://www.php.net/manual/es/function.xml-set-start-namespace-decl-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/functions/xml-set-start-namespace-decl-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 18aa2012f
order: 102870
---

xml_set_start_namespace_decl_handler

Configura el gestor de caracteres

## Descripción

```php
xml_set_start_namespace_decl_handler(XMLParser $parser, callable $handler): true
```php

Establece el gestor a llamar cuando se declara el espacio de nombres. Las declaraciones de espacio de nombres ocurren en las etiquetas de inicio. Pero el gestor de inicio, llamado al declarar el espacio de nombres, es llamado antes que el gestor de la etiqueta de inicio para cada espacio de nombres declarado en dicha etiqueta.

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
handler(XMLParser $parser, string $prefix, string $uri): void
```

`parser`  
El analizador XML que llama al controlador.

`prefix`  
El prefijo es un `string` utilizado para referenciar el espacio de nombres de un objeto XML. `false` si no existe ningún prefijo.

`uri`  
Identificador de recurso uniforme (URI) de un espacio de nombres.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Pasar un valor no `callable` de tipo `string` a `handler` ahora está obsoleto; utilice un callable apropiado para los métodos, o `null` para reinicializar el gestor. |
| 8.4.0 | La validez de `handler` como `callable` ahora se verifica al definir el gestor en lugar de verificarse al invocarlo. |
| 8.0.0 | `parser` ahora espera una instancia de `XMLParser` ; anteriormente, se esperaba un recurso `xml` de tipo `resource` válido. |

## Véase también

`xml_set_end_namespace_decl_handler`
