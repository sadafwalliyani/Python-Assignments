import pyautogui
"""open opera and type pakistan
"""
print(pyautogui.position())

pyautogui.moveTo(34,1044)
pyautogui.click() 
pyautogui.write('This Pc', interval=0.25)
pyautogui.moveTo(303,222)
pyautogui.click()
pyautogui.moveTo(1171,582)
pyautogui.click()
# pyautogui.moveTo(593,79)
# pyautogui.click()               
# pyautogui.write('upwork', interval=0.25)

"""
Find position of mouse
"""
# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

# distance = 200
# while distance > 0:
#         pyauto.drag(distance, 0, duration=0.5)   # move right
#         distance -= 5
#         pyauto.drag(0, distance, duration=0.5)   # move down
#         pyauto.drag(-distance, 0, duration=0.5)  # move left
#         distance -= 5
#         pyauto.drag(0, -distance, duration=0.5)  # move up