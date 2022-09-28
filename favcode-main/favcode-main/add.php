<?php
session_start();
require_once "pdo.php";
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);


//If user is not logged in, redirect to index.php
if(! isset($_SESSION["user_id"])){
  die("ACCESS DENIED");
  return;
}

//if user requested cancel, go back to index.php
if( isset($_POST['cancel'])){
  header('Location: index.php');
  return;
}


// Handle incoming data
if (isset($_POST['fav_lang']) && 
    isset($_POST['fav_lib']) && 
    isset($_POST['other_fav']) &&
    isset($_POST['yrs_dev']) ){
      if (strlen($_POST['fav_lang']) == 0 ||
          strlen($_POST['fav_lib']) == 0 ||
          strlen($_POST['other_fav']) == 0 ||
          strlen($_POST['yrs_dev']) == 0 ) {
        $_SESSION['error'] = "All fields are required";
        header("Location: add.php");
        return;
      }
      
      $stmt = $pdo->prepare('INSERT INTO favcode
              (user_id, favlang, favlib, otherfav, yearsdev)
              VALUES (:uid, :lang, :lib, :other, :yrs)');

      $stmt->execute(array(
      ':uid' => $_SESSION['user_id'],
      ':lang' => htmlentities($_POST['fav_lang']),
      ':lib' => htmlentities($_POST['fav_lib']),
      ':other' => htmlentities($_POST['other_fav']),
      ':yrs' => htmlentities($_POST['yrs_dev'])));
      $_SESSION['success'] = "Profile added";
      header('Location: index.php');
      return;
    }
?>

<!DOCTYPE html>
<html>
  <head>
    <title>Add Your Favorite</title>
  </head>

  <body>
  <!-- <?php 

    if( isset($_SESSION['error'])){
      echo "<p style='color:red'>".$_SESSION['error']."</p>\n";
      unset($_SESSION['error']);
    }

    if( isset($_SESSION['success'])){
      echo '<p style="color:green">'.$_SESSION['success']."</p>\n";
      unset($_SESSION['success']);
    }
    ?> -->

    <form method="POST">
      <p><label for="fav_lang">Favorite Coding Language:</label>
      <input type="text" name="fav_lang" size="60"></p>
      
      <p><label for="fav_lib">Favorite Library:</label>
      <input type="text" name="fav_lib" size="60"></p>

      <p><label for="other_fav">Other Favorites in Coding:</label>
      <input type="text" name="other_fav" size="80"></p>

      <p><label for="yrs_dev">Years in Development:</label>
      <input type="text"  name="yrs_dev" size="30"></p>


      <button type = "submit" id="Add" name="Add" value = "Add">Add</button>
      <button type = "submit" id="cancel" name="cancel" value = "cancel"><a href="index.php">Cancel</a></button>

    </form>


  </body>
</html>
