---
title: Manejadores de eventos
source_url: https://www.php.net/manual/es/xml.eventhandlers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/eventhandlers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_revision: 47065812c
order: 102650
---

Los manejadores XML de eventos definidos son:

| Función PHP para configurar el manejador | Descripción del evento |
|----|----|
| `xml_set_element_handler` | Los eventos de elemento se producen cada vez que el intérprete XML encuentra etiquetas de inicio o de final. Hay manejadores separados para etiquetas de inicio y final. |
| `xml_set_character_data_handler` | Por definición los datos de caracteres es todo el contenido no marcado de los documentos XML, incluidos los espacios en blanco entre etiquetas. Tenga en cuenta que el intérprete XML no añade o elimina ningún espacio en blanco, eso depende de la aplicación (usted) decidir si el espacio en blanco es significativo. |
| `xml_set_processing_instruction_handler` | Los programadores de PHP ya deberían estar familiarizados con las instrucciones de procesado (PI). \<?php ?\> es una instrucción de procesado, donde \<php\> se denomina "PI destino". El manejo de ellos es específico para cada aplicación, excepto los PI destinos que empiecen con "XML", ya que estan reservados. |
| `xml_set_default_handler` | Lo que no va a otro manejador va al manejador predeterminado. En el controlador predeterminado se obtendran cosas como el XML y las declaraciones de tipo de documento. |
| `xml_set_unparsed_entity_decl_handler` | Este manejador será llamado para la declaración de una entidad no analizada (NDATA). |
| `xml_set_notation_decl_handler` | Este manejador es llamado para la declaración de una notación. |
| `xml_set_external_entity_ref_handler` | Este manejador es llamado cuando el intérprete XML encuentra una referencia a una entidad general externa analizada. Por ejemplo puede ser una referencia a un fichero o una URL. Ver [el ejemplo de entidad externa](#example.xml-external-entity) para una demostración. |
| `xml_set_start_namespace_decl_handler` | Este manejador es llamado al principio de una declaración de namespace. |
| `xml_set_end_namespace_decl_handler` | Este manejador es llamado al fin de un espacio de una declaración de namespace. Tenga en cuenta que este evento *no* es bajo LibXML. |

Manejadores XML soportados
