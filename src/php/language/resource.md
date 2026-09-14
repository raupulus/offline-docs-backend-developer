---
title: Recursos
source_url: https://www.php.net/manual/es/language.types.resource.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/resource.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 95bdd6883
order: 4520
---

## Recursos

Un valor tipo `resource` es una variable especial, que contiene una referencia a un recurso externo. Los recursos son creados y usados por funciones especiales. Vea el [apéndice](#resource) para un listado de todas estas funciones y los tipos `resource` correspondientes.

Vea también la función `get_resource_type`.

## Conversión a recurso

Dado que las variables `resource` contienen gestores especiales a archivos abiertos, conexiones con bases de datos, áreas de pintura de imágenes y cosas por el estilo, la conversión a tipo `resource` carece de sentido.

## Liberación de recursos

Gracias al sistema de conteo de referencias introducido con el Motor Zend, un valor de tipo `resource` sin más referencias es detectado automáticamente, y es liberado por el recolector de basura. Por esta razón, rara vez se necesita liberar la memoria manualmente.

> [!NOTE]
> Los enlaces persistentes con bases de datos son una excepción a esta regla. Ellos *no* son destruidos por el recolector de basura. Vea también la sección sobre [conexiones persistentes](#features.persistent-connections) para más información.
