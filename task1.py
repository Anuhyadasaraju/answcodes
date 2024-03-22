from seleniumbase import BaseCase
from prezent_task.common_functions import CommonFunctions

'''Task1 : Logging into the URL, fetching the current template name and doing sign out'''

class PrezentTask1(BaseCase):
    def testing_task1(self):

        #logging in
        CommonFunctions().do_login(self,"https://prezent-uatstaging.myprezent.com/signin","trial4.pf.noreply@abbvie.com","kiqjemkh")
        print("\n----Logged In----")

        #Locating Teplate
        self.click(".right-nav-item.profile-link", timeout=15)
        self.click("#templates-tab", timeout=10)
        self.wait_for_element_present(".v-card__title.cardTitleForViewer", timeout=15)
        name = self.find_element(".v-card__title.cardTitleForViewer", timeout=10)
        print("Selected Template is: " + name.text)

        #LogOut
        CommonFunctions().do_logout(self)
        print("----Sign Out----")



