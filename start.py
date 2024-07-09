from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://wpilates031.cafe24.com/index.php?mid=yeyak&act=dispYeyakOrder"
# url = "https://wpilates031.cafe24.com/index.php?mid=yeyak&act=dispYeyakOrder&date=20240712"
login_data_dir = '../user_data/wpilates031'
ID = 'id'
PW = 'pw'
DATE = '2024-07-09'
TIME = '2030'


options = Options()
# options.add_argument("user-data-dir="+login_data_dir)
options.add_experimental_option("detach", True)

# 로그인
def login(id: str, pw: str):
    # <input type="text" class="form-control" value="" name="id" placeholder="회원 아이디">
    # <input type="password" class="form-control" value="" name="passwd" placeholder="패스워드">
    input_id = driver.find_element(By.NAME, 'id')
    input_id.send_keys(id)
    input_pw = driver.find_element(By.NAME, 'passwd')
    input_pw.send_keys(pw)
    input_pw.send_keys(Keys.RETURN)


def reserve(date: str, time: str):
    enables = driver.find_elements(By.CSS_SELECTOR, f'li.li-data[data-vdate="{date}"][data-classtime="{time}"]')
    print(f"get_enable : {len(enables)}")

    if not enables:
        return False
    
    for enable in enables:
        if not enable.get_attribute('usedata'):
            print('already reserved')
            return True

    # 확인버튼 클릭
    enables[0].click()
    print("click!!")
    return True


# main
driver = webdriver.Chrome(options=options)
driver.get(url)
login(ID, PW)

# 다음주 버튼 클릭
# move_next_week = driver.find_element(By.LINK_TEXT, '다음주').click()

result = reserve(DATE, TIME)
print(f"result : {result}")




# <li class="li-data " data-id="412" data-unit="3" data-usedate="20240708" data-vw="월" data-vtitle="황톨" data-vdate="2024-07-08" data-vclasstitle="바렐" data-classtime="2030" data-am="오후" data-h="8" data-m="30">&nbsp;</li>
