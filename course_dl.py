from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webbrowser
import os
import requests

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")

#Change chrome driver path accordingly
chrome_driver = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)


from time import sleep

# driver.refresh()
def get_video_url(driver):
    return driver.find_element_by_xpath('//video').get_attribute('src')

def download_video(url):
    r = requests.get(url, allow_redirects=True)


def get_course_url(url):
    return url.split('learning/')[0], url.split('learning/')[1].split('/', 1)[0]  #'introduction-to-data-science-2'


def DownloadFile(url, i,videotitle,learningpath,course_name):
    if learningpath:
        local_filename = './{}/'.format(learningpath)+course_name+'/{}-{}.mp4'.format(str(i),videotitle)
    else:
        local_filename = './'+course_name+'/{}-{}.mp4'.format(str(i),videotitle)
    print(local_filename)
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    print("Successfully Saved the file: "+ local_filename)
    return

sleep(5)
#video: //video/@src
#urls: //li/a/@href

def get_path(learningpath):
    try: 
        if "https://www.linkedin.com/learning/paths/" not in path:
            learningpath = "https://www.linkedin.com/learning/paths/become-a-django-developer"
        driver.get(learningpath)
        linkedin_url, path_name = learningpath.split("/learning/paths/")
        sleep(10)
        course_urls = driver.find_elements_by_xpath("//h3/a")
        li = []
        li = [ url.get_attribute("href") for url in course_urls ]
        [get_course(course.split("?")[0],path_name) for course in li]
        return "OK"
    except Exception as e:
        print(e)
        return "ERR"

def get_course(course_url, learningpath=""):
    try: 
        if "https://www.linkedin.com/learning/" not in course_url:
            course_url = "https://www.linkedin.com/learning/introduction-to-data-science-2/beginning-your-data-science-exploration?autoAdvance=true&autoSkip=false&autoplay=true&resume=true"
        driver.get(course_url)
        linkedin_url, course_url = get_course_url(course_url)
        sleep(10)
        lesson_urls = driver.find_elements_by_xpath("//li/a")
        li = []
        for url in lesson_urls:
            url = url.get_attribute("href")
            if course_url in url and "quiz" not in url:
                li.append(url)
        video_urls = []
        if learningpath != "":
            if not os.path.exists(learningpath):
                os.mkdir(learningpath)
            if not os.path.exists("{}/{}".format(learningpath,course_url)):
                os.mkdir("{}/{}".format(learningpath,course_url))
        else:
            if not os.path.exists(course_url):
                os.mkdir(course_url)
        for i, url in enumerate(li):
            print("Figuring out this url ===> ")
            print(url)
            video_title = url.split("/learning/")[1].split("?")[0].split("/")[1]
            print("PART ",i,":",video_title)
            driver.get(url)
            sleep(10)
            video_url = get_video_url(driver)
            video_urls.append(video_url)
            print(video_url)
            DownloadFile(video_url, i,video_title, learningpath,course_url)
        return "OK"
    except Exception as e:
        print(e)
        return "ERR"
"""

Approach:
1. Given:course url, login credentials
2. Bot Starts: Open that page
3. Start downloading videos one by one with a gap of 0-60 seconds delay for each video

"""
def continueusing():
    print("ENTER Y or y to continue, type anything else to exit...")
    cont = input().strip()
    if cont in ['Y','y']:
        return True
    else:
        return False


repeat = True
while repeat:
    print("Enter 1 to download course, 2 to download Learning Path")
    download_type = int(input().strip())
    if download_type == 1:
        print("provide course url")
        course_url=input().strip()
        print("COURSE DOWNLOAD STATUS :",get_course(course_url))
        repeat = continueusing()
    if download_type ==2:
        print("provide learning path url")
        path=input().strip()
        print("PATH DOWNLOAD STATUS :",get_path(path))
        repeat = continueusing()



# exec /usr/bin/google-chrome -remote-debugging-port=9014 --user-data-dir="/home/kanika/projects/linkedincopyvideos/LinkedIn-dl/chrome_debug"`
