import signal as _signal
import threading as _threading
import time as _time

from pydrive.auth import GoogleAuth as _GoogleAuth
from pydrive.drive import GoogleDrive as _GoogleDrive


class Drive_Communicator(_threading.Thread):
    
    def __init__(self, fileId):
        super().__init__()
        self.fileId = fileId

        _signal.signal(_signal.SIGINT, self.sendData)
        _signal.signal(_signal.SIGTERM, self.sendData)

        self._setup()
        self.getData()
        self.start()

    def _setup(self):
        self.gauth = _GoogleAuth()

        self.gauth.LoadCredentialsFile("_credentials")
        if self.gauth.credentials is None:
            self.gauth.LocalWebserverAuth()
        elif self.gauth.access_token_expired:
            self.gauth.Refresh()
        else:
            self.gauth.Authorize()

        self.gauth.SaveCredentialsFile("_credentials")
        self.drive = _GoogleDrive(self.gauth)
        self.data_file = self.drive.CreateFile({'id': self.fileId})

    def getData(self):
        self._download()

    def sendData(self):
        self._upload()

    def _download(self):
        self.data_file = self.drive.CreateFile({'id': self.fileId})
        self.data_file.GetContentFile('data.json')
        self.data_file = None

    def _upload(self):
        self.data_file = self.drive.CreateFile({'id': self.fileId})
        self.data_file.SetContentFile('data.json')
        self.data_file.Upload()
        self.data_file = None

    def run(self):
        try:
            while True:
                self.sendData()
                _time.sleep(3600)
        except:
            self.data_file = None