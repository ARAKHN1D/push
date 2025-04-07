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
from random import choice

@Gtk.Template(resource_path="/app/drey/Push/gtk/window.ui")
class PushWindow(Adw.ApplicationWindow):
    __gtype_name__ = "PushWindow"

    # Categories
    body_no_buttons = (
        {"title": _("Command Completed"), "body": _("<COMMAND>")},
        {"title": _("Text Copied"), "body": _('"<TEXT>"')},
        {"title": _("Destination Reached"), "body": _("<DESTINATION>")}
    )
    body_one_button = (
        {"title": _("Email Received"), "body": _('"<SUBJECT>" from <EMAIL>.'),
                "buttons": [_("Open")]},
        {"title": _("Updates Downloaded"), "body": _("Updates are ready to be installed."),
                "buttons": [_("Install")]},
        {"title": _("Download Finished"), "body": _('"<FILE>" successfully downloaded.'),
                "buttons": [_("Open")]}
    )
    body_two_buttons = (
        {"title": _("Message Received"), "body": _("<MESSAGE>"),
                "buttons": [_("Open"), _("Mark as Read")]},
        {"title": _("Sharing Requested"), "body": _("Sharing requested from <USER>."),
                "buttons": [_("Allow"), _("Deny")]},
        {"title": _("<APP> Crashed"), "body": _("Crash occured in component <COMPONENT>."),
                "buttons": [_("Relaunch"), _("Show Details")]}
    )
    body_three_buttons = (
        {"title": _("Project Invitation"), "body": _("<USER> invited you to project <PROJECT>"),
                "buttons": [_("Accept"), _("Decline"), _("Show Details")]},
        {"title": _("Extension Updates Available"), "body": _("Logout to apply extension updates."),
                "buttons": [_("Logout"), _("Remind Later"), _("Show Details")]},
        {"title": _("Battery Low"), "body": _("Switching the Power Mode to Power Saver may decrease battery usage."),
                "buttons": [_("Switch"), _("Dismiss"), _("Show Details")]}
    )
    no_body_no_buttons = (
        {"title": _("File Operations Completed")},
        {"title": _("<USER> Logged In")},
        {"title": _("Updates Installed")}
    )
    no_body_one_button = (
        {"title": _("Updates Installed"), "buttons": [_("Show Details")]},
        {"title": _("Timer Finished"), "buttons": [_("Restart")]},
        {"title": _("<APP> Ready"), "buttons": [_("Launch")]}
    )
    no_body_two_buttons = (
        {"title": _("Alarm Went Off"), "buttons": [_("Stop"), _("Snooze")]},
        {"title": _("<USER> is Calling"), "buttons": [_("Join"), _("Ignore")]},
        {"title": _("Screensharing Requested"), "buttons": [_("Allow"), _("Deny")]}
    )
    no_body_three_buttons = (
        {"title": _("Software Updates Available"),
                "buttons": [_("Install"), _("Remind Later"), _("Show Details")]},
        {"title": _("<USER> Requested Remote Access"),
                "buttons": [_("Allow"), _("Deny"), _("Show Details")]},
        {"title": _("Meeting Invitation"),
                "buttons": [_("Accept"), _("Decline"), _("Show Details")]}
    )

    body_row = Gtk.Template.Child()
    buttons_row = Gtk.Template.Child()
    icon_row = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_send_row_activated(self, send_row):
        notification = Gio.Notification.new(_(""))
        has_body = self.body_row.get_active()
        buttons_amount = self.buttons_row.get_value()
        has_icon = self.icon_row.get_active()

        match (has_body, buttons_amount):
            case (True, 0):
                preset = choice(self.body_no_buttons)
            case (True, 1):
                preset = choice(self.body_one_button)
            case (True, 2):
                preset = choice(self.body_two_buttons)
            case (True, 3):
                preset = choice(self.body_three_buttons)
            case (False, 0):
                preset = choice(self.no_body_no_buttons)
            case (False, 1):
                preset = choice(self.no_body_one_button)
            case (False, 2):
                preset = choice(self.no_body_two_buttons)
            case (False, 3):
                preset = choice(self.no_body_three_buttons)

        notification.set_title(preset["title"])
        if "body" in preset:
            notification.set_body(preset["body"])
        if "buttons" in preset:
            for button in preset["buttons"]:
                notification.add_button(button, "app.button-clicked")
        if has_icon:
            notification.set_icon(Gio.Icon.new_for_string("app.drey.Push"))

        self.get_application().send_notification("notification-testing", notification)
