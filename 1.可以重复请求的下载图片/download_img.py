

import os
import requests
import urllib.request

from retrying import retry
from urllib.error import URLError
import os



def retry_if_io_error(exception):
    return isinstance(exception,URLError)

#  重复请求

class DownloadIMG():

    @retry(retry_on_exception=retry_if_io_error)
    def exec(self,url,filename):
        imgName = self.make_filename(filename)
        self.download_image(url,imgName)
        print("{0} :  ----  OK  ---- ".format(filename))


    # 画像をダウンロードする
    def download_image(self,url,imgPath):
        urllib.request.urlretrieve(url,imgPath)

    # 画像のファイル名を決める
    def make_filename(self,filename):
        image_path = os.path.join(os.getcwd(),"images")
        if bool(os.path.exists(image_path)) != True:
            os.mkdir("images")

        imgName = filename + ".png"
        fullpath = os.path.join(image_path, imgName)
        return fullpath






if __name__ == "__main__":
    a = "https://rpcx.io/img/logo.png"
    b = "rpcx"
    c = DownloadIMG()
    c.exec(a,b)
