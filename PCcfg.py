class CPU :
	def __init__(self, name = "AMD Ryzen 9", function = "Gaming") :
		self.name = name
		self.function = function 
	def get_info_cpu(self) :
		print(f"Processor card ({self.name}) used for {self.function}")

class GPU :
	def __init__(self, name = "AMD R3" , function = "Business") :
		self.name = name
		self.function = function
	def get_info_gpu(self) :
		print(f"Graphic card ({self.name}) used for {self.function}")

class PC:
	def __init__(self, type_pc):
		self.type_pc = type_pc
		self.CPU = CPU()
		self.GPU = GPU()
	def get_info(self):
		print(f"This PC used for {self.type_pc}.Its powered by {self.CPU} and {self.GPU}")

PCgaming = PC("Gaming")
PCgaming.get_info()
PCgaming.CPU.get_info_cpu()
PCgaming.GPU.get_info_gpu()
