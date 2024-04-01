from seleniumbase import BaseCase
from answcodes.prezent_task.common_functions import CommonFunctions

'''Task2 : Logging into the URL, generating the fingerprint and doing sign out'''

class PrezentTask2(BaseCase):
    def testing_task2(self):
        #log in
        CommonFunctions().do_login(self,"https://prezent-uatstaging.myprezent.com/signin","trial4.pf.noreply@abbvie.com","kiqjemkh")
        print("\n----Signed In----")

        #Generating Fingerprint
        print("Clicking on profile option")
        self.click(".right-nav-item.profile-link",timeout=15)
        self.click("#fingerprint-tab",timeout=10)
        print("Clicking on Re-take fingerprint test")
        self.click("//div[contains(text(), 'Re-take fingerprint test')]",timeout=10)
        self.click("#discover",timeout=10)
        print("Selecting the images")
        options = ['left', 'right', 'left', 'right', 'left', 'right']
        for option in options:
            print(f"Clicking on {option} image")
            if option == 'left':
                self.click_nth_visible_element("div.card-item .text-white", number=1, timeout=10)
            else:
                self.click_nth_visible_element("div.card-item .text-white", number=2, timeout=10)
            self.wait(1)
        print("Clicking on next")
        self.click("#show-fingerprint-for-btn--auto",timeout=10)
        print("Skipping the additional details")
        #Skkiping the additional details
        for i in range(6):
            self.wait_for_element_present(".skip-button", timeout=10)
            self.click(".skip-button")
            self.wait(2)

        print("Clicking on View my fingerprint")
        self.wait_for_element_present(".primary-button", timeout=10)
        self.click(".primary-button")
        print("Clicking on Back to Prezent")
        self.wait_for_element_present("//span[contains(text(), 'Back to Prezent')]",timeout=10)
        self.click("//span[contains(text(), 'Back to Prezent')]")
        print("Generated Fingerprint")

        #Sign Out
        CommonFunctions().do_logout(self)
        print("----Sign Out----")




