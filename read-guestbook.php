<!--  File: read-guestbook.php

      Write comments to guestbook file,
      then redirect to Guestbook Homepage.
-->

<html>

<head>
<title>Guestbook Example</title>
<link rel="stylesheet" type="text/css" href="../styles.css">
</head>

<body>

<h2>Guestbook Example</h2>

<h3>Add to Guestbook</h3>

 <p>

<p><a href="guestbook-home.htm">To Guestbook Homepage</a></p>

<?php
    $fguestbook = fopen(
        "e:/ectserver/sjost/Database/guestbook.txt", "rb");
    while($line = fgets($fguestbook, 100))
    {
        echo "<p style=\"color:blue\">";
        echo $line;
        echo "</p>";
        $line = fgets($fguestbook);
        echo "<p>";
        echo $line;
        echo "</p>";
    }
?>
</body>
</html>