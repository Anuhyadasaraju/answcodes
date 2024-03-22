
class CommonFunctions():
    #Login Module
    def do_login(self,sb,url,username,password):
        sb.open(url)
        print(f"Typing {username} as username")
        sb.type("#username", username)
        sb.click("#continue", timeout=10)
        print(f"Typing {password} as password")
        sb.type("#password", password)
        print("Clicking on Submit button")
        sb.click("#submit", timeout=10)
        sb.wait_for_element_present(".right-nav-item.profile-link", timeout=10)


    #Sign Out Module
    def do_logout(selfb,sb):
        sb.wait_for_element_present("div.profile-image-wrapper .profile-image-upload",timeout=10)
        print("Clicking on Profile icon")
        sb.click("div.profile-image-wrapper .profile-image-upload", timeout=10)
        sb.wait_for_element_present("#basics-tab", timeout=10)
        print("Clicking on Basics tab")
        sb.click("#basics-tab", timeout=15)
        print("Clicking on Sing Out button")
        sb.click("button.log-out-button",timeout=10)
        sb.wait_for_element_present("#username", timeout=10)