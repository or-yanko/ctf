
<?php
$filePath = "/etc/natas_webpass/natas13";

if (file_exists($filePath)) {
    $fileContents = file_get_contents($filePath);
    if ($fileContents !== false) {
        echo "File Contents: " . $fileContents;
    } else {
        echo "Unable to read file.";
    }
} else {
    echo "File does not exist.";
}
?>
