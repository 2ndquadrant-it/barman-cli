MANPAGES=barman-wal-restore.1

.PHONY: all clean help subdirs $(SUBDIRS)

all: $(MANPAGES) $(DOCS) $(SUBDIRS)

barman-wal-restore.1: barman-wal-restore.1.md
	pandoc -s -t man -o $@ $<

clean:
	    rm -f $(MANPAGES)

help:
	    @echo "Usage:"
	    @echo "    $$ make"
