const fs = require('fs');
const path = require('path');

let nodemailer;
try {
  nodemailer = require('nodemailer');
} catch (e) {
  nodemailer = null;
}

/**
 * Sends a DevOps presentation invitation email.
 * @param {string} toEmail - The recipient's email address.
 * @param {string} firstName - The recipient's first name.
 * @returns {Promise<{success: boolean, messageId?: string, previewUrl?: string, error?: any}>}
 */
async function sendInvitation(toEmail, firstName) {
  // 1. Check if nodemailer is installed
  if (!nodemailer) {
    console.warn('\n⚠️ [Email Service] Warning: "nodemailer" is not installed.');
    console.warn('   To enable automatic email invitations, run: npm install nodemailer\n');
    return { success: false, error: 'nodemailer_not_installed' };
  }

  // 2. Setup transporter (configured SMTP or Ethereal test account fallback)
  let transporter;
  let isDefaultSMTP = !process.env.SMTP_HOST || process.env.SMTP_HOST === 'smtp.example.com' || !process.env.SMTP_USER || !process.env.SMTP_PASS;

  try {
    if (isDefaultSMTP) {
      console.log('ℹ️ [Email Service] SMTP credentials not configured. Generating Ethereal test account...');
      const testAccount = await nodemailer.createTestAccount();
      transporter = nodemailer.createTransport({
        host: 'smtp.ethereal.email',
        port: 587,
        secure: false, // true for 465, false for other ports
        auth: {
          user: testAccount.user, // generated ethereal user
          pass: testAccount.pass, // generated ethereal password
        },
      });
      console.log(`🔑 [Email Service] Ethereal test account created: User=${testAccount.user}`);
    } else {
      transporter = nodemailer.createTransport({
        host: process.env.SMTP_HOST,
        port: parseInt(process.env.SMTP_PORT || '587', 10),
        secure: process.env.SMTP_PORT === '465', // true for 465, false for others
        auth: {
          user: process.env.SMTP_USER,
          pass: process.env.SMTP_PASS,
        },
      });
    }
  } catch (err) {
    console.error('❌ [Email Service] Failed to initialize email transporter:', err.message);
    return { success: false, error: 'transporter_initialization_failed' };
  }

  try {
    // 3. Load the HTML template
    const templatePath = path.join(__dirname, '../email/email_template.html');
    if (!fs.existsSync(templatePath)) {
      throw new Error(`Email template not found at: ${templatePath}`);
    }
    let htmlContent = fs.readFileSync(templatePath, 'utf8');

    // 4. Interpolate variables
    const presentationUrl = process.env.PRESENTATION_URL || 'http://localhost:3001';
    htmlContent = htmlContent
      .replace(/\{\{first_name\}\}/g, firstName)
      .replace(/\{\{presentation_url\}\}/g, presentationUrl);

    // 5. Define attachment paths
    const timHuzaPhotoPath = path.join(__dirname, '../email/static/tim-huza.png');
    const devopsPresentationPath = path.join(__dirname, '../email/static/devops-presentation.png');

    const attachments = [];
    if (fs.existsSync(timHuzaPhotoPath)) {
      attachments.push({
        filename: 'tim-huza.png',
        path: timHuzaPhotoPath,
        cid: 'tim-huza', // matches src="cid:tim-huza"
      });
    } else {
      console.warn(`⚠️ [Email Service] Warning: Profile photo not found at ${timHuzaPhotoPath}`);
    }

    if (fs.existsSync(devopsPresentationPath)) {
      attachments.push({
        filename: 'devops-presentation.png',
        path: devopsPresentationPath,
        cid: 'devops-presentation', // matches src="cid:devops-presentation"
      });
    } else {
      console.warn(`⚠️ [Email Service] Warning: Presentation image not found at ${devopsPresentationPath}`);
    }

    // 6. Mail options
    const mailOptions = {
      from: isDefaultSMTP ? '"Tim Huza (DevOps Presentation)" <invitations@example.com>' : (process.env.SMTP_FROM || '"Tim Huza" <invitations@example.com>'),
      to: toEmail,
      subject: "You're Invited: DevOps Presentation",
      html: htmlContent,
      attachments: attachments,
    };

    // 7. Send the mail
    const info = await transporter.sendMail(mailOptions);
    console.log(`✅ [Email Service] Invitation successfully sent to ${toEmail}. MessageID: ${info.messageId}`);
    
    if (isDefaultSMTP) {
      const previewUrl = nodemailer.getTestMessageUrl(info);
      console.log(`🔗 [Email Service] View your email preview here: ${previewUrl}`);
      return { success: true, messageId: info.messageId, previewUrl };
    }
    
    return { success: true, messageId: info.messageId };

  } catch (error) {
    console.error('❌ [Email Service] Failed to send email invitation:', error.message);
    return { success: false, error: error };
  }
}

module.exports = {
  sendInvitation,
};
