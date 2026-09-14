---
title: 1. Incrustando Python en otra aplicación
source_url: https://docs.python.org/es/3
source_path: extending/embedding.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: extending
order: 980
---

# 1. Incrustando Python en otra aplicación

Los capítulos anteriores discutieron cómo extender Python, es decir,
cómo extender la funcionalidad de Python al adjuntarle una biblioteca
de funciones C. También es posible hacerlo al revés: enriquezca su
aplicación C/C++ incrustando Python en ella. La incrustación
proporciona a su aplicación la capacidad de implementar parte de la
funcionalidad de su aplicación en Python en lugar de C o C++. Esto se
puede usar para muchos propósitos; Un ejemplo sería permitir a los
usuarios adaptar la aplicación a sus necesidades escribiendo algunos
scripts en Python. También puede usarlo usted mismo si parte de la
funcionalidad se puede escribir en Python más fácilmente.

Incrustar Python es similar a extenderlo, pero no del todo. La
diferencia es que cuando extiende Python, el programa principal de la
aplicación sigue siendo el intérprete de Python, mientras que si
incrusta Python, el programa principal puede no tener nada que ver con
Python --- en cambio, algunas partes de la aplicación ocasionalmente
llaman al Intérprete de Python para ejecutar algún código de Python.

Entonces, si está incrustando Python, está proporcionando su propio
programa principal. Una de las cosas que tiene que hacer este programa
principal es inicializar el intérprete de Python. Como mínimo, debe
llamar a la función "Py_Initialize()". Hay llamadas opcionales para
pasar argumentos de línea de comandos a Python. Luego, puede llamar al
intérprete desde cualquier parte de la aplicación.

Hay varias formas diferentes de llamar al intérprete: puede pasar una
cadena que contiene declaraciones de Python a "PyRun_SimpleString()",
o puede pasar un puntero de archivo estándar y un nombre de archivo
(solo para identificación en mensajes de error) a
"PyRun_SimpleFile()". También puede llamar a las operaciones de nivel
inferior descritas en los capítulos anteriores para construir y usar
objetos de Python.

Ver también:

  Python/C API reference manual
     Los detalles de la interfaz C de Python se dan en este manual.
     Una gran cantidad de información necesaria se puede encontrar
     aquí.

## 1.1. Incrustación de muy alto nivel

La forma más simple de incrustar Python es el uso de la interfaz de
muy alto nivel. Esta interfaz está diseñada para ejecutar un script de
Python sin necesidad de interactuar directamente con la aplicación.
Esto puede usarse, por ejemplo, para realizar alguna operación en un
archivo.

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   int
   main(int argc, char *argv[])
   {
       PyStatus status;
       PyConfig config;
       PyConfig_InitPythonConfig(&config);

       /* optional but recommended */
       status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
       if (PyStatus_Exception(status)) {
           goto exception;
       }

       status = Py_InitializeFromConfig(&config);
       if (PyStatus_Exception(status)) {
           goto exception;
       }
       PyConfig_Clear(&config);

       PyRun_SimpleString("from time import time,ctime\n"
                          "print('Today is', ctime(time()))\n");
       if (Py_FinalizeEx() < 0) {
           exit(120);
       }
       return 0;

     exception:
        PyConfig_Clear(&config);
        Py_ExitStatusException(status);
   }

Nota:

  "#define PY_SSIZE_T_CLEAN" se usaba para indicar que "Py_ssize_t"
  debería usarse en algunas APIs en lugar de "int". No es necesario
  desde Python 3.13, pero lo mantenemos aquí por compatibilidad. Ver
  Cadena de caracteres y búferes para una descripción de esta macro.

La configuración "PyConfig.program_name" debe llamarse antes de
"Py_InitializeFromConfig()" para informar al intérprete sobre las
rutas a las bibliotecas de tiempo de ejecución de Python. A
continuación, el intérprete de Python se inicializa con
"Py_Initialize()", seguido de la ejecución de un script Python
codificado que imprime la fecha y la hora. Luego, la llamada
"Py_FinalizeEx()" cierra el intérprete, seguido por el final del
programa. En un programa real, es posible que desee obtener el script
de Python de otra fuente, tal vez una rutina de editor de texto, un
archivo o una base de datos. Obtener el código Python de un archivo se
puede hacer mejor usando la función "PyRun_SimpleFile()", que le
ahorra la molestia de asignar espacio de memoria y cargar el contenido
del archivo.

## 1.2. Más allá de la incrustación de muy alto nivel: una visión general

La interfaz de alto nivel le permite ejecutar piezas arbitrarias de
código Python desde su aplicación, pero el intercambio de valores de
datos es bastante engorroso, por decir lo menos. Si lo desea, debe
usar llamadas de nivel inferior. A costa de tener que escribir más
código C, puede lograr casi cualquier cosa.

Cabe señalar que extender Python e incrustar Python es la misma
actividad, a pesar de la intención diferente. La mayoría de los temas
tratados en los capítulos anteriores siguen siendo válidos. Para
mostrar esto, considere lo que realmente hace el código de extensión
de Python a C:

1. Convierte valores de datos de Python a C,

2. Realice una llamada de función a una rutina C usando los valores
   convertidos, y

3. Convierte los valores de datos de la llamada de C a Python.

Al incrustar Python, el código de interfaz hace:

1. Convierte valores de datos de C a Python,

2. Realice una llamada de función a una rutina de interfaz de Python
   utilizando los valores convertidos, y

3. Convierte los valores de datos de la llamada de Python a C.

Como puede ver, los pasos de conversión de datos simplemente se
intercambian para acomodar la dirección diferente de la transferencia
de idiomas cruzados. La única diferencia es la rutina que llama entre
ambas conversiones de datos. Al extender, llama a una rutina C, al
incrustar, llama a una rutina Python.

Este capítulo no discutirá cómo convertir datos de Python a C y
viceversa. Además, se supone que se entiende el uso adecuado de las
referencias y el tratamiento de errores. Dado que estos aspectos no
difieren de extender el intérprete, puede consultar los capítulos
anteriores para obtener la información requerida.

## 1.3. Incrustación pura

El primer programa tiene como objetivo ejecutar una función en un
script Python. Al igual que en la sección sobre la interfaz de muy
alto nivel, el intérprete de Python no interactúa directamente con la
aplicación (pero eso cambiará en la siguiente sección).

El código para ejecutar una función definida en un script de Python
es:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   int
   main(int argc, char *argv[])
   {
       PyObject *pName, *pModule, *pFunc;
       PyObject *pArgs, *pValue;
       int i;

       if (argc < 3) {
           fprintf(stderr,"Usage: call pythonfile funcname [args]\n");
           return 1;
       }

       Py_Initialize();
       pName = PyUnicode_DecodeFSDefault(argv[1]);
       /* Error checking of pName left out */

       pModule = PyImport_Import(pName);
       Py_DECREF(pName);

       if (pModule != NULL) {
           pFunc = PyObject_GetAttrString(pModule, argv[2]);
           /* pFunc is a new reference */

           if (pFunc && PyCallable_Check(pFunc)) {
               pArgs = PyTuple_New(argc - 3);
               for (i = 0; i < argc - 3; ++i) {
                   pValue = PyLong_FromLong(atoi(argv[i + 3]));
                   if (!pValue) {
                       Py_DECREF(pArgs);
                       Py_DECREF(pModule);
                       fprintf(stderr, "Cannot convert argument\n");
                       return 1;
                   }
                   /* pValue reference stolen here: */
                   PyTuple_SetItem(pArgs, i, pValue);
               }
               pValue = PyObject_CallObject(pFunc, pArgs);
               Py_DECREF(pArgs);
               if (pValue != NULL) {
                   printf("Result of call: %ld\n", PyLong_AsLong(pValue));
                   Py_DECREF(pValue);
               }
               else {
                   Py_DECREF(pFunc);
                   Py_DECREF(pModule);
                   PyErr_Print();
                   fprintf(stderr,"Call failed\n");
                   return 1;
               }
           }
           else {
               if (PyErr_Occurred())
                   PyErr_Print();
               fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
           }
           Py_XDECREF(pFunc);
           Py_DECREF(pModule);
       }
       else {
           PyErr_Print();
           fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
           return 1;
       }
       if (Py_FinalizeEx() < 0) {
           return 120;
       }
       return 0;
   }

Este código carga un script de Python usando "argv[1]" y llama a la
función nombrada en "argv[2]". Sus argumentos enteros son los otros
valores del arreglo "argv". Si usted compila y enlaza este programa
(llamemos al ejecutable terminado **call**), y úselo para ejecutar un
script Python, como:

   def multiply(a,b):
       print("Will compute", a, "times", b)
       c = 0
       for i in range(0, a):
           c = c + b
       return c

entonces el resultado debería ser:

   $ call multiply multiply 3 2
   Will compute 3 times 2
   Result of call: 6

Aunque el programa es bastante grande por su funcionalidad, la mayor
parte del código es para la conversión de datos entre Python y C, y
para informes de errores. La parte interesante con respecto a
incrustar Python comienza con:

   Py_Initialize();
   pName = PyUnicode_DecodeFSDefault(argv[1]);
   /* Error checking of pName left out */
   pModule = PyImport_Import(pName);

After initializing the interpreter, the script is loaded using
"PyImport_Import()".  This routine needs a Python string as its
argument, which is constructed using the "PyUnicode_DecodeFSDefault()"
data conversion routine.

   pFunc = PyObject_GetAttrString(pModule, argv[2]);
   /* pFunc is a new reference */

   if (pFunc && PyCallable_Check(pFunc)) {
       ...
   }
   Py_XDECREF(pFunc);

Una vez que se carga el script, el nombre que estamos buscando se
recupera usando "PyObject_GetAttrString()". Si el nombre existe y el
objeto retornado es invocable, puede asumir con seguridad que es una
función. Luego, el programa continúa construyendo una tupla de
argumentos como de costumbre. La llamada a la función Python se
realiza con:

   pValue = PyObject_CallObject(pFunc, pArgs);

Al regresar la función, "pValue" es "NULL" o contiene una referencia
al valor de retorno de la función. Asegúrese de liberar la referencia
después de examinar el valor.

## 1.4. Extendiendo Python incrustado

Hasta ahora, el intérprete de Python incorporado no tenía acceso a la
funcionalidad de la aplicación misma. La API de Python lo permite al
extender el intérprete incorporado. Es decir, el intérprete
incorporado se amplía con las rutinas proporcionadas por la
aplicación. Si bien suena complejo, no es tan malo. Simplemente olvide
por un momento que la aplicación inicia el intérprete de Python. En
cambio, considere que la aplicación es un conjunto de subrutinas y
escriba un código de pegamento que le otorgue a Python acceso a esas
rutinas, al igual que escribiría una extensión normal de Python. Por
ejemplo:

   static int numargs=0;

   /* Return the number of arguments of the application command line */
   static PyObject*
   emb_numargs(PyObject *self, PyObject *args)
   {
       if(!PyArg_ParseTuple(args, ":numargs"))
           return NULL;
       return PyLong_FromLong(numargs);
   }

   static PyMethodDef emb_module_methods[] = {
       {"numargs", emb_numargs, METH_VARARGS,
        "Return the number of arguments received by the process."},
       {NULL, NULL, 0, NULL}
   };

   static struct PyModuleDef emb_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "emb",
       .m_size = 0,
       .m_methods = emb_module_methods,
   };

   static PyObject*
   PyInit_emb(void)
   {
       return PyModuleDef_Init(&emb_module);
   }

Inserte el código anterior justo encima de la función "main()".
Además, inserte las siguientes dos declaraciones antes de la llamada a
"Py_Initialize()":

   numargs = argc;
   PyImport_AppendInittab("emb", &PyInit_emb);

Estas dos líneas inicializan la variable "numargs" y hacen que la
función "emb.numargs()" sea accesible para el intérprete de Python
incorporado. Con estas extensiones, el script de Python puede hacer
cosas como

   import emb
   print("Number of arguments", emb.numargs())

En una aplicación real, los métodos expondrán una API de la aplicación
a Python.

## 1.5. Incrustando Python en C++

También es posible incrustar Python en un programa C++; precisamente
cómo se hace esto dependerá de los detalles del sistema C++ utilizado;
en general, necesitará escribir el programa principal en C++ y usar el
compilador de C++ para compilar y vincular su programa. No es
necesario volver a compilar Python usando C++.

## 1.6. Compilar y enlazar bajo sistemas tipo Unix

No es necesariamente trivial encontrar los indicadores correctos para
pasar a su compilador (y enlazador) para incrustar el intérprete de
Python en su aplicación, particularmente porque Python necesita cargar
módulos de biblioteca implementados como extensiones dinámicas en C
(archivos ".so") enlazados en su contra.

Para conocer los indicadores necesarios del compilador y el enlazador,
puede ejecutar el script "python*X.Y*-config" que se genera como parte
del proceso de instalación (también puede estar disponible un script
"python3-config" ) Este script tiene varias opciones, de las cuales
las siguientes serán directamente útiles para usted:

* "pythonX.Y-config --cflags" le dará las banderas recomendadas al
  compilar:

     $ /opt/bin/python3.11-config --cflags
     -I/opt/include/python3.11 -I/opt/include/python3.11 -Wsign-compare  -DNDEBUG -g -fwrapv -O3 -Wall

* "pythonX.Y-config --ldflags --embed" le dará las banderas
  recomendadas al vincular:

     $ /opt/bin/python3.11-config --ldflags --embed
     -L/opt/lib/python3.11/config-3.11-x86_64-linux-gnu -L/opt/lib -lpython3.11 -lpthread -ldl  -lutil -lm

Nota:

  Para evitar confusiones entre varias instalaciones de Python (y
  especialmente entre el sistema Python y su propio Python compilado),
  se recomienda que use la ruta absoluta a "python*X.Y*-config", como
  en el ejemplo anterior.

Si este procedimiento no funciona para usted (no se garantiza que
funcione para todas las plataformas tipo Unix; sin embargo, le damos
la bienvenida informes de errores) deberá leer la documentación de su
sistema sobre dinámica vincular o examinar Python "Makefile" (use
"sysconfig.get_makefile_filename()" para encontrar su ubicación) y las
opciones de compilación. En este caso, el módulo "sysconfig" es una
herramienta útil para extraer mediante programación los valores de
configuración que querrá combinar. Por ejemplo:

   >>> import sysconfig
   >>> sysconfig.get_config_var('LIBS')
   '-lpthread -ldl  -lutil'
   >>> sysconfig.get_config_var('LINKFORSHARED')
   '-Xlinker -export-dynamic'
