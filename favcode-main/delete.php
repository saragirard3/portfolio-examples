<?php
require_once "pdo.php";
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
session_start();

if (isset($_POST['delete']) && isset($_POST['favcode_id'])){
  $sql = "DELETE FROM favcode WHERE favcode_id = :zip";
  $stmt = $pdo->prepare($sql);
  $stmt->execute(array(':zip' => $_POST['favcode_id']));
  $_SESSION['success'] = 'Record deleted';
  header('Location: index.php');
  return;
}

$stmt = $pdo->prepare("SELECT favlang, favcode_id FROM favcode where favcode_id = :xyz");
$stmt->execute(array(":xyz" =>$_GET['favcode_id']));
$row = $stmt->fetch(PDO::FETCH_ASSOC);
if ($row === false){
  $_SESSION['error'] = 'Bad value for favcode_id';
  header('Location: index.php');
  return;
}
 ?>

 <p> Confirm: Deleting <?=htmlentities($row['favlang']) ?></p>
<form method = "post"><input type="hidden" name="favcode_id" value="<?= $row['favcode_id']?>">
  <input type="submit" value="Delete" name="delete">
  <a href="index.php">Cancel</a>
</form>
