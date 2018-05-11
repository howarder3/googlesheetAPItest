# googlesheetAPItest
> 主學習網站

https://city.shaform.com/blog/2016/03/19/gspread.html

> interminal 
> environment

```javascript

環境：
$ pyvenv-3.5 my_env
$ source my_env/bin/activate

套件：
$ pip install beautifulsoup4 gspread oauth2client pyOpenSSL

```

> git 

```javascript
  286  cd ./my_env
  319  git clone https://github.com/howarder3/googlesheetAPItest.git
  323  git log -3
  324  git status
  325  git add .
  326  git commit -m 'add env'
  331  git log
  332  git push
  343  source my_env/bin/activate
  
  後來原本環境壞了，改開新的env：
  384  python3 -m venv env
  385  source ./env/bin/activate
  387  python -m pip install oauth2client
  389  python -m pip install gspread
  390  python login.py 
  391  python update.py
  392  python -m pip install beautifulsoup4
```

> 處理時間(年月日時分秒)問題

https://stackoverflow.com/questions/30071886/how-to-get-current-time-in-python-and-break-up-into-year-month-day-hour-minu

> linux 找東西

https://blog.gtwang.org/linux/unix-linux-find-command-examples/

> linux 自動執行程式

http://linux.vbird.org/linux_basic/0430cron.php
https://blog.csdn.net/baidu_23966735/article/details/79193462
