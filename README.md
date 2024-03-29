<p align="center">
  <img width="350" height="350" src="https://raw.githubusercontent.com/sys113/negar/master/negar.png">
</p>

---
<div align="center">
  
![](https://img.shields.io/github/stars/SYS113/negar.svg)
![](https://img.shields.io/badge/language-python-orange.svg)
![](https://img.shields.io/github/forks/SYS113/negar.svg)
![](https://img.shields.io/github/release/SYS113/negar.svg)
![](https://img.shields.io/github/issues/SYS113/negar.svg)
![](https://img.shields.io/badge/license-MIT-informational.svg)
</div>

---
## *review*
<p align="center">
  <img src="https://raw.githubusercontent.com/sys113/negar/master/example/review.png">
</p>

---
## *what is <ins>negar</ins>*
*call <ins>negar</ins> module in your python source code and write error log & text log to a file</ins> ...<br />*

---
## *installation*

+ #### *install by pip*

      # linux
      
      sudo python3 -m pip install negar
      
      # windows
      
      py -m pip install negar
      
+ #### *install by setup.py*

      # linux
      
      sudo python3 -m pip install https://github.com/sys113/negar/archive/0.6.0.zip
      
      # windows
      
      py -m pip install https://github.com/sys113/negar/archive/0.6.0.zip

---
## *example*
+ #### text function &nbsp;&nbsp;&nbsp;&nbsp;
```python

# method one - good

import negar

print("start ...")

def test():
    a = 'sys113'
    return a

negar.text(f"'test' function return value is '{test()}'")

print("end ...")
```

```python

# method two - excellent

from negar import text

print("start ...")

def test():
    a = 'sys113'
    return a

text(text_log = f"'test' function return value is '{test()}'" , save = "file.txt" , size = 1 , title = "Project Logs" , time = False , line = True , date = True)

print("end ...")
```
<p align="center">
  <img src="https://raw.githubusercontent.com/sys113/negar/master/example/text.png">
</p>

+ #### error function   &nbsp;&nbsp;
```python

# method one - good

import negar

def project():
    print("hi!")
    X

try:
    project()
except:
    negar.error()
```

```python

# method two - excellent

from negar import error

def project():
    print("hi!")
    X

try:
    project()
except:
    error(size = 1 , save = 'error.txt' , title = "Project Errors" , time = True , line = True , date = True)
```

<p align="center">
  <img src="https://raw.githubusercontent.com/sys113/negar/master/example/error.png">
</p>

---
## *description*
  + #### *log_text*
    ```python
      # write 'log_text' to log file
      log_text = 'negar' 
    ```
  + #### *line*
    ```python
      # set 'Flase' and 'True' value for show line python file in log file , default is False ... 
      line = True
    ```

  + #### *date*
    ```python
      # set 'Flase' and 'True' value for show date in log file , default is True ... 
      date = True
    ```

  + #### *time*
    ```python
      # set 'Flase' and 'True' value for time in log file , default is True ... 
      time = True
    ```
    
  + #### *save*
    ```python
      # write log to 'negar-log.txt'
      save = 'negar-log.txt' 
    ```
  + #### *size*
    ```python
      # set 'size' for log file 
      size = 2
    ```
  + #### *title*
    ```python
      # set 'title' for write custom log file title , defult is 'city < country < continent | user name | os > os version > architecture'
      title = 'log file title'
    ```
---

## *tips*
+ *log file default size is 2 ...*
+ *log file size range is 1 ... 5 number ...*
+ *maximum size of python file name support is 15 character ...*
+ *maximum number to numbering lines support is 9999999 ...*
+ *maximum python source code line number support is 999999 ...*
+ *default log file name is log.txt ...*
+ *previously defined log file size can'not be resized!<br />*
---
## *copyright*
*copyright <ins>SYS113</ins> - <ins>2019</ins>.*

---
## *license* 
*<ins>MIT</ins> license , please see <ins>LICENSE</ins> file.*

---
## *donate* 
+ *for <ins>iranian</ins> users &nbsp; :  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <ins>  id pay </ins> &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://idpay.ir/sys113*
+ *for <ins>global</ins> users &nbsp; : &nbsp;<ins>BTC wallet id</ins>&nbsp; - &nbsp; 149JgUmFqG6MvFg79Ldrvdk2bN35ByhMuw*
---
## *contact me* 
* *[email](mailto:051.SYS113@gmail.com)*
* *[telegram](https://t.me/SYS113/)*
* *[instagram](https://instagram.com/sys113/)*
---
## *thanks*
+ *mohamad moradiyani for negar module logo*
+ *Hamed 169 for optimize negar module source code*
---
## *last word*
*hope this is <ins>negar</ins> useful to you and enjoy it.*

---
