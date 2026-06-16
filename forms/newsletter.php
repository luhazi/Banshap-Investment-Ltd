<?php
/**
 * BANSHAP INVESTMENT COMPANY LIMITED - Newsletter Subscription Handler[cite: 8]
 */

$receiving_email_address = 'info@banshap.co.tz';

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['email'])) {
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    
    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $subject = "New Newsletter Subscription Request";
        $content = "Email Address: " . $email;
        $headers = "From: Banshap Notification <" . $receiving_email_address . ">\r\n";
        $headers .= "X-Mailer: PHP/" . phpversion();
        
        if (mail($receiving_email_address, $subject, $content, $headers)) {
            http_response_code(200);
            echo "OK";
        } else {
            http_response_code(500);
            echo "Subscription failed.";
        }
    } else {
        http_response_code(400);
        echo "Invalid email format.";
    }
}
?>