# johnCrack

## 环境

linux系统，已经安装了 `John`

## Usage

```
usage: johnCrack.py <hash_file>

example:
	python .\johnCrack.py .\demo\hash
```

## 演示

1. 生成hash

```
$ zip2john demo/exp.zip > demo/hash
ver 2.0 exp.zip/exp.txt PKZIP Encr: TS_chk, cmplen=58, decmplen=44, crc=9CEAF20F ts=A64E cs=a64e type=8
```

2. 开始爆破

```
$ python3 johnCrack.py demo/hash
```

**运行结果：**

```
$ john --incremental:Alnum --min-length=1 --max-length=4 demo/hash
Using default input encoding: UTF-8
Will run 20 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
0g 0:00:00:00 DONE (2023-05-28 12:01) 0g/s 31954Kp/s 31954Kc/s 31954KC/s VPQn..XQQ
Session completed.

$ john --incremental:LowerNum --min-length=5 --max-length=5 demo/hash
Using default input encoding: UTF-8
Will run 20 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
0g 0:00:00:01 DONE (2023-05-28 12:01) 0g/s 43500Kp/s 43500Kc/s 43500KC/s x9o69..x9wvx
Session completed.

$ john --incremental:UpperNum --min-length=5 --max-length=5 demo/hash
Using default input encoding: UTF-8
Will run 20 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
0g 0:00:00:01 DONE (2023-05-28 12:01) 0g/s 54474Kp/s 54474Kc/s 54474KC/s X5KXA..XQWQF
Session completed.

$ john --incremental:Digits --min-length=6 --max-length=8 demo/hash
Using default input encoding: UTF-8
Will run 20 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
0g 0:00:00:02 DONE (2023-05-28 12:01) 0g/s 50454Kp/s 50454Kc/s 50454KC/s 73654101..73673952
Session completed.

$ john --wordlist=/mnt/c/Users/97766/Downloads/WSL/johnCrack/wordlists/Byxs20_top2w5.txt demo/hash
Using default input encoding: UTF-8
Will run 20 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
1g 0:00:00:00 DONE (2023-05-28 12:01) 33.33g/s 812666p/s 812666c/s 812666C/s ..sunyanzi
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
Loaded 1 password hash (PKZIP [32/64])
<password>       (exp.zip/exp.txt)
```

3. 重复运行的话

```
$ python3 johnCrack.py demo/hash
```

```
$ john --incremental:Alnum --min-length=1 --max-length=4 demo/hash
Using default input encoding: UTF-8
没有需要攻击的hash, 自动帮您运行 john --show <hash_file>

exp.zip/exp.txt:<password>:exp.txt:exp.zip::demo/exp.zip

1 password hash cracked, 0 left
```

## 补充

### 爆破的流程：

1. 首先使用掩码爆破：

```
1~4位 字符集：a-z,A-Z,0-9
5位 字符集: a-z, 0-9
5位 字符集: A-Z, 0-9
6~8位 字符集: 0-9
```

2. 再使用字典爆破：

```
Byxs20_top2w5.txt
Byxs20_top10w.txt
```

`john` 爆破成功结果会保存在 `~/.john/john.pot` 文件中

