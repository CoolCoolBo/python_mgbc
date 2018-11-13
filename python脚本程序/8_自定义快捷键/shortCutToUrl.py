# 获取键盘输入的快捷键 -->解析快捷键-->输出
from pynput.keyboard import Key, Listener, Controller
import threading
import time

class ComboListener:

	def __init__(self):
		self.cur_keys = []
		self._run()
		self.behavior = {"aaa": "Hello world",
					"bbb": "balalabalala",
					}

	def _on_press(self, key):
		try:
			self.cur_keys.append(key.char)
		except AttributeError:
			self.cur_keys.append(key.name)

	def get_combo(self):
		if len(self.cur_keys) >= 3:
			return self.cur_keys[-3:]

	def prase_combo(self):
		cur_keys = self.get_combo()
		if cur_keys:
			keys = ''.join(cur_keys)
			for e in self.behavior:
				if keys == e:
					return self.behavior[e]

	def _cleaner(self):
		while True:
			time.sleep(1)
			self.cur_keys.clear()

	def _run(self):
		l = Listener(on_press=self._on_press)
		l.daemon = True
		l.start()

		t = threading.Thread(target=self._cleaner)
		t.daemon = True
		t.start()

listener = ComboListener()
keyboard = Controller()
while True:
	mes = listener.prase_combo()
	if mes:
		print(mes)

