import _thread
import time
import pyautogui
import keyboard

pyautogui.FAILSAFE = False
w_blue = 'blue'
w_red = 'red'
w_yellow = 'yellow'
w_limit = 'limit'

keyColorMap = {
  'w': w_blue,
  'a': w_red,
  'e': w_yellow,
}

# 全局开关
open = True
def toggle():
  global open
  open = not open
  print('!! 运行状态', 'Y' if open else 'N')

# 识别技能状态
def parseRgb(r, g, b):
  if (r <= 74 and g >= 130 and g <= 196 and b >= 161 and b <= 237):
    return w_limit
  if (r >= 79 and g <= 54 and b <= 59):
    return w_red
  if (r >= 66 and g >= 57 and b <= 68):
    return w_yellow
  if (r <= 205 and g <= 208 and b >= 60):
    return w_blue

running = False
def selectCard(key):
  global running
  running = True

  expectColor = keyColorMap[key]
  print('!!', key, expectColor)
  # 非w按键要手动按一次
  if key != 'w':
    keyboard.send('w')
  # 等技能响应高亮
  time.sleep(0.3)
  start = time.perf_counter()
  while True:
    if not open:
      print('xx 中断选牌')
      running = False
      return
    # 技能选择超时
    passTime = time.perf_counter() - start
    if passTime > 3:
      print('?? 选牌超时')
      break
    # 技能颜色识别
    r, g, b = pyautogui.pixel(x, y)
    color = parseRgb(r, g, b)
    print('>> 识别', color)
    if color == w_limit:
      print('?? 蓝不够')
      break
    if color == expectColor:
      print('## 锁定 ##')
      keyboard.send('w')
      break
    time.sleep(0.2)
  print('------------')
  running = False

# 响应按键
def handleHotKey(key):
  if running or not open:
    return
  # 用另一个线程选牌
  _thread.start_new_thread(selectCard, (key,))

print('鼠标指向w技能正中间后, 按空格键确认')
keyboard.wait('space')
x, y = pyautogui.position()
print('设置', 'x', x, 'y', y)

print('w', keyColorMap['w'])
print('a', keyColorMap['a'])
print('e', keyColorMap['e'])
print('f1', '全局开关')
print('---- 开始监听按键 ----')
keyboard.add_hotkey('w', lambda: handleHotKey('w'))
keyboard.add_hotkey('a', lambda: handleHotKey('a'))
keyboard.add_hotkey('e', lambda: handleHotKey('e'))
keyboard.add_hotkey('f1', toggle)
keyboard.wait()
