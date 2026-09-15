---
title: Memory Allocation Routines
source_url: https://www.sqlite.org/c3ref/mem_methods.html
source_path: c3ref/mem_methods.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1480
---

> \
> typedef struct sqlite3_mem_methods sqlite3_mem_methods;\
> struct sqlite3_mem_methods {\
>   void \*(\*xMalloc)(int);         /\* Memory allocation function \*/\
>   void (\*xFree)(void\*);          /\* Free a prior allocation \*/\
>   void \*(\*xRealloc)(void\*,int);  /\* Resize an allocation \*/\
>   int (\*xSize)(void\*);           /\* Return the size of an allocation \*/\
>   int (\*xRoundup)(int);          /\* Round up request size to allocation size \*/\
>   int (\*xInit)(void\*);           /\* Initialize the memory allocator \*/\
>   void (\*xShutdown)(void\*);      /\* Deinitialize the memory allocator \*/\
>   void \*pAppData;                /\* Argument to xInit() and xShutdown() \*/\
> };\

An instance of this object defines the interface between SQLite and low-level memory allocation routines.

This object is used in only one place in the SQLite interface. A pointer to an instance of this object is the argument to [sqlite3_config()](../c3ref/config.md) when the configuration option is [SQLITE_CONFIG_MALLOC](../c3ref/c_config_covering_index_scan.md#sqliteconfigmalloc) or [SQLITE_CONFIG_GETMALLOC](../c3ref/c_config_covering_index_scan.md#sqliteconfiggetmalloc). By creating an instance of this object and passing it to [sqlite3_config](../c3ref/config.md)([SQLITE_CONFIG_MALLOC](../c3ref/c_config_covering_index_scan.md#sqliteconfigmalloc)) during configuration, an application can specify an alternative memory allocation subsystem for SQLite to use for all of its dynamic memory needs.

Note that SQLite comes with several [built-in memory allocators](../malloc.md#altalloc) that are perfectly adequate for the overwhelming majority of applications and that this object is only useful to a tiny minority of applications with specialized memory allocation requirements. This object is also used during testing of SQLite in order to specify an alternative memory allocator that simulates memory out-of-memory conditions in order to verify that SQLite recovers gracefully from such conditions.

The xMalloc, xRealloc, and xFree methods must work like the malloc(), realloc() and free() functions from the standard C library. SQLite guarantees that the second argument to xRealloc is always a value returned by a prior call to xRoundup.

xSize should return the allocated size of a memory allocation previously obtained from xMalloc or xRealloc. The allocated size is always at least as big as the requested size but may be larger.

The xRoundup method returns what would be the allocated size of a memory allocation given a particular requested size. Most memory allocators round up memory allocations at least to the next multiple of 8. Some allocators round up to a larger multiple or to a power of 2. Every memory allocation request coming in through [sqlite3_malloc()](../c3ref/free.md) or [sqlite3_realloc()](../c3ref/free.md) first calls xRoundup. If xRoundup returns 0, that causes the corresponding memory allocation to fail.

The xInit method initializes the memory allocator. For example, it might allocate any required mutexes or initialize internal data structures. The xShutdown method is invoked (indirectly) by [sqlite3_shutdown()](../c3ref/initialize.md) and should deallocate any resources acquired by xInit. The pAppData pointer is used as the only parameter to xInit and xShutdown.

SQLite holds the [SQLITE_MUTEX_STATIC_MAIN](../c3ref/c_mutex_fast.md) mutex when it invokes the xInit method, so the xInit method need not be threadsafe. The xShutdown method is only called from [sqlite3_shutdown()](../c3ref/initialize.md) so it does not need to be threadsafe either. For all other methods, SQLite holds the [SQLITE_MUTEX_STATIC_MEM](../c3ref/c_mutex_fast.md) mutex as long as the [SQLITE_CONFIG_MEMSTATUS](../c3ref/c_config_covering_index_scan.md#sqliteconfigmemstatus) configuration option is turned on (which it is by default) and so the methods are automatically serialized. However, if [SQLITE_CONFIG_MEMSTATUS](../c3ref/c_config_covering_index_scan.md#sqliteconfigmemstatus) is disabled, then the other methods must be threadsafe or else make their own arrangements for serialization.

SQLite will never invoke xInit() more than once without an intervening call to xShutdown().

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
