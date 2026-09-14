---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/pdo-ibm.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_ibm/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_ibm
translation_status: ready
translation_reviewed: true
translation_revision: e8ac70bf5
order: 62340
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [pdo_ibm.i5_dbcs_alloc](#ini.pdo-ibm.i5-dbcs-alloc) | "0" | `INI_SYSTEM` | Añadido en PDO_IBM 1.5.0 |
| [pdo_ibm.i5_override_ccsid](#ini.pdo-ibm.i5-override-ccsid) | "0" | `INI_SYSTEM` | Añadido en PDO_IBM 1.5.0 |

Opciones de configuración PDO_IBM

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`pdo_ibm.i5_dbcs_alloc` `int`  
Esta opción afecta a la estrategia de asignación de memoria interna en IBM i. Por omisión, esta opción es 0. Cuando esta opción está definida, se asignan búferes con un tamaño mucho mayor, por si la base de datos engañara sobre el tamaño de los caracteres durante la conversión entre codificaciones. Esta opción utiliza seis veces más memoria para los búferes (para tener en cuenta las secuencias UTF-8 más largas), pero puede ser necesaria si se devuelven datos truncados.

- 0 - Se asigna el tamaño mínimo de los búferes.

- 1 - Se asigna un tamaño mayor de los búferes.

`pdo_ibm.i5_override_ccsid` `int`  
El CCSID ASCII a utilizar para la conversión de EBCDIC en IBM i. Al definirlo como 1208, se utilizará UTF-8. Por omisión es 0, lo que seleccionará el CCSID ASCII de trabajo predeterminado.

Para obtener más información sobre los CCSID en IBM i, consulte la [documentación de IBM](https://www.ibm.com/docs/en/i/7.5?topic=information-ccsid-reference).
