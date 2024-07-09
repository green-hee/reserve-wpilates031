from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://wpilates031.cafe24.com/index.php?mid=yeyak&act=dispYeyakOrder"
# url = "https://wpilates031.cafe24.com/index.php?mid=yeyak&act=dispYeyakOrder&date=20240712"
login_data_dir = '../user_data/wpilates031'
ID = 'id'
PW = 'pw'


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


# main
driver = webdriver.Chrome(options=options)
driver.get(url)
login(ID, PW)
