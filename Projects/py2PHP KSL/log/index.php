<!-- Py2PHP KSL -->
<!-- Pythogen -->

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