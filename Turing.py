from re import *

class Turing():
	def __init__(self):
		self.tape = ['B']*10
		self.rules = {}
		self.condition = 'q1'

	def new_data(self, line):
		if len(line) > 1000:
			print('Too long data')
		for i in range(len(line)):
			self.tape[i] = line[i]

	def new_commands(self, line):
		a, b = line.split('->')
		self.rules[a] = b

	def do_commands(self):
		i = 1
		while True:
			command = self.tape[i] + self.condition 
			self.tape[i] = self.rules[command][0]
			if search('STOP', self.rules[command]):
				self.condition = 'STOP'
			else:
				self.condition = search('q[0-9]', self.rules[command]).group(0)
			if self.rules[command][-1] == 'R':
					i+=1
			elif self.rules[command][-1] == 'L':
				i-=1
				break
			if self.condition == 'STOP':
				break

task = Turing()
task.new_data(input('print your tape\n'))
number_of_commands = int(input('print number of commands\n'))
for i in range(number_of_commands):
	task.new_commands(input())
task.do_commands()
print(*task.tape)


#It is not final variant
