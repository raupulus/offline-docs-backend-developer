---
title: API Funcional
source_url: https://www.php.net/manual/es/functional.parallel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/functional.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 59940
---

La API `parallel\Runtime` proporciona un alto grado de control al desarrollador PHP experimentado, y a aquellos que están íntimamente familiarizados con la escritura de aplicaciones que utilizan la concurrencia paralela.

La API funcional proporciona menos control a cambio de la capacidad de tomar decisiones para el desarrollador:

- todos los runtimes en ejecución se inician de manera idéntica

- la programación es determinada por la API, y no por el desarrollador

`parallel\run` proporciona la garantía de que la tarea comenzará a ejecutarse en paralelo tan pronto como las restricciones de hardware y del sistema operativo lo permitan, sin crear innecesariamente espacios de ejecución. Para la mayoría de las aplicaciones, la API funcional debería ser preferida.
