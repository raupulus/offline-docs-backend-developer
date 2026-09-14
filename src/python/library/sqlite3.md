---
title: '"sqlite3" --- DB-API 2.0 interfaz para bases de datos SQLite'
source_url: https://docs.python.org/es/3
source_path: library/sqlite3.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3870
---

# "sqlite3" --- DB-API 2.0 interfaz para bases de datos SQLite

**Código fuente:** Lib/sqlite3/

SQLite es una biblioteca de C que provee una base de datos ligera
basada en disco que no requiere un proceso de servidor separado y
permite acceder a la base de datos usando una variación no estándar
del lenguaje de consulta SQL. Algunas aplicaciones pueden usar SQLite
para almacenamiento interno. También es posible prototipar una
aplicación usando SQLite y luego transferir el código a una base de
datos más grande como PostgreSQL u Oracle.

The "sqlite3" module was written by Gerhard Häring.  It provides an
SQL interface compliant with the DB-API 2.0 specification described by
**PEP 249**, and requires the third-party SQLite library.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

Esta documentación contiene cuatro secciones principales:

* Tutorial enseña como usar el módulo "sqlite3" module.

* Referencia describe las clases y funciones que se definen en este
  módulo.

* Guías prácticas detalla como manipular tareas específicas.

* Explicación proporciona en profundidad información sobre el control
  transaccional.

Ver también:

  https://www.sqlite.org
     La página web SQLite; la documentación describe la sintaxis y los
     tipos de datos disponibles para el lenguaje SQL soportado.

  https://www.w3schools.com/sql/
     Tutorial, referencia y ejemplos para aprender sintaxis SQL.

  **PEP 249** - Especificación de la API 2.0 de base de datos
     PEP escrito por Marc-André Lemburg.

## Tutorial

En este tutorial, será creada una base de datos de películas Monty
Python usando funcionalidades básicas de "sqlite3". Se asume un
entendimiento fundamental de conceptos de bases de dados, como cursors
y transactions.

Primero, necesitamos crear una nueva base de datos y abrir una
conexión de base de datos para permitir que "sqlite3" trabaje con
ella. Llamamos a "sqlite3.connect()" para crear una conexión a la base
de datos "tutorial.db" en el directorio de trabajo actual, creándola
implícitamente si no existe:

   import sqlite3
   con = sqlite3.connect("tutorial.db")

El retorno será un objecto de la clase "Connection" representado en
"con" como una base de datos local.

Con el fin de ejecutar sentencias SQL y obtener resultados de
consultas SQL, necesitaremos usar un cursor para la base de datos.
Llamando "con.cursor()" se creará el "Cursor":

   cur = con.cursor()

Ahora que hemos configurado una conexión y un cursor, podemos crear
una tabla "movie" con las columnas *title*, *release year*, y *review
score*. Para simplificar, podemos solamente usar nombres de columnas
en la declaración de la tabla -- gracias al recurso de flexible typing
SQLite, especificar los tipos de datos es opcional. Ejecuta la
sentencia "CREATE TABLE" llamando "cur.execute(...)":

   cur.execute("CREATE TABLE movie(title, year, score)")

Podemos verificar que una nueva tabla ha sido creada consultando la
tabla "sqlite_master" incorporada en SQLite, la cual ahora debería
contener una entrada para la tabla "movie" (consulte The Schema Table
para más información). Ejecute esa consulta llamando a
"cur.execute(...)", asigne el resultado a "res" y llame a
"res.fetchone()" para obtener la fila resultante:

   >>> res = cur.execute("SELECT name FROM sqlite_master")
   >>> res.fetchone()
   ('movie',)

Podemos ver que la tabla ha sido creada, ya que la consulta devuelve
un "tuple" que contiene el nombre de la tabla. Si consultamos
"sqlite_master" para una tabla inexistente "spam", "res.fetchone()"
devolverá "None":

   >>> res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
   >>> res.fetchone() is None
   True

Ahora, agrega dos filas de datos proporcionados como SQL literales,
ejecutando la sentencia "INSERT", una vez más llamando a
"cur.execute(...)":

   cur.execute("""
       INSERT INTO movie VALUES
           ('Monty Python and the Holy Grail', 1975, 8.2),
           ('And Now for Something Completely Different', 1971, 7.5)
   """)

La sentencia "INSERT" implícitamente abre una transacción, la cual
necesita ser confirmada antes que los cambios sean guardados en la
base de datos (consulte Control transaccional para más información).
Llamando a "con.commit()" sobre el objeto de la conexión, se
confirmará la transacción:

   con.commit()

Podemos verificar que la información fue introducida correctamente
ejecutando la consulta "SELECT". Ejecute el ahora conocido
"cur.execute(...)" para asignar el resultado a "res", y luego llame a
"res.fetchall()" para obtener todas las filas como resultado:

   >>> res = cur.execute("SELECT score FROM movie")
   >>> res.fetchall()
   [(8.2,), (7.5,)]

El resultado es una "list" de dos "tuple"s, una por fila, cada una
conteniendo el valor del "score" de esa fila.

Ahora, introduzca tres filas más llamando "cur.executemany(...)":

   data = [
       ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
       ("Monty Python's The Meaning of Life", 1983, 7.5),
       ("Monty Python's Life of Brian", 1979, 8.0),
   ]
   cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
   con.commit()  # Remember to commit the transaction after executing INSERT.

Note que los marcadores de posición "?" son usados para enlazar "data"
a la consulta. SIempre use marcadores de posición en lugar de string
formatting para unir valores Python a sentencias SQL, y así evitará
SQL injection attacks (consulte Cómo usar marcadores de posición para
vincular valores en consultas SQL para más información).

Podemos verificar que las nuevas filas fueron introducidas ejecutando
una consulta "SELECT", esta vez iterando sobre los resultados de la
consulta:

   >>> for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
   ...     print(row)
   (1971, 'And Now for Something Completely Different')
   (1975, 'Monty Python and the Holy Grail')
   (1979, "Monty Python's Life of Brian")
   (1982, 'Monty Python Live at the Hollywood Bowl')
   (1983, "Monty Python's The Meaning of Life")

Cada fila es una "tuple" de dos items con "(year, title)", donde las
columnas seleccionadas coinciden con la consulta.

Finalmente, se puede verificar que la base de datos ha sido escrita en
disco, llamando "con.close()" para cerrar la conexión existente,
abriendo una nueva, creando un nuevo cursor y luego consultando la
base de datos:

   >>> con.close()
   >>> new_con = sqlite3.connect("tutorial.db")
   >>> new_cur = new_con.cursor()
   >>> res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
   >>> title, year = res.fetchone()
   >>> print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
   The highest scoring Monty Python movie is 'Monty Python and the Holy Grail', released in 1975
   >>> new_con.close()

Ahora ha creado una base de datos SQLite usando el módulo "sqlite3",
insertado datos y recuperado valores de varias maneras.

Ver también:

  * Guías prácticas para lecturas de interés:

    * Cómo usar marcadores de posición para vincular valores en
      consultas SQL

    * Cómo adaptar tipos de Python personalizados a valores de SQLite

    * Como convertir valores SQLite a tipos de Python personalizados

    * Como usar la conexión con un administrador de contexto

    * Cómo crear y utilizar fábricas de filas

  * Explicación para obtener información detallada sobre el control de
    transacciones..

## Referencia

### Funciones del módulo

sqlite3.connect(database, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False, *, autocommit=sqlite3.LEGACY_TRANSACTION_CONTROL)

   Abre una conexión con una base de datos SQLite.

   Parámetros:
      * **database** (*path-like object*) -- La ruta al archivo de
        base de datos que se va a abrir. Puede pasar "":memory:"" para
        crear un SQLite database existing only in memory y abrir una
        conexión con él.

      * **timeout** (*float*) -- Cuántos segundos debe esperar la
        conexión antes de generar un "OperationalError" cuando una
        tabla está bloqueada. Si otra conexión abre una transacción
        para modificar una tabla, esa tabla se bloqueará hasta que se
        confirme la transacción. El valor predeterminado es cinco
        segundos.

      * **detect_types** (*int*) -- Control whether and how data types
        not natively supported by SQLite are looked up to be converted
        to Python types, using the converters registered with
        "register_converter()". Set it to any combination (using "|",
        bitwise or) of "PARSE_DECLTYPES" and "PARSE_COLNAMES" to
        enable this. Column names take precedence over declared types
        if both flags are set. By default ("0"), type detection is
        disabled.

      * **isolation_level** (*str** | **None*) -- Controla el
        comportamiento de manejo de transacciones heredadas. Consulta
        "Connection.isolation_level" y Control de transacciones
        mediante el atributo isolation_level para obtener más
        información. Puede ser ""DEFERRED"" (predeterminado),
        ""EXCLUSIVE"" o ""IMMEDIATE""; o "None" para deshabilitar la
        apertura de transacciones de manera implícita. No tiene efecto
        a menos que "Connection.autocommit" se configure en
        "LEGACY_TRANSACTION_CONTROL" (predeterminado).

      * **check_same_thread** (*bool*) -- Si es "True"
        (predeterminado), se generará "ProgrammingError" si la
        conexión de la base de datos la utiliza un subproceso distinto
        del que la creó. Si es "False", se puede acceder a la conexión
        en varios subprocesos; es posible que el usuario deba
        serializar las operaciones de escritura para evitar la
        corrupción de datos. Consulte "threadsafety" para obtener más
        información.

      * **factory** (*Connection*) -- Una subclase personalizada de
        "Connection" con la que crear la conexión, sino la
        "Connection" será la predeterminada.

      * **cached_statements** (*int*) -- El número de instrucciones
        que "sqlite3" debe almacenar internamente en caché para esta
        conexión, para evitar la sobrecarga de análisis. El valor
        predeterminada, son 128 instrucciones.

      * **uri** (*bool*) -- Si se establece en "True", *database* es
        interpretada como una URI (Uniform Resource Identifier) con la
        ruta de un archivo y una consulta de cadena de caracteres de
        modo opcional. La parte del esquema *debe* ser ""file:"", y la
        ruta puede ser relativa o absoluta. La consulta permite pasar
        parámetros a SQLite, habilitando varias Como trabajar con URIs
        SQLite.

      * **autocommit** (*bool*) -- Controla el comportamiento de
        manejo de transacciones de **PEP 249**. Consulta
        "Connection.autocommit" y Control de transacciones mediante el
        atributo autocommit para obtener más información. *autocommit*
        tiene como valor predeterminado "LEGACY_TRANSACTION_CONTROL".
        El valor predeterminado cambiará a "False" en una futura
        versión de Python.

   Tipo del valor devuelto:
      *Connection*

   Lanza un auditing event "sqlite3.connect" con el argumento
   "database".

   Lanza un auditing event "sqlite3.connect/handle" con el argumento
   "connection_handle".

   Distinto en la versión 3.4: Se agregó el parámetro *uri*.

   Distinto en la versión 3.7: *database* ahora también puede ser un
   *path-like object*, no solo una cadena de caracteres.

   Distinto en la versión 3.10: Se agregó el evento de auditoría
   "sqlite3.connect/handle".

   Distinto en la versión 3.12: Se agregó el parámetro *autocommit*.

   Distinto en la versión 3.13: El uso posicional de los parámetros
   *timeout*, *detect_types*, *isolation_level*, *check_same_thread*,
   *factory*, *cached_statements* y *uri* está obsoleto. Se
   convertirán en parámetros de solo palabras clave en Python 3.15.

sqlite3.complete_statement(statement)

   Retorna "True" si la cadena de caracteres *statement* pareciera
   contener uno o más sentencias SQL completas. No se realiza ninguna
   verificación o análisis sintáctico de ningún tipo, aparte de
   comprobar que no hay cadena de caracteres literales sin cerrar y
   que la sentencia se termine con un punto y coma.

   Por ejemplo:

      >>> sqlite3.complete_statement("SELECT foo FROM bar;")
      True
      >>> sqlite3.complete_statement("SELECT foo")
      False

   Esta función puede ser útil con entradas de línea de comando para
   determinar si los textos introducidos parecen formar una sentencia
   completa SQL, o si una entrada adicional se necesita antes de
   llamar a "execute()".

   Consulte "runsource()" en Lib/sqlite3/__main__.py para uso en el
   mundo real.

sqlite3.enable_callback_tracebacks(flag, /)

   Habilita o deshabilita seguimiento de retrollamadas. Por defecto no
   se obtendrá ningún *tracebacks* en funciones *aggregates*,
   *converters*, autorizador de *callbacks* etc, definidas por el
   usuario. Si quieres depurarlas, se puede llamar esta función con
   *flag* establecida como "True". Después se obtendrán *tracebacks*
   de los *callbacks* en "sys.stderr". Usar "False" para deshabilitar
   la característica de nuevo.

   Nota:

     Los errores en las devoluciones de llamadas de funciones
     definidas por el usuario se registran como excepciones que no se
     pueden generar. Utilice un "unraisable hook handler" para la
     introspección de la devolución de llamada fallida.

sqlite3.register_adapter(type, adapter, /)

   Registre un *adapter* *callable* para adaptar el tipo Python *type*
   a un tipo SQLite. El adaptador se llama con un objeto Python de
   tipo *type* como único argumento y debe devolver un valor type that
   SQLite natively understands.

sqlite3.register_converter(typename, converter, /)

   Registre *converter* *callable* para convertir objetos SQLite de
   tipo *typename* en un objeto Python de un tipo específico. El
   convertidor se invoca para todos los valores SQLite de tipo
   *typename*; se le pasa un objeto "bytes" y debe devolver un objeto
   del tipo Python deseado. Consulte el parámetro *detect_types* de
   "connect()" para obtener información sobre cómo funciona la
   detección de tipos.

   Nota: *typename* y el nombre del tipo en tu consulta coinciden sin
   distinción entre mayúsculas y minúsculas.

### Constantes del módulo

sqlite3.LEGACY_TRANSACTION_CONTROL

   Establezca "autocommit" en esta constante para seleccionar el
   comportamiento de control de transacciones de estilo antiguo
   (anterior a Python 3.12). Consulte Control de transacciones
   mediante el atributo isolation_level para obtener más información.

sqlite3.PARSE_DECLTYPES

   Pasa este valor de flag como parámetro *detect_types* de la
   "connect()" para buscar una función *converter* usando los tipos
   declarados para cada columna. Los tipos son declarados cuando la
   tabla de la base de datos se creó. "sqlite3" buscará una función
   *converter* usando la primera palabra del tipo declarado como la
   llave del diccionario conversor. Por ejemplo:

      CREATE TABLE test(
         i integer primary key,  ! will look up a converter named "integer"
         p point,                ! will look up a converter named "point"
         n number(10)            ! will look up a converter named "number"
       )

   Esta puede ser combinada con "PARSE_COLNAMES" usando el operador
   "|" (*bitwise or*).

   Nota:

     Generated fields (for example "MAX(p)") are returned as "str".
     Use "PARSE_COLNAMES" to enforce types for such queries.

sqlite3.PARSE_COLNAMES

   Pass this flag value to the *detect_types* parameter of "connect()"
   to look up a converter function by using the type name, parsed from
   the query column name, as the converter dictionary key. The query
   column name must be wrapped in double quotes (""") and the type
   name must be wrapped in square brackets ("[]").

      SELECT MAX(p) as "p [point]" FROM test;  ! will look up converter "point"

   Esta flag puede ser combinada con "PARSE_DECLTYPES" usando el
   operador "|" (*bitwise or*) .

sqlite3.SQLITE_OK
sqlite3.SQLITE_DENY
sqlite3.SQLITE_IGNORE

   Banderas que debe devolver el *authorizer_callback* que *callable*
   pasa a "Connection.set_authorizer()", para indicar si:

   * Acceso es permitido ("SQLITE_OK"),

   * La sentencia SQL debería ser abortada con un error
     ("SQLITE_DENY")

   * La columna debería ser tratada como un valor "NULL"
     ("SQLITE_IGNORE")

sqlite3.apilevel

   Cadena de caracteres constante que indica el nivel DB-API
   soportado. Requerido por DB-API. Codificado de forma rígida en
   ""2.0"".

sqlite3.paramstyle

   Cadena de caracteres que indica el tipo de formato del marcador de
   parámetros esperado por el módulo "sqlite3". Requerido por DB-API.
   Codificado de forma rígida en ""qmark"".

   Nota:

     También se admite el estilo de parámetro "named" DB-API.

sqlite3.sqlite_version

   El número de versión de la librería SQLite en tiempo de ejecución,
   como una "cadena de caracteres".

sqlite3.sqlite_version_info

   El número de versión de la librería SQLite en tiempo de ejecución,
   como una "tupla" de "enteros".

sqlite3.threadsafety

   Constante de tipo entero requerida por la DB-API 2.0, la cual
   indica el nivel de seguridad de subproceso que "sqlite3" soporta.
   Este atributo se establece basándose en el modo de subprocesamiento
   por defecto con el que la biblioteca SQLite se compila. Los modos
   de subprocesamiento de SQLite son:

   1. **Single-thread**: En este modo, todos los *mutexes* son
      deshabilitados y no es seguro usar SQLite en más de un solo hilo
      a la vez.

   2. **Multi-thread**: En este modo, es seguro usar SQLite desde
      varios hilos dado que que ninguna conexión de base de datos sea
      usada simultáneamente en dos o más hilos.

   3. **Serialized**: En el modo serializado, es seguro usar SQLite
      por varios hilos sin restricción.

   Las asignaciones de los modos de subprocesos SQLite a los niveles
   de seguridad de subprocesos de DB-API 2.0 son las siguientes:

   +--------------------+------------------------+------------------------+---------------------------------+
   | Modo de            | **threadsafety**       | SQLITE_THREADSAFE      | Significado de DB-API 2.0       |
   | subprocesamiento   |                        |                        |                                 |
   | SQLite             |                        |                        |                                 |
   |====================|========================|========================|=================================|
   | single-thread      | 0                      | 0                      | Hilos no pueden compartir el    |
   |                    |                        |                        | módulo                          |
   +--------------------+------------------------+------------------------+---------------------------------+
   | multi-thread       | 1                      | 2                      | Hilos pueden compartir el       |
   |                    |                        |                        | módulo, pero no conexiones      |
   +--------------------+------------------------+------------------------+---------------------------------+
   | serialized         | 3                      | 1                      | Hilos pueden compartir el       |
   |                    |                        |                        | módulo, conexiones y cursores   |
   +--------------------+------------------------+------------------------+---------------------------------+

   Distinto en la versión 3.11: Establece *threadsafety* dinámicamente
   en vez de codificarlo rígidamente a "1".

sqlite3.SQLITE_DBCONFIG_DEFENSIVE
sqlite3.SQLITE_DBCONFIG_DQS_DDL
sqlite3.SQLITE_DBCONFIG_DQS_DML
sqlite3.SQLITE_DBCONFIG_ENABLE_FKEY
sqlite3.SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER
sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION
sqlite3.SQLITE_DBCONFIG_ENABLE_QPSG
sqlite3.SQLITE_DBCONFIG_ENABLE_TRIGGER
sqlite3.SQLITE_DBCONFIG_ENABLE_VIEW
sqlite3.SQLITE_DBCONFIG_LEGACY_ALTER_TABLE
sqlite3.SQLITE_DBCONFIG_LEGACY_FILE_FORMAT
sqlite3.SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE
sqlite3.SQLITE_DBCONFIG_RESET_DATABASE
sqlite3.SQLITE_DBCONFIG_TRIGGER_EQP
sqlite3.SQLITE_DBCONFIG_TRUSTED_SCHEMA
sqlite3.SQLITE_DBCONFIG_WRITABLE_SCHEMA

   Estas constantes se utilizan para los métodos
   "Connection.setconfig()" y "getconfig()".

   La disponibilidad de estas constantes varía según la versión de
   SQLite con la que se compiló Python.

   Added in version 3.12.

   Ver también:

     https://www.sqlite.org/c3ref/c_dbconfig_defensive.html
        Documentación de SQLite: Opciones de configuración de la
        conexión a la base de datos

Deprecated since version 3.12, removed in version 3.14: The "version"
and "version_info" constants.

### Objetos de conexión

class sqlite3.Connection

   Cada base de datos SQLite abierta es representada por un objeto
   "Connection", el cual se crea usando "sqlite3.connect()". Su
   objetivo principal es crear objetos "Cursor", y Control
   transaccional.

   Ver también:

     * Cómo utilizar los métodos de acceso directo de conexión

     * Como usar la conexión con un administrador de contexto

   Distinto en la versión 3.13: Se emite un "ResourceWarning" si no se
   llama a "close()" antes de eliminar un objeto "Connection".

   Una conexión a una base de datos SQLite tiene los siguientes
   atributos y métodos:

   cursor(factory=Cursor)

      Crea y devuelve un objeto "Cursor". El método del cursor acepta
      un único parámetro opcional, *factory*. Si se proporciona, debe
      ser un *callable* que devuelva una instancia de "Cursor" o sus
      subclases.

   blobopen(table, column, rowid, /, *, readonly=False, name='main')

      Abre una "Blob" para manejar un BLOB (Binary Large OBject)
      existente.

      Parámetros:
         * **table** (*str*) -- El nombre de la tabla donde el *blob*
           está ubicado.

         * **column** (*str*) -- El nombre de la columna donde el
           *blob* está ubicado.

         * **rowid** (*int*) -- The row id where the blob is located.

         * **readonly** (*bool*) -- Se define como "True" si el *blob*
           deberá ser abierto sin permisos de escritura. El valor por
           defecto es "False".

         * **name** (*str*) -- El nombre de la base de datos donde el
           *blob* está ubicado. El valor por defecto es ""main"".

      Muestra:
         **OperationalError** -- Cuando se intenta abrir un *blob* en
         una tabla "WITHOUT ROWID".

      Tipo del valor devuelto:
         Blob

      Nota:

        El tamaño de un *blob* no puede ser cambiado usando la clase
        "Blob". Usa la función de SQL "zeroblob" para crear un *blob*
        con un tamaño fijo.

      Added in version 3.11.

   commit()

      Confirma cualquier transacción pendiente en la base de datos. Si
      "autocommit" es "True" o no hay ninguna transacción abierta,
      este método no hace nada. Si "autocommit" es "False", se abre
      implícitamente una nueva transacción si se confirmó una
      transacción pendiente con este método.

   rollback()

      Revertir al inicio de cualquier transacción pendiente. Si
      "autocommit" es "True" o no hay ninguna transacción abierta,
      este método no hace nada. Si "autocommit" es "False", se abre
      implícitamente una nueva transacción si se revirtió una
      transacción pendiente con este método.

   close()

      Cierre la conexión a la base de datos. Si "autocommit" es
      "False", cualquier transacción pendiente se revierte
      implícitamente. Si "autocommit" es "True" o
      "LEGACY_TRANSACTION_CONTROL", no se ejecuta ningún control de
      transacción implícito. Asegúrese de ejecutar "commit()" antes de
      cerrar para evitar perder los cambios pendientes.

   execute(sql, parameters=(), /)

      Crea un nuevo objeto "Cursor" y llama "execute()" con los
      parámetros y el SQL dados. Retorna el nuevo objeto cursor.

   executemany(sql, parameters, /)

      Crea una nueva "Cursor" object and call "executemany()" con los
      parámetros y el SQL dados. Retorna el nuevo objeto cursor.

   executescript(sql_script, /)

      Crea una nueva "Cursor" object and call "executescript()" con el
      *sql_script* dado. Retorna el nuevo objeto cursor.

   create_function(name, narg, func, *, deterministic=False)

      Crea o elimina una función SQL definida por el usuario.

      Parámetros:
         * **name** (*str*) -- El nombre de la función SQL.

         * **narg** (*int*) -- El número de argumentos que la función
           SQL puede aceptar. Si es "-1", podrá entonces recibir
           cualquier cantidad de argumentos.

         * **func** (*callback* | None) -- Un *callable* que se llama
           cuando se invoca la función SQL. El invocable debe devolver
           a type natively supported by SQLite. Establézcalo en "None"
           para eliminar una función SQL existente.

         * **deterministic** (*bool*) -- Si se establece "True", la
           función SQL creada se marcará como determinista, lo cual
           permite a SQLite realizar optimizaciones adicionales.

      Distinto en la versión 3.8: Se agregó el parámetro
      *deterministic*.

      Ejemplo:

         >>> import hashlib
         >>> def md5sum(t):
         ...     return hashlib.md5(t).hexdigest()
         >>> con = sqlite3.connect(":memory:")
         >>> con.create_function("md5", 1, md5sum)
         >>> for row in con.execute("SELECT md5(?)", (b"foo",)):
         ...     print(row)
         ('acbd18db4cc2f85cedef654fccc4a4d8',)
         >>> con.close()

      Distinto en la versión 3.13: El uso de *name*, *narg* y *func*
      como argumentos de palabras clave ya no es recomendable. Estos
      parámetros pasarán a ser solo posicionales en Python 3.15.

   create_aggregate(name, n_arg, aggregate_class)

      Crea o elimina una función agregada SQL definida por el usuario.

      Parámetros:
         * **name** (*str*) -- El nombre de la función agregada SQL.

         * **n_arg** (*int*) -- El número de argumentos que la función
           agregada SQL puede aceptar. Si es "-1", podrá entonces
           recibir cualquier cantidad de argumentos.

         * **aggregate_class** (*class* | None) -- Una clase debe
           implementar los siguientes métodos: * "step()": Adiciona
           una fila al *aggregate*. * "finalize()": Retorna el
           resultado final del *aggregate* como un tipo soportado
           nativamente por SQLite. La cantidad de argumentos que el
           método "step()" puede aceptar, es controlado por *n_arg*.
           Establece "None" para eliminar una función agregada SQL
           existente.

      Ejemplo:

         class MySum:
             def __init__(self):
                 self.count = 0

             def step(self, value):
                 self.count += value

             def finalize(self):
                 return self.count

         con = sqlite3.connect(":memory:")
         con.create_aggregate("mysum", 1, MySum)
         cur = con.execute("CREATE TABLE test(i)")
         cur.execute("INSERT INTO test(i) VALUES(1)")
         cur.execute("INSERT INTO test(i) VALUES(2)")
         cur.execute("SELECT mysum(i) FROM test")
         print(cur.fetchone()[0])

         con.close()

      Distinto en la versión 3.13: El uso de *name*, *n_arg* y
      *aggregate_class* como argumentos de palabras clave ya no es
      recomendable. Estos parámetros pasarán a ser solo posicionales
      en Python 3.15.

   create_window_function(name, num_params, aggregate_class, /)

      Crea o elimina una función agregada de ventana definida por el
      usuario.

      Parámetros:
         * **name** (*str*) -- El nombre de la función agregada de
           ventana a ser creada o eliminada.

         * **num_params** (*int*) -- La cantidad de argumentos que la
           función agregada de ventana SQL acepta. Si es "-1", podrá
           entonces recibir cualquier cantidad de argumentos.

         * **aggregate_class** (*class* | None) -- Una clase debe
           implementar los siguientes métodos:  * "step()": Agrega una
           fila a la ventana actual. * "value()": Retorna el valor
           actual del *aggregate* . * "inverse()": Elimina una fila de
           la ventana actual. * "finalize()": Retorna el resultado
           final del *aggregate* como una un tipo soportado
           nativamente por SQLite. La cantidad de argumentos que los
           métodos "step()" y "value()" pueden aceptar son controlados
           por *num_params*. Establece "None" para eliminar una
           función agregada de ventana SQL.

      Muestra:
         **NotSupportedError** -- Si es usado con una versión de
         SQLite inferior a 3.25.0, la cual no soporte funciones
         agregadas de ventana.

      Added in version 3.11.

      Ejemplo:

         # Example taken from https://www.sqlite.org/windowfunctions.html#udfwinfunc
         class WindowSumInt:
             def __init__(self):
                 self.count = 0

             def step(self, value):
                 """Add a row to the current window."""
                 self.count += value

             def value(self):
                 """Return the current value of the aggregate."""
                 return self.count

             def inverse(self, value):
                 """Remove a row from the current window."""
                 self.count -= value

             def finalize(self):
                 """Return the final value of the aggregate.

                 Any clean-up actions should be placed here.
                 """
                 return self.count

         con = sqlite3.connect(":memory:")
         cur = con.execute("CREATE TABLE test(x, y)")
         values = [
             ("a", 4),
             ("b", 5),
             ("c", 3),
             ("d", 8),
             ("e", 1),
         ]
         cur.executemany("INSERT INTO test VALUES(?, ?)", values)
         con.create_window_function("sumint", 1, WindowSumInt)
         cur.execute("""
             SELECT x, sumint(y) OVER (
                 ORDER BY x ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
             ) AS sum_y
             FROM test ORDER BY x
         """)
         print(cur.fetchall())
         con.close()

   create_collation(name, callable, /)

      Crea una colación nombrada *name* usando la función *collating*
      *callable*. A *callable* se le pasan dos argumentos "string", y
      este debería retornar un "entero":

      * "1" si el primero es ordenado más alto que el segundo

      * "-1" si el primero es ordenado más pequeño que el segundo

      * "0" si están ordenados de manera igual

      El siguiente ejemplo muestra una ordenación de colación inversa:

         def collate_reverse(string1, string2):
             if string1 == string2:
                 return 0
             elif string1 < string2:
                 return 1
             else:
                 return -1

         con = sqlite3.connect(":memory:")
         con.create_collation("reverse", collate_reverse)

         cur = con.execute("CREATE TABLE test(x)")
         cur.executemany("INSERT INTO test(x) VALUES(?)", [("a",), ("b",)])
         cur.execute("SELECT x FROM test ORDER BY x COLLATE reverse")
         for row in cur:
             print(row)
         con.close()

      Elimina una función de colación al establecer el *callable* como
      "None".

      Distinto en la versión 3.11: El nombre de la colación puede
      contener cualquier caracter Unicode. Anteriormente, solamente
      caracteres ASCII eran permitidos.

   interrupt()

      Llame a este método desde un subproceso diferente para cancelar
      cualquier consulta que pueda estar ejecutándose en la conexión.
      Las consultas canceladas generarán un error "OperationalError".

   set_authorizer(authorizer_callback)

      Registre *callable* *authorizer_callback* para que se invoque
      cada vez que se intente acceder a una columna de una tabla en la
      base de datos. La devolución de llamada debe devolver uno de los
      siguientes: "SQLITE_OK", "SQLITE_DENY" o "SQLITE_IGNORE" para
      indicar cómo debe gestionar la biblioteca SQLite subyacente el
      acceso a la columna.

      El primer argumento del callback significa que tipo de operación
      será autorizada. El segundo y tercer argumento serán argumentos
      o "None" dependiendo del primer argumento. El cuarto argumento
      es el nombre de la base de datos ("main", "temp", etc.) si
      aplica. El quinto argumento es el nombre del disparador más
      interno o vista que es responsable por los intentos de acceso o
      "None" si este intento de acceso es directo desde el código SQL
      de entrada.

      Por favor consulte la documentación de SQLite sobre los posibles
      valores para el primer argumento y el significado del segundo y
      tercer argumento dependiendo del primero. Todas las constantes
      necesarias están disponibles en el módulo "sqlite3".

      Pasando "None" como *authorizer_callback* deshabilitará el
      autorizador.

      Distinto en la versión 3.11: Agregado soporte para deshabilitar
      el autorizador usando "None".

      Distinto en la versión 3.13: El uso de *authorizer_callback*
      como argumento de palabra clave ya no es recomendable. El
      parámetro pasará a ser solo posicional en Python 3.15.

   set_progress_handler(progress_handler, n)

      Registre *callable* *progress_handler* para que se invoque para
      cada instrucción *n* de la máquina virtual SQLite. Esto es útil
      si desea recibir llamadas de SQLite durante operaciones de larga
      duración, por ejemplo, para actualizar una GUI.

      Si se desea limpiar cualquier *progress_handler* instalado
      anteriormente, llame el método con "None" para
      *progress_handler*.

      Si se devuelve un valor distinto de cero desde la función del
      controlador, se finalizará la consulta que se está ejecutando
      actualmente y se generará una excepción "DatabaseError".

      Distinto en la versión 3.13: El uso de *progress_handler* como
      argumento de palabra clave ya no es recomendable. El parámetro
      pasará a ser solo posicional en Python 3.15.

   set_trace_callback(trace_callback)

      Registre *callable* *trace_callback* para que se invoque para
      cada declaración SQL que realmente ejecute el backend de SQLite.

      El único argumento pasado a la retrollamada es la declaración
      (como "str") que se está ejecutando. El valor de retorno de la
      retrollamada es ignorado. Tenga en cuenta que el backend no solo
      ejecuta declaraciones pasadas a los métodos "Cursor.execute()".
      Otras fuentes incluyen el transaction management del módulo
      "sqlite3" y la ejecución de disparadores definidos en la base de
      datos actual.

      Pasando "None" como *trace_callback* deshabilitará el *trace
      callback*.

      Nota:

        Las excepciones que se producen en la llamada de retorno no se
        propagan. Como ayuda para el desarrollo y la depuración,
        utilice "enable_callback_tracebacks()" para habilitar la
        impresión de *tracebacks* de las excepciones que se producen
        en la llamada de retorno.

      Added in version 3.3.

      Distinto en la versión 3.13: El uso de *trace_callback* como
      argumento de palabra clave ya no es recomendable. El parámetro
      pasará a ser solo posicional en Python 3.15.

   enable_load_extension(enabled, /)

      Habilita el motor de SQLite para cargar extensiones SQLite de
      bibliotecas compartidas si *enabled* se establece como "True";
      sino deshabilitará la carga de extensiones SQLite. Las
      extensiones SQLite pueden definir implementaciones de nuevas
      funciones, agregaciones, o tablas virtuales enteras. Una
      extensión bien conocida es *fulltext-search* distribuida con
      SQLite.

      Nota:

        El módulo "sqlite3" no está construido con soporte de
        extensión cargable de forma predeterminada, porque algunas
        plataformas (especialmente macOS) tienen bibliotecas SQLite
        que se compilan sin esta función. Para obtener soporte para
        extensiones cargables, debe pasar la opción "--enable-
        loadable-sqlite-extensions" a **configure**.

      Lanza un auditing event "sqlite3.enable_load_extension" con los
      argumentos "connection", "enabled".

      Added in version 3.2.

      Distinto en la versión 3.10: Agregado el evento de auditoría
      "sqlite3.enable_load_extension".

         con.enable_load_extension(True)

         # Load the fulltext search extension
         con.execute("select load_extension('./fts3.so')")

         # alternatively you can load the extension using an API call:
         # con.load_extension("./fts3.so")

         # disable extension loading again
         con.enable_load_extension(False)

         # example from SQLite wiki
         con.execute("CREATE VIRTUAL TABLE recipe USING fts3(name, ingredients)")
         con.executescript("""
             INSERT INTO recipe (name, ingredients) VALUES('broccoli stew', 'broccoli peppers cheese tomatoes');
             INSERT INTO recipe (name, ingredients) VALUES('pumpkin stew', 'pumpkin onions garlic celery');
             INSERT INTO recipe (name, ingredients) VALUES('broccoli pie', 'broccoli cheese onions flour');
             INSERT INTO recipe (name, ingredients) VALUES('pumpkin pie', 'pumpkin sugar flour butter');
             """)
         for row in con.execute("SELECT rowid, name, ingredients FROM recipe WHERE name MATCH 'pie'"):
             print(row)

   load_extension(path, /, *, entrypoint=None)

      Cargue una extensión SQLite desde una biblioteca compartida.
      Habilite la carga de extensiones con "enable_load_extension()"
      antes de llamar a este método.

      Parámetros:
         * **path** (*str*) -- La ruta a la extensión SQLite.

         * **entrypoint** (*str** | **None*) -- Nombre del punto de
           entrada. Si es "None" (el valor predeterminado), SQLite
           creará un nombre de punto de entrada propio; consulte la
           documentación de SQLite Loading an Extension para obtener
           más detalles.

      Lanza un auditing event "sqlite3.load_extension" con argumentos
      "connection", "path".

      Added in version 3.2.

      Distinto en la versión 3.10: Agregado el evento de auditoría
      "sqlite3.load_extension".

      Distinto en la versión 3.12: Se agregó el parámetro
      *entrypoint*.

   iterdump(*, filter=None)

      Retorna un *iterator* para volcar la base de datos en un texto
      de formato SQL. Es útil cuando guardamos una base de datos en
      memoria para una posterior restauración. Esta función provee las
      mismas capacidades que el comando ".dump" en el *shell*
      **sqlite3**.

      Parámetros:
         **filter** (*str** | **None*) -- Un patrón "LIKE" opcional
         para volcar objetos de la base de datos, p. ej., "prefix_%".
         Si se usa "None" (el valor predeterminado), se incluirán
         todos los objetos de la base de datos.

      Ejemplo:

         # Convert file example.db to SQL dump file dump.sql
         con = sqlite3.connect('example.db')
         with open('dump.sql', 'w') as f:
             for line in con.iterdump():
                 f.write('%s\n' % line)
         con.close()

      Ver también:

        Cómo manejar codificaciones de texto que no sean UTF-8

      Distinto en la versión 3.13: Se agregó el parámetro *filter*.

   backup(target, *, pages=-1, progress=None, name='main', sleep=0.250)

      Crea una copia de seguridad de la base de datos SQLite.

      Funciona incluso si la base de datos está siendo accedida por
      otros clientes al mismo tiempo sobre la misma conexión.

      Parámetros:
         * **target** (*Connection*) -- La conexión de la base de
           datos para guardar la copia de seguridad.

         * **pages** (*int*) -- Cantidad de páginas que serán copiadas
           cada vez. Si es menor o igual a "0", toda la base de datos
           será copiada en un solo paso. El valor por defecto es "-1".

         * **progress** (*callback* | None) -- Si se configura en
           *callable*, se invoca con tres argumentos enteros para cada
           iteración de copia de seguridad: el *status* de la última
           iteración, el *remaining* número de páginas que aún se
           deben copiar y el *total* número de páginas. El valor
           predeterminado es "None".

         * **name** (*str*) -- El nombre de la base de datos a ser
           guardada. O bien sea ""main"" (valor por defecto) para la
           base de datos *main*, ""temp"" para la base de datos
           temporal, o el nombre de una base de datos personalizada
           adjuntada usando la sentencia "ATTACH DATABASE".

         * **sleep** (*float*) -- Número de segundos a dormir entre
           sucesivos intentos para respaldar páginas restantes.

      Ejemplo 1, copiar una base de datos existente en otra:

         def progress(status, remaining, total):
             print(f'Copied {total-remaining} of {total} pages...')

         src = sqlite3.connect('example.db')
         dst = sqlite3.connect('backup.db')
         with dst:
             src.backup(dst, pages=1, progress=progress)
         dst.close()
         src.close()

      Ejemplo 2: copiar una base de datos existente en una copia
      transitoria:

         src = sqlite3.connect('example.db')
         dst = sqlite3.connect(':memory:')
         src.backup(dst)
         dst.close()
         src.close()

      Added in version 3.7.

      Ver también:

        Cómo manejar codificaciones de texto que no sean UTF-8

   getlimit(category, /)

      Obtiene el límite de tiempo de ejecución de una conexión.

      Parámetros:
         **category** (*int*) -- La SQLite limit category a ser
         consultada.

      Tipo del valor devuelto:
         int

      Muestra:
         **ProgrammingError** -- Si *category* no se reconoce por las
         capas inferiores de la biblioteca SQLite.

      Ejemplo, consulta el tamaño máximo de una sentencia SQL para la
      "Connection" "con" (el valor por defecto es 1000000000):

         >>> con.getlimit(sqlite3.SQLITE_LIMIT_SQL_LENGTH)
         1000000000

      Added in version 3.11.

   setlimit(category, limit, /)

      Establezca un límite de tiempo de ejecución de la conexión. Los
      intentos de aumentar un límite por encima de su límite superior
      estricto se truncan de forma silenciosa hasta el límite superior
      estricto. Independientemente de si se modificó o no el límite,
      se devuelve el valor anterior del límite.

      Parámetros:
         * **category** (*int*) -- La SQLite limit category a ser
           establecido.

         * **limit** (*int*) -- El valor del nuevo límite. Si es
           negativo, el límite actual no cambia.

      Tipo del valor devuelto:
         int

      Muestra:
         **ProgrammingError** -- Si *category* no se reconoce por las
         capas inferiores de la biblioteca SQLite.

      Por ejemplo, limite el número de bases de datos adjuntas a 1
      para la "Connection" "con" (el valor por defecto es 10):

         >>> con.setlimit(sqlite3.SQLITE_LIMIT_ATTACHED, 1)
         10
         >>> con.getlimit(sqlite3.SQLITE_LIMIT_ATTACHED)
         1

      Added in version 3.11.

   getconfig(op, /)

      Consultar una opción de configuración de conexión booleana.

      Parámetros:
         **op** (*int*) -- Un SQLITE_DBCONFIG code.

      Tipo del valor devuelto:
         bool

      Added in version 3.12.

   setconfig(op, enable=True, /)

      Establezca una opción de configuración de conexión booleana.

      Parámetros:
         * **op** (*int*) -- Un SQLITE_DBCONFIG code.

         * **enable** (*bool*) -- "True" si la opción de configuración
           debe estar habilitada (predeterminado); "False" si debe
           estar deshabilitada.

      Added in version 3.12.

   serialize(*, name='main')

      Serializa la base de datos en un objeto "bytes". Para un archivo
      ordinario de base de datos en disco, la serialización es solo
      una copia del archivo de disco. Para el caso de una base de
      datos en memoria o una base de datos "temp", la serialización es
      la misma secuencia de bytes que se escribiría en el disco si se
      hiciera una copia de seguridad de esa base de datos en el disco.

      Parámetros:
         **name** (*str*) -- El nombre de la base de datos a ser
         serializada. El valor por defecto es ""main"".

      Tipo del valor devuelto:
         bytes

      Nota:

        Este método solo está disponible si las capas internas de la
        biblioteca SQLite tienen la API *serialise*.

      Added in version 3.11.

   deserialize(data, /, *, name='main')

      Deserializa una base de datos "serializsda" en una clase
      "Connection". Este método hace que la conexión de base de datos
      se desconecte de la base de datos *name*, y la abre nuevamente
      como una base de datos en memoria, basada en la serialización
      contenida en *data*.

      Parámetros:
         * **data** (*bytes*) -- Una base de datos serializada.

         * **name** (*str*) -- El nombre de la base de datos a ser
           deserializada. El valor por defecto es ""main"".

      Muestra:
         * **OperationalError** -- Si la conexión con la base de datos
           está actualmente involucrada en una transacción de lectura
           o una operación de copia de seguridad.

         * **DatabaseError** -- Si *data* no contiene una base de
           datos SQLite válida.

         * **OverflowError** -- Si "len(data)" es más grande que
           "2**63 - 1".

      Nota:

        Este método solo está disponible si las capas internas de la
        biblioteca SQLite tienen la API *deserialize*.

      Added in version 3.11.

   autocommit

      Este atributo controla el comportamiento de las transacciones
      conforme a **PEP 249**. "autocommit" tiene tres valores
      permitidos:

      * "False": Seleccione un comportamiento de transacción
        compatible con **PEP 249**, lo que implica que "sqlite3"
        garantiza que una transacción esté siempre abierta. Utilice
        "commit()" y "rollback()" para cerrar transacciones.

        Este es el valor recomendado de "autocommit".

      * "True": Utilice autocommit mode de SQLite. "commit()" y
        "rollback()" no tienen efecto en este modo.

      * "LEGACY_TRANSACTION_CONTROL": Control de transacciones
        anterior a Python 3.12 (no compatible con **PEP 249**).
        Consulte "isolation_level" para obtener más detalles.

        Este es actualmente el valor predeterminado de "autocommit".

      Cambiar "autocommit" a "False" abrirá una nueva transacción y
      cambiarlo a "True" confirmará cualquier transacción pendiente.

      Consulte Control de transacciones mediante el atributo
      autocommit para obtener más detalles.

      Nota:

        El atributo "isolation_level" no tiene efecto a menos que
        "autocommit" sea "LEGACY_TRANSACTION_CONTROL".

      Added in version 3.12.

   in_transaction

      Este atributo de solo lectura corresponde al autocommit mode de
      SQLite de bajo nivel.

      "True" si una transacción está activa (existen cambios sin
      confirmar),``False`` en caso contrario.

      Added in version 3.2.

   isolation_level

      Controla el legacy transaction handling mode de "sqlite3". Si se
      configura en "None", las transacciones nunca se abren de forma
      implícita. Si se configura en uno de los valores ""DEFERRED"",
      ""IMMEDIATE"" o ""EXCLUSIVE"", correspondiente al SQLite
      transaction behaviour subyacente, se ejecuta implicit
      transaction management.

      Si no se sobreescribe por el parámetro *isolation_level* de
      "connect()", el valor predeterminado es """", que es un alias
      para ""DEFERRED"".

      Nota:

        Se recomienda utilizar "autocommit" para controlar el manejo
        de transacciones en lugar de "isolation_level".
        "isolation_level" no tiene efecto a menos que "autocommit" se
        configure en "LEGACY_TRANSACTION_CONTROL" (el valor
        predeterminado).

   row_factory

      El "row_factory" inicial para los objetos "Cursor" creados a
      partir de esta conexión. La asignación a este atributo no afecta
      al "row_factory" de los cursores existentes que pertenecen a
      esta conexión, solo a los nuevos. Es "None" de forma
      predeterminada, lo que significa que cada fila se devuelve como
      "tuple".

      Consulte Cómo crear y utilizar fábricas de filas para obtener
      más detalles.

      Distinto en la versión 3.14.6: Deleting the "row_factory"
      attribute is no longer allowed.

   text_factory

      Un *callable* que acepta un parámetro "bytes" y devuelve una
      representación de texto del mismo. El objeto invocable se invoca
      para valores SQLite con el tipo de datos "TEXT". De manera
      predeterminada, este atributo está configurado en "str".

      Consulte Cómo manejar codificaciones de texto que no sean UTF-8
      para obtener más detalles.

      Distinto en la versión 3.14.6: Deleting the "text_factory"
      attribute is no longer allowed.

   total_changes

      Retorna el número total de filas de la base de datos que han
      sido modificadas, insertadas o borradas desde que la conexión a
      la base de datos fue abierta.

### Objetos cursor

   Un objeto "Cursor" representa un database cursor que se utiliza
   para ejecutar sentencias SQL y administrar el contexto de una
   operación de búsqueda. Los cursores son creados usando
   "Connection.cursor()", o por usar alguno de los connection shortcut
   methods.

   Los objetos cursores son *iterators*, lo que significa que si
   "execute()" una consulta "SELECT", simplemente podrás iterar sobre
   el cursor para obtener las filas resultantes:

      for row in cur.execute("SELECT t FROM data"):
          print(row)

class sqlite3.Cursor

   Una instancia "Cursor" tiene los siguientes atributos y métodos.

   execute(sql, parameters=(), /)

      Ejecuta una única declaración SQL, vinculando opcionalmente
      valores de Python mediante placeholders.

      Parámetros:
         * **sql** (*str*) -- Una sola declaración SQL.

         * **parameters** ("dict" | *sequence*) -- Valores de Python
           para vincular a marcadores de posición en *sql*. Un "dict"
           si se utilizan marcadores de posición con nombre. Un
           *sequence* si se utilizan marcadores de posición sin
           nombre. Consulte Cómo usar marcadores de posición para
           vincular valores en consultas SQL.

      Muestra:
         **ProgrammingError** -- When *sql* contains more than one SQL
         statement. When named placeholders are used and *parameters*
         is a sequence instead of a "dict".

      Si "autocommit" es "LEGACY_TRANSACTION_CONTROL",
      "isolation_level" no es "None", *sql* es una declaración
      "INSERT", "UPDATE", "DELETE" o "REPLACE" y no hay ninguna
      transacción abierta, se abre implícitamente una transacción
      antes de ejecutar *sql*.

      Distinto en la versión 3.14: "ProgrammingError" is emitted if
      named placeholders are used and *parameters* is a sequence
      instead of a "dict".

      Utilice "executescript()" para ejecutar múltiples declaraciones
      SQL.

   executemany(sql, parameters, /)

      Para cada elemento en *parameters*, ejecute repetidamente la
      instrucción SQL parameterized DML (lenguaje de manipulación de
      datos) *sql*.

      Utiliza el mismo manejo de transacciones implícitas que
      "execute()".

      Parámetros:
         * **sql** (*str*) -- Una sola declaración DML de SQL.

         * **parameters** (*iterable*) -- Un *iterable* de parámetros
           para vincular con los marcadores de posición en *sql*.
           Consulte Cómo usar marcadores de posición para vincular
           valores en consultas SQL.

      Muestra:
         **ProgrammingError** -- When *sql* contains more than one SQL
         statement or is not a DML statement, When named placeholders
         are used and the items in *parameters* are sequences instead
         of "dict"s.

      Ejemplo:

         rows = [
             ("row1",),
             ("row2",),
         ]
         # cur is an sqlite3.Cursor object
         cur.executemany("INSERT INTO data VALUES(?)", rows)

      Nota:

        Se descartan todas las filas resultantes, incluidas las
        declaraciones DML con RETURNING clauses.

      Distinto en la versión 3.14: "ProgrammingError" is emitted if
      named placeholders are used and the items in *parameters* are
      sequences instead of "dict"s.

   executescript(sql_script, /)

      Ejecute las sentencias SQL en *sql_script*. Si "autocommit" es
      "LEGACY_TRANSACTION_CONTROL" y hay una transacción pendiente,
      primero se ejecuta una sentencia "COMMIT" implícita. No se
      realiza ningún otro control de transacción implícito; cualquier
      control de transacción debe agregarse a *sql_script*.

      *sql_script* debe ser una instancia de "string".

      Ejemplo:

         # cur is an sqlite3.Cursor object
         cur.executescript("""
             BEGIN;
             CREATE TABLE person(firstname, lastname, age);
             CREATE TABLE book(title, author, published);
             CREATE TABLE publisher(name, address);
             COMMIT;
         """)

   fetchone()

      Si "row_factory" es "None", devuelve el siguiente conjunto de
      resultados de consulta de fila como "tuple". De lo contrario,
      páselo a la fábrica de filas y devuelve su resultado. Devuelve
      "None" si no hay más datos disponibles.

   fetchmany(size=cursor.arraysize)

      Retorna el siguiente conjunto de filas del resultado de una
      consulta como una "list". Una lista vacía será retornada cuando
      no hay más filas disponibles.

      El número de filas que se van a obtener por llamada se
      especifica mediante el parámetro *size*. Si *size* no es
      informado, entonces "arraysize" determinará el número de filas
      que se van a recuperar. Si hay menos filas *size* disponibles,
      se retornan tantas filas como estén disponibles.

      Nótese que hay consideraciones de desempeño involucradas con el
      parámetro *size*. Para un optimo desempeño, es usualmente mejor
      usar el atributo *arraysize*. Si el parámetro *size* es usado,
      entonces es mejor retener el mismo valor de una llamada
      "fetchmany()" a la siguiente.

      Distinto en la versión 3.14.1: Negative *size* values are
      rejected by raising "ValueError".

   fetchall()

      Retorna todas las filas (restantes) de un resultado de consulta
      como "list". Retorna una lista vacía si no hay filas
      disponibles. Tenga en cuenta que el atributo "arraysize" puede
      afectar al rendimiento de esta operación.

   close()

      Cierra el cursor ahora (en lugar que cuando "__del__" es
      llamado)

      El cursor no será usable de este punto en adelante; una
      excepción "ProgrammingError" será lanzada si se intenta
      cualquier operación con el cursor.

   setinputsizes(sizes, /)

      Requerido por la DB-API. No hace nada en "sqlite3".

   setoutputsize(size, column=None, /)

      Requerido por la DB-API. No hace nada en "sqlite3".

   arraysize

      Atributo de lectura/escritura que controla el número de filas
      retornadas por "fetchmany()". El valor por defecto es 1, lo cual
      significa que una única fila será obtenida por llamada.

      Distinto en la versión 3.14.1: Negative values are rejected by
      raising "ValueError".

   connection

      Este atributo de solo lectura que provee la "Connection" de la
      base de datos SQLite pertenece al cursor. Un objeto "Cursor"
      creado llamando a "con.cursor()" tendrá un atributo "connection"
      que hace referencia a *con*:

         >>> con = sqlite3.connect(":memory:")
         >>> cur = con.cursor()
         >>> cur.connection == con
         True
         >>> con.close()

   description

      Este atributo de solo lectura provee el nombre de las columnas
      de la última consulta. Para seguir siendo compatible con la API
      de base de datos de Python, retornará una tupla de 7 elementos
      para cada columna donde los últimos seis elementos de cada tupla
      son "Ninguno".

      También es configurado para sentencias "SELECT" sin ninguna fila
      coincidente.

   lastrowid

      Atributo de solo lectura que proporciona el identificador de
      fila de la última insertada. Solo se actualiza después de que
      las sentencias "INSERT" o "REPLACE" hayan sido exitosas usando
      el método "execute()". Para otras instrucciones, después de
      "executemany()" o "executescript()", o si se produjo un error en
      la inserción, el valor de "lastrowid" se deja sin cambios. El
      valor inicial de "lastrowid" es "None".

      Nota:

        Las inserciones en tablas "WITHOUT ROWID" no se registran.

      Distinto en la versión 3.6: Se agregó soporte para sentencias
      "REPLACE".

   rowcount

      Atributo de solo lectura que proporciona la cantidad de filas
      modificadas para las instrucciones "INSERT", "UPDATE", "DELETE"
      y "REPLACE"; es "-1" para otras instrucciones, incluidas las
      consultas CTE (Common Table Expression) . Solo se actualiza
      mediante los métodos "execute()" y "executemany()", después de
      que la instrucción se haya ejecutado hasta su finalización. Esto
      significa que se deben obtener todas las filas resultantes para
      que se actualice "rowcount".

   row_factory

      Controla cómo se representa una fila obtenida de este "Cursor".
      Si es "None", una fila se representa como "tuple". Se puede
      configurar como "sqlite3.Row" incluido; o como *callable* que
      acepta dos argumentos, un objeto "Cursor" y el "tuple" de
      valores de fila, y devuelve un objeto personalizado que
      representa una fila de SQLite.

      El valor predeterminado es el valor que se estableció en
      "Connection.row_factory" cuando se creó "Cursor". La asignación
      a este atributo no afecta a "Connection.row_factory" de la
      conexión principal.

      Consulte Cómo crear y utilizar fábricas de filas para obtener
      más detalles.

      Distinto en la versión 3.14.6: Deleting the "row_factory"
      attribute is no longer allowed.

### Objetos fila (*Row*)

class sqlite3.Row

   Una instancia de "Row" sirve como una instancia "row_factory"
   altamente optimizada para objetos "Connection". Admite iteración,
   pruebas de igualdad, acceso a "len()" y *mapping* por nombre de
   columna e índice.

   Dos objetos "Row" se consideran iguales si tienen nombres de
   columna y valores idénticos.

   Consulte Cómo crear y utilizar fábricas de filas para obtener más
   detalles.

   keys()

      Este método retorna una "list" con los nombre de columnas como
      "strings". Inmediatamente después de una consulta, es el primer
      miembro de cada tupla en "Cursor.description".

   Distinto en la versión 3.5: Agrega soporte para segmentación.

### Objetos fila (*Row*)

class sqlite3.Blob

   Added in version 3.11.

   Una instancia "Blob" es un *file-like object* que puede leer y
   escribir datos en un SQLite BLOB (Binary Large OBject). Llame a
   "len(blob)" para obtener el tamaño (número de bytes) del blob. Use
   índices y *slices* para obtener acceso directo a los datos del
   blob.

   Use "Blob" como *context manager* para asegurarse de que el
   identificador de blob se cierra después de su uso.

      con = sqlite3.connect(":memory:")
      con.execute("CREATE TABLE test(blob_col blob)")
      con.execute("INSERT INTO test(blob_col) VALUES(zeroblob(13))")

      # Write to our blob, using two write operations:
      with con.blobopen("test", "blob_col", 1) as blob:
          blob.write(b"hello, ")
          blob.write(b"world.")
          # Modify the first and last bytes of our blob
          blob[0] = ord("H")
          blob[-1] = ord("!")

      # Read the contents of our blob
      with con.blobopen("test", "blob_col", 1) as blob:
          greeting = blob.read()

      print(greeting)  # outputs "b'Hello, world!'"
      con.close()

   close()

      Cierra el *blob*.

      El cursor no será usable de este punto en adelante; una
      excepción "Error" (o subclase) será lanzada si se intenta
      cualquier operación con el cursor.

   read(length=-1, /)

      Leer bytes *length* de datos del blob en la posición de
      desplazamiento actual. Si se alcanza el final del blob, se
      devolverán los datos hasta EOF (End of File). Cuando *length* no
      se especifica, o es negativo, "read()" se leerá hasta el final
      del blob.

   write(data, /)

      Escriba *data* en el blob en el desplazamiento actual. Esta
      función no puede cambiar la longitud del blob. Escribir más allá
      del final del blob generará un "ValueError".

   tell()

      Devolver la posición de acceso actual del blob.

   seek(offset, origin=os.SEEK_SET, /)

      Establezca la posición de acceso actual del blob en *offset*. El
      argumento *origin* tiene como valor predeterminado "os.SEEK_SET"
      (posición absoluta del blob). Otros valores para *origin* son
      "os.SEEK_CUR" (búsqueda relativa a la posición actual) y
      "os.SEEK_END" (búsqueda relativa al final del blob).

### Objetos PrepareProtocol

class sqlite3.PrepareProtocol

   El único propósito del tipo *PrepareProtocol* es actuar como un
   protocolo de adaptación de estilo **PEP 246** para objetos que
   pueden adapt themselves a native SQLite types.

### Excepciones

La jerarquía de excepciones está definida por DB-API 2.0 (**PEP
249**).

exception sqlite3.Warning

   Esta excepción no se genera actualmente en el módulo "sqlite3",
   pero puede ser provocada por aplicaciones que usan :mod:!sqlite3`,
   por ejemplo, si una función definida por el usuario trunca datos
   durante la inserción. "Warning" es una subclase de "Exception".

exception sqlite3.Error

   La clase base de las otras excepciones de este módulo. Use esto
   para detectar todos los errores con una sola instrucción
   "except".``Error`` is una subclase de "Exception".

   Si la excepción se originó dentro de la biblioteca SQLite, se
   agregan los siguientes dos atributos a la excepción:

   sqlite_errorcode

      El código de error numérico de SQLite API

      Added in version 3.11.

   sqlite_errorname

      El nombre simbólico del código de error numérico de SQLite API

      Added in version 3.11.

exception sqlite3.InterfaceError

   Excepción lanzada por el uso indebido de la API de SQLite C de bajo
   nivel. En otras palabras, si se lanza esta excepción, probablemente
   indica un error en el módulo "sqlite3". "InterfaceError" es una
   subclase de "Error".

exception sqlite3.DatabaseError

   Excepción lanzada por errores relacionados con la base de datos.
   Esto sirve como excepción base para varios tipos de errores de base
   de datos. Solo se genera implícitamente a través de las subclases
   especializadas. "DatabaseError" es una subclase de "Error".

exception sqlite3.DataError

   Excepción lanzada por errores causados por problemas con los datos
   procesados, como valores numéricos fuera de rango y cadenas de
   caracteres demasiado largas. "DataError" es una subclase de
   "DatabaseError".

exception sqlite3.OperationalError

   Excepción lanzada por errores que están relacionados con el
   funcionamiento de la base de datos y no necesariamente bajo el
   control del programador. Por ejemplo, no se encuentra la ruta de la
   base de datos o no se pudo procesar una transacción.
   "OperationalError" es una subclase de "DatabaseError".

exception sqlite3.IntegrityError

   Excepción lanzada cuando la integridad de la base de datos es
   afectada, por ejemplo la comprobación de una llave foránea falla.
   Es una subclase de "DatabaseError".

exception sqlite3.InternalError

   Se genera una excepción cuando SQLite encuentra un error interno.
   Si se genera esto, puede indicar que hay un problema con la
   biblioteca SQLite en tiempo de ejecución. "InternalError" es una
   subclase de "DatabaseError".

exception sqlite3.ProgrammingError

   Excepción lanzada por errores de programación de la API de
   "sqlite3", por ejemplo, proporcionar el número incorrecto de
   enlaces a una consulta, o intentar operar en una "Connection"
   cerrada. "ProgrammingError" es una subclase de "DatabaseError".

exception sqlite3.NotSupportedError

   Excepción lanzada en caso que la biblioteca SQLite subyacente no
   admita un método o una API de base de datos. Por ejemplo,
   establecer *determinista* como "Verdadero" en "create_function()",
   si la biblioteca SQLite subyacente no admite funciones
   *deterministic*. "NotSupportedError" es una subclase de
   "DatabaseError".

### SQLite y tipos de Python

SQLite soporta de forma nativa los siguientes tipos: "NULL",
"INTEGER", "REAL", "TEXT", "BLOB".

Los siguientes tipos de Python se pueden enviar a SQLite sin problema
alguno:

+---------------------------------+---------------+
| Tipo de Python                  | Tipo de       |
|                                 | SQLite        |
|=================================|===============|
## | "None"                          | "NULL"        |

## | "int"                           | "INTEGER"     |

## | "float"                         | "REAL"        |

## | "str"                           | "TEXT"        |

## | "bytes"                         | "BLOB"        |

De esta forma es como los tipos de SQLite son convertidos a tipos de
Python por defecto:

+---------------+------------------------------------------------+
| Tipo de       | Tipo de Python                                 |
| SQLite        |                                                |
|===============|================================================|
## | "NULL"        | "None"                                         |

## | "INTEGER"     | "int"                                          |

## | "REAL"        | "float"                                        |

## | "TEXT"        | depende de "text_factory", "str" por defecto   |

## | "BLOB"        | "bytes"                                        |

El sistema de tipos del módulo "sqlite3" es extensible en dos formas:
se puede almacenar tipos de Python adicionales en una base de datos
SQLite vía a objetos adaptadores, y se puede permitir que "sqlite3"
convierta tipos SQLite a diferentes tipos de Python vía converters.

### Adaptadores y convertidores predeterminados (en desuso)

Nota:

  Los adaptadores y convertidores predeterminados están obsoletos a
  partir de Python 3.12. En su lugar, utilice Ejemplos para
  adaptadores y convertidores y adáptelos a sus necesidades.

Los adaptadores y convertidores predeterminados obsoletos consisten
en:

* Un adaptador para objetos "datetime.date" a "strings" en formato ISO
  8601.

* Un adaptador para objetos "datetime.datetime" a cadenas en formato
  ISO 8601.

* Un convertidor de tipos "fecha" declared a objetos "datetime.date".

* Un convertidor de tipos de "marca de tiempo" declarados a objetos
  "datetime.datetime". Las partes fraccionarias se truncarán a 6
  dígitos (precisión de microsegundos).

Nota:

  El convertidor por defecto "timestamp" ignora las compensaciones UTC
  en la base de datos y siempre devuelve un objeto "datetime.datetime"
  *naive*. Para conservar las compensaciones UTC en las marcas de
  tiempo, deje los convertidores deshabilitados o registre un
  convertidor que reconozca la compensación con
  "register_converter()".

Obsoleto desde la versión 3.12.

### Interfaz de línea de comandos

El módulo "sqlite3" se puede invocar como un script, utilizando el
modificador "-m" del intérprete, para proporcionar un shell SQLite
simple. La firma del argumento es la siguiente:

   python -m sqlite3 [-h] [-v] [filename] [sql]

Escriba ".quit" o CTRL-D para salir del shell.

-h, --help

   Ayuda de la CLI de impresión.

-v, --version

   Imprima la versión de la biblioteca SQLite subyacente.

Added in version 3.12.

## Guías prácticas

### Cómo usar marcadores de posición para vincular valores en consultas SQL

Las operaciones SQL suelen necesitar utilizar valores de variables de
Python. Sin embargo, tenga cuidado al utilizar las operaciones de
cadena de Python para ensamblar consultas, ya que son vulnerables a
SQL injection attacks. Por ejemplo, un atacante puede simplemente
cerrar la comilla simple e inyectar "OR TRUE" para seleccionar todas
las filas:

   >>> # Never do this -- insecure!
   >>> symbol = input()
   ' OR TRUE; --
   >>> sql = "SELECT * FROM stocks WHERE symbol = '%s'" % symbol
   >>> print(sql)
   SELECT * FROM stocks WHERE symbol = '' OR TRUE; --'
   >>> cur.execute(sql)

En su lugar, utilice la sustitución de parámetros de DB-API. Para
insertar una variable en una cadena de consulta, utilice un marcador
de posición en la cadena y sustituya los valores reales en la consulta
proporcionándolos como un "tuple" de valores al segundo argumento del
método "execute()" del cursor.

Una sentencia SQL puede utilizar uno de dos tipos de marcadores de
posición: signos de interrogación (estilo qmark) o marcadores de
posición con nombre (estilo con nombre). Para el estilo qmark,
*parameters* debe ser un *sequence* cuya longitud debe coincidir con
el número de marcadores de posición, o se genera un
"ProgrammingError". Para el estilo con nombre, *parameters* debe ser
una instancia de un "dict" (o una subclase), que debe contener claves
para todos los parámetros con nombre; se ignoran todos los elementos
adicionales. A continuación, se muestra un ejemplo de ambos estilos:

   con = sqlite3.connect(":memory:")
   cur = con.execute("CREATE TABLE lang(name, first_appeared)")

   # This is the named style used with executemany():
   data = (
       {"name": "C", "year": 1972},
       {"name": "Fortran", "year": 1957},
       {"name": "Python", "year": 1991},
       {"name": "Go", "year": 2009},
   )
   cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)

   # This is the qmark style used in a SELECT query:
   params = (1972,)
   cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
   print(cur.fetchall())
   con.close()

Nota:

  Los marcadores de posición numéricos **PEP 249** son compatibles con
  *not*. Si se utilizan, se interpretarán como marcadores de posición
  con nombre.

### Cómo adaptar tipos de Python personalizados a valores de SQLite

SQLite solo admite un conjunto limitado de tipos de datos de forma
nativa. Para almacenar tipos personalizados de Python en bases de
datos SQLite, adáptelos a uno de los tipos Python que SQLite entiende
de forma nativa.

Hay dos formas de adaptar los objetos de Python a los tipos de SQLite:
dejar que su objeto se adapte a sí mismo o usar un *adapter callable*.
Este último prevalecerá sobre el primero. Para una biblioteca que
exporta un tipo personalizado, puede tener sentido permitir que ese
tipo se adapte. Como desarrollador de aplicaciones, puede tener más
sentido tomar el control directo registrando funciones de adaptador
personalizadas.

#### Cómo escribir objetos adaptables

Supongamos que tenemos una clase "Point" que representa un par de
coordenadas, "x" e "y", en un sistema de coordenadas cartesianas. El
par de coordenadas se almacenará como una cadena de texto en la base
de datos, utilizando un punto y coma para separar las coordenadas.
Esto se puede implementar agregando un método "__conform__(self,
protocol)" que retorna el valor adaptado. El objeto pasado a
*protocolo* será de tipo "PrepareProtocol".

   class Point:
       def __init__(self, x, y):
           self.x, self.y = x, y

       def __conform__(self, protocol):
           if protocol is sqlite3.PrepareProtocol:
               return f"{self.x};{self.y}"

   con = sqlite3.connect(":memory:")
   cur = con.cursor()

   cur.execute("SELECT ?", (Point(4.0, -3.2),))
   print(cur.fetchone()[0])
   con.close()

#### Como registrar un adaptador invocable

La otra posibilidad es crear una función que convierta el objeto
Python a un tipo compatible de SQLite. Esta función puede de esta
forma ser registrada usando un "register_adapter()".

   class Point:
       def __init__(self, x, y):
           self.x, self.y = x, y

   def adapt_point(point):
       return f"{point.x};{point.y}"

   sqlite3.register_adapter(Point, adapt_point)

   con = sqlite3.connect(":memory:")
   cur = con.cursor()

   cur.execute("SELECT ?", (Point(1.0, 2.5),))
   print(cur.fetchone()[0])
   con.close()

### Como convertir valores SQLite a tipos de Python personalizados

Escribir un adaptador le permite convertir *de* tipos personalizados
de Python *a* valores SQLite. Para poder convertir *de* valores SQLite
*a* tipos personalizados de Python, usamos *convertidores*.

Regresemos a la clase "Point". Almacenamos las coordenadas x y y
separadas por punto y coma como una cadena de caracteres en SQLite.

Primero, se define una función de conversión que acepta la cadena de
texto como un parámetro y construya un objeto "Point" de ahí.

Nota:

  Las funciones de conversión **siempre** son llamadas con un objeto
  "bytes", no importa bajo qué tipo de dato se envió el valor a
  SQLite.

   def convert_point(s):
       x, y = map(float, s.split(b";"))
       return Point(x, y)

Ahora necesitamos decirle a "sqlite3" cuando debería convertir un
valor dado SQLite. Esto se hace cuando se conecta a una base de datos,
utilizando el parámetro *detect_types* de "connect()". Hay tres
opciones:

* Implícito: establece *detect_types* para que "PARSE_DECLTYPES"

* Explícito: establece *detect_types* para que "PARSE_COLNAMES"

* Ambos: establece *detect_types* para "sqlite3.PARSE_DECLTYPES |
  sqlite3.PARSE_COLNAMES". Los nombres de columna tienen prioridad
  sobre los tipos declarados.

El siguiente ejemplo ilustra ambos enfoques:

   class Point:
       def __init__(self, x, y):
           self.x, self.y = x, y

       def __repr__(self):
           return f"Point({self.x}, {self.y})"

   def adapt_point(point):
       return f"{point.x};{point.y}"

   def convert_point(s):
       x, y = list(map(float, s.split(b";")))
       return Point(x, y)

   # Register the adapter and converter
   sqlite3.register_adapter(Point, adapt_point)
   sqlite3.register_converter("point", convert_point)

   # 1) Parse using declared types
   p = Point(4.0, -3.2)
   con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
   cur = con.execute("CREATE TABLE test(p point)")

   cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
   cur.execute("SELECT p FROM test")
   print("with declared types:", cur.fetchone()[0])
   cur.close()
   con.close()

   # 2) Parse using column names
   con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
   cur = con.execute("CREATE TABLE test(p)")

   cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
   cur.execute('SELECT p AS "p [point]" FROM test')
   print("with column names:", cur.fetchone()[0])
   cur.close()
   con.close()

### Ejemplos para adaptadores y convertidores

En esta sección se muestran ejemplos para adaptadores y convertidores
comunes.

   import datetime as dt
   import sqlite3

   def adapt_date_iso(val):
       """Adapt datetime.date to ISO 8601 date."""
       return val.isoformat()

   def adapt_datetime_iso(val):
       """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
       return val.replace(tzinfo=None).isoformat()

   def adapt_datetime_epoch(val):
       """Adapt datetime.datetime to Unix timestamp."""
       return int(val.timestamp())

   sqlite3.register_adapter(dt.date, adapt_date_iso)
   sqlite3.register_adapter(dt.datetime, adapt_datetime_iso)
   sqlite3.register_adapter(dt.datetime, adapt_datetime_epoch)

   def convert_date(val):
       """Convert ISO 8601 date to datetime.date object."""
       return dt.date.fromisoformat(val.decode())

   def convert_datetime(val):
       """Convert ISO 8601 datetime to datetime.datetime object."""
       return dt.datetime.fromisoformat(val.decode())

   def convert_timestamp(val):
       """Convert Unix epoch timestamp to datetime.datetime object."""
       return dt.datetime.fromtimestamp(int(val))

   sqlite3.register_converter("date", convert_date)
   sqlite3.register_converter("datetime", convert_datetime)
   sqlite3.register_converter("timestamp", convert_timestamp)

### Cómo utilizar los métodos de acceso directo de conexión

Usando los métodos "execute()", "executemany()", y "executescript()"
de la clase "Connection", su código se puede escribir de manera más
concisa porque no tiene que crear los (a menudo superfluo) objetos
"Cursor" explícitamente. Por el contrario, los objetos "Cursor" son
creados implícitamente y esos métodos de acceso directo retornarán
objetos cursores. De esta forma, se puede ejecutar una sentencia
"SELECT" e iterar sobre ella directamente usando un simple llamado
sobre el objeto de clase "Connection".

   # Create and fill the table.
   con = sqlite3.connect(":memory:")
   con.execute("CREATE TABLE lang(name, first_appeared)")
   data = [
       ("C++", 1985),
       ("Objective-C", 1984),
   ]
   con.executemany("INSERT INTO lang(name, first_appeared) VALUES(?, ?)", data)

   # Print the table contents
   for row in con.execute("SELECT name, first_appeared FROM lang"):
       print(row)

   print("I just deleted", con.execute("DELETE FROM lang").rowcount, "rows")

   # close() is not a shortcut method and it's not called automatically;
   # the connection object should be closed manually
   con.close()

### Como usar la conexión con un administrador de contexto

Un objeto "Connection" se puede utilizar como un administrador de
contexto que confirma o revierte automáticamente las transacciones
abiertas al salir del cuerpo del administrador de contexto. Si el
cuerpo de la instrucción "with" finaliza sin excepciones, la
transacción se confirma. Si esta confirmación falla, o si el cuerpo de
la instrucción "with" genera una excepción no detectada, la
transacción se revierte. Si "autocommit" es "False", se abre
implícitamente una nueva transacción después de confirmar o revertir.

Si no hay ninguna transacción abierta al salir del cuerpo de la
declaración "with", o si "autocommit" es "True", el administrador de
contexto no hace nada.

Nota:

  El administrador de contexto no abre implícitamente una nueva
  transacción ni cierra la conexión. Si necesita un administrador de
  contexto de cierre, considere usar "contextlib.closing()".

   con = sqlite3.connect(":memory:")
   con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")

   # Successful, con.commit() is called automatically afterwards
   with con:
       con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))

   # con.rollback() is called after the with block finishes with an exception,
   # the exception is still raised and must be caught
   try:
       with con:
           con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))
   except sqlite3.IntegrityError:
       print("couldn't add Python twice")

   # Connection object used as context manager only commits or rollbacks transactions,
   # so the connection object should be closed manually
   con.close()

### Como trabajar con URIs SQLite

Algunos trucos útiles de URI incluyen:

* Abra una base de datos en modo de solo lectura:

   >>> con = sqlite3.connect("file:tutorial.db?mode=ro", uri=True)
   >>> con.execute("CREATE TABLE readonly(data)")
   Traceback (most recent call last):
   OperationalError: attempt to write a readonly database
   >>> con.close()

* No cree implícitamente un nuevo archivo de base de datos si aún no
  existe; esto lanzará un "OperationalError" si no puede crear un
  nuevo archivo:

   >>> con = sqlite3.connect("file:nosuchdb.db?mode=rw", uri=True)
   Traceback (most recent call last):
   OperationalError: unable to open database file

* Crea un nombre compartido sobre una base de datos en memoria:

   db = "file:mem1?mode=memory&cache=shared"
   con1 = sqlite3.connect(db, uri=True)
   con2 = sqlite3.connect(db, uri=True)
   with con1:
       con1.execute("CREATE TABLE shared(data)")
       con1.execute("INSERT INTO shared VALUES(28)")
   res = con2.execute("SELECT data FROM shared")
   assert res.fetchone() == (28,)

   con1.close()
   con2.close()

Más información sobre esta característica, incluyendo una lista de
opciones reconocidas, pueden encontrarse en SQLite URI documentation.

### Cómo crear y utilizar fábricas de filas

De forma predeterminada, "sqlite3" representa cada fila como "tuple".
Si "tuple" no se adapta a sus necesidades, puede utilizar la clase
"sqlite3.Row" o una "row_factory" personalizada.

Si bien "row_factory" existe como atributo tanto en "Cursor" como en
"Connection", se recomienda configurar "Connection.row_factory", de
modo que todos los cursores creados a partir de la conexión utilicen
la misma fábrica de filas.

"Row" proporciona acceso indexado y sin distinción entre mayúsculas y
minúsculas a las columnas, con una sobrecarga de memoria y un impacto
en el rendimiento mínimos en comparación con "tuple". Para utilizar
"Row" como una fábrica de filas, asígnelo al atributo "row_factory":

   >>> con = sqlite3.connect(":memory:")
   >>> con.row_factory = sqlite3.Row

Las consultas ahora devuelven objetos "Row":

   >>> res = con.execute("SELECT 'Earth' AS name, 6378 AS radius")
   >>> row = res.fetchone()
   >>> row.keys()
   ['name', 'radius']
   >>> row[0]         # Access by index.
   'Earth'
   >>> row["name"]    # Access by name.
   'Earth'
   >>> row["RADIUS"]  # Column names are case-insensitive.
   6378
   >>> con.close()

Nota:

  La cláusula "FROM" se puede omitir en la declaración "SELECT", como
  en el ejemplo anterior. En tales casos, SQLite devuelve una sola
  fila con columnas definidas por expresiones, por ejemplo, literales,
  con los alias indicados "expr AS alias".

Puede crear un "row_factory" personalizado que devuelva cada fila como
un "dict", con nombres de columnas asignados a valores:

   def dict_factory(cursor, row):
       fields = [column[0] for column in cursor.description]
       return {key: value for key, value in zip(fields, row)}

Al usarlo, las consultas ahora devuelven un "dict" en lugar de un
"tuple":

   >>> con = sqlite3.connect(":memory:")
   >>> con.row_factory = dict_factory
   >>> for row in con.execute("SELECT 1 AS a, 2 AS b"):
   ...     print(row)
   {'a': 1, 'b': 2}
   >>> con.close()

La siguiente fábrica de filas devuelve un *named tuple*:

   from collections import namedtuple

   def namedtuple_factory(cursor, row):
       fields = [column[0] for column in cursor.description]
       cls = namedtuple("Row", fields)
       return cls._make(row)

"namedtuple_factory()" se puede utilizar de la siguiente manera:

   >>> con = sqlite3.connect(":memory:")
   >>> con.row_factory = namedtuple_factory
   >>> cur = con.execute("SELECT 1 AS a, 2 AS b")
   >>> row = cur.fetchone()
   >>> row
   Row(a=1, b=2)
   >>> row[0]  # Indexed access.
   1
   >>> row.b   # Attribute access.
   2
   >>> con.close()

Con algunos ajustes, la receta anterior se puede adaptar para utilizar
un "dataclass", o cualquier otra clase personalizada, en lugar de un
"namedtuple".

### Cómo manejar codificaciones de texto que no sean UTF-8

De forma predeterminada, "sqlite3" utiliza "str" para adaptar los
valores de SQLite con el tipo de datos "TEXT". Esto funciona bien para
texto codificado en UTF-8, pero puede fallar para otras codificaciones
y UTF-8 no válido. Puede utilizar un "text_factory" personalizado para
manejar estos casos.

Debido a flexible typing de SQLite, no es raro encontrar columnas de
tabla con el tipo de datos "TEXT" que contienen codificaciones que no
son UTF-8, o incluso datos arbitrarios. Para demostrarlo, supongamos
que tenemos una base de datos con texto codificado en ISO-8859-2
(Latin-2), por ejemplo, una tabla de entradas de diccionario checo-
inglés. Suponiendo que ahora tenemos una instancia "Connection" "con"
conectada a esta base de datos, podemos decodificar el texto
codificado en Latin-2 utilizando este "text_factory":

   con.text_factory = lambda data: str(data, encoding="latin2")

Para datos UTF-8 no válidos o arbitrarios almacenados en las columnas
de la tabla "TEXT", puede utilizar la siguiente técnica, tomada
prestada de CÓMO (HOWTO) Unicode:

   con.text_factory = lambda data: str(data, errors="surrogateescape")

Nota:

  La API del módulo "sqlite3" no admite cadenas que contengan
  sustitutos.

Ver también: CÓMO (HOWTO) Unicode

## Explicación

### Control transaccional

"sqlite3" ofrece múltiples métodos para controlar si se abren y
cierran las transacciones de la base de datos, cuándo y cómo. Se
recomienda Control de transacciones mediante el atributo autocommit,
mientras que Control de transacciones mediante el atributo
isolation_level conserva el comportamiento anterior a Python 3.12.

#### Control de transacciones mediante el atributo "autocommit"

La forma recomendada de controlar el comportamiento de las
transacciones es a través del atributo "Connection.autocommit", que
preferiblemente debe configurarse utilizando el parámetro *autocommit*
de "connect()".

Se recomienda configurar *autocommit* en "False", lo que implica un
control de transacciones compatible con **PEP 249**. Esto significa:

* "sqlite3" garantiza que una transacción esté siempre abierta, por lo
  que "connect()", "Connection.commit()" y "Connection.rollback()"
  abrirán implícitamente una nueva transacción (inmediatamente después
  de cerrar la pendiente, en el caso de las dos últimas). "sqlite3"
  utiliza instrucciones "BEGIN DEFERRED" al abrir transacciones.

* Las transacciones deben confirmarse explícitamente mediante
  "commit()".

* Las transacciones deben revertirse explícitamente utilizando
  "rollback()".

* Se realiza una reversión implícita si la base de datos está
  modificada como "close()" con cambios pendientes.

Establezca *autocommit* en "True" para habilitar autocommit mode de
SQLite. En este modo, "Connection.commit()" y "Connection.rollback()"
no tienen efecto. Tenga en cuenta que el modo de confirmación
automática de SQLite es distinto del atributo "Connection.autocommit"
compatible con **PEP 249**; utilice "Connection.in_transaction" para
consultar el modo de confirmación automática de bajo nivel de SQLite.

Establezca *autocommit* en "LEGACY_TRANSACTION_CONTROL" para dejar el
comportamiento de control de transacciones al atributo
"Connection.isolation_level". Consulte Control de transacciones
mediante el atributo isolation_level para obtener más información.

#### Control de transacciones mediante el atributo "isolation_level"

Nota:

  La forma recomendada de controlar las transacciones es mediante el
  atributo "autocommit". Consulte Control de transacciones mediante el
  atributo autocommit.

Si "Connection.autocommit" se configura en
"LEGACY_TRANSACTION_CONTROL" (el valor predeterminado), el
comportamiento de la transacción se controla mediante el atributo
"Connection.isolation_level". De lo contrario, "isolation_level" no
tiene ningún efecto.

Si el atributo de conexión "isolation_level" no es "None", las nuevas
transacciones se abrirán implícitamente antes de "execute()" y
"executemany()" ejecutará sentencias "INSERT", "UPDATE", "DELETE" o
"REPLACE"; para otras sentencias, no se realiza ningún manejo de
transacción implícito. Utilice los métodos "commit()" y "rollback()"
para confirmar y deshacer respectivamente las transacciones
pendientes. Puede elegir el SQLite transaction behaviour  subyacente,
es decir, si y qué tipo de declaraciones "BEGIN" "sqlite3" se
ejecutarán implícitamente, a través del atributo "isolation_level".

Si "isolation_level" se establece como "None", no se abre ninguna
transacción implícitamente. Esto deja la biblioteca SQLite subyacente
en autocommit mode, pero también permite que el usuario realice su
propio manejo de transacciones usando declaraciones SQL explícitas. El
modo de confirmación automática de la biblioteca SQLite subyacente se
puede consultar mediante el atributo "in_transaction".

El método "executescript()" guarda implícitamente cualquier
transacción pendiente antes de la ejecución del script SQL dado,
independientemente del valor de "isolation_level".

Distinto en la versión 3.6: "sqlite3" solía realizar commit en
transacciones implícitamente antes de sentencias DDL. Este ya no es el
caso.

Distinto en la versión 3.12: La forma recomendada de controlar las
transacciones ahora es a través del atributo "autocommit".
