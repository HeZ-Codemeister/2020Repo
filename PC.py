class CPU :
	def __init__(self, name, function = "Business") :
		self.name = name
		self.function = function 
	def cpu_benchmark(self) :
		print(f"Processor  used for {self.function}")

class GPU :
	def __init__(self, name, function = "Business") :
		self.name = name
		self.function = function
	def gpu_benchmark(self) :
		print(f"Graphic card used for {self.function}")

class PC :
	def __init__(self) :
		self.cpu = CPU("AMD Ryzen 9", "Gaming")
		self.gpu = GPU("AMD R3")

CPU.cpu_benchmark(__init__)
