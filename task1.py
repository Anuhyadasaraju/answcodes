
from seleniumbase import BaseCase
from prezent_task.CommonFunctions import CommonFunctions


class PrezentTask1(BaseCase):
    '''Task1 : Logging into the URL, fetching the current template name and doing sign out'''
    def testing_task1(self):
        #logging in
        CommonFunctions().do_login(self,"https://prezent-uatstaging.myprezent.com/signin","trial4.pf.noreply@abbvie.com","kiqjemkh")
        #Locating Teplate
        CommonFunctions().do_get_active_tmpl_name(self)
        #LogOut
        CommonFunctions().do_logout(self)



