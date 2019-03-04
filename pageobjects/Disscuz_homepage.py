from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time

class HomePage(BasePage):
#     定位

        username = (By.NAME, 'username')
        password = (By.NAME, 'password')
        login1=(By.CSS_SELECTOR,".fastlg_l button")


        moren_bankuai= (By.CSS_SELECTOR,".fl_tb h2 a")          #有问题

        biao=(By.ID,"subject")
        wen=(By.CSS_SELECTOR,".pt")

        first_fa=(By.CSS_SELECTOR,".bm_c button")

        # tui退出
        tui=(By.LINK_TEXT,"退出")
        # sha删除
        dele=(By.NAME,"moderate[]")
        shan=(By.LINK_TEXT,"删除")
        sure=(By.CSS_SELECTOR,".tm_c button")

        #管理中心
        guan=(By.LINK_TEXT,"管理中心")
        #管理登录
        guan_login=(By.CSS_SELECTOR,".loginform input")
        tijiao=(By.CSS_SELECTOR,".loginnofloat input")
        #论坛
        lun=(By.ID,"header_forum")
        #xinbankuai新版块
        add=(By.CSS_SELECTOR,".lastboard a")
        tj=(By.CSS_SELECTOR,".fixsel input")
        #刷新
        sh=(By.CSS_SELECTOR,".wp img")
        #xin新版块发帖
        new=(By.CSS_SELECTOR,".fl_row h2 a")
        again_fa=(By.CSS_SELECTOR,".bm_c button")
        hf=(By.CSS_SELECTOR,".area textarea")
        dj_huifu=(By.CSS_SELECTOR,".plc button")
#  搜索按钮
        sousuo_button=(By.CSS_SELECTOR,".scbar_btn_td button")
#  搜索框
        sousuo_wen=(By.CSS_SELECTOR,".scbar_txt_td input")
# #  点击搜索
#         dj_sousuo=(By.CSS_SELECTOR,".td_srchbtn button")
#   点击搜索内容
        result=(By.CSS_SELECTOR,".xs3 a")
#验证
        #yan_ti=(By.CSS_SELECTOR,".ts span")

#  发投票帖子
        dj_fatie=(By.CSS_SELECTOR,".mn img")
        dj_faToupiao=(By.LINK_TEXT,"发起投票")
        kuang1=(By.CSS_SELECTOR,".z span input")
        kuang2=(By.CSS_SELECTOR,".mbm input")
        kuang3=(By.CSS_SELECTOR,".mbm p:nth-child(2) input")
        kuang4=(By.CSS_SELECTOR,".mbm p:nth-child(3) input")
        ###kuang5=(By.CSS_SELECTOR,".area iframe")
#    发起投票
        fatoupiao=(By.CSS_SELECTOR,".mtm button")
#票
        piao1=(By.CSS_SELECTOR,".pvt label")
        piao1_bai=(By.CSS_SELECTOR,".pcht tr:nth-child(2)")
        piao2=(By.CSS_SELECTOR,".pcht tr:nth-child(3) label")
        piao2_bai=(By.CSS_SELECTOR,".pcht tr:nth-child(4)")
        piao3=(By.CSS_SELECTOR,".pcht tr:nth-last-child(3) label")
        piao3_bai=(By.CSS_SELECTOR,".pcht tr:nth-child(6)")


        n1 = "选项一"
        n2 = "选项二"
        n3 = "选项三"
#tou投
        tou=(By.CSS_SELECTOR,".pslt input")
        tj_tou=(By.CSS_SELECTOR,".pcht tr:nth-last-child(1) button")
#bio标题
        tou_biao=(By.CSS_SELECTOR,".ts span")



        #登录
        def search(self,user,pad):
            self.sendkeys(user, *self.username)
            self.sendkeys(pad, *self.password)
            time.sleep(3)
            self.click(*self.login1)
            time.sleep(5)

        def moren(self):
            self.click(*self.moren_bankuai)
            # self.driver.switch_to_window(self.driver.current_window_handle)
            # time.sleep(5)

        # 发表帖子
        def fa(self,biao,wen):
            self.sendkeys(biao,*self.biao)
            self.sendkeys(wen,*self.wen)
            self.click(*self.first_fa)

        #退出
        def logout(self):
            self.click(*self.tui)


        #删除帖子
        def delect(self):
            self.click(*self.dele)
            self.click(*self.shan)
            self.click(*self.sure)

        #guan管理中心
        def guanli_center(self):
            self.click(*self.guan)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(5)

        #管理员登录s
        def guanliyuan_login(self,login):
            self.sendkeys(login,*self.guan_login)
            self.click(*self.tijiao)
            time.sleep(5)
        #论坛
        def luntan(self):
            self.click(*self.lun)
        #添加新版块
        def new_bankuai(self):
            self.driver.switch_to_frame(0)       #  you有警告
            self.click(*self.add)
            self.click(*self.tj)
        def guanbi(self):
            self.driver.close()
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.click(*self.tui)
    #用户登录
        def again_search(self,user,pad):
            self.sendkeys(user, *self.username)
            self.sendkeys(pad, *self.password)
            time.sleep(3)
            self.click(*self.login1)
        def shua(self):
            self.click(*self.sh)
        def new_fa(self):
            self.click(*self.new)
        # def fasong(self):
        #     self.click(*self.again_fa)
        #回复
        def huifu(self,h):
            self.sendkeys(h,*self.hf)
            self.click(*self.dj_huifu)
        #点击搜索按钮
        def sousuo(self):
            self.click(*self.sousuo_button)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(5)
        #sou搜索内容
        def sousuoWen(self,s):
            self.sendkeys(s,*self.sousuo_wen)
        #点击搜索内容
        def Dresult(self):
            self.click(*self.result)
            self.driver.switch_to.window(self.driver.window_handles[2])
            time.sleep(5)
        def yanzheng(self):
            yan_ti=self.driver.find_element_by_css_selector(".ts span")
            return yan_ti.text

        #发投票帖子
        def fa_toupiao(self):
            self.click(*self.dj_fatie)
            time.sleep(3)
            self.click(*self.dj_faToupiao)
        def Writes(self,k1,k2,k3,k4):
            self.sendkeys(k1,*self.kuang1)
            self.sendkeys(k2, *self.kuang2)
            self.sendkeys(k3, *self.kuang3)
            self.sendkeys(k4, *self.kuang4)
            self.click(*self.fatoupiao)
            time.sleep(15)

        def Tou(self):
            self.click(*self.tou)
            self.click(*self.tj_tou)
        def Print(self):

            self.text(*self.piao1)
            self.text(*self.piao1_bai)
            self.text(*self.piao2)
            self.text(*self.piao2_bai)
            self.text(*self.piao3)
            self.text(*self.piao3_bai)
            self.text(*self.tou_biao)


"""
    def zhuti(self,k5):
        self.driver.switch_to_frame(0)
        self.sendkeys(k5,*self.kuang5)

"""





