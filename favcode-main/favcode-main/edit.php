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


$stmt = $pdo->prepare("SELECT * FROM favcode where favcode_id = :xyz");
$stmt->execute(array(":xyz" =>$_GET['favcode_id']));
$row = $stmt->fetch(PDO::FETCH_ASSOC);
if ($row === false){
  $_SESSION['error'] = 'Bad value for favcode_id';
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
        header("Location: index.php");
        return;
      }
      
      $stmt = $pdo->prepare('UPDATE favcode SET favlang = :lang, favlib = :lib, otherfav = :other, yearsdev = :yrs WHERE favcode_id = :favcode_id');
      $stmt->execute(array(
      ':lang' => htmlentities($_POST['fav_lang']),
      ':lib' => htmlentities($_POST['fav_lib']),
      ':other' => htmlentities($_POST['other_fav']),
      ':yrs' => htmlentities($_POST['yrs_dev']),
      ':favcode_id' => ($_POST['favcode_id'])));
      $_SESSION['success'] = "Entry updated";
      header('Location: index.php');
      return;
    }
    
    
$lang = htmlentities($row['favlang']);
$lib = htmlentities($row['favlib']);
$other = htmlentities($row['otherfav']);
$years = htmlentities($row['yearsdev']);
$fid = $row['favcode_id'];
?>

<!DOCTYPE html>
<html>
  <head>
    <title>Edit Favorite</title>
  </head>

  <body>
  
   <?php 

    if( isset($_SESSION['error'])){
      echo "<p style='color:red'>".$_SESSION['error']."</p>\n";
      unset($_SESSION['error']);
    }

    if( isset($_SESSION['success'])){
      echo '<p style="color:green">'.$_SESSION['success']."</p>\n";
      unset($_SESSION['success']);
    }
    ?>

    <form method="POST">
      <p>Favorite Coding Language:
      <input type="text" name="fav_lang" size="60" value="<?= $lang ?>"></p>
      
      <p>Favorite Library:
      <input type="text" name="fav_lib" size="60" value="<?= $lib ?>"></p>

      <p>Other Favorites in Coding:
      <input type="text" name="other_fav" size="80" value="<?= $other ?>"></p>

      <p>Years in Development:
      <input type="text"  name="yrs_dev" size="30" value="<?= $years ?>"></p>

      <input type="hidden" name="favcode_id" value="<?= $fid ?>">
      
      <button type = "submit" id="Update" name="Update" value = "Update">Update</button>
      <button type = "submit" id="cancel" name="cancel" value = "cancel"><a href="index.php">Cancel</a></button>

    </form>


  </body>
</html>