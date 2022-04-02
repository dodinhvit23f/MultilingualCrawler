import pdb
import os
from selenium import webdriver
"""
hàm này dùng để tránh bị websites phát hiện là công cụ chạy test tự động
"""
def getChromeDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # đặt ngôn ngữ việt công cụ
    options.add_argument("--lang=vi")
    # tạo nơi lưu trữ thông tin user-cookie
    #options.add_argument("user-data-dir=C:\\User\\Admin\\AppData\\Google\\Chrome\\User Data\\")
    # loại bỏ các bảo vệ của chrome, và thông báo software auto ....
    options.add_argument("--disable-extensions");
    options.add_argument("--disable-security");
    options.add_argument("--no-sandbox");
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--allow-running-insecure-content");
    # đặt định dạng tiếng việt
    options.add_argument("accept-language=vi")
    # tránh nhận dạnh của các trang web là trình duyệt tự động.
    options.add_argument('--disable-blink-features=AutomationControlled')
    #options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    
    driver = webdriver.Chrome(os.path.abspath(os.getcwd()+"/chromedriver"),options= options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    #pdb.set_trace()
    return driver