---
title: Interfaz principal para el código C y los datos
source_url: https://www.php.net/manual/es/class.ffi.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 23100
---

## Introducción

Los objetos de esta clase son creados por los métodos de fábrica FFI::cdef, FFI::load o FFI::scope. Las variables C definidas están disponibles como propiedades de la instancia FFI, y las funciones C definidas están disponibles como métodos de la instancia FFI. Los tipos C declarados pueden ser utilizados para crear nuevas estructuras de datos C utilizando FFI::new y FFI::type.

El análisis de las definiciones FFI y la carga de las bibliotecas compartidas pueden llevar mucho tiempo. No es útil hacerlo en cada solicitud HTTP en un entorno Web. Sin embargo, es posible precargar las definiciones FFI y las bibliotecas al inicio de PHP, e instanciar los objetos FFI cuando sea necesario. Los archivos de encabezado pueden ser extendidos con definiciones `FFI_SCOPE` especiales (por ejemplo `#define FFI_SCOPE "foo"`; el ámbito por omisión es "C") y luego cargados por FFI::load durante la precarga. Esto conduce a la creación de una ligadura persistente, que estará disponible para todas las solicitudes siguientes a través de FFI::scope. Consulte el [ejemplo completo PHP/FFI/preloading](#ffi.examples-complete) para más detalles.

Es posible precargar más de un archivo de encabezado C en el mismo ámbito.

## Sinopsis de la clase

final

FFI

Constantes

public

const

int

FFI::\_\_BIGGEST_ALIGNMENT\_\_

Métodos

## Constantes predefinidas

`FFI::__BIGGEST_ALIGNMENT__`
