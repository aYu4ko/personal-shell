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
            if cmd[5:] in valid_cmds:
                print(f"{cmd[5:]} is a shell builtin")
            else:
                print(f"{cmd[5:]}: not found")
        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
