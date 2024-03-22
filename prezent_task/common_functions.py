
class CommonFunctions():
    #Login Module
    def do_login(self,sb,url,username,password):
        sb.open(url)
        sb.type("#username", username)
        sb.click("#continue")
        sb.type("#password", password)
        sb.click("#submit")

    #Sign Out Module
    def do_logout(selfb,sb):
        sb.wait_for_element_present(".right-nav-item.profile-link",timeout=10)
        sb.click(".right-nav-item.profile-link")
        sb.wait_for_element_present("#basics-tab", timeout=10)
        sb.click("#basics-tab")
        sb.wait(2)
        sb.click("button.log-out-button",timeout=10)
        sb.wait(2)