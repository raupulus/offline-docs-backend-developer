---
title: Error y gestión de errores
source_url: https://www.php.net/manual/es/com.error-handling.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/error-handling.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 888334f15
order: 7660
---

## Error y gestión de errores

Esta extensión lanzará instancias de la clase `com_exception` para cualquier error fatal reportado por COM. Todas las excepciones COM tienen una propiedad `code` que corresponde al valor de retorno HRESULT de las diversas operaciones COM. Este código puede ser utilizado para elegir de forma automática cómo gestionar esta excepción.
