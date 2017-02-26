#! /usr/bin/env python

#def travel(distance):
#	print distance
#	return distance
import time
class travel():
	"""docstring for travel"""
	def __init__(self):
		#super(travel, self).__init__()
		self.distance = 0
		self.temps = 0
		self.listtemps=[0]
		self.listtemperatureE=[0]
		self.listtemperatureB=[0]
		self.cible = ""
		self.X = 0

	def get_distance(self):
		#self.distance = distance
		return self.distance

	def set_distance(self,ndistance):
		self.distance = ndistance
		#print ndistance
		#self.distance=ndistance



	def get_temps(self):
		#self.distance = distance
		return self.temps


	def set_temps(self,ntempss):
		self.temps = ntempss
		#print ntempss



	def get_listtemps(self):
		#self.distance = distance
		temps = 0.00
		self.X += 0.033
		#print "%3.2f"%self.X
		#temps = self.X / 60
		#print "%3.2f"%temps
		self.listtemps.append(self.X)
		return self.listtemps[:150]


	def set_listtemps(self,nlisttemps):
		#self.listtemps = alex

		self.listtemps.append(nlisttemps)
		#print self.listtemps[:150]
		#print ntempss



	def get_listtemperatureE(self):
		#self.distance = distance
		return self.listtemperatureE[-150:]


	def set_listtemperatureE(self,nlisttemperatureE):
		#self.listtemps = alex
		self.listtemperatureE.append(nlisttemperatureE)
		#print self.listtemperatureE[-150:]
		#print ntempss



	def get_listtemperatureB(self):
		#self.distance = distance
		return self.listtemperatureB[-150:]


	def set_listtemperatureB(self,nlisttemperatureB):
		#self.listtemps = alex
		self.listtemperatureB.append(nlisttemperatureB)
		#print self.listtemperatureB[-150:]
		##print ntempss

	def get_cible(self):
		#self.distance = distance
		return self.cible

	def set_cible(self,ncible):
		self.cible = ncible
		#print ndistance
		#self.distance=ndistance