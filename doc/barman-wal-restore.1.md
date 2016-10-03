% BARMAN-WAL-RESTORE(1) Barman User manuals | Version 1.2
% 2ndQuadrant Italy <http://www.2ndQuadrant.it>
% October 3, 2016

# NAME

barman-wal-restore - 'restore_command' based on Barman's get-wal


# SYNOPSIS

barman-wal-restore [*OPTIONS*] *BARMAN_HOST* *SERVER_NAME* *WAL_NAME* *WAL_DEST*


# DESCRIPTION

This script can be used as a 'restore_command' for PostgreSQL servers,
retrieving WAL files using the 'get-wal' feature of Barman. An SSH
connection will be opened to the Barman host.
`barman-wal-restore` allows the integration of Barman in PostgreSQL
clusters for better business continuity results.

This script and Barman are administration tools for disaster recovery
of PostgreSQL servers written in Python and maintained by 2ndQuadrant.


# POSITIONAL ARGUMENTS

BARMAN\_HOST
:    the host of the Barman server.

SERVER\_NAME
:    the server name configured in Barman from which WALs are taken.

WAL\_NAME
:    the value of the '%f' keyword (according to 'restore\_command').

WAL\_DEST
:    the value of the '%p' keyword (according to 'restore\_command').

# OPTIONS

-h, --help
:    show a help message and exit

-V, --version
:    show program's version number and exit

-U *USER*, --user *USER*
:    the user used for the ssh connection to the Barman server. Defaults
     to 'barman'.

-s *SECONDS*, --sleep *SECONDS*
:    sleep for SECONDS after a failure of get-wal request. Defaults
     to 0 (nowait).

-p *JOBS*, --parallel *JOBS*
:    specifies the number of files to peek and transfer in parallel,
     defaults to 0 (disabled).

-z, --gzip
:    transfer the WAL files compressed with gzip

-j, --bzip2
:    transfer the WAL files compressed with bzip2

-c *CONFIG*, --config *CONFIG*
:    configuration file on the Barman server


# EXIT STATUS

0
:   Success

Not zero
:   Failure


# SEE ALSO

`barman` (1), `barman` (5).


# BUGS

Barman has been extensively tested, and is currently being used in several
production environments. However, we cannot exclude the presence of bugs.

Any bug can be reported via the Github issue tracker.


# RESOURCES

* Homepage: <http://www.pgbarman.org/>
* Documentation: <http://docs.pgbarman.org/>
* Professional support: <http://www.2ndQuadrant.com/>


# COPYING

Barman is the property of 2ndQuadrant Italia
and its code is distributed under GNU General Public License v3.

Copyright (C) 2011-2016 2ndQuadrant Italia Srl - <http://www.2ndQuadrant.it/>.
