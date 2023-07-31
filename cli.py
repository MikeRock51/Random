import cmd

class MyCmd(cmd.Cmd):
    # prompt = '> '
    history = []
    
    def precmd(self, line):
        self.history.append(line)
        return line
    
    def do_hello(self, arg):
        print('Hello,', arg)
    
    def do_quit(self, arg):
        print("Do quit exitting")
        return True

    def do_EOF(self, arg):
        return True
    
    def postcmd(self, stop, line):
        print('Command executed:', line)
        return stop
    
if __name__ == '__main__':
    MyCmd().cmdloop()

