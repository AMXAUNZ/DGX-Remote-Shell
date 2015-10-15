import wx
import telnetlib
import dgx_rs_gui


class DGXRSFrame(dgx_rs_gui.DGXRSFrame):
    def __init__(self, parent):
        dgx_rs_gui.DGXRSFrame.__init__(self, parent)

        self.parent = parent
        self.version = 'v0.0.2'
        icon_bundle = wx.IconBundle()
        icon_bundle.AddIconFromFile(r"icon/dgx_rs.ico", wx.BITMAP_TYPE_ANY)
        self.SetIcons(icon_bundle)
        self.display_txt.SetValue(
            'Please connect Netlinx Studio to the DGX you would like to ' +
            'query. \r\rTurn on device notifications for device 5002, ' +
            'port 3, and the DGX\'s system number. \rOnly enable \'Commands ' +
            'From Device\'. \r\rEnsure the DGX IP above is correct and then ' +
            'select one of the predefined commands or enter your own.')
        self.display_txt.Enable(False)

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
            'notifications and paste them here.\r\r Press Clear to paste\r' +
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
        self.send_command(command.lower(), cmd_type='DGS Shell>')

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


def main():
    """Launch the main program"""

    dgx_rx_interface = wx.App()  # redirect=True, filename="log.txt")
    main_window = DGXRSFrame(None)
    main_window.Show()
    dgx_rx_interface.MainLoop()

if __name__ == '__main__':
    main()