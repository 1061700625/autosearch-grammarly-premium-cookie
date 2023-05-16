<?php

  header('Content-Type: text/html; charset=utf-8');
  
  if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = $_POST['email']; // 获取email的值
    
    // 检查输入是否为空
    if (empty($email)) {
        echo  "email is null";
        return;
    }
    
    // 安全过滤
    $email = trim($email); // 去除首尾空格
    $email = htmlspecialchars($email); // 转义特殊字符
    
    $file = fopen("./mails.txt", "a+"); // 打开mails.txt文件以追加方式写入
    fwrite($file, $email . "\n"); // 将email写入文件，并添加换行符
    fclose($file); // 关闭文件
    echo  "add success";
  }
?>
