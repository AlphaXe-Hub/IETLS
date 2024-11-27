from windows_toasts import WindowsToaster, Toast
import time

def notification(word):
    # Prepare the toaster for bread (or your notification)
    toaster = WindowsToaster('IETLS')
    # Initialise the toast
    newToast = Toast()
    # Set the body of the notification
    newToast.text_fields = word
    # And display it!
    toaster.show_toast(newToast)
def main():
    print("雅思乱序表 启动    tip：在下方输入时间间隔按回车开始。     若想关闭直接按ctrl+c 或者关闭该命令框")
    second = int(input("设定间隔时常(单位秒): "))
    with open('word.txt', 'r',encoding='utf-8') as file: 
        lines = file.readlines() 
        for line in lines: 
            print(line)
            notification(list(filter(None,line.split('%'))))
            time.sleep(second)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('error: ',e)
        input("按任意键继续")

