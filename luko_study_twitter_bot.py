from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(10)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(5)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('r-3s2u2q')
            links = [elem.get_attribute('href') for elem in tweets]
            # bot.get('https://twitter.com/'+links)
            # print('{}'.format(links))
            for link in links:
                if link != None:
                    bot.get('{}'.format(link))
                    try:
                        #bot.find_elements_by_class_name('css-1dbjc4n r-sdzlij r-1p0dtai r-xoduu5 r-1d2f490 r-xf4iuw r-u8s1d r-zchlnj r-ipm5af r-o7ynqc r-6416eg').click()
                        #bot.find_element_by_css_selector('div.css-1dbjc4n.r-13awgt0.r-12vffkv div.css-1dbjc4n.r-13awgt0.r-12vffkv div.css-1dbjc4n.r-18u37iz.r-1pi2tsx.r-13qz1uu.r-417010 main.css-1dbjc4n.r-1habvwh.r-16y2uox.r-1wbh5a2:nth-child(4) div.css-1dbjc4n.r-150rngu.r-16y2uox.r-1wbh5a2.r-rthrr5 div.css-1dbjc4n.r-aqfbo4.r-16y2uox div.css-1dbjc4n.r-1oszu61.r-1niwhzg.r-18u37iz.r-16y2uox.r-1wtj0ep.r-2llsf.r-13qz1uu div.css-1dbjc4n.r-14lw9ot.r-1tlfku8.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c:nth-child(1) div.css-1dbjc4n div.css-1dbjc4n:nth-child(2) div.css-1dbjc4n section.css-1dbjc4n div.css-1dbjc4n div.css-1dbjc4n.r-my5ep6.r-qklmqi.r-1adg3ll article.css-1dbjc4n.r-1udh08x div.css-1dbjc4n div.css-1dbjc4n.r-1j3t67a div.css-1dbjc4n:nth-child(3) div.css-1dbjc4n.r-1oszu61.r-1gkumvb.r-1efd50x.r-5kkj8d.r-18u37iz.r-ahm1il.r-a2tzq0:nth-child(4) div.css-1dbjc4n.r-18u37iz.r-1h0z5md.r-3qxfft.r-h4g966.r-rjfia:nth-child(3) div.css-18t94o4.css-1dbjc4n.r-1777fci.r-11cpok1.r-1ny4l3l.r-bztko3.r-lrvibr div.css-901oao.r-1awozwy.r-daml9f.r-6koalj.r-1qd0xha.r-a023e6.r-16dba41.r-1h0z5md.r-ad9z0x.r-bcqeeo.r-o7ynqc.r-clp7b1.r-3s2u2q.r-qvutc0 div.css-1dbjc4n.r-xoduu5 > div.css-1dbjc4n.r-wcu338.r-sdzlij.r-1p0dtai.r-xoduu5.r-1d2f490.r-xf4iuw.r-u8s1d.r-zchlnj.r-ipm5af.r-o7ynqc.r-6416eg').click()
                        #bot.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[3]/div[4]/div[3]/div[1]').click()
                        bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/article/div/div/div[3]/div[4]/div[3]/div/div/div/div').click()
                        time.sleep(5)
                    except Exception as ex:
                        ("Uncontrolled error: " + str(ex))
                        time.sleep(10)
        print ('The end of the script!')



ars = TwitterBot('vadzyo.protsiuk@gmail.com', 'luko_study1(9#')
ars.login()
ars.like_tweet('LvivIT')
