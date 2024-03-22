from seleniumbase import BaseCase
from prezent_task.common_functions import CommonFunctions

'''Task1 : Logging into the URL, fetching the current template name and doing sign out'''

class PrezentTask1(BaseCase):
    def testing_task1(self):

        #logging in
        CommonFunctions().do_login(self,"https://prezent-uatstaging.myprezent.com/signin","trial4.pf.noreply@abbvie.com","kiqjemkh")
        print("\n----Logged In----")

        #Downloading the Autogenerator slide
        self.wait_for_element_present("//div[contains(text(), 'Auto Generator')]")
        self.click("//div[contains(text(), 'Auto Generator')]",timeout=10)
        self.wait(2)
        self.click(".v-text-field__slot",timeout=10)
        self.wait(2)
        self.click("#generate-suggested-2")
        self.wait_for_element_present("//span[contains(text(), 'Generate')]",timeout=10)
        self.click("//span[contains(text(), 'Generate')]", timeout=10)
        self.wait(3)
        #Waiting for the slides to load
        self.wait_for_element_absent("div.v-spinner.loading-spinner",timeout=300)
        #Downloading the slide
        self.wait_for_element_present("name=download-icon",timeout=10)
        self.click("name=download-icon",timeout=10)
        self.wait_for_element_present("//span[contains(text(), 'Download')]", timeout = 10)
        self.click("//span[contains(text(), 'Download')]", timeout=100)
        print("Downloaded the slide")
        #print(f"Downloaded the slide - {self.get_downloaded_files(regex='Brand*.pptx')}")
        self.wait(30)

        #LogOut
        CommonFunctions().do_logout(self)
        print("----Sign Out----")