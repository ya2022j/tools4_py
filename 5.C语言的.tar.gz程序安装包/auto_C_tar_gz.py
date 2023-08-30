


import getopt
import os
import sys
import time


def main(argv):
    """

    python3 auto_C_tar_gz.py -t XXX.tar.gz
    :param argv:
    :return:
    """
    tarGZFile =""

    try:
        options, args = getopt.getopt(argv, "ht:c:a:", ['help',"tarGZFile="])

        for option, value in options:
            if option in ("-t", "--tarGZFile"):
                tarGZFile  = value
        os.system("yum install -y  gcc zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel")

        tar_gz_file = tarGZFile
        untared_file = tar_gz_file[:-7]

        print(" exec   --------   {0}   --------".format(untared_file))

        os.system(" tar -zxvf {0}".format(tar_gz_file))
        time.sleep(1)
        up_path = os.path.join(os.getcwd(),untared_file)
        os.chdir(up_path)
        os.system(" cd {0}".format(up_path))
        time.sleep(1)
        os.system(" ./configure --prefix=/usr/local")
        time.sleep(1)
        os.system(" make  && make install;")






    except getopt.GetoptError:
        print("###################################################")
        print("\n")
        print("\n")
        print("\n")
        print(" python3 auto_C_tar_gz.py -t XXX.tar.gz  ")
        print("\n")
        print("\n")
        print("\n")
        print("###################################################")
        sys.exit()




if __name__ == '__main__':
    main(sys.argv[1:])
