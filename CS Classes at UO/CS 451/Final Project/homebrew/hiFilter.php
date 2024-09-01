<?php

include('connectionData.txt');

$conn = mysqli_connect($server, $user, $pass, $dbname, $port)
or die('Error connecting to MySQL server.');

?>

<html>
<head>
  <title>MySQL D&D Database Program</title>
  </head>
  
  <body bgcolor="#89CFF0">
  
  
  <hr>
  
  
<?php

  
$hi = $_POST['hi'];

$hi = mysqli_real_escape_string($conn, $hi);
// this is a small attempt to avoid SQL injection
// better to use prepared statements


$query = "SELECT hb_name, hb_rarity, homebrew_descr\n
          FROM homebrew_items \n
          WHERE oname = ";
$query = $query."'".$hi."';"

?>

<p>
The query:
<p>
<?php
$query_array = (explode("\n", $query));
foreach ($query_array as $i) {
  echo "$i <br>";
}
?>

<hr>
<p>
Result of query:
<p>


<?php

$result = mysqli_query($conn, $query)
or die(mysqli_error($conn));

$output = "";




print "<pre>";
while($row = mysqli_fetch_array($result, MYSQLI_BOTH)){
    print "\n";
    $padded_hbname = str_pad($row['hb_name'], 35, " ", STR_PAD_RIGHT);
    $padded_hbrarity = str_pad($row['hb_rarity'], 35, " ", STR_PAD_RIGHT);
    print "$padded_hbname $padded_hbrarity $row[homebrew_descr]";

  }
print "</pre>";

mysqli_close($conn);

?>

<p>
<hr>

<p>
<a href="hiFilter.txt" >Contents</a>
of the PHP program that created this page. 	 

<p>
<a href="https://ix.cs.uoregon.edu/~icortez6/finalProj/homePage.html">Home Page</a>
</p>
 
</body>
</html>