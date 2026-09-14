---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/libxml.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_revision: 7dce59104
order: 43640
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`LIBXML_BIGLINES` (`int`)  
Permite señalar correctamente los números de línea superiores a 65535.

> [!NOTE]
> Disponible únicamente en PHP 7.0.0 con Libxml \>= 2.9.0

`LIBXML_COMPACT` (`int`)  
Activa la optimización de la asignación de pequeños nodos. Esto podría aumentar la rapidez de la aplicación sin necesidad de modificar el código.

> [!NOTE]
> Disponible únicamente en Libxml \>= 2.6.21

`LIBXML_DTDATTR` (`int`)  
Atributo DTD por defecto

> [!CAUTION]
> Activar la carga de atributos DTD permitirá la recuperación de entidades externas. La constante `LIBXML_NO_XXE` puede ser utilizada para evitar esto (disponible únicamente en Libxml \>= 2.13.0, a partir de PHP 8.4.0).

`LIBXML_DTDLOAD` (`int`)  
Carga el subconjunto externo

> [!CAUTION]
> Activar la carga de subconjuntos externos permitirá la recuperación de entidades externas. La constante `LIBXML_NO_XXE` puede ser utilizada para evitar esto (disponible únicamente en Libxml \>= 2.13.0, a partir de PHP 8.4.0).

`LIBXML_DTDVALID` (`int`)  
Valida con la DTD

> [!CAUTION]
> Activar la validación de DTD puede facilitar ataques por entidades externas XML (XXE). La constante `LIBXML_NO_XXE` puede ser utilizada para evitar esto (disponible únicamente en Libxml \>= 2.13.0, a partir de PHP 8.4.0).

`LIBXML_HTML_NOIMPLIED` (`int`)  
Define el flag HTML_PARSE_NOIMPLIED, que desactiva la adición automática de elementos html/body...

> [!NOTE]
> Disponible únicamente en Libxml \>= 2.7.7 (desde PHP \>= 5.4.0)

`LIBXML_HTML_NODEFDTD` (`int`)  
Define el flag HTML_PARSE_NODEFDTD, que impide la adición automática de un doctype si no se encuentra ninguno.

> [!NOTE]
> Disponible únicamente en Libxml \>= 2.7.8 (desde PHP \>= 5.4.0)

`LIBXML_LOADED_VERSION` (`string`)  
Versión del módulo principal del analizador libxml.

`LIBXML_NOBLANKS` (`int`)  
Eliminación de nodos vacíos

`LIBXML_NOCDATA` (`int`)  
Fusión de CDATA en nodos de texto

`LIBXML_NOEMPTYTAG` (`int`)  
Expande las etiquetas vacías (por ejemplo, `<br/>` en `<br></br>`)

> [!NOTE]
> Esta opción está actualmente disponible únicamente con las funciones [???](#domdocument.save) y [???](#domdocument.savexml).

`LIBXML_NOENT` (`int`)  
Sustitución de entidades

> [!CAUTION]
> Activar la sustitución de entidades puede facilitar ataques XML External Entity (XXE).

`LIBXML_NOERROR` (`int`)  
Supresión de informes de error

`LIBXML_NONET` (`int`)  
Desactivación de la red durante la carga de documentos

`LIBXML_NOWARNING` (`int`)  
Supresión de informes de advertencia

`LIBXML_NOXMLDECL` (`int`)  
Anula la declaración XML durante la guardado del documento

> [!NOTE]
> Disponible únicamente en Libxml \>= 2.6.21

`LIBXML_NO_XXE` (`int`)  
Desactiva las entidades externas XML (XXE) durante la sustitución de entidades

> [!NOTE]
> Disponible únicamente en Libxml \>= 2.13.0, a partir de PHP 8.4.0

`LIBXML_NSCLEAN` (`int`)  
Eliminación de espacios de nombres redundantes

`LIBXML_PARSEHUGE` (`int`)  
Afecta al flag XML_PARSE_HUGE. Aumenta algunos límites del analizador codificados en el código. Esto afecta a límites como la profundidad máxima de un documento o la recursión de entidades, pero también a los límites del tamaño del texto de los nodos.

> [!CAUTION]
> Dado que esto aumenta los límites codificados en el código, solo debería utilizarse con datos de confianza. Aumentar el límite de profundidad sobre datos no confiables puede provocar un consumo excesivo de recursos, como un desbordamiento de pila al procesar un documento profundamente anidado.

> [!NOTE]
> Disponible únicamente desde Libxml \>= 2.7.0 (desde PHP \>= 5.3.2 y PHP \>= 5.2.12)

`LIBXML_PEDANTIC` (`int`)  
Define el flag XML_PARSE_PEDANTIC, que activa el informe de error pedantic.

> [!NOTE]
> Disponible a partir de PHP \>= 5.4.0

`LIBXML_RECOVER` (`int`)  
Activa el modo de recuperación durante el análisis de un documento.

> [!NOTE]
> Disponible únicamente a partir de PHP 8.4.0

`LIBXML_XINCLUDE` (`int`)  
Ejecuta la sustitución XInclude (solo para analizadores pull, es decir, `XMLReader`).

`LIBXML_ERR_ERROR` (`int`)  
Error no fatal

`LIBXML_ERR_FATAL` (`int`)  
Error fatal

`LIBXML_ERR_NONE` (`int`)  
Ningún error

`LIBXML_ERR_WARNING` (`int`)  
Una advertencia simple

`LIBXML_VERSION` (`int`)  
Versión de libxml en formato 20605 o 20617

`LIBXML_DOTTED_VERSION` (`string`)  
Versión de libxml en formato 2.6.5 o 2.6.17

`LIBXML_SCHEMA_CREATE` (`int`)  
Crea el valor por defecto/fijo del nodo durante la validación del esquema XSD

> [!NOTE]
> Disponible únicamente en Libxml \>= 2.6.14 (a partir de PHP \>= 5.5.2)
