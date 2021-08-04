import platform
import os

operating_system = platform.system()

if operating_system == 'Linux':
    path = os.getcwd() + '/chromedriver/chromedriver_linux/chromedriver'
    print(path)
elif operating_system == 'Windows':
    path = os.getcwd() + '/chromedriver/chromedriver_win/chromedriver'
elif operating_system == 'Darwin':
    path = os.getcwd() + '/chromedriver/chromedriver_mac64/chromedriver'
else:
    raise OSError(f'Unsupported operating system.Expected: Linux, Windows, or Darwin')
