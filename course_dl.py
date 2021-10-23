from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webbrowser
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")

#Change chrome driver path accordingly
chrome_driver = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

from time import sleep

#sleep(3*60*60)

sleep(5)
#video: //video/@src
#urls: //li/a/@href

"""

Approach:
1. Given:course url, login credentials
2. Bot Starts: Open that page
3. Start downloading videos one by one with a gap of 0-60 seconds delay for each video

"""
print("provide course url")
course_url=input().strip()
try: 
    if "https://www.linkedin.com/learning/" not in course_url:
        course_url = "https://www.linkedin.com/learning/introduction-to-data-science-2/beginning-your-data-science-exploration?autoAdvance=true&autoSkip=false&autoplay=true&resume=true"
    driver.get(course_url)

    def get_course_url(url):
        return url.split('learning/')[0], url.split('learning/')[1].split('/', 1)[0]  #'introduction-to-data-science-2'

    linkedin_url, course_url = get_course_url(course_url)
    # def click_next_video(url):

<<<<<<< HEAD
    sleep(10)

    # driver.refresh()
    def get_video_url(driver):

        return driver.find_element_by_xpath('//video').get_attribute('src')


=======
linkedin_url, course_url = get_course_url(course_url)
# def click_next_video(url):

sleep(10)

# driver.refresh()
def get_video_url(driver):
    return driver.find_element_by_xpath('//video').get_attribute('src')

def download_video(url):
    r = requests.get(url, allow_redirects=True)
>>>>>>> effefc7b7d809b3583e98cd4f413a02c02f88818

    def download_video(url):
        r = requests.get(url, allow_redirects=True)

    import requests
    #from tqdm import tqdm

    def DownloadFile(url, i):
        local_filename = './'+course_url+'/'+course_url+"-"+str(i)+".mp4"
        r = requests.get(url)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        print("Successfully Saved the file: "+ local_filename)
        return

    print(linkedin_url)

    lesson_urls = driver.find_elements_by_xpath("//li/a")
    print("====================")


<<<<<<< HEAD
    #print(lesson_urls)
    print("====================")
=======
li = []
for url in lesson_urls:
    url = url.get_attribute("href")
    if course_url in url and "quiz" not in url:
        li.append(url)
        #print(url)
>>>>>>> effefc7b7d809b3583e98cd4f413a02c02f88818

    li = []
    for url in lesson_urls:
        url = url.get_attribute("href")
        if course_url in url and "quiz" not in url:
            li.append(url)
            #print(url)


    # print(li)

<<<<<<< HEAD
    video_urls = []
    import os
    if not os.path.exists(course_url):
        os.mkdir(course_url)

    for i, url in enumerate(li):
        print("Figuring out this url ===> ")
        print(url)
        driver.get(url)
        sleep(10)
        video_url = get_video_url(driver)
        video_urls.append(video_url)
        print(video_url)

        DownloadFile(video_url, i)
=======
for i, url in enumerate(li):
    print("Figuring out this url ===> ")
    print(url)
    driver.get(url)
    sleep(10)
    video_url = get_video_url(driver)
    video_urls.append(video_url)
    print(video_url)
    #DownloadFile(video_url, i)
    print("VIDEO URLS: ")
    print(video_urls)
    print("Trying to loop")
>>>>>>> effefc7b7d809b3583e98cd4f413a02c02f88818

        print("VIDEO URLS: ")
        print(video_urls)
        print("Trying to loop")

<<<<<<< HEAD

except Exception as e:
    print(e)
# exec /usr/bin/google-chrome -remote-debugging-port=9014 --user-data-dir="/home/kanika/projects/linkedincopyvideos/LinkedIn-dl/chrome_debug"`
=======
>>>>>>> effefc7b7d809b3583e98cd4f413a02c02f88818
