# Copyright (C) 2013-2016 2ndQuadrant Italia Srl
#
# Client Utilities for Barman, Backup and Recovery Manager for PostgreSQL
#
# Barman is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Barman is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Barman.  If not, see <http://www.gnu.org/licenses/>.

import imp

import mock

try:
    # Execution from the project root
    bwr = imp.load_source('bwr', 'barman-wal-restore')
except IOError:
    # Execution from the 'tests' directory
    bwr = imp.load_source('bwr', '../barman-wal-restore')


# noinspection PyMethodMayBeStatic
class TestRemoteGetWal(object):

    @mock.patch('bwr.subprocess.Popen')
    def test_string_dest_file(self, popen_mock, tmpdir):
        config = mock.Mock(
            compression=False,
            user='barman',
            barman_host='remote.barman.host',
            config=None,
            server_name='this-server')
        dest_file = tmpdir.join('test-dest').strpath

        # dest_file is a str object
        bwr.RemoteGetWal(
            config, '000000010000000000000001', dest_file)

        # In python2 the dest_file can be an unicode object
        if hasattr(dest_file, 'decode'):
            bwr.RemoteGetWal(
                config, '000000010000000000000001', dest_file.decode())
