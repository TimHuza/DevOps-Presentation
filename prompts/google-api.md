I have a Apps Script in google console scripts to send an email after a user clicks **Register** button on a `register.html` web page. In this google console I have 3 files there:

1. `email_template.html`
This is the exact same file that I have in `email/` folder in here not in google console

2. `sendEmail.gs`
This is the sending email script. Code is here:
```js
const CLIENT_SCRIPT_FILE = "client_secret.json";
const API_NAME = "gmail";
const API_VERSION = "v1";
const SCOPES = ["https://mail.google.com/"];

const service = Create_Service(CLIENT_SCRIPT_FILE, API_NAME, API_VERSION, SCOPES);

const htmlTemplate = HtmlService.createTemplateFromFile("email_template");
htmlTemplate.userName = "Subscriber";

const htmlBody = htmlTemplate.evaluate().getContent();

const mimeMessage =
  "To: coderacer650@gmail.com\r\n" +
  "Subject: You won\r\n" +
  "MIME-Version: 1.0\r\n" +
  "Content-Type: text/html; charset=utf-8\r\n\r\n" +
  htmlBody;

const raw_string = Utilities.base64EncodeWebSafe(
  Utilities.newBlob(mimeMessage).getBytes()
);

const message = Gmail.Users.Messages.send(
  { raw: raw_string },
  "me"
);

console.log(message);
```

3. `Google.gs`
This is a file where my `Create_Service` and `cinvert_to_RCF_datetime` functions are. Here is the code for this file:
```js
function Create_Service(client_secret_file, api_name, api_version, ...scopes) {
  console.log(
    client_secret_file + "-" +
    api_name + "-" +
    api_version + "-" +
    JSON.stringify(scopes)
  );

  const CLIENT_SECRET_FILE = client_secret_file;
  const API_SERVICE_NAME = api_name;
  const API_VERSION = api_version;
  const SCOPES = [...scopes[0]];

  console.log(SCOPES);

  let cred = null;

  const pickle_file = `token_${API_SERVICE_NAME}_${API_VERSION}.pickle`;

  if (cred === null || !cred.valid) {
    if (cred && cred.expired && cred.refresh_token) {
      cred.refresh();
    } else {
      cred = null;
    }
  }

  try {
    const service = Gmail;
    console.log(API_SERVICE_NAME + " service created successfully");
    return service;
  } catch (e) {
    console.log("Unable to connect.");
    console.log(e);
    return null;
  }
}

function convert_to_RFC_datetime(year = 1900, month = 1, day = 1, hour = 0, minute = 0) {
  const dt = new Date(year, month - 1, day, hour, minute, 0).toISOString();
  return dt;
}
```

Now I have questions:
1. Do I create them here but instead of `gs` to `js`. ANd them link them in `register.html` file?
2. Check if the code is right?
3. Can you help me to set up this so it works and sends the email when user presses the `Register` button?