from seleniumbase import BaseCase
from answcodes.prezent_task.common_functions import CommonFunctions

'''Task1 : Logging into the URL, fetching the current template name and doing sign out'''

class PrezentTask3(BaseCase):
    def testing_task3(self):

        #logging in
        CommonFunctions().do_login(self,"https://prezent-uatstaging.myprezent.com/signin","trial4.pf.noreply@abbvie.com","kiqjemkh")
        print("\n----Signed In----")

        #Downloading the Auto-generator slide
        print("Clicking on Auto Generator tab")
        self.wait_for_element_present("//div[contains(text(), 'Auto Generator')]",timeout=15)
        self.click("//div[contains(text(), 'Auto Generator')]",timeout=15)
        #self.wait(2)
        print("Clicking on suggested slides")
        self.wait_for_element_present(".v-text-field__slot",timeout=15)
        self.click(".v-text-field__slot",timeout=15)
        #self.wait(2)
        print("Selecting third suggested option")
        self.click("#generate-suggested-2", timeout=15)
        print("Clicking on generate option")
        self.wait_for_element_present("//span[contains(text(), 'Generate')]",timeout=10)
        self.click("//span[contains(text(), 'Generate')]", timeout=10)
        self.wait(3)
        #Waiting for the slides to load
        print("waiting for the slides to load")
        self.wait_for_element_absent("div.v-spinner.loading-spinner",timeout=300)
        #Downloading the slide
        print("Clicking on download icon")
        self.wait_for_element_present("name=download-icon",timeout=10)
        self.click("name=download-icon",timeout=10)
        print("Clicking on download")
        self.wait_for_element_present("//span[contains(text(), 'Download')]", timeout = 10)
        self.click("//span[contains(text(), 'Download')]", timeout=100)
        self.wait_for_element_absent("div.v-spinner.loading-spinner", timeout=30)
        print("Downloaded the slide")
        #print(f"Downloaded the slide - {self.get_downloaded_files(regex='Brand*.pptx')}")
        #self.wait_for_element_absent("//span[contains(text(), 'Download')]")
        #self.wait(30)

        #LogOut
        CommonFunctions().do_logout(self)
        print("----Sign Out----")