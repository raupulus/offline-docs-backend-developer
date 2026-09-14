---
title: Introducción
source_url: https://www.php.net/manual/es/mysqlnd.overview.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlnd/overview.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlnd
translation_status: ready
translation_reviewed: false
translation_revision: 9598935f2
order: 56170
---

## Introducción

**Lo que no es**

Aunque el driver nativo de MySQL está escrito como una extensión PHP, es importante señalar que no proporciona una nueva API al programador PHP. Las API para programadores son proporcionadas por la extensión MySQL, `mysqli` y PDO MySQL. Estas extensiones pueden ahora utilizar los servicios del driver nativo MySQL para comunicarse con el servidor MySQL. Por lo tanto, el driver nativo MySQL no debe ser considerado como una API.

**¿Por qué utilizarlo?**

Utilizar el driver nativo de MySQL ofrece numerosas ventajas en comparación con la biblioteca cliente de MySQL.

La antigua biblioteca cliente de MySQL fue escrita por MySQL AB (ahora parte de Oracle Corporation) y, por lo tanto, fue publicada bajo la licencia MySQL, lo que tuvo como consecuencia la desactivación del soporte de MySQL por defecto en PHP. Dado que el driver nativo de MySQL fue desarrollado como parte integral del proyecto PHP, se publica bajo la licencia PHP, lo que resuelve los problemas de licencia que existían en el pasado.

Además, anteriormente, era necesario compilar las extensiones de base de datos MySQL en relación con una copia de la biblioteca cliente de MySQL, lo que significaba que se debía tener instalado MySQL en la máquina donde se compilaba PHP a partir de los fuentes. Por lo tanto, cuando se ejecutaba la aplicación PHP, las extensiones MySQL llamaban a los archivos de la biblioteca cliente de MySQL al inicio, los cuales debían estar obligatoriamente instalados en el sistema. Con el driver nativo de MySQL, esto ya no es necesario ya que está incluido en la distribución estándar. Por lo tanto, ya no será necesario tener instalado MySQL para compilar PHP o ejecutar aplicaciones PHP que hagan uso de una base de datos.

Dado que el driver nativo de MySQL está escrito como una extensión PHP, está íntimamente ligado al núcleo de PHP. Esto implica una mejor eficiencia, especialmente en lo que respecta al uso de la memoria, ya que el driver utiliza la asignación de memoria de PHP y, por lo tanto, soporta los límites de memoria. Utilizar el driver nativo de MySQL resulta en un rendimiento igual o mejor que con la biblioteca cliente de MySQL, ya que el uso de la memoria es mucho más eficiente. El hecho de que, al utilizar la biblioteca cliente de MySQL, cada registro se almacene dos veces en memoria, mientras que el cliente nativo de MySQL solo lo almacena una vez, es un buen ejemplo de una buena gestión de la memoria.

> [!NOTE]
> Debido a que el driver nativo de MySQL utiliza el sistema de gestión de memoria de PHP, su uso de memoria puede ser supervisado con la función `memory_get_usage`. Esto no es posible con la biblioteca libmysqlclient ya que utiliza la función C malloc() en su lugar.

**Funcionalidades especiales**

El driver nativo de MySQL también proporciona algunas funcionalidades especiales no disponibles con la biblioteca cliente de MySQL, listadas a continuación:

- Conexiones persistentes mejoradas

- La función especial `mysqli_fetch_all`

- Llamadas a las estadísticas de rendimiento: `mysqli_get_client_stats`, `mysqli_get_connection_stats`

Las estadísticas de rendimiento pueden ser muy útiles para identificar cuellos de botella de rendimiento.

El driver nativo de MySQL también proporciona conexiones persistentes al utilizarlo con la extensión `mysqli`.

**Soporte de SSL**

El driver nativo de MySQL (MySQL Native Driver) soporta SSL.

**Soporte del protocolo comprimido**

El driver nativo de MySQL soporta el protocolo cliente/servidor MySQL comprimido. La extensión `ext/mysqli`, si está configurada para utilizar el driver nativo de MySQL, también puede beneficiarse de esta funcionalidad. Es importante señalar que `PDO_MYSQL` no soporta *EN ABSOLUTO* la compresión cuando se utiliza con mysqlnd.

**Soporte de pipes nombrados**

Los pipes nombrados pueden ser utilizados para conectarse bajo Windows.
