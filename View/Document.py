import os
from wand.image import Image

class DocumentRead:
		def _init_(self):
			self.TempPath = "/data/Temp/document/"
			self.Paths = "/data/document/"

		def DirWalk(self, Paths):
			files = []
			for roots, dirs, filenames in os.walk(Paths)
					files.append(filenames)
			return files

		def PDF_to_Picture(self,filenames,fileArray):
			for i in fileArray:
				os.mkdir(self.TempPath + str(i))
				with Image(filename = i) as Picture:
						with Picture.convert('jpeg') as Img:
								Img.save(filename=self.TempPath+str(i))

		def Doc_to_Picture(self):
			