import cv2
import time
import schedule
import sqlite3

class CameraCapture:
	def _init_(self):
		print("Camera Capture Start!")
		self.Paths = "/Rose/CameraCapTempData/"
		self.con = sqlite3.connect('CameraCapture.db').cursor()

	def CameraCap(self):
		self.cap = cv2.VideoCapture(0)
		rets, binary = self.cap.read()
		cv2.imwrite(self.Paths + str(time.time()), binary)
		self.cap.release()

	def WalkDirs(self,Paths):
		files = []
		for roots, dirs, filenames in os.walk(Paths)
				files.append(filenames)
		return files

	def WalkCameraCapture(self):
		for i in self.WalkDirs(self.Paths):
			TextInPicture = pytesseract.image_to_string(Image.open(self.Paths + str(i)))
			self.con.execute('insert into PicTexTemp (PicText) values (?)',( TextInPicture ))
			os.remove(self.Paths + str(i))

	def main(self):
		schedule.every(1).seconds.do(CameraCap)
		schedule.every(10).seconds.do(WalkCameraCapture)
