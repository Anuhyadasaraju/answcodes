from seleniumbase import BaseCase
from prezent_task.common_functions import CommonFunctions

'''Task2 : Logging into the URL, generating the fingerprint and doing sign out'''

class PrezentTask2(BaseCase):
    def testing_task2(self):
        #log in
        CommonFunctions().do_login(self,"https://prezent-uatstaging.myprezent.com/signin","trial4.pf.noreply@abbvie.com","kiqjemkh")
        print("\n----Logged in----")

        #Generating Fingerprint
        self.click(".right-nav-item.profile-link",timeout=15)
        self.click("#fingerprint-tab",timeout=10)
        self.click("//div[contains(text(), 'Re-take fingerprint test')]",timeout=10)
        self.click("#discover",timeout=10)
        #Selecting the templates
        for i in range(6):
            self.click(".v-image__image.v-image__image--contain", timeout=10)
            self.wait(2)

        self.click("#show-fingerprint-for-btn--auto",timeout=10)
        #Skkiping the additional details
        for i in range(6):
            self.wait_for_element_present(".skip-button", timeout=10)
            self.click(".skip-button")
            self.wait(2)

        self.wait_for_element_present(".primary-button", timeout=10)
        self.click(".primary-button")
        self.wait_for_element_present("//span[contains(text(), 'Back to Prezent')]",timeout=10)
        self.click("//span[contains(text(), 'Back to Prezent')]")
        print("----Generated Fingerprint----")

        #Sign Out
        CommonFunctions().do_logout(self)
        print("----Sign Out----")




