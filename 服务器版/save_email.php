<?php
/*
 * @Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @Date: 2023-05-17 18:17:49
 * @LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
 * @LastEditTime: 2023-05-17 18:18:38
 * @FilePath: \undefinedc:\Users\Administrator\Desktop\save_email.php
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
  header('Content-Type: text/html; charset=utf-8');
  // 邮箱列表文件名
  $filename = 'mails.txt';

  if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // 获取email的值
    $email = $_POST['email'];
    // 检查输入是否为空
    if (empty($email)) {
        echo  "email is null";
        return;
    }
    // 安全过滤
    $email = trim($email);
    $email = htmlspecialchars($email);

    // 检查邮箱是否存在于列表中
    if (file_exists($filename)) {
        $emails = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        if ($emails!==false && in_array($email, $emails)) {
            echo $email." already exists";
            return;
        }
    }
    
    // 将email以追加方式写入文件mails.txt，并添加换行符
    $file = fopen($filename, "a+");
    fwrite($file, $email . "\n"); 
    fclose($file);
    echo  "add success";

    // try {
    //   // 给我发个通知
    //   $msg = "【grammarly】有新邮箱了：".$email;
    //   $url = "http://xfxuezhang.cn:9966/QQ/send/friend?target=1061700625&msg=".urlencode($msg);
    //   file_get_contents($url);
    //   // echo $url;
    // } catch (Exception $e) {
    //     // 处理异常
    //     echo "An error occurred: " . $e->getMessage();
    // }
  }
?>
