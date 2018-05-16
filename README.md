## Starbucks WiFi auto-connector
Check wifi connectivity when accessing WiFi @ Starbucks
and re-login if necessary to make life easier.

### Prerequisite
- OSX
- Chrome

Make sure the Starbucks Wifi is at the top of your Wifi List. 

![image](images/wifi-setting.png)

#### Environment setting
Install dependencies inside the repo by using

Conda:
```commandline
conda create -f environment.yaml
```
Pip:
```commandline
pip install -r requirements.txt
```


### Usage
Open your CLI, direct to the repo and run
```commandline
python keep_wifi_alive.py
```

and you're done.

### Future Work
- args 設定 check 間隔
- chrome driver 過期怎麼辦？
- 不同國家的starbuck能用嗎？


### References
- [Checking network connection](https://stackoverflow.com/questions/3764291/checking-network-connection)
- [Turn on/off Wifi on OSX](https://stackoverflow.com/questions/37313958/turn-on-off-wifi-with-python-on-osx)
- [Check whether HTTP request is redirected](https://stackoverflow.com/questions/13482777/when-i-use-python-requests-to-check-a-site-if-the-site-redirects-me-to-another)