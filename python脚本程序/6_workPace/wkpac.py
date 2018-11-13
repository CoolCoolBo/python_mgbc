from subprocess import call 
import os
from sconfig import CONFIGS


class WorkSpace:

	def __init__(self, c):
		self.folders = c['folders']
		self.name    = c['name']
		self.target  = c['target']

	def switch(self):
		for f in os.listdir(self.target):
			if f.endswith('_wspc'):
				path = self.target + f
				os.remove(path)
		# mklink
		for source in self.folders:
			real_target = self.target + source.split('/')[-1] + '_wspc'
			commands = ['ln', '-s', source, real_target]
			print(commands)
			call(commands)


workspaces = [WorkSpace(c) for c in CONFIGS]

choice = input("Choose your workspace: ")
for w in workspaces:
	if w.name == choice:
		w.switch()