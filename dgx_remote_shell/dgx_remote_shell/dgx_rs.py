import wx
import telnetlib
import dgx_rs_gui


class DGXRSFrame(dgx_rs_gui.DGXRSFrame):
    def __init__(self, parent):
        dgx_rs_gui.DGXRSFrame.__init__(self, parent)

        self.parent = parent
        self.version = 'v0.0.1'
        self.dgx_system = '5002:3:0'

    def on_submit(self, event):
        """Get the DGX command """
        command = self.dgx_command_txt.GetValue()
        

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