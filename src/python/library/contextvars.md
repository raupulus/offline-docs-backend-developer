---
title: '"contextvars" --- Context Variables'
source_url: https://docs.python.org/es/3
source_path: library/contextvars.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2130
---

# "contextvars" --- Context Variables

======================================================================

Este módulo proporciona APIs para gestionar, almacenar y acceder a
estados en el contexto local. La clase "ContextVar" se utiliza para
declarar y trabajar con Variables de Contexto (*Context Variables*).
La función "copy_context()" y la clase "Context" deberían ser
utilizadas para gestionar el contexto actual en frameworks asíncronos.

Context managers that have state should use Context Variables instead
of "threading.local()" to prevent their state from bleeding to other
code unexpectedly, when used in concurrent code.

Ver **PEP 567** para más detalles.

Added in version 3.7.

## variables de contexto

class contextvars.ContextVar(name[, *, default])

   Esta clase se utiliza para declarar una nueva Variable de Contexto,
   por ejemplo:

      var: ContextVar[int] = ContextVar('var', default=42)

   El parámetro obligatorio *name* se utiliza para introspección y
   depuración.

   El parámetro opcional de sólo palabra clave *default* es utilizado
   por "ContextVar.get()", cuando en el contexto actual no se
   encuentra ningún valor para la variable.

   **Importante:** las Variables de Contexto deberían ser creadas en
   lo más alto a nivel de módulo y nunca en clausura. Los objetos
   "Context" mantienen referencias a variables de contexto, lo cual no
   permitiría que estas variables de contexto sean limpiadas por el
   recolector de basura.

   "ContextVar"s are generic over the type of their contained value.

   name

      El nombre de la variable. Propiedad de sólo lectura.

      Added in version 3.7.1.

   get([default])

      Retorna un valor para la variable de contexto en el contexto
      actual.

      Si la variable no tiene ningún valor en el contexto actual, el
      método:

      * retornará el valor del argumento *default* del método, si
        alguno fue dado; o

      * retornará el valor por defecto de la variable de contexto, si
        ésta fue creada con alguno; o

      * lanzará "LookupError".

   set(value)

      Establece un nuevo valor para la variable de contexto en el
      contexto actual.

      El argumento obligatorio *value* es el nuevo valor de la
      variable de contexto.

      Retorna un objeto "Token" que puede utilizarse para restaurar la
      variable a su valor anterior, utilizando el método
      "ContextVar.reset()".

      For convenience, the token object can be used as a context
      manager to avoid calling "ContextVar.reset()" manually:

         var = ContextVar('var', default='default value')

         with var.set('new value'):
             assert var.get() == 'new value'

         assert var.get() == 'default value'

      It is a shorthand for:

         var = ContextVar('var', default='default value')

         token = var.set('new value')
         try:
             assert var.get() == 'new value'
         finally:
             var.reset(token)

         assert var.get() == 'default value'

      Added in version 3.14: Added support for using tokens as context
      managers.

   reset(token)

      Restablece la variable de contexto al valor que tenía antes de
      llamar al método "ContextVar.set()", que creó el *token*
      utilizado.

      Por ejemplo:

         var = ContextVar('var')

         token = var.set('new value')
         # code that uses 'var'; var.get() returns 'new value'.
         var.reset(token)

         # After the reset call the var has no value again, so
         # var.get() would raise a LookupError.

      The same *token* cannot be used twice.

class contextvars.Token

   *Token* objects are returned by the "ContextVar.set()" method. They
   can be passed to the "ContextVar.reset()" method to revert the
   value of the variable to what it was before the corresponding
   *set*. A single token cannot reset a context variable more than
   once.

   Tokens support the context manager protocol to automatically reset
   context variables. See "ContextVar.set()".

   Tokens are generic over the same type as the "ContextVar" which
   created them.

   Added in version 3.14: Added support for usage as a context
   manager.

   var

      Propiedad de sólo lectura. Apunta al objeto "ContextVar" que
      creó el *token*.

   old_value

      Propiedad de sólo lectura. Es el valor que la variable tenía
      antes de llamar al método "ContextVar.set()" que creó el
      *token*. Apunta a "Token.MISSING" si la variable no estaba
      establecida antes de la llamada.

   MISSING

      Marcador utilizado por "Token.old_value".

## Gestión de contexto manual

contextvars.copy_context()

   Retorna una copia del objeto "Context" actual.

   El siguiente código obtiene una copia del contexto actual e imprime
   todas las variables y sus valores establecidos en el contexto:

      ctx: Context = copy_context()
      print(list(ctx.items()))

   The function has an *O*(1) complexity, i.e. works equally fast for
   contexts with a few context variables and for contexts that have a
   lot of them.

class contextvars.Context

   Mapeo de "ContextVars" con sus valores.

   "Context()" crea un contexto vacío sin valores. Para obtener una
   copia del contexto actual, se puede utilizar la función
   "copy_context()".

   Each thread has its own effective stack of "Context" objects.  The
   *current context* is the "Context" object at the top of the current
   thread's stack.  All "Context" objects in the stacks are considered
   to be *entered*.

   *Entering* a context, which can be done by calling its "run()"
   method, makes the context the current context by pushing it onto
   the top of the current thread's context stack.

   *Exiting* from the current context, which can be done by returning
   from the callback passed to the "run()" method, restores the
   current context to what it was before the context was entered by
   popping the context off the top of the context stack.

   Since each thread has its own context stack, "ContextVar" objects
   behave in a similar fashion to "threading.local()" when values are
   assigned in different threads.

   Attempting to enter an already entered context, including contexts
   entered in other threads, raises a "RuntimeError".

   After exiting a context, it can later be re-entered (from any
   thread).

   Any changes to "ContextVar" values via the "ContextVar.set()"
   method are recorded in the current context.  The "ContextVar.get()"
   method returns the value associated with the current context.
   Exiting a context effectively reverts any changes made to context
   variables while the context was entered (if needed, the values can
   be restored by re-entering the context).

   *Context* implementa la interfaz "collections.abc.Mapping".

   run(callable, *args, **kwargs)

      Enters the Context, executes "callable(*args, **kwargs)", then
      exits the Context.  Returns *callable*'s return value, or
      propagates an exception if one occurred.

      Example:

         import contextvars

         var = contextvars.ContextVar('var')
         var.set('spam')
         print(var.get())  # 'spam'

         ctx = contextvars.copy_context()

         def main():
             # 'var' was set to 'spam' before
             # calling 'copy_context()' and 'ctx.run(main)', so:
             print(var.get())  # 'spam'
             print(ctx[var])  # 'spam'

             var.set('ham')

             # Now, after setting 'var' to 'ham':
             print(var.get())  # 'ham'
             print(ctx[var])  # 'ham'

         # Any changes that the 'main' function makes to 'var'
         # will be contained in 'ctx'.
         ctx.run(main)

         # The 'main()' function was run in the 'ctx' context,
         # so changes to 'var' are contained in it:
         print(ctx[var])  # 'ham'

         # However, outside of 'ctx', 'var' is still set to 'spam':
         print(var.get())  # 'spam'

   copy()

      Retorna una copia superficial (*shallow copy*) del objeto de
      contexto.

   var in context

      Retorna "True" si *context* tiene un valor establecido para
      *var*; de lo contrario, retorna "False".

   context[var]

      Retorna el valor de la variable "ContextVar" *var*. Si la
      variable no está establecida en el contexto actual, se lanzará
      "KeyError".

   get(var[, default])

      Retorna el valor de *var*, si *var* tiene el valor en el objeto
      de contexto; de lo contrario, retorna *default*. Si *default* no
      es dado, retorna "None".

   iter(context)

      Retorna un iterador de las variables almacenadas en el objeto de
      contexto.

   len(proxy)

      Retorna el número de variables establecidas en el objeto de
      contexto.

   keys()

      Retorna un listado de todas las variables en el objeto de
      contexto.

   values()

      Retorna un listado de los valores de todas las variables en el
      objeto de contexto.

   items()

      Retorna un listado de dos tuplas que contienen todas las
      variables y sus variables en el contexto actual.

## Soporte asyncio

Las variables de contexto están soportadas de forma nativa en
"asyncio" y se pueden utilizar sin ninguna configuración adicional.
Por ejemplo, el siguiente código crea un servidor simple de respuesta,
que utiliza una variable de contexto que hace que la dirección del
cliente remoto esté disponible en la *Task* que gestiona al cliente:

   import asyncio
   import contextvars

   client_addr_var = contextvars.ContextVar('client_addr')

   def render_goodbye():
       # The address of the currently handled client can be accessed
       # without passing it explicitly to this function.

       client_addr = client_addr_var.get()
       return f'Good bye, client @ {client_addr}\r\n'.encode()

   async def handle_request(reader, writer):
       addr = writer.transport.get_extra_info('socket').getpeername()
       client_addr_var.set(addr)

       # In any code that we call is now possible to get
       # client's address by calling 'client_addr_var.get()'.

       while True:
           line = await reader.readline()
           print(line)
           if not line.strip():
               break

       writer.write(b'HTTP/1.1 200 OK\r\n')  # status line
       writer.write(b'\r\n')  # headers
       writer.write(render_goodbye())  # body
       writer.close()

   async def main():
       srv = await asyncio.start_server(
           handle_request, '127.0.0.1', 8081)

       async with srv:
           await srv.serve_forever()

   asyncio.run(main())

   # To test it you can use telnet or curl:
   #     telnet 127.0.0.1 8081
   #     curl 127.0.0.1:8081
