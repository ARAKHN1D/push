# window.py
#
# Copyright 2025 ARAKHNID
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Gtk, Gio, Adw

@Gtk.Template(resource_path="/app/drey/Push/gtk/window.ui")
class PushWindow(Adw.ApplicationWindow):
    __gtype_name__ = "PushWindow"

    icon_row = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_send_row_activated(self, send_row):
        notification = Gio.Notification.new(_("Notification sent"))
        icon = self.icon_row.get_active()

        if icon:
            notification.set_icon(Gio.Icon.new_for_string("app.drey.Push"))

        self.get_application().send_notification("notification-testing", notification)
