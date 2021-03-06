import os
from modules.tf_model import run



class Model:

	def __init__(self, name=None, backbone=None):
		self.name = name
		self._backbone = backbone
		self._dataset = None


	#setup dataset name
	def set_dataset(self, dataset):
		self._dataset = dataset

	def set_model(self):
		
		return 0

	def train(self):
		run(self.name, self._backbone, self._dataset)

