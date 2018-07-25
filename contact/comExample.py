import win32com.client

def run():
    # excel = win32com.client.Dispatch("Excel.Application")
    # excel.Visible = True
    explore = win32com.client.Dispatch("InternetExplorer.Application")
    explore.Visible = True
    # word example
    # word = win32com.client.Dispatch("Word.Application")
    # word.Visible = True
    # Excel example



if __name__ == "__main__":
    run()
