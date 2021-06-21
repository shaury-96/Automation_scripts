def prank():
    from selenium import webdriver
    import time

    pn=input("Enter target phone no.")
    t=int(input("kitni bar message bhejna hai?"))
    browser=webdriver.Chrome("E:\\SOFTWARES\\chromedriver_win32\\chromedriver.exe")
    browser.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    po=browser.find_element_by_id("ap_email")
    po.send_keys(pn)
    cnt = browser.find_element_by_id("continue")
    cnt.click()
    time.sleep(20)
    fp=browser.find_element_by_id("auth-fpp-link-bottom")
    fp.click()
    time.sleep(20)
    cn = browser.find_element_by_id("continue")
    cn.click()
    n=t-1
    for i in range(n):

        ro=browser.find_element_by_link_text("Resend OTP")
        ro.click()

    browser.quit()
prank()



