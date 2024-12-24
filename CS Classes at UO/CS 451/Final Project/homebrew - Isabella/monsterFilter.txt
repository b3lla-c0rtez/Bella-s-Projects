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

  
$monster = $_POST['monster'];

$monster = mysqli_real_escape_string($conn, $monster);
// this is a small attempt to avoid SQL injection
// better to use prepared statements


$query = "SELECT monster_name, monster_cr, monster_type, monster_descr\n
          FROM monsters\n
          WHERE oname = ";
$query = $query."'".$monster."';"

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
    $padded_mname = str_pad($row['monster_name'], 40, " ", STR_PAD_RIGHT);
    $padded_mcr = str_pad($row['monster_cr'], 40, " ", STR_PAD_RIGHT);
    $padded_mtype = str_pad($row['monster_type'], 40, " ", STR_PAD_RIGHT);
    print "$padded_mname $padded_mcr $padded_mtype $row[monster_descr]";

  }
print "</pre>";

mysqli_close($conn);

?>

<p>
<hr>

<p>
<a href="monsterFilter.txt" >Contents</a>
of the PHP program that created this page. 	 

<hr>
<p>
<a href="https://ix.cs.uoregon.edu/~icortez6/finalProj/homePage.html">Home Page</a>
</p>
 
</body>
</html>