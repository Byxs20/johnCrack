import os
import sys
import subprocess


if len(sys.argv) == 1:
    print("Usage: python3 john_crack.py <hash_file>")
    exit()

def crack(command):
    global isCrack
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
    out = proc.stdout.read()
    lis = out.splitlines()
    
    if len(lis) > 1:
        if lis[1] == "No password hashes left to crack (see FAQ)":
            print("没有需要攻击的hash, 自动帮您运行 john --show <hash_file>\n")
            os.system(f"john --show {hash_file}")
            exit()
        else:
            isCrack = True
            print(out.rstrip("\r\n"))
    
    if isCrack:
        exit()

    print()

if __name__ == '__main__':
    commands = [
        "--incremental:Alnum --min-length=1 --max-length=4".split(" "), # 1~4 | a-z, A-Z, 0-9
        "--incremental:LowerNum --min-length=5 --max-length=5".split(" "), # 5 | a-z, 0-9
        "--incremental:UpperNum --min-length=5 --max-length=5".split(" "), # 5 | A-Z, 0-9
        "--incremental:Digits --min-length=6 --max-length=8".split(" "), # 6~8 | 0-9
    ]

    isCrack = False
    hash_file = sys.argv[1]
    
    for command in commands:
        run_command = ["john"]
        for i in command:
            run_command.append(i)
        run_command.append(f"{hash_file}")
        print(f"$ {' '.join(run_command)}")
        crack(run_command)

    baseDir = os.path.dirname(os.path.abspath(__file__))
    wordlistsPath = baseDir + "/wordlists/%s"

    for wordlistsName in ["Byxs20_top2w5.txt", "Byxs20_top10w.txt"]:
        run_command = ["john", f"--wordlist={wordlistsPath % wordlistsName}", f"{hash_file}"]
        crack(run_command)
