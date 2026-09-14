---
title: Gestión de la memoria
source_url: https://www.php.net/manual/es/mysqlnd.memory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlnd/memory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlnd
translation_status: ready
translation_reviewed: false
translation_revision: 9598935f2
order: 56150
---

## Gestión de la memoria

**Introducción**

El driver nativo MySQL gestiona la memoria de forma diferente a la biblioteca cliente MySQL. Las bibliotecas difieren en la forma en que la memoria es asignada y liberada, en la forma en que la memoria es asignada por fragmentos durante la lectura de los resultados desde MySQL, qué opciones de depuración y desarrollo existen, y cómo los resultados leídos desde MySQL son vinculados a las variables de usuario PHP.

Las notas siguientes son una introducción y un resumen destinados a los usuarios interesados en comprender el driver nativo MySQL desde el punto de vista del código C.

**Funciones utilizadas en la gestión de memoria**

Todas las asignaciones y desasignaciones se realizan utilizando las funciones de gestión de memoria de PHP. Sin embargo, el consumo de memoria de mysqlnd puede ser monitoreado utilizando llamadas a APIs de PHP, como `memory_get_usage`. Debido a que la memoria es asignada y liberada utilizando la gestión de memoria de PHP, las modificaciones pueden no ser inmediatamente visibles a nivel del sistema operativo. El gestor de memoria de PHP funciona como un proxy que puede tener un poco de retraso en la liberación de memoria del sistema. Además, la comparación del uso de memoria del driver nativo MySQL y de la biblioteca cliente MySQL se vuelve difícil. La biblioteca cliente MySQL llama directamente al gestor de memoria del sistema operativo, y por lo tanto, los efectos pueden ser vistos inmediatamente a nivel del sistema operativo.

Todas las limitaciones de memoria realizadas por PHP afectan también al driver nativo MySQL. Esto puede causar errores de excedente de memoria al recuperar juegos de resultados demasiado grandes, excediendo el tamaño de la memoria restante disponible para PHP. Debido a que la biblioteca cliente MySQL no utiliza las funciones de gestión de memoria de PHP, no tiene en cuenta ninguna limitación de memoria definida por PHP. Si se utiliza la biblioteca cliente MySQL, según el modelo de despliegue, la huella de memoria del proceso PHP puede aumentar y superar el límite de memoria impuesto por PHP. Además, los scripts PHP pueden analizar juegos de resultados más grandes, asignando así más memoria para el juego de resultados de la que el control del motor PHP permite.

Las funciones de gestión de memoria de PHP son llamadas por el driver nativo MySQL a través de un gestor ligero. Entre otras cosas, este gestor facilita el depuración.

**Gestión de los juegos de resultados**

Los diferentes servidores MySQL y las diferentes APIs de clientes se diferencian según el [buffering o no](#mysqli.quickstart.statements) de los juegos de resultados. Los juegos de resultados que no son bufferizados son transferidos línea por línea desde MySQL hacia el cliente, y el cliente recorrerá los resultados. Los resultados que son bufferizados son recuperados en su totalidad por la biblioteca cliente antes de pasarlos al cliente.

El driver nativo MySQL utiliza flujos PHP para la comunicación en red con el servidor MySQL. Los resultados enviados por MySQL son recuperados desde la memoria buffer de los flujos de red PHP hacia la memoria buffer de resultados de mysqlnd. La memoria buffer de resultados está compuesta por zvals. En una etapa siguiente, los resultados son puestos a disposición del script PHP. La transferencia final desde la memoria buffer de resultados hacia las variables PHP impacta el consumo de memoria y esto se vuelve muy visible al utilizar juegos de resultados bufferizados.

Por omisión, el driver nativo MySQL intenta no conservar en memoria dos veces los resultados bufferizados. Los resultados son conservados una sola vez en la memoria buffer interna de resultados, así como en sus zvals. Cuando los resultados son recuperados en las variables PHP por el script PHP, las variables referenciarán la memoria buffer interna de resultados. Los resultados de consultas de base de datos no son copiados y son conservados en memoria solo una vez. Cuando un usuario modifica el contenido de una variable que contiene un resultado de base de datos, una operación de copia-al-escritura debe ser realizada para evitar modificar la memoria buffer interna de resultado referenciada. El contenido de la memoria buffer no debe ser modificado porque el usuario puede decidir leer el juego de resultados una segunda vez. La operación de copia-al-escritura está implementada utilizando un gestor de lista de referencia adicional, así como el uso de los contadores de referencia zvals estándar. La operación de copia-al-escritura también debe ser realizada si el usuario lee un juego de resultados en las variables PHP y libera un juego de resultado antes de que las variables sean eliminadas.

En general, este mecanismo funciona bien para los scripts que leen un juego de resultados una sola vez, y no modifican las variables que contienen los resultados. Su principal desventaja es la sobrecarga de memoria causada por el gestor de referencia adicional, que proviene principalmente del hecho de que las variables de usuario que contienen los resultados no pueden ser liberadas completamente mientras el gestor de referencia mysqlnd las siga referenciando. El driver nativo MySQL elimina la referencia a las variables de usuario cuando el juego de resultados es liberado o cuando se realiza una operación de copia-al-escritura. Un observador puede ver que el consumo total de memoria aumenta mientras el juego de resultados no sea liberado. Utilice las [estadísticas](#mysqlnd.stats) para verificar si un script libera el juego de resultados explícitamente, o si el driver lo libera implícitamente, haciendo que la memoria sea utilizada más tiempo del necesario. Las estadísticas también pueden ayudar a ver las operaciones de copia-al-escritura.

Un script PHP que lee muchas pequeñas líneas de un juego de resultados bufferizado utilizando líneas de código como `while ($row = $res->fetch_assoc()) { ... }` puede optimizar el consumo de memoria solicitando una copia en lugar de referencias. Aunque solicitar copias significa conservar dos veces el resultado en memoria, esto permite a PHP liberar la copia contenida en `$row` sabiendo que el juego de resultados está siendo recorrido y antes de liberar el juego de resultados en sí. En un servidor cargado, la optimización del uso de memoria puede mejorar el rendimiento del sistema en general, aunque para un script individual, el enfoque de la copia puede ser más lento debido a las operaciones adicionales de asignación y copia de memoria.

**Supervisión y depuración**

Existen varias formas de supervisar el uso de memoria del driver nativo MySQL. Si el objetivo es obtener una vista rápida de alto nivel, o verificar la eficiencia de memoria de los scripts PHP, entonces revise las [estadísticas](#mysqlnd.stats) recopiladas por la biblioteca. Estas le permiten, por ejemplo, ver las consultas SQL que generan más resultados de los analizados por un script PHP.

El rastreo de [depuración](#ini.mysqlnd.debug) en el historial puede ser configurado para registrar las llamadas al gestor de memoria. Esto puede ayudar a ver cuándo la memoria es asignada o liberada. Sin embargo, el tamaño de los fragmentos de memoria solicitados puede no estar listado.

Las versiones recientes del driver nativo MySQL intentan emular situaciones de excedente de memoria aleatorio. Esto es útil únicamente para los desarrolladores C de la biblioteca, o para los desarrolladores del [complemento](#mysqlnd.plugin) mysqlnd. Consulte el código fuente para las opciones de configuración de PHP correspondientes, así como para obtener más detalles sobre este mecanismo. Esta funcionalidad se considera privada, y puede ser modificada en cualquier momento sin previo aviso.
