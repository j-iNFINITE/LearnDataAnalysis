import cmd,multiprocessing,time
def keep_alive():
    while 1:
        print('aaaa')
        time.sleep(10)

class ee(cmd.Cmd):
    def do_1(self,line):
       print('bbb')
kee
if __name__ == '__main__':
    keep_alive_process = multiprocessing.Process(target=kee)
    keep_alive_process.start()
    ee().cmdloop()