# PiCar 
# 安装  pigpio 
$ sudo apt-get install pigpio python-pigpio
# 配置  pigpiod 自启动 
$ sudo crontab -e
        @reboot pigpiod &
# 配置 GPIO PIN 
L298N MOTOR PIN (GPIO.BOARD) 
IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15
SERV
SERVO1 = 13
SERVO2 = 19
