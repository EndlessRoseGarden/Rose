from PIL import ImageGrab
from PIL import Image
import os, schedule
import pytesseract
import sqlite3


class ScreenCap:
	def _init_(self):
		self.DataCon = sqlite3.connect('PicTexTemp.db').cursor()
		self.ScreenCapTempDatabase = "/Rose/ScreenCapTempDatabase/"
		self.main()

	def ScreenCap(self):
		ScreenCap = ImageGrab.grab()
		ScreenCap.save(self.ScreenCapTempDatabase,'png')

	def WalkDirs(self,Paths):
		files = []
		for roots, dirs, filenames in os.walk(Paths)
				files.append(filenames)
		return files

	def WalkPicture(self):
		for i in self.WalkDirs(self.ScreenCapTempDatabase):
			TextInPicture = pytesseract.image_to_string(Image.open(self.ScreenCapTempDatabase + str(i)))
			self.DataCon.execute('insert into PicTexTemp (PicText) values (?)',( TextInPicture ))
			os.remove(self.ScreenCapTempDatabase + str(i))

	def main(self):
		schedule.every(1).seconds.do(ScreenCap)
		schedule.every(10).seconds.do(WalkPicture)
