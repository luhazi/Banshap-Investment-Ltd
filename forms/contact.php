<?php
/**
 * BANSHAP INVESTMENT COMPANY LIMITED - Contact Form Handler[cite: 8]
 * Location: Samora Avenue near Salamanda Tower, Samora road[cite: 8]
 */

// Define receiving corporate email address
$receiving_email_address = 'info@banshap.co.tz'; 

// Security verification: Only accept POST requests
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    die('Invalid request protocol.');
}

// Check for the existence of Arsha template vendor components if using PHP-Email-Form
if (file_exists($php_email_form = '../assets/vendor/php-email-form/php-email-form.php' )) {
    include($php_email_form);
} else {
    // Fallback to standard native PHP mail architecture if the vendor folder is clean
    $name = strip_tags(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $subject = strip_tags(trim($_POST['subject']));
    $message = trim($_POST['message']);

    // Input sanitization validation
    if (empty($name) || empty($subject) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo "Please complete all fields correctly and try again.";
        exit;
    }

    // Construct clean email headers
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Message:\n$message\n";

    $email_headers = "From: Banishap Web Portal <" . $receiving_email_address . ">\r\n";
    $email_headers .= "Reply-To: $name <$email>\r\n";
    $email_headers .= "X-Mailer: PHP/" . phpversion();

    // Execute transmission payload
    if (mail($receiving_email_address, "Web Contact: " . $subject, $email_content, $email_headers)) {
        http_response_code(200);
        echo "OK"; // Arsha's main.js checks specifically for "OK" to trigger the success message banner
    } else {
        http_response_code(500);
        echo "Form transmission failed. Please try again later.";
    }
    exit;
}

// Alternative Arsha Class Initialization if PHP-Email-Form is active
$contact = new PHP_Email_Form;
$contact->ajax = true;
$contact->to = $receiving_email_address;
$contact->from_name = $_POST['name'];
$contact->from_email = $_POST['email'];
$contact->subject = $_POST['subject'];

$contact->add_message($_POST['name'], 'From');
$contact->add_message($_POST['email'], 'Email');
$contact->add_message($_POST['message'], 'Message', 10);

echo $contact->send();
?>