<?php

  header('Content-Type: text/html; charset=utf-8');
  
  if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = $_POST['email']; // ��ȡemail��ֵ
    
    // ��������Ƿ�Ϊ��
    if (empty($email)) {
        echo  "email is null";
        return;
    }
    
    // ��ȫ����
    $email = trim($email); // ȥ����β�ո�
    $email = htmlspecialchars($email); // ת�������ַ�
    
    $file = fopen("./mails.txt", "a+"); // ��mails.txt�ļ���׷�ӷ�ʽд��
    fwrite($file, $email . "\n"); // ��emailд���ļ�������ӻ��з�
    fclose($file); // �ر��ļ�
    echo  "add success";
  }
?>
