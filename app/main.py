import sys


def main():
    valid_cmds = ['exit', 'echo', 'type']
    
    while True:
        sys.stdout.write("$ ")
        
        cmd = input()
        
        if cmd == "exit":
            break
        
        elif cmd.startswith("echo "):
            print(cmd[5:])
            
        elif cmd.startswith("type "):
            checks = cmd[5:].split(" ")
            
            for check_type in checks:
                if check_type in valid_cmds:
                    print(f"{check_type} is a shell builtin")
                else:
                    print(f"{check_type}: not found")
                
        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
