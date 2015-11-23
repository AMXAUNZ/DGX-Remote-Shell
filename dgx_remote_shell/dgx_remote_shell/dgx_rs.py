"""DGX Remote Shell is a program that allows remote access to the DGX shell for
debugging and information gathering.

The MIT License (MIT)

Copyright (c) 2015 Jim Maciejewski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import wx
import telnetlib
import dgx_rs_gui
from threading import Thread
import requests
from bs4 import BeautifulSoup
from distutils.version import StrictVersion
import os
import sys


class DGXRSFrame(dgx_rs_gui.DGXRSFrame):
    def __init__(self, parent):
        dgx_rs_gui.DGXRSFrame.__init__(self, parent)

        self.parent = parent
        self.version = 'v0.1.2'
        icon_bundle = wx.IconBundle()
        icon_bundle.AddIconFromFile(r"icon/dgx_rs.ico", wx.BITMAP_TYPE_ANY)
        self.SetIcons(icon_bundle)
        self.SetTitle("DGX Remote Shell " + self.version)
        self.display_txt.SetValue(
            'Please connect Netlinx Studio to the DGX you would like to ' +
            'query. \r\rTurn on device notifications for device 5002, ' +
            'port 3, and the DGX\'s system number. \rOnly enable \'Commands ' +
            'From Device\'. \r\rEnsure the DGX IP above is correct and then ' +
            'select one of the predefined commands or enter your own.')
        self.display_txt.Enable(False)
        self.cert_path = self.resource_path('cacert.pem')
        Thread(target=self.update_check).start()

    def establish_telnet(self, ip_address, tel_port=23):
        """Creates the telnet instance"""
        telnet_session = telnetlib.Telnet(ip_address, tel_port, 5)
        telnet_session.set_option_negotiation_callback(self.call_back)
        return telnet_session

    def call_back(self, sock, cmd, opt):
        """ Turns on server side echoing"""
        if opt == telnetlib.ECHO and cmd in (telnetlib.WILL, telnetlib.WONT):
            sock.sendall(telnetlib.IAC + telnetlib.DO + telnetlib.ECHO)

    def send_command(self, command, cmd_type='DGX Shell>'):
        """Sends a command to the master"""
        try:
            feedback = ''
            telnet_session = self.establish_telnet(self.dgx_ip_txt.GetValue())
            feedback = feedback + telnet_session.read_until('>')
            if cmd_type == 'DGX Shell>':
                telnet_session.write('send_command 5002:3:0, \"$03, \'' +
                                     str(command) + '\',13,10\"\r')
            else:
                telnet_session.write('send_command 5002:3:0, \"\'' +
                                     str(command) + '\'\"\r')
            feedback = feedback + telnet_session.read_until('>')
            telnet_session.close()
        except Exception as error:
            self.display_txt.SetValue(
                'Error: ' + str(error))
            return
        self.show_process_directions(feedback)

    def show_process_directions(self, feedback):
        """Tell them how to do it"""
        self.display_txt.SetValue(
            feedback + '\r' +
            'In about 3 seconds, when the notifications show up in ' +
            'Netlinx Studio notifications. \rPlease copy these ' +
            'notifications and paste them here.\r\rPress Clear to paste\r' +
            'Then click Process.\r')
        self.display_txt.Enable(False)

    def on_clear(self, event):
        """Clears the window"""
        self.display_txt.SetValue('')
        self.display_txt.Enable(True)
        event.Skip()

    def on_command_button(self, event):
        """Send command from button event"""
        command = event.GetEventObject().GetLabel()
        self.send_command(command.lower(), cmd_type='DGX Shell>')

    def on_bcs_button(self, event):
        """Send bcs from button event"""
        command = event.GetEventObject().GetLabel()
        self.send_command(command.lower(), cmd_type='BCS>')

    def on_submit(self, event):
        """Get the DGX command """
        command = self.dgx_command_txt.GetValue()
        self.dgx_command_txt.SetValue('')
        self.send_command(command, self.type_cmb.GetValue())

    def on_apply(self, event):
        """process text"""
        text = self.display_txt.GetValue()
        self.display_txt.SetValue(self.process_text(text))

    def process_text(self, text):
        """remove and clean up text"""
        lines = text.split('\n')
        unwanted = [('^13', ''),
                    ('$03', ''),
                    ('1G', ''),
                    ('$1B1;1H$1B2J', ''),
                    ('$0D$0A', '\r'),
                    ('$0D $0A', '\r'),
                    ('$09', '\t'),
                    ('$1BDGX_SHELL>$1B1', 'DGX_SHELL>')]

        output = ''
        for line in lines:
            try:
                my_line = line.split('-', 1)[1]
            except:
                break
            my_line = my_line.replace('[', '')
            my_line = my_line.replace(']', '')
            output = output + my_line
        for item in unwanted:
            output = output.replace(item[0], item[1])
        return output

    def on_save(self, event):
        """Save the results"""
        dlg = wx.FileDialog(
                self,
                message='Select file to save',
                defaultFile="",
                wildcard="TXT files (*.txt)|*.txt",
                style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            with open(path, 'w') as f:
                f.write(self.display_txt.GetValue())

    def update_check(self):
        """Checks on line for updates"""
        # print 'in update'
        try:
            webpage = requests.get(
              'https://github.com/AMXAUNZ/DGX-Remote-Shell/releases',
              verify=self.cert_path)
            # Scrape page for latest version
            soup = BeautifulSoup(webpage.text)
            # Get the <div> sections in lable-latest
            # print 'divs'
            divs = soup.find_all("div", class_="release label-latest")
            # Get the 'href' of the release
            url_path = divs[0].find_all('a')[-3].get('href')
            # Get the 'verison' number
            online_version = url_path.split('/')[-2][1:]
            if StrictVersion(online_version) > StrictVersion(self.version[1:]):
                # Try update
                # print 'try update'
                self.do_update(url_path, online_version)
            else:
                # All up to date pass
                # print 'up to date'
                return
        except Exception as error:
            # print 'error'error
            # we have had a problem, maybe update will work next time.
            # print 'error ', error
            pass

    def do_update(self, url_path, online_version):
        """download and install"""
        # ask if they want to update
        dlg = wx.MessageDialog(
                parent=self,
                message='A new DGX Remote Shell is available v' +
                        str(StrictVersion(online_version)) + '\r' +
                        'Do you want to download and update?',
                        caption='Do you want to update?',
                        style=wx.OK | wx.CANCEL)
        if dlg.ShowModal() == wx.ID_OK:
            response = requests.get('https://github.com' + url_path,
                                    verify=self.cert_path, stream=True)
            # print response
            if not response.ok:
                return
            total_length = response.headers.get('content-length')
            if total_length is None:  # no content length header
                pass
            else:
                total_length = int(total_length)
                dlg2 = wx.ProgressDialog(
                    "Download Progress",
                    "Downloading update now",
                    maximum=total_length,
                    parent=self,
                    style=wx.PD_APP_MODAL |
                    wx.PD_AUTO_HIDE |
                    wx.PD_CAN_ABORT |
                    wx.PD_ELAPSED_TIME)
                temp_folder = os.environ.get('temp')
                with open(temp_folder +
                          '\DGX_Remote_Shell_Setup_' +
                          str(StrictVersion(online_version)) +
                          '.exe', 'wb') as handle:

                    count = 0
                    for data in response.iter_content(1024):
                        count += len(data)
                        handle.write(data)
                        (cancel, skip) = dlg2.Update(count)
                        if not cancel:
                            break

            dlg2.Destroy()
            if not cancel:
                return
            self.install_update(online_version, temp_folder)

    def install_update(self, online_version, temp_folder):
        """Installs the downloaded update"""
        dlg = wx.MessageDialog(
            parent=self,
            message='Do you want to update to v' +
                    str(StrictVersion(online_version)) + ' now?',
            caption='Update program',
            style=wx.OK | wx.CANCEL)

        if dlg.ShowModal() == wx.ID_OK:
            os.startfile(temp_folder +
                         '\DGX_Remote_Shell_Setup_' +
                         str(StrictVersion(online_version)) +
                         '.exe')
            self.Destroy()

    def resource_path(self, relative):
        return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),
                            relative)


def main():
    """Launch the main program"""

    dgx_rx_interface = wx.App()  # redirect=True, filename="log.txt")
    main_window = DGXRSFrame(None)
    main_window.Show()
    dgx_rx_interface.MainLoop()

if __name__ == '__main__':
    main()
