<?php

include('connectionData.txt');

$conn = mysqli_connect($server, $user, $pass, $dbname, $port)
or die('Error connecting to MySQL server.');

?>

<html>
<head>
  <title>MySQL STORES7 Program</title>
  </head>
  
  <body bgcolor="#89CFF0">
  
  
  <hr>
  
  
<?php

  
$manufact = $_POST['manufact'];

$manufact = mysqli_real_escape_string($conn, $manufact);
// this is a small attempt to avoid SQL injection
// better to use prepared statements


$query = "SELECT c.fname, c.lname, s.description\n
          FROM customer c\n
          JOIN orders o ON o.customer_num = c.customer_num\n
          JOIN items i ON i.order_num = o.order_num\n
          JOIN stock s ON s.stock_num = i.stock_num AND i.manu_code = s.manu_code\n
          JOIN manufact m ON m.manu_code = s.manu_code\n
          WHERE m.manu_name = ";
$query = $query."'".$manufact."';"

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

    $padded_fname = str_pad($row['fname'], 20, " ", STR_PAD_RIGHT);
    $padded_lname = str_pad($row['lname'], 20, " ", STR_PAD_RIGHT);
    print "$padded_fname $padded_lname $row[description]";

  }
print "</pre>";

mysqli_close($conn);

?>

<p>
<hr>

<p>
<a href="findCustManufacturer.txt" >Contents</a>
of the PHP program that created this page. 	 
 
</body>
</html>