from seleniumbase import BaseCase
from answcodes.prezent_task.common_functions import CommonFunctions

'''Task1 : Logging into the URL, fetching the current template name and doing sign out'''

class PrezentTask1(BaseCase):
    def testing_task1(self):

        #logging in
        CommonFunctions().do_login(self,"https://prezent-uatstaging.myprezent.com/signin","trial4.pf.noreply@abbvie.com","kiqjemkh")
        print("\n----Signed In----")

        #Locating Teplate
        print("Clicking on top right - Profile icon")
        self.click(".right-nav-item.profile-link", timeout=15)
        print("Clicking on Templates tab")
        self.click("#templates-tab", timeout=10)
        print("Getting the current template text")
        self.wait_for_element_present(".v-card__title.cardTitleForViewer", timeout=15)
        name = self.find_element(".v-card__title.cardTitleForViewer", timeout=10)
        print("Selected Template is: " + name.text)

        #LogOut
        CommonFunctions().do_logout(self)
        print("----Signed Out----")



