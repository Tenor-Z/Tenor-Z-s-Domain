<?php
    if (isset($_POST["subEnter"]))
    {
        $name = $_POST["textName"];
        $date_time = date("n/j/y g:i:s a");
        $comments = $_POST["textAreaComments"];
        $entry = $_POST["textAreaComments"];
        $fguestbook = fopen(
            "guestbook.txt", "a");
        fwrite($fguestbook, $name . " " . $date_time . "\r\n");
        fwrite($fguestbook, $entry . "\r\n");
        fclose($fguestbook);

        // Redirect to Guestbook Homepage.
        header("Location: guestbook-home.htm");
        exit;
    }
?>