<?php
session_start();
require_once "pdo.php";
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
?>
<!DOCTYPE html>
<html>
  <head>
    <title>Favorite Coding Tools</title>
  </head>
  <body>
    <h1>Favorite Coding Tools</h1>

<?php
 //check to see if user is logged in
    if(! isset($_SESSION["user_id"])){
?>
    <p><a href="login.php">Please log in</a></p>
      
<?php
    ;} else {
        
       echo('<table border="1">'."\n");
          $stmt = $pdo->query("SELECT * FROM favcode");
          $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
          echo("<tr><th>");
          echo("Favorite Languages");
          echo("</th><th>");
          echo("Favorite Libraries");
          echo("</th><th>");
          echo("Other Favorites");
          echo("</th><th>");
          echo("Years in Technology");
          echo("</th><th>");
          echo("Action");
          echo("</th></tr>");
          foreach ( $rows as $row ) {
            echo("<tr><td>");
            echo($row['favlang']);
            echo("</td><td>");
            echo($row['favlib']);
            echo("</td><td>");
            echo($row['otherfav']);
            echo("</td><td>");
            echo($row['yearsdev']);
            echo("</td><td>");
            echo('<a href="edit.php?favcode_id='.$row['favcode_id'].'">Edit</a> / ');
            echo('<a href="delete.php?favcode_id='.$row['favcode_id'].'">Delete</a> ');
            echo("\n</form>\n");
            echo("</td></tr>\n");} 
?>

 <!--main viewing page-->
 <p><a href="add.php">Add New Entry</a></p>
 <p><a href="logout.php">Logout</a></p>

<?php
;}
?>
 

  </body>
</html>
