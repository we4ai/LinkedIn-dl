# LinkedIn Courses Downloader

This repository provides a script that can be directly used to download courses for offline access from LinkedIn (if you have a premium subscription).

Here's the list of python packages that are required
- Selenium python
- requests
- time



Approach:
1. Given:course url, login credentials
2. Bot Starts: Open that page
3. Start downloading videos one by one with a gap of 0-60 seconds delay for each video


Steps :
1. Start terminal and change to project directory
2. Check this thread: [link](https://stackoverflow.com/questions/51214668/python-selenium-how-to-use-debugger-address-option-in-chrome-driver-for-remote). 
Execute: 
```

mkdir chrome_debug
chrome.exe -remote-debugging-port=9014 --user-data-dir="PATH_OF_chrome_debug_directory"`

```
3. This will fire a new instance of chrome. Consider logging in to your LinkedIn account and accept chrome's save credentials option. 
4. Mention course url in course_dl.py file. 
5. Execute course_dl.py file to download the course videos. 