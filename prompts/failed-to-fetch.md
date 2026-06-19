On my python files, the script for sending emails is working and it sends the email. it used these files:
* `venv/`
* `client_server.json`
* `sendEmail.py`
* `Google.py`

I deployed my app for sending emails in **Google Apps Script** and the files I have are:
* `sendEmail.gs`
* `email_template.html`

my `sendEmail.gs` file:
```
function doPost(e) {
  const data = JSON.parse(e.postData.contents);

  const firstName = data.firstName;
  const lastName = data.lastName;
  const userEmail = data.email;

  const userName = data.name || "Subscriber";

  const template = HtmlService.createTemplateFromFile("email_template");

  template.userName = `${firstName} ${lastName}`;

  const htmlBody = template.evaluate().getContent();

  GmailApp.sendEmail(
    userEmail,
    "Invitation to DevOps Presentation",
    "Please view this email in HTML format.",
    {
      htmlBody: htmlBody
    }
  );

  return ContentService
    .createTextOutput(
      JSON.stringify({
        success: true
      })
    )
    .setMimeType(ContentService.MimeType.JSON);
}

function testEmail() {

  const template =
    HtmlService.createTemplateFromFile(
      "email_template"
    );

  template.userName = "Tim";

  const htmlBody =
    template.evaluate().getContent();

  GmailApp.sendEmail(
    "tim.ca2023@gmail.com",
    "Test DevOps Invitation",
    "Please view this email in HTML format.",
    {
      htmlBody: htmlBody
    }
  );
}
```

and my `email_template.html` file is the exact same file from `email/` folder.

but when I go to registration form and enter **Complete Registration** I get **Failed to fetch** and when I press `F12` and got to `Console` tab i get these logs/errors:
Uncaught TypeError: Cannot set properties of null (setting 'innerHTML')
    at updateIndicators ((index):797:33)
    at (index):915:9
/favicon.ico:1  Failed to load resource: the server responded with a status of 404 ()
(index):1 Access to fetch at 'https://script.google.com/macros/s/AKfycbz_v1rgCWl0HdJfqv2qcSgh_qffEp3TLXt5Q-SsJxdt139bWzNc81-Z5G4ElD_Kc_bV/exec' from origin 'https://devops-presentation.onrender.com' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource.
script.google.com/macros/s/AKfycbz_v1rgCWl0HdJfqv2qcSgh_qffEp3TLXt5Q-SsJxdt139bWzNc81-Z5G4ElD_Kc_bV/exec:1  Failed to load resource: net::ERR_FAILED
installHook.js:1 Registration failed: TypeError: Failed to fetch
    at handleRegistration ((index):887:40)
    at HTMLFormElement.onsubmit ((index):733:101)
overrideMethod @ installHook.js:1
(index):1 Access to fetch at 'https://script.google.com/macros/s/AKfycbz_v1rgCWl0HdJfqv2qcSgh_qffEp3TLXt5Q-SsJxdt139bWzNc81-Z5G4ElD_Kc_bV/exec' from origin 'https://devops-presentation.onrender.com' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource.
script.google.com/macros/s/AKfycbz_v1rgCWl0HdJfqv2qcSgh_qffEp3TLXt5Q-SsJxdt139bWzNc81-Z5G4ElD_Kc_bV/exec:1  Failed to load resource: net::ERR_FAILED
installHook.js:1 Registration failed: TypeError: Failed to fetch
    at handleRegistration ((index):887:40)
    at HTMLFormElement.onsubmit ((index):733:101)
overrideMethod @ installHook.js:1
(index):1 Access to fetch at 'https://script.google.com/macros/s/AKfycbz_v1rgCWl0HdJfqv2qcSgh_qffEp3TLXt5Q-SsJxdt139bWzNc81-Z5G4ElD_Kc_bV/exec' from origin 'https://devops-presentation.onrender.com' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource.
script.google.com/macros/s/AKfycbz_v1rgCWl0HdJfqv2qcSgh_qffEp3TLXt5Q-SsJxdt139bWzNc81-Z5G4ElD_Kc_bV/exec:1  Failed to load resource: net::ERR_FAILED
installHook.js:1 Registration failed: TypeError: Failed to fetch
    at handleRegistration ((index):887:40)
    at HTMLFormElement.onsubmit ((index):733:101)
overrideMethod @ installHook.js:1
(index):1 Access to fetch at 'https://script.google.com/macros/s/AKfycbz_v1rgCWl0HdJfqv2qcSgh_qffEp3TLXt5Q-SsJxdt139bWzNc81-Z5G4ElD_Kc_bV/exec' from origin 'https://devops-presentation.onrender.com' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource.
script.google.com/macros/s/AKfycbz_v1rgCWl0HdJfqv2qcSgh_qffEp3TLXt5Q-SsJxdt139bWzNc81-Z5G4ElD_Kc_bV/exec:1  Failed to load resource: net::ERR_FAILED
installHook.js:1 Registration failed: TypeError: Failed to fetch
    at handleRegistration ((index):887:40)
    at HTMLFormElement.onsubmit ((index):733:101)

what might be the problem?