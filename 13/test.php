<?php
// $path='/home/lyr/Pictures/wallpapers/fsoc.php';
// $path='./img.php';
$path='./payload.php';

if (exif_imagetype($path)) {
    echo "yes";
} else {
    echo "no";
}
?>