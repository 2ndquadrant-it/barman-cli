MANPAGES=barman-wal-archive.1 barman-wal-restore.1

.PHONY: all clean help subdirs $(SUBDIRS)

all: $(MANPAGES) $(DOCS) $(SUBDIRS)

barman-wal-archive.1: barman-wal-archive.1.md
	pandoc -s -t man -o $@ $<

barman-wal-restore.1: barman-wal-restore.1.md
	pandoc -s -t man -o $@ $<

clean:
	    rm -f $(MANPAGES)

help:
	    @echo "Usage:"
	    @echo "    $$ make"
