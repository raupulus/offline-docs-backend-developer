---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/xml.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 765b2d6ee
order: 102890
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere la extensión PHP [libxml](#book.libxml). Esto significa pasar la opción de configuración `--with-libxml`, o anterior a PHP 7.4 la opción de configuración `--enable-libxml`, aunque esto se realiza implícitamente ya que libxml está activado por defecto.

Esta extensión PHP utiliza expat compat layer por omisión. Asimismo puede utilizar expat, que está disponible en <https://libexpat.github.io/>. El fichero Makefile incluido con expat no construye una biblioteca por omisión: es necesario utilizar la siguiente línea:

```php
libexpat.a: $(OBJS)
    ar -rc $@ $(OBJS)
    ranlib $@

   
```

Un paquete RPM fuente de expat está disponible en <https://sourceforge.net/projects/expat/>.

## Tipos de recursos

Anterior a PHP 8.0.0, el recurso `xml` es retornado por `xml_parser_create` y `xml_parser_create_ns`, y representa un analizador XML para ser utilizado con las otras funciones de esta extensión.
