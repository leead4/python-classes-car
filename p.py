# import sys

class Cars():
	def __init__(self):
		self.make_list = list()
		self.model_list = list()
		self.show_dict = dict()

	def read_makes(self):
		with open('cars-makes.txt', 'r') as car_make:
			for cars in car_make:
				# print(cars)
				self.make_list.append(cars[:-1])
			return self.make_list
			# self.make_list.append(car_make.read())
			# print(make_list)
			# print(car_make.read(self))

	def read_models(self):
		with open('cars-models.txt', 'r') as car_model:
			for potato in car_model:
				self.model_list.append(potato[:-1])
			return self.model_list
			# print(car_model.read(self))

	def make_key(self):

		self.read_models()
		self.read_makes()



		self.show_dict = self.show_dict.fromkeys(self.make_list, "string")

		# print("showdict", self.show_dict)

		for key, value in self.show_dict.items():

			for model in self.model_list:
				if model[0] == key[0]:
					mod_len = len(model) 
					clean_model = model[2:mod_len]
					self.show_dict[key] = [clean_model]
					# print("val", self.show_dict[key])
					# print("this value", this_value)
					# print("value", value)
		print("new dict", self.show_dict)

demo = Cars()
demo.make_key()


	

