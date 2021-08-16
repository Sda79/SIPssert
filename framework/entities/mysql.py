#!/usr/bin/env python
##
## TODO: update project's name
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.
##

from framework.entities.entity import Entity

class MysqlEntity(Entity):

    entity_default_image = "mysql"
    mysql_default_env = {"MYSQL_ALLOW_EMPTY_PASSWORD":"yes"}
    entity_default_daemon = True

    def get_entity_env(self):

        env_dict = {}

        if "MYSQL_ROOT_PASSWORD" in self.config:
            self.root_password = self.config["MYSQL_ROOT_PASSWORD"]

        if self.root_password:
            env_dict["MYSQL_ROOT_PASSWORD"] = self.root_password
        else:
            env_dict = self.mysql_default_env

        return env_dict

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
