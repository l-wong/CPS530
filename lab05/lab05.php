<!DOCTYPE html>
<html>
<head>
<title>Lab 05</title>
 <link href="https://fonts.googleapis.com/css?family=Creepster" rel="stylesheet">

<link href="https://fonts.googleapis.com/css?family=Nosifer" rel="stylesheet">

<style>

h1 {
  text-align: center;
  font-family: 'Creepster';
  color:  #003300;
  font-size: 50px;
}

h2 {
  font-family: 'Nosifer';
  color: #990000;
}

body {
  background-image: url(http://www.bluewheelers.com.au/wp-content/themes/blue-wheelers/assets/images/dog-pug-face.png);
  background-repeat: no-repeat;
  background-position: 100px 560px;
  background-color: #00cc99;
  text-align: center;
}
</style>
</head>


<body>
  <h1>Lab 05 Part 1</h1>
  <h2> Lisa Wong - 500692069 </h2>
  <p> Insert numbers to generate a multiplication table. </p>
  <form action="lab05.php" method="get">
  <div class="input">
    <input name="firstNum" type="text"> x <input name="secondNum" type="text">
    <input type="submit">
  </div>

  </form>

<?php

//multiplication table

$rows = $_GET['firstNum'];
$cols = $_GET['secondNum'];

echo "<table border=\"1\" align=\"center\">";

for ($r = 0; $r <= $rows; $r++){

  echo'<tr>';

    for ($c = 0; $c <= $cols; $c++)

      echo '<td>' .$c * $r.'</td>';

  echo '</tr>';

}

echo "</table>";



//hit counter
echo "<br>";
session_start();
if(isset($_SESSION['views']))
  $_SESSION['views'] = $_SESSION['views']+ 1;
else
  $_SESSION['views'] = 1;

echo "Hitcount = ". $_SESSION['views'];
?>

</body>

</html>
