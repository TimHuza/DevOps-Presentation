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
  // 1. Check if we should use Resend API (HTTP-based) instead of SMTP
  const useResend = !!process.env.RESEND_API_KEY;

  // 2. Load the HTML template
  let htmlContent;
  let attachments = [];
  try {
    const templatePath = path.join(__dirname, '../email/email_template.html');
    if (!fs.existsSync(templatePath)) {
      throw new Error(`Email template not found at: ${templatePath}`);
    }
    htmlContent = fs.readFileSync(templatePath, 'utf8');

    // Interpolate variables
    const presentationUrl = process.env.PRESENTATION_URL || 'http://localhost:3001';
    htmlContent = htmlContent
      .replace(/\{\{first_name\}\}/g, firstName)
      .replace(/\{\{presentation_url\}\}/g, presentationUrl);

    // Define attachment paths
    const timHuzaPhotoPath = path.join(__dirname, '../email/static/tim-huza.png');
    const devopsPresentationPath = path.join(__dirname, '../email/static/devops-presentation.png');

    if (useResend) {
      // For Resend API, to guarantee delivery and correct image rendering in Gmail,
      // we reference the images directly from your public GitHub repository.
      // This also slashes email size from ~1.5MB to just ~20KB, preventing spam filter triggers!
      const githubRepoBase = 'https://raw.githubusercontent.com/TimHuza/DevOps-Presentation/main/email/static';
      htmlContent = htmlContent
        .replace(/cid:tim-huza/g, `${githubRepoBase}/tim-huza.png`)
        .replace(/cid:devops-presentation/g, `${githubRepoBase}/devops-presentation.png`);
    } else {
      // For Nodemailer SMTP
      if (fs.existsSync(timHuzaPhotoPath)) {
        attachments.push({
          filename: 'tim-huza.png',
          path: timHuzaPhotoPath,
          cid: 'tim-huza',
        });
      }
      if (fs.existsSync(devopsPresentationPath)) {
        attachments.push({
          filename: 'devops-presentation.png',
          path: devopsPresentationPath,
          cid: 'devops-presentation',
        });
      }
    }
  } catch (error) {
    console.error('❌ [Email Service] Failed to load email assets:', error.message);
    return { success: false, error: error };
  }

  // --- Option B: Resend HTTP API ---
  if (useResend) {
    try {
      console.log('ℹ️ [Email Service] Using Resend HTTP API to send email...');
      
      // Resend onboarding sender is "onboarding@resend.dev" by default
      const fromEmail = process.env.SMTP_FROM || 'onboarding@resend.dev';
      
      const payload = {
        from: fromEmail,
        to: toEmail,
        subject: "You're Invited: DevOps Presentation",
        html: htmlContent,
      };

      if (attachments && attachments.length > 0) {
        payload.attachments = attachments;
      }

      const response = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      const resData = await response.json();

      if (!response.ok) {
        throw new Error(resData.message || `HTTP error! status: ${response.status}`);
      }

      console.log(`✅ [Email Service] Invitation successfully sent via Resend to ${toEmail}. MessageID: ${resData.id}`);
      return { success: true, messageId: resData.id };
    } catch (error) {
      console.error('❌ [Email Service] Resend API failed to send email:', error.message);
      return { success: false, error: error };
    }
  }

  // --- Option A / Fallback: SMTP / Nodemailer ---
  if (!nodemailer) {
    console.warn('\n⚠️ [Email Service] Warning: "nodemailer" is not installed.');
    console.warn('   To enable automatic email invitations, run: npm install nodemailer\n');
    return { success: false, error: 'nodemailer_not_installed' };
  }

  let transporter;
  let isDefaultSMTP = !process.env.SMTP_HOST || process.env.SMTP_HOST === 'smtp.example.com' || !process.env.SMTP_USER || !process.env.SMTP_PASS;

  try {
    if (isDefaultSMTP) {
      console.log('ℹ️ [Email Service] SMTP credentials not configured. Generating Ethereal test account...');
      const testAccount = await nodemailer.createTestAccount();
      transporter = nodemailer.createTransport({
        host: 'smtp.ethereal.email',
        port: 587,
        secure: false,
        auth: {
          user: testAccount.user,
          pass: testAccount.pass,
        },
      });
      console.log(`🔑 [Email Service] Ethereal test account created: User=${testAccount.user}`);
    } else {
      transporter = nodemailer.createTransport({
        host: process.env.SMTP_HOST,
        port: parseInt(process.env.SMTP_PORT || '587', 10),
        secure: process.env.SMTP_PORT === '465',
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
    const mailOptions = {
      from: isDefaultSMTP ? '"Tim Huza (DevOps Presentation)" <invitations@example.com>' : (process.env.SMTP_FROM || '"Tim Huza" <invitations@example.com>'),
      to: toEmail,
      subject: "You're Invited: DevOps Presentation",
      html: htmlContent,
      attachments: attachments,
    };

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
