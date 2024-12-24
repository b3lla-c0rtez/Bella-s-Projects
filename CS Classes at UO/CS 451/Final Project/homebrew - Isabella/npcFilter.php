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

  
$npc = $_POST['npc'];

$npc = mysqli_real_escape_string($conn, $npc);
// this is a small attempt to avoid SQL injection
// better to use prepared statements


$query = "SELECT n.npc_first, n.npc_last, s.shop_name, s.shop_location, l.location_descr\n
          FROM npcs n\n
          JOIN shops s on n.shop_id = s.shop_id\n
          JOIN locations l on s.location_id = l.location_id\n
          WHERE s.oname = ";
$query = $query."'".$npc."';"

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
    $padded_fname = str_pad($row['npc_first'], 40, " ", STR_PAD_RIGHT);
    $padded_lname = str_pad($row['npc_last'], 40, " ", STR_PAD_RIGHT);
    $padded_sname = str_pad($row['shop_name'], 40, " ", STR_PAD_RIGHT);
    $padded_slocation = str_pad($row['shop_location'], 40, " ", STR_PAD_RIGHT);
    print "$padded_fname $padded_lname $padded_sname $padded_slocation $row[location_descr]";

  }
print "</pre>";

mysqli_close($conn);

?>

<p>
<hr>

<p>
<a href="npcFilter.txt" >Contents</a>
of the PHP program that created this page. 	 

<hr>
<p>
<a href="https://ix.cs.uoregon.edu/~icortez6/finalProj/homePage.html">Home Page</a>
</p>
 
</body>
</html>