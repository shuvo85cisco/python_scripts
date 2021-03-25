import pyAesCrypt
from os import stat, remove

bufferSize = 64 * 1024
password = "Password"

with open("sample.txt", "rb") as fIn:
	with open("sample.txt.aes", "wb") as fOut:
		pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

encFileSize = stat("sample.txt.aes").st_size
