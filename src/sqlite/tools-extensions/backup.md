---
title: SQLite Backup API
source_url: https://www.sqlite.org/backup.html
source_path: backup.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: tools-extensions
order: 140
---

# 1. Using the SQLite Online Backup API

Historically, backups (copies) of SQLite databases have been created using the following method:

1.  Establish a shared lock on the database file using the SQLite API (i.e. the shell tool).
2.  Copy the database file using an external tool (for example the unix 'cp' utility or the DOS 'copy' command).
3.  Relinquish the shared lock on the database file obtained in step 1.

This procedure works well in many scenarios and is usually very fast. However, this technique has the following shortcomings:

- Any database clients wishing to write to the database file while a backup is being created must wait until the shared lock is relinquished.
- It cannot be used to copy data to or from in-memory databases.
- If a power failure or operating system failure occurs while copying the database file the backup database may be corrupted following system recovery.

The [Online Backup API](c3ref/backup_finish.md#sqlite3backupinit) was created to address these concerns. The online backup API allows the contents of one database to be copied into another database file, replacing any original contents of the target database. The copy operation may be done incrementally, in which case the source database does not need to be locked for the duration of the copy, only for the brief periods of time when it is actually being read from. This allows other database users to continue without excessive delays while a backup of an online database is made.

The effect of completing the backup call sequence is to make the destination a bit-wise identical copy of the source database as it was when the copying commenced. (The destination becomes a "snapshot.")

The online backup API is [documented here](c3ref/backup_finish.md#sqlite3backupinit). The remainder of this page contains two C language examples illustrating common uses of the API and discussions thereof. Reading these examples is no substitute for reading the API documentation!

## 1.1. Other Backup Techniques

The Online Backup API is the original method for making backups of a live SQLite databases. Other more recent techniques for accomplishing the same thing include:

- The [VACUUM INTO](lang_vacuum.md#vacuuminto) command will make a vacuumed copy of a live SQLite database into a separate file.

- The [sqlite3_rsync](rsync.md) program makes a copy of a live SQLite database to or from a remote system using an SSH connection.

# 2. Example 1: Loading and Saving In-Memory Databases

\
<span style="color:blue;font-style:italic;">/\*</span>\
<span style="color:blue;font-style:italic;">\*\* This function is used to load the contents of a database file on disk </span>\
<span style="color:blue;font-style:italic;">\*\* into the "main" database of open database connection pInMemory, or</span>\
<span style="color:blue;font-style:italic;">\*\* to save the current contents of the database opened by pInMemory into</span>\
<span style="color:blue;font-style:italic;">\*\* a database file on disk. pInMemory is probably an in-memory database, </span>\
<span style="color:blue;font-style:italic;">\*\* but this function will also work fine if it is not.</span>\
<span style="color:blue;font-style:italic;">\*\*</span>\
<span style="color:blue;font-style:italic;">\*\* Parameter zFilename points to a nul-terminated string containing the</span>\
<span style="color:blue;font-style:italic;">\*\* name of the database file on disk to load from or save to. If parameter</span>\
<span style="color:blue;font-style:italic;">\*\* isSave is non-zero, then the contents of the file zFilename are </span>\
<span style="color:blue;font-style:italic;">\*\* overwritten with the contents of the database opened by pInMemory. If</span>\
<span style="color:blue;font-style:italic;">\*\* parameter isSave is zero, then the contents of the database opened by</span>\
<span style="color:blue;font-style:italic;">\*\* pInMemory are replaced by data loaded from the file zFilename.</span>\
<span style="color:blue;font-style:italic;">\*\*</span>\
<span style="color:blue;font-style:italic;">\*\* If the operation is successful, SQLITE_OK is returned. Otherwise, if</span>\
<span style="color:blue;font-style:italic;">\*\* an error occurs, an SQLite error code is returned.</span>\
<span style="color:blue;font-style:italic;">\*/</span>\
int loadOrSaveDb([sqlite3](c3ref/sqlite3.md) \*pInMemory, const char \*zFilename, int isSave){\
  int rc;                   <span style="color:blue;font-style:italic;">/\* Function return code \*/</span>\
  [sqlite3](c3ref/sqlite3.md) \*pFile;           <span style="color:blue;font-style:italic;">/\* Database connection opened on zFilename \*/</span>\
  [sqlite3_backup](c3ref/backup.md) \*pBackup;  <span style="color:blue;font-style:italic;">/\* Backup object used to copy data \*/</span>\
  [sqlite3](c3ref/sqlite3.md) \*pTo;             <span style="color:blue;font-style:italic;">/\* Database to copy to (pFile or pInMemory) \*/</span>\
  [sqlite3](c3ref/sqlite3.md) \*pFrom;           <span style="color:blue;font-style:italic;">/\* Database to copy from (pFile or pInMemory) \*/</span>\
\
  <span style="color:blue;font-style:italic;">/\* Open the database file identified by zFilename. Exit early if this fails</span>\
  <span style="color:blue;font-style:italic;">\*\* for any reason. \*/</span>\
  rc = [sqlite3_open](c3ref/open.md)(zFilename, &pFile);\
  if( rc==SQLITE_OK ){\
\
    <span style="color:blue;font-style:italic;">/\* If this is a 'load' operation (isSave==0), then data is copied</span>\
    <span style="color:blue;font-style:italic;">\*\* from the database file just opened to database pInMemory. </span>\
    <span style="color:blue;font-style:italic;">\*\* Otherwise, if this is a 'save' operation (isSave==1), then data</span>\
    <span style="color:blue;font-style:italic;">\*\* is copied from pInMemory to pFile.  Set the variables pFrom and</span>\
    <span style="color:blue;font-style:italic;">\*\* pTo accordingly. \*/</span>\
    pFrom = (isSave ? pInMemory : pFile);\
    pTo   = (isSave ? pFile     : pInMemory);\
\
    <span style="color:blue;font-style:italic;">/\* Set up the backup procedure to copy from the "main" database of </span>\
    <span style="color:blue;font-style:italic;">\*\* connection pFile to the main database of connection pInMemory.</span>\
    <span style="color:blue;font-style:italic;">\*\* If something goes wrong, pBackup will be set to NULL and an error</span>\
    <span style="color:blue;font-style:italic;">\*\* code and message left in connection pTo.</span>\
    <span style="color:blue;font-style:italic;">\*\*</span>\
    <span style="color:blue;font-style:italic;">\*\* If the backup object is successfully created, call backup_step()</span>\
    <span style="color:blue;font-style:italic;">\*\* to copy data from pFile to pInMemory. Then call backup_finish()</span>\
    <span style="color:blue;font-style:italic;">\*\* to release resources associated with the pBackup object.  If an</span>\
    <span style="color:blue;font-style:italic;">\*\* error occurred, then an error code and message will be left in</span>\
    <span style="color:blue;font-style:italic;">\*\* connection pTo. If no error occurred, then the error code belonging</span>\
    <span style="color:blue;font-style:italic;">\*\* to pTo is set to SQLITE_OK.</span>\
    <span style="color:blue;font-style:italic;">\*/</span>\
    pBackup = [sqlite3_backup_init](c3ref/backup_finish.md#sqlite3backupinit)(pTo, "main", pFrom, "main");\
    if( pBackup ){\
      (void)[sqlite3_backup_step](c3ref/backup_finish.md#sqlite3backupstep)(pBackup, -1);\
      (void)[sqlite3_backup_finish](c3ref/backup_finish.md#sqlite3backupfinish)(pBackup);\
    }\
    rc = [sqlite3_errcode](c3ref/errcode.md)(pTo);\
  }\
\
  <span style="color:blue;font-style:italic;">/\* Close the database connection opened on database file zFilename</span>\
  <span style="color:blue;font-style:italic;">\*\* and return the result of this function. \*/</span>\
  (void)[sqlite3_close](c3ref/close.md)(pFile);\
  return rc;\
}\

The C function above demonstrates one of the simplest, and most common, uses of the backup API: loading and saving the contents of an in-memory database to a file on disk. The backup API is used as follows in this example:

1.  Function [sqlite3_backup_init()](c3ref/backup_finish.md#sqlite3backupinit) is called to create an [sqlite3_backup](c3ref/backup.md) object to copy data between the two databases (either from a file and into the in-memory database, or vice-versa).
2.  Function [sqlite3_backup_step()](c3ref/backup_finish.md#sqlite3backupstep) is called with a parameter of `-1` to copy the entire source database to the destination.
3.  Function [sqlite3_backup_finish()](c3ref/backup_finish.md#sqlite3backupfinish) is called to clean up resources allocated by [sqlite3_backup_init()](c3ref/backup_finish.md#sqlite3backupinit).

## 2.1. Error handling

If an error occurs in any of the three main backup API routines then the [error code](rescode.md) and [message](c3ref/errcode.md) are attached to the destination [database connection](c3ref/sqlite3.md). Additionally, if [sqlite3_backup_step()](c3ref/backup_finish.md#sqlite3backupstep) encounters an error, then the [error code](rescode.md) is returned by both the [sqlite3_backup_step()](c3ref/backup_finish.md#sqlite3backupstep) call itself, and by the subsequent call to [sqlite3_backup_finish()](c3ref/backup_finish.md#sqlite3backupfinish). So a call to [sqlite3_backup_finish()](c3ref/backup_finish.md#sqlite3backupfinish) does not overwrite an [error code](rescode.md) stored in the destination [database connection](c3ref/sqlite3.md) by [sqlite3_backup_step()](c3ref/backup_finish.md#sqlite3backupstep). This feature is used in the example code to reduce the amount of error handling required. The return values of the [sqlite3_backup_step()](c3ref/backup_finish.md#sqlite3backupstep) and [sqlite3_backup_finish()](c3ref/backup_finish.md#sqlite3backupfinish) calls are ignored and the error code indicating the success or failure of the copy operation is collected from the destination [database connection](c3ref/sqlite3.md) afterward.

## 2.2. Possible Enhancements

The implementation of this function could be enhanced in at least two ways:

1.  Failing to obtain the lock on database file zFilename (an [SQLITE_BUSY](rescode.md#busy) error) could be handled, and
2.  Cases where the page-sizes of database pInMemory and zFilename are different could be handled better.

Since database zFilename is a file on disk, then it may be accessed externally by another process. This means that when the call to sqlite3_backup_step() attempts to read from or write data to it, it may fail to obtain the required file lock. If this happens, this implementation will fail, returning SQLITE_BUSY immediately. The solution would be to register a busy-handler callback or timeout with [database connection](c3ref/sqlite3.md) pFile using [sqlite3_busy_handler()](c3ref/busy_handler.md) or [sqlite3_busy_timeout()](c3ref/busy_timeout.md) as soon as it is opened. If it fails to obtain a required lock immediately, [sqlite3_backup_step()](c3ref/backup_finish.md#sqlite3backupstep) uses any registered busy-handler callback or timeout in the same way as [sqlite3_step()](c3ref/step.md) or [sqlite3_exec()](c3ref/exec.md) does.

Usually, it does not matter if the page-sizes of the source database and the destination database are different before the contents of the destination are overwritten. The page-size of the destination database is simply changed as part of the backup operation. The exception is if the destination database happens to be an in-memory database. In this case, if the page sizes are not the same at the start of the backup operation, then the operation fails with an SQLITE_READONLY error. Unfortunately, this could occur when loading a database image from a file into an in-memory database using function loadOrSaveDb().

However, if in-memory database pInMemory has just been opened (and is therefore completely empty) before being passed to function loadOrSaveDb(), then it is still possible to change its page size using an SQLite "PRAGMA page_size" command. Function loadOrSaveDb() could detect this case, and attempt to set the page-size of the in-memory database to the page-size of database zFilename before invoking the online backup API functions.

# 3. Example 2: Online Backup of a Running Database

\
<span style="color:blue;font-style:italic;">/\*</span>\
<span style="color:blue;font-style:italic;">\*\* Perform an online backup of database pDb to the database file named</span>\
<span style="color:blue;font-style:italic;">\*\* by zFilename. This function copies 5 database pages from pDb to</span>\
<span style="color:blue;font-style:italic;">\*\* zFilename, then unlocks pDb and sleeps for 250 ms, then repeats the</span>\
<span style="color:blue;font-style:italic;">\*\* process until the entire database is backed up.</span>\
<span style="color:blue;font-style:italic;">\*\* </span>\
<span style="color:blue;font-style:italic;">\*\* The third argument passed to this function must be a pointer to a progress</span>\
<span style="color:blue;font-style:italic;">\*\* function. After each set of 5 pages is backed up, the progress function</span>\
<span style="color:blue;font-style:italic;">\*\* is invoked with two integer parameters: the number of pages left to</span>\
<span style="color:blue;font-style:italic;">\*\* copy, and the total number of pages in the source file. This information</span>\
<span style="color:blue;font-style:italic;">\*\* may be used, for example, to update a GUI progress bar.</span>\
<span style="color:blue;font-style:italic;">\*\*</span>\
<span style="color:blue;font-style:italic;">\*\* While this function is running, another thread may use the database pDb, or</span>\
<span style="color:blue;font-style:italic;">\*\* another process may access the underlying database file via a separate </span>\
<span style="color:blue;font-style:italic;">\*\* connection.</span>\
<span style="color:blue;font-style:italic;">\*\*</span>\
<span style="color:blue;font-style:italic;">\*\* If the backup process is successfully completed, SQLITE_OK is returned.</span>\
<span style="color:blue;font-style:italic;">\*\* Otherwise, if an error occurs, an SQLite error code is returned.</span>\
<span style="color:blue;font-style:italic;">\*/</span>\
int backupDb(\
  [sqlite3](c3ref/sqlite3.md) \*pDb,               <span style="color:blue;font-style:italic;">/\* Database to back up \*/</span>\
  const char \*zFilename,      <span style="color:blue;font-style:italic;">/\* Name of file to back up to \*/</span>\
  void(\*xProgress)(int, int)  <span style="color:blue;font-style:italic;">/\* Progress function to invoke \*/     </span>\
){\
  int rc;                     <span style="color:blue;font-style:italic;">/\* Function return code \*/</span>\
  [sqlite3](c3ref/sqlite3.md) \*pFile;             <span style="color:blue;font-style:italic;">/\* Database connection opened on zFilename \*/</span>\
  [sqlite3_backup](c3ref/backup.md) \*pBackup;    <span style="color:blue;font-style:italic;">/\* Backup handle used to copy data \*/</span>\
\
  <span style="color:blue;font-style:italic;">/\* Open the database file identified by zFilename. \*/</span>\
  rc = [sqlite3_open](c3ref/open.md)(zFilename, &pFile);\
  if( rc==SQLITE_OK ){\
\
    <span style="color:blue;font-style:italic;">/\* Open the [sqlite3_backup](c3ref/backup.md) object used to accomplish the transfer \*/</span>\
    pBackup = [sqlite3_backup_init](c3ref/backup_finish.md#sqlite3backupinit)(pFile, "main", pDb, "main");\
    if( pBackup ){\
\
      <span style="color:blue;font-style:italic;">/\* Each iteration of this loop copies 5 database pages from database</span>\
      <span style="color:blue;font-style:italic;">\*\* pDb to the backup database. If the return value of backup_step()</span>\
      <span style="color:blue;font-style:italic;">\*\* indicates that there are still further pages to copy, sleep for</span>\
      <span style="color:blue;font-style:italic;">\*\* 250 ms before repeating. \*/</span>\
      do {\
        rc = [sqlite3_backup_step](c3ref/backup_finish.md#sqlite3backupstep)(pBackup, 5);\
        xProgress(\
            [sqlite3_backup_remaining](c3ref/backup_finish.md#sqlite3backupremaining)(pBackup),\
            [sqlite3_backup_pagecount](c3ref/backup_finish.md#sqlite3backuppagecount)(pBackup)\
        );\
        if( rc==SQLITE_OK \|\| rc==SQLITE_BUSY \|\| rc==SQLITE_LOCKED ){\
          [sqlite3_sleep](c3ref/sleep.md)(250);\
        }\
      } while( rc==SQLITE_OK \|\| rc==SQLITE_BUSY \|\| rc==SQLITE_LOCKED );\
\
      <span style="color:blue;font-style:italic;">/\* Release resources allocated by backup_init(). \*/</span>\
      (void)[sqlite3_backup_finish](c3ref/backup_finish.md#sqlite3backupfinish)(pBackup);\
    }\
    rc = [sqlite3_errcode](c3ref/errcode.md)(pFile);\
  }\
  \
  <span style="color:blue;font-style:italic;">/\* Close the database connection opened on database file zFilename</span>\
  <span style="color:blue;font-style:italic;">\*\* and return the result of this function. \*/</span>\
  (void)[sqlite3_close](c3ref/close.md)(pFile);\
  return rc;\
}\

The function presented in the previous example copies the entire source database in one call to [sqlite3_backup_step()](c3ref/backup_finish.md#sqlite3backupstep). This requires holding a read-lock on the source database file for the duration of the operation, preventing any other database user from writing to the database. It also holds the mutex associated with database pInMemory throughout the copy, preventing any other thread from using it. The C function in this section, designed to be called by a background thread or process for creating a backup of an online database, avoids these problems using the following approach:

1.  Function [sqlite3_backup_init()](c3ref/backup_finish.md#sqlite3backupinit) is called to create an [sqlite3_backup](c3ref/backup.md) object to copy data from database pDb to the backup database file identified by zFilename.
2.  Function [sqlite3_backup_step()](c3ref/backup_finish.md#sqlite3backupstep) is called with a parameter of 5 to copy 5 pages of database pDb to the backup database (file zFilename).
3.  If there are still more pages to copy from database pDb, then the function sleeps for 250 milliseconds (using the [sqlite3_sleep()](c3ref/sleep.md) utility) and then returns to step 2.
4.  Function [sqlite3_backup_finish()](c3ref/backup_finish.md#sqlite3backupfinish) is called to clean up resources allocated by [sqlite3_backup_init()](c3ref/backup_finish.md#sqlite3backupinit).

## 3.1. File and Database Connection Locking

During the 250 ms sleep in step 3 above, no read-lock is held on the database file and the mutex associated with pDb is not held. This allows other threads to use [database connection](c3ref/sqlite3.md) pDb and other connections to write to the underlying database file.

If another thread or process writes to the source database while this function is sleeping, then SQLite detects this and usually restarts the backup process when sqlite3_backup_step() is next called. There is one exception to this rule: If the source database is not an in-memory database, and the write is performed from within the same process as the backup operation and uses the same database handle (pDb), then the destination database (the one opened using connection pFile) is automatically updated along with the source. The backup process may then be continued after the sqlite3_sleep() call returns as if nothing had happened.

Whether or not the backup process is restarted as a result of writes to the source database mid-backup, the user can be sure that when the backup operation is completed the backup database contains a consistent and up-to-date snapshot of the original. However:

- Writes to an in-memory source database, or writes to a file-based source database by an external process or thread using a database connection other than pDb are significantly more expensive than writes made to a file-based source database using pDb (as the entire backup operation must be restarted in the former two cases).
- If the backup process is restarted frequently enough it may never run to completion and the backupDb() function may never return.

## 3.2. backup_remaining() and backup_pagecount()

The backupDb() function uses the sqlite3_backup_remaining() and sqlite3_backup_pagecount() functions to report its progress via the user-supplied xProgress() callback. Function sqlite3_backup_remaining() returns the number of pages left to copy and sqlite3_backup_pagecount() returns the total number of pages in the source database (in this case the database opened by pDb). So the percentage completion of the process may be calculated as:

Completion = 100% \* (pagecount() - remaining()) / pagecount()

The sqlite3_backup_remaining() and sqlite3_backup_pagecount() APIs report values stored by the previous call to sqlite3_backup_step(), they do not actually inspect the source database file. This means that if the source database is written to by another thread or process after the call to sqlite3_backup_step() returns but before the values returned by sqlite3_backup_remaining() and sqlite3_backup_pagecount() are used, the values may be technically incorrect. This is not usually a problem.
