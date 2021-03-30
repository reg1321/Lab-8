Hash.py creates a file called "hashedinfo.csv" which contains a hash of every
single file of the file system (except for ones explicitly ignored using a list
of "nogo" directories. In addition to the hash, the file name and its corresponding
path as well as the time the hash was taken will be provided. We utilized the
os.walk function to "walk" through the file system, the SHA256 hashing function,
and the datetime function in order to do this. We imported these python libraries
to do this with ease. We also counted file changes using the builtins library
and stepped through adding a count each time.
