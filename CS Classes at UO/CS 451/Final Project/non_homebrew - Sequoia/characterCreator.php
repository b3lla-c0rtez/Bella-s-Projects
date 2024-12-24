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
$character_name = $_POST['character_name'];
$class_name = $_POST['class'];
$race_name = $_POST['race'];
$weapon_name = $_POST['weapon'];
$armor_name = $_POST['armor'];
$spell_name = $_POST['spell'];

// Sanitize input
$character_name = mysqli_real_escape_string($conn, $character_name);
$class_name = mysqli_real_escape_string($conn, $class_name);
$race_name = mysqli_real_escape_string($conn, $race_name);
$weapon_name = mysqli_real_escape_string($conn, $weapon_name);
$armor_name = mysqli_real_escape_string($conn, $armor_name);
$spell_name = mysqli_real_escape_string($conn, $spell_name);

// Get class_id, race_id, weapon_id, armor_id, and spell_id
$class_query = "SELECT class_id FROM class WHERE class_name = '$class_name'";
$race_query = "SELECT race_id FROM race WHERE race_name = '$race_name'";
$weapon_query = "SELECT weapon_id FROM weapons WHERE weapon_name = '$weapon_name'";
$armor_query = "SELECT armor_id FROM armor WHERE armor_name = '$armor_name'";
$spell_query = "SELECT spell_id FROM spells WHERE spell_name = '$spell_name'";

$class_result = mysqli_query($conn, $class_query) or die(mysqli_error($conn));
$race_result = mysqli_query($conn, $race_query) or die(mysqli_error($conn));
$weapon_result = mysqli_query($conn, $weapon_query) or die(mysqli_error($conn));
$armor_result = mysqli_query($conn, $armor_query) or die(mysqli_error($conn));
$spell_result = mysqli_query($conn, $spell_query) or die(mysqli_error($conn));

$class_row = mysqli_fetch_assoc($class_result);
$race_row = mysqli_fetch_assoc($race_result);
$weapon_row = mysqli_fetch_assoc($weapon_result);
$armor_row = mysqli_fetch_assoc($armor_result);
$spell_row = mysqli_fetch_assoc($spell_result);

$class_id = $class_row['class_id'];
$race_id = $race_row['race_id'];
$weapon_id = $weapon_row['weapon_id'];
$armor_id = $armor_row['armor_id'];
$spell_id = $spell_row['spell_id'];

// Insert new character
$insert_query = "INSERT INTO characters (character_name, class_id, race_id, weapon_id, armor_id, spell_id) VALUES ('$character_name', $class_id, $race_id, $weapon_id, $armor_id, $spell_id)";

mysqli_query($conn, $insert_query) or die(mysqli_error($conn));

echo "<p><b>You have created $character_name, the $race_name $class_name, equipped with $weapon_name, $armor_name, and the spell $spell_name. Adventure awaits!</b></p>";

mysqli_close($conn);
?>

<hr>
<p>
    <a href="characterFilter.txt">Contents</a> of the PHP program that created this page.
</p>
<hr>
<p>
    <a href="https://ix.cs.uoregon.edu/~icortez6/finalProj/homePage.html">Home Page</a>
</p>
</body>
</html>
