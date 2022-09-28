<?php
require_once "pdo.php";
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

session_start();
unset($_SESSION['name']); //log user out
unset($_SESSION['user_id']); //log user out

if ( isset($_POST['cancel'] ) ) {
  header("Location: index.php");
  return;
}

$salt = '83jmfid#294.ocmj';

if(isset($_POST['user']) && isset($_POST['pass']) ) {
  if(strlen($_POST['user'])< 1 || strlen($_POST['pass'])< 1) {
    $_SESSION['error'] = "Username and password are required";
    header("Location: login.php");
    return;
  }

  $check = hash('md5',$salt.$_POST['pass']);
  $stmt = $pdo->prepare('SELECT user_id, name FROM users WHERE name = :user and password = :pw');
  $stmt->execute(array(':user'=> $_POST['user'],':pw'=> $check));
  $row = $stmt->fetch(PDO::FETCH_ASSOC);

  if ($row !== false){
    $_SESSION['name'] = $row['name'];
    $_SESSION['user_id'] = $row['user_id'];
    //redirect to the browser
    header("Location: index.php");
    return;
  }else{
    $_SESSION['error'] = "Incorrect password";
    header("Location: login.php");
    return;
  }

}

?>

<!DOCTYPE html>
<html>
<head>
<title>Login</title>
</head>
<body>
<div class="container">
<h1>Please Log In</h1>
<p><em>Note: Look in the dev tools for un & pw</em></p>
<?php

if ( isset($_SESSION['error'])) {
  echo('<p style="color: red;">'.htmlentities($_SESSION['error'])."</p>\n");
  unset($_SESSION['error']);
}
?>
<!--username: access password: Youcan@ccessth!s1  -->

<form method="POST" action="login.php">
<label for="user">Username</label>
<input type="text" name="user" id="user"><br/>
<label for="pass">Password</label>
<input type="text" name="pass" id="pass"><br/>
<input type="submit" onclick="return doValidate();" value="Log In">
<input type="submit" name="cancel" value="Cancel">

</form>

<script>  
function doValidate(){
  console.log('Validating...');
  try {
    addr = document.getElementById('user').value;
    pw = document.getElementById('pass').value;
    console.log("Validating addr="+addr+" pw="+pw);
    if (addr == null || addr == "" || pw == null || pw == "") {
      alert('Both fields must be filled out');
      return false;
    }
    
    return true;
  }
  catch(e) {
    return false;
  }
  return false;
}
</script>

</div>
</body>
</html>