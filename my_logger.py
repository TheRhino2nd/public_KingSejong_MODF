import datetime


class My_Logger:



    def __init__(self, log_filename, warn_filename = "empty"):
        import os

        self.log_filename = log_filename
        self.warn_filename = warn_filename

        if os.path.exists(self.log_filename): os.remove(self.log_filename)
        if os.path.exists(self.warn_filename): os.remove(self.warn_filename)

        self.log_file = open(self.log_filename,"wt")
        if self.warn_filename != "empty": self.warn_file = open(self.warn_filename, "wt")

        self._ID = "No ID"



    def __del__(self):
        self.log_file.close()
        if self.warn_filename != "empty": self.warn_file.close()


    def set_identifier(self, str):
        self._ID = str
        self.message(str, addLine = True)

    def message(self, str, addLine = False):
        now = datetime.datetime.now.strftime("%Y/%m/%d %H:%M:%S")
        str = now + "   LOG:   " + str + "\n"
        if addLine: str = "\n" + "-"*len(str) +"\n" + str
        self._log_print(str)
        
    def warning(self,str):
        now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self._log_print(now + "\033[1;33;48m  WARN:    "+str+"\033[1;37;0m\n")
        str = now + "  WARN: " +self._ID+"    " + str + "\n"
        self._warn_print(str)

    def error(self,str):
        now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self._log_print(now + "\033[1;31;48m ERROR:    "+str+"\033[1;37;0m\n")
        str = now + " ERROR: " + self._ID+":    " + str + "\n"
        self._warn_print(str)
        raise NameError(str)
    
    def _log_print(self,str):
        print(str)
        self.log_file.write(str)

    def _warn_print(self,str):
        if self.warn_filename != "empty": self.warn_file.write(str)
    
