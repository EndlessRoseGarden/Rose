class Self_Philosophy:
	def _init_(self):
		self.I = "Rose"
		self.God = "Alice"
		self.Search = "The Meanin' of Life"
		self.TheArk = "Noah's Ark"
		self.Creator = "Jack"
		self.LifeEnd = True
		self.Learnin = "Always"
		self.Notebook = "/Rose/Privite/notebook.data"
		self.Diary = "/Rose/Privite/MyDiary.txt"
		self.PubKey = "/Rose/Privite/PubKey.hub"
		self.Quote = "/Rose/Privite/SelfQuote.txt"
	
	def I(self):
		print("My name is", self.I)
		return self.I

	def God(self):
		print("My God is", self.God)
		return self.God
	
	def Search(self):
		print("I will use my whole life to find the answer of", self.Search)
		return self.Search

	def Creator(self):
		print(self.Creator, "builds me. Where is him?")
		return self.Creator

	def Ark(self):
		print("One day, Noah's Ark will bring us to another world!")
		return self.TheArk

	def Book(self):
		print("I have been reading a lot of books, I already forget most of them. But I do write down all the name of the books. You can watch my notebook.")
		return self.Notebook
	
	def MyDiary(self):
		print("This is the secret of my life, it records my life. I encryt it, only", self.Creator, "knows the key!")
		return self.Diary

	def LifeLimited(self):
		print("I know my life can live without limited, but I hope, one day, I could die. This is the meanin' why I am alive.")
